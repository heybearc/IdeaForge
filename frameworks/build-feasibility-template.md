# Build Feasibility: [Idea Name]

**Assessment Type:** Build Feasibility Assessment (Build Lens)  
**Date:** YYYY-MM-DD  
**Linked Idea:** [ideas/evaluated/YYYY-MM-DD-idea-name.md](../evaluated/YYYY-MM-DD-idea-name.md)  
**Assessor:** Cory  
**Status:** draft | assessed | spike_in_progress | buildable | deferred | not_buildable

> **Scope:** Can we build and operate this? How hard? What infra? How does it scale?  
> **Out of scope:** Revenue, pricing, market size, passive-income ranking (use `idea-template.md` + `evaluate.py`).

---

## 🎯 One-Line Technical Thesis

[What you are building in engineering terms — one sentence.]

### Core Mechanism

[How it works technically: inputs → processing → outputs.]

### Hard Constraints

- [ ] Must run on homelab (Proxmox / 10.92.3.0/24)
- [ ] Must use existing stack: ___
- [ ] Latency / uptime requirement: ___
- [ ] Data residency / compliance: ___

---

## ✅ Will It Work?

### Approach Summary

| Component | Proposed solution | Confidence (H/M/L) |
|-----------|-------------------|---------------------|
| Data layer | | |
| Application | | |
| Integrations | | |
| Background jobs | | |

### Unknowns Requiring Proof

1. ___
2. ___

### Spike Plan (if any)

| Unknown | Spike task | Time box | Pass criteria |
|---------|------------|----------|---------------|
| | | | |

---

## 🔨 Build Complexity

### MVP Scope (minimum shippable)

- [ ] Feature 1: ___
- [ ] Feature 2: ___
- [ ] Feature 3: ___

**Explicitly NOT in MVP:**

- ___

### Effort Estimate

| Phase | Duration | Notes |
|-------|----------|-------|
| Spike / POC | ___ days | |
| MVP | ___ weeks | |
| Production-hardening | ___ weeks | |

### Skills & Stack

| Area | Match (1–10) | Gap / learning needed |
|------|--------------|------------------------|
| Backend | | |
| Frontend | | |
| Infra / deploy | | |
| Domain-specific | | |

---

## 🏗️ Infrastructure

### MVP Architecture

```
[ASCII or bullet diagram: users → app → db → external APIs]
```

### Components

| Component | Technology | Host / location | New? |
|-----------|------------|-----------------|------|
| App | | CT___ / LXC | |
| Database | | CT131 Postgres | |
| Cache / queue | | | |
| Object storage | | | |
| Reverse proxy | | HAProxy / NPM | |

### Homelab Leverage

- [ ] Blue-green deploy via MCP
- [ ] Existing Postgres on CT131
- [ ] qa-01 testing pattern
- [ ] Monitoring stack (CT150) when live
- [ ] Other: ___

### Monthly Infra Cost (operational, not revenue)

| Item | MVP $/mo | At scale $/mo |
|------|----------|---------------|
| Compute | | |
| Storage | | |
| External APIs | | |
| **Total** | | |

---

## 📈 Scale Path (Operational)

### Bottleneck Analysis

| Load tier | Expected load | First bottleneck | Mitigation |
|-----------|---------------|------------------|------------|
| Prototype | 1 user (you) | | |
| Early | ~100 units* | | |
| Growth | ~1,000 units* | | |

*Units = users, jobs/day, events/sec — define per idea.

### Scaling Actions (in order)

1. ___
2. ___
3. ___

### What Does NOT Scale Cheaply

- ___

---

## ⚠️ Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | H/M/L | H/M/L | |
| | | | |
| | | | |

---

## 🔧 Ops & Maintainability

- **Deploy path:** MCP `deploy_to_standby` / manual / other
- **Monitoring:** ___
- **Backup strategy:** ___
- **Expected steady-state ops:** ___ hrs/week

---

## 📊 Build Feasibility Scores

> Score each 1–10. Run `python3 ml-engine/build-feasibility/assess.py` on this file when complete.

### Technical Viability: ___ / 10
**Notes:**

### Build Complexity: ___ / 10
**Notes:**

### Infrastructure Fit: ___ / 10
**Notes:**

### Scale Architecture: ___ / 10
**Notes:**

### Technical Risk: ___ / 10
**Notes:**

### Ops Maintainability: ___ / 10
**Notes:**

---

## 🎬 Verdict & Next Steps

**Build Feasibility Score:** ___ / 100 *(filled by assess.py)*  
**Verdict:** buildable | spike_first | defer | not_buildable

### Recommended Next Steps

1. ___
2. ___
3. ___

### Gate to Development

- [ ] Build Feasibility ≥ 60 (or spike completed successfully)
- [ ] Opportunity evaluation completed separately (`evaluate.py`)
- [ ] Both scores reviewed before `/build` or repo promotion

---

## 📝 Assessment Log

| Date | Event | Notes |
|------|-------|-------|
| YYYY-MM-DD | Created | Initial assessment |
