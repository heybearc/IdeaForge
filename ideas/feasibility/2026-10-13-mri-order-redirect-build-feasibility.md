# Build Feasibility: MRI Order Redirect

**Assessment Type:** Build Feasibility Assessment (Build Lens)  
**Date:** 2026-10-13  
**Linked Idea:** [ideas/evaluated/2026-10-13-mri-order-redirect.md](../evaluated/2026-10-13-mri-order-redirect.md)  
**Assessor:** Cory  
**Status:** assessed

> **Scope:** Can we build and operate the booking platform?  
> **Out of scope:** Whether a center will pay. That is the opportunity validation.

---

## 🎯 One-Line Technical Thesis

A two-sided web app: a patient submits city, study, and phone number; a center sees the request, marks it confirmed or completed, and a ledger adds the per-scan fee.

### Core Mechanism

```
Patient form → API stores booking (no clinical order) → center portal lists it
→ staff sets status → completed status appends one per-scan fee row
```

### Hard Constraints

- [x] Must run on homelab (Proxmox / 10.92.3.0/24) for the pilot
- [x] Must use existing stack: a small web app and Postgres
- [ ] Latency / uptime requirement: best-effort pilot, no SLA
- [x] Data residency / compliance: v1 schema has no name, date of birth, or order document

---

## ✅ Will It Work?

### Approach Summary

| Component | Proposed solution | Confidence (H/M/L) |
|-----------|-------------------|---------------------|
| Data layer | Postgres: centers, bookings, fee rows | H |
| Application | Patient form + center sign-in | H |
| Integrations | None in v1. The center confirms by hand. | H |
| Background jobs | None. Status changes are clicks. | H |

### Unknowns Requiring Proof

1. A public homelab page can accept a booking without fields that make it a medical record.
2. The center can finish the loop (requested → confirmed → completed) without an API into their own scheduler.

### Spike Plan

| Unknown | Spike task | Time box | Pass criteria |
|---------|------------|----------|---------------|
| Schema stays non-clinical | Create the booking table and the form | 1 day | Saved columns are phone, city, study, center, status. No name, date of birth, or attachment. |
| Hand confirmation | Click a fake booking through to completed | 1 day | One fee row appears. Nothing is sent to a hospital system. |

This spike waits on a center saying yes. Building it before that does not test the product.

---

## 🔨 Build Complexity

### MVP Scope (minimum shippable)

- [x] Feature 1: patient form for one city and MRI only
- [x] Feature 2: center list of bookings with status
- [x] Feature 3: per-scan fee row when status becomes completed

**Explicitly NOT in MVP:**

- Patient accounts and subscriptions
- Upload or storage of the MRI order
- Hospital, EHR, or insurance integrations
- Card billing until a center has agreed to the fees
- More than one study

### Effort Estimate

| Phase | Duration | Notes |
|-------|----------|-------|
| Spike / POC | 2 days | After a center says yes |
| MVP | 2–4 weeks | Both sides of the web app |
| Production-hardening | later | Only if orders are stored |

### Skills & Stack

| Area | Match (1–10) | Gap / learning needed |
|------|--------------|------------------------|
| Backend | 8 | Ordinary CRUD |
| Frontend | 8 | Two screens |
| Infra / deploy | 7 | Public page on the homelab |
| Domain-specific | 4 | When a booking becomes stored health information |

---

## 🏗️ Infrastructure

### MVP Architecture

```
Patient browser → homelab web app → Postgres
Center browser  → same app, signed in → same bookings and fee rows
```

No hospital system is in the path.

### Components

| Component | Technology | Host / location | New? |
|-----------|------------|-----------------|------|
| App | Small web app | Homelab LXC | Yes, the app. The host pattern exists. |
| Database | Postgres | Existing Postgres if the pilot stays non-clinical | Table is new |
| Cache / queue | None | | |
| Object storage | None | | |
| Reverse proxy | NPM or HAProxy | Existing | Route only |

### Homelab Leverage

- [ ] Blue-green deploy via MCP — not a fleet app yet
- [x] Existing Postgres on CT131 — only while the schema stays non-clinical
- [ ] qa-01 testing pattern
- [ ] Monitoring stack (CT150) when live
- [x] Other: phone and a spreadsheet are the fallback if the portal slips

### Monthly Infra Cost (operational, not revenue)

| Item | MVP $/mo | At scale $/mo |
|------|----------|---------------|
| Compute | 0 on the homelab | A separate host if health data is stored |
| Storage | 0 | Unestimated |
| External APIs | 0 | Card processing fees only |
| **Total** | 0 | Unknown until the record-storage decision |

---

## 📈 Scale Path (Operational)

### Bottleneck Analysis

| Load tier | Expected load | First bottleneck | Mitigation |
|-----------|---------------|------------------|------------|
| Prototype | 1 center, a few requests | The person confirming by phone | Leave it manual |
| Early | ~100 bookings | Same person, plus center staff learning the list | Center clicks their own status |
| Growth | ~1,000 bookings | Confirmation labor, not the database | Centers manage slots. Still no EHR feed. |

### Scaling Actions (in order)

1. One center, hand confirmation
2. That center updates status in the portal
3. A second center on the same tables

### What Does NOT Scale Cheaply

- A human placing every phone call once volume is real
- Any step that starts storing the MRI order. That is a different system, not a bigger database.

---

## ⚠️ Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| The form collects clinical fields "just in case" | M | H | Spike pass criteria forbid those columns |
| Public homelab page is scraped or abused | M | M | Rate-limit the form. No patient documents on it. |
| A later EHR integration is assumed | L | H | v1 has no integration slot. Adding one is a new assessment. |

---

## 🔧 Ops & Maintainability

- **Deploy path:** manual on the homelab for the pilot
- **Monitoring:** the center list is the monitor. An empty list means no orders.
- **Backup strategy:** Postgres backup already used for the homelab database, once the table lives there
- **Expected steady-state ops:** a few hours a week while confirmation is by hand

---

## 📊 Build Feasibility Scores

### Technical Viability: 7 / 10
**Notes:** A booking list is proven software. The unknown is the non-clinical schema, and that is a one-day spike.

### Build Complexity: 7 / 10
**Notes:** Two screens and a fee row. About two to four weeks after a center says yes. Matrix band for a 7 is two to four weeks.

### Infrastructure Fit: 8 / 10
**Notes:** Homelab web app and Postgres. No new stack while the order stays off the server.

### Scale Architecture: 7 / 10
**Notes:** The database is not the bottleneck. Confirmation labor is, and the portal removes it one center at a time.

### Technical Risk: 5 / 10
**Notes:** Low third-party dependency. The risk is drifting into stored health information. A 5 leaves that risk visible.

### Ops Maintainability: 6 / 10
**Notes:** The app is small. The phone confirmation is the ongoing work until centers click status themselves.

---

## 🎬 Verdict & Next Steps

**Build Feasibility Score:** 69.0 / 100  
**Verdict:** spike_first

### Recommended Next Steps

1. Finish the center calls in the validation plan. A spike with no center does not change the decision.
2. If a center says yes, spend two days on the schema spike.
3. Build the two screens only after that spike passes.

### Gate to Development

- [x] Build Feasibility ≥ 60 (or spike completed successfully) — score 69, spike still required
- [x] Opportunity evaluation completed separately (`evaluate.py`) — 65.0, Validate Market
- [ ] Both scores reviewed before `/build` or repo promotion — do not promote yet

---

## 📝 Assessment Log

| Date | Event | Notes |
|------|-------|-------|
| 2026-10-13 | Created | Scored after the opportunity evaluation |
