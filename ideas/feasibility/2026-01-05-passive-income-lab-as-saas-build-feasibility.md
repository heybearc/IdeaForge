# Build Feasibility: Passive Income Lab as SaaS Platform - "IdeaForge"

**Assessment Type:** Build Feasibility Assessment (Build Lens)  
**Date:** 2026-06-02  
**Linked Idea:** [ideas/brainstorm/2026-01-05-passive-income-lab-as-saas.md](../brainstorm/2026-01-05-passive-income-lab-as-saas.md)  
**Assessor:** Cory  
**Status:** assessed

> **Scope:** Can we build and operate IdeaForge-as-SaaS technically?  
> **Out of scope:** Revenue model, pricing, market validation (see linked idea file).

---

## 🎯 One-Line Technical Thesis

Multi-tenant web app: users submit idea markdown → Python scorer runs → results stored per user → optional export; MVP on existing Next.js + FastAPI + Postgres homelab stack.

### Core Mechanism

Browser form / file upload → API persists idea doc → worker or sync call to `evaluate.py` logic → scores + recommendation returned → dashboard history.

### Hard Constraints

- [x] Must run on homelab (Proxmox / 10.92.3.0/24)
- [x] Must use existing stack: Next.js, FastAPI, Postgres
- [ ] Latency / uptime requirement: best-effort MVP; no SLA initially
- [ ] Data residency / compliance: single-tenant homelab OK for MVP

---

## ✅ Will It Work?

### Approach Summary

| Component | Proposed solution | Confidence (H/M/L) |
|-----------|-------------------|---------------------|
| Data layer | Postgres per-tenant rows + object storage for uploads | H |
| Application | Next.js UI + FastAPI API (mirror TIP Generator pattern) | H |
| Integrations | Optional OAuth (Authentik) later | M |
| Background jobs | Sync scoring for MVP; Celery/RQ if batch grows | H |

### Unknowns Requiring Proof

1. Multi-tenant isolation model (row-level vs schema-per-tenant)
2. Running ML scorer safely for untrusted markdown input

### Spike Plan (if any)

| Unknown | Spike task | Time box | Pass criteria |
|---------|------------|----------|---------------|
| Untrusted input | Sandbox `evaluate.py` on arbitrary markdown | 2 days | No code execution; bounded runtime |
| Multi-tenant | RLS prototype on Postgres | 1 day | Two test users cannot read each other's rows |

---

## 🔨 Build Complexity

### MVP Scope (minimum shippable)

- [ ] User auth (single user or simple OAuth)
- [ ] Create idea + paste/upload markdown
- [ ] Run opportunity scorer; display score + recommendation
- [ ] List past evaluations

**Explicitly NOT in MVP:**

- Done-for-you MVP marketplace
- Team collaboration
- Billing / Stripe

### Effort Estimate

| Phase | Duration | Notes |
|-------|----------|-------|
| Spike / POC | 3 days | RLS + scorer sandbox |
| MVP | 3–4 weeks | Reuse TIP Generator infra patterns |
| Production-hardening | 2 weeks | Monitoring, backups, rate limits |

### Skills & Stack

| Area | Match (1–10) | Gap / learning needed |
|------|--------------|------------------------|
| Backend | 9 | FastAPI familiar |
| Frontend | 8 | Next.js familiar |
| Infra / deploy | 9 | Blue-green + MCP |
| Domain-specific | 7 | Multi-tenant RLS patterns |

---

## 🏗️ Infrastructure

### MVP Architecture

```
Users → NPM/HAProxy → Next.js (CT TBD) → FastAPI → Postgres (CT131)
                              ↓
                     evaluate.py (in-process or worker)
```

### Components

| Component | Technology | Host / location | New? |
|-----------|------------|-----------------|------|
| App | Next.js + FastAPI | New LXC 10.92.3.x | Yes |
| Database | Postgres | CT131 shared or dedicated DB | Maybe |
| Cache / queue | Redis (optional) | CT100 if async jobs | Optional |
| Reverse proxy | HAProxy / NPM | Existing | No |

### Homelab Leverage

- [x] Blue-green deploy via MCP (when second node added)
- [x] Existing Postgres on CT131
- [ ] qa-01 testing pattern
- [ ] Monitoring stack (CT150) when live
- [x] TIP Generator as reference architecture

### Monthly Infra Cost (operational, not revenue)

| Item | MVP $/mo | At scale $/mo |
|------|----------|---------------|
| Compute | ~$0 (homelab) | +1–2 LXC |
| Storage | ~$0 | MinIO if file volume grows |
| External APIs | $0 MVP | LLM API if added later |
| **Total** | ~$0 | Low until LLM-heavy features |

---

## 📈 Scale Path (Operational)

### Bottleneck Analysis

| Load tier | Expected load | First bottleneck | Mitigation |
|-----------|---------------|------------------|------------|
| Prototype | 1 user | — | — |
| Early | ~50 users, sync scoring | API CPU / scorer runtime | Background queue |
| Growth | ~500 users | Postgres connections | PgBouncer, read replica |

### Scaling Actions (in order)

1. Move scoring to async worker + Redis queue
2. Add PgBouncer; separate read replica if needed
3. Horizontal app replicas behind HAProxy

### What Does NOT Scale Cheaply

- Synchronous LLM calls per evaluation (if added later)
- Heavy file parsing on request thread

---

## ⚠️ Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Scorer abuse (DoS via huge files) | M | M | Size limits, timeout, queue |
| Multi-tenant data leak | L | H | RLS + tests |
| Shared Postgres noisy neighbor | M | M | Dedicated DB or quotas |

---

## 🔧 Ops & Maintainability

- **Deploy path:** MCP blue-green when dual-node; single LXC for MVP
- **Monitoring:** CT150 Prometheus when deployed
- **Backup strategy:** Postgres pg_dump + app config in git
- **Expected steady-state ops:** 1–2 hrs/week at MVP

---

## 📊 Build Feasibility Scores

### Technical Viability: 8 / 10
**Notes:** Core path proven locally; SaaS wrapper is standard CRUD + scorer.

### Build Complexity: 7 / 10
**Notes:** 3–4 week MVP with existing patterns; multi-tenant adds scope.

### Infrastructure Fit: 9 / 10
**Notes:** Fits homelab; TIP Generator precedent.

### Scale Architecture: 7 / 10
**Notes:** Clear path to queue + horizontal app; DB first bottleneck known.

### Technical Risk: 7 / 10
**Notes:** Untrusted input and tenancy need spikes, not blockers.

### Ops Maintainability: 8 / 10
**Notes:** Familiar deploy stack; low moving parts for MVP.

---

## 🎬 Verdict & Next Steps

**Build Feasibility Score:** 76 / 100  
**Verdict:** spike_first — run RLS + scorer sandbox spikes before full MVP

### Recommended Next Steps

1. Run spikes (RLS + scorer sandbox)
2. Opportunity evaluate separately if pursuing as business
3. Promote to repo only if both lenses pass gates

### Gate to Development

- [ ] Build Feasibility ≥ 60 (or spike completed successfully)
- [ ] Opportunity evaluation completed separately
- [ ] Both scores reviewed before repo promotion

---

## 📝 Assessment Log

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-02 | Created | Example assessment for Build Lens feature |
