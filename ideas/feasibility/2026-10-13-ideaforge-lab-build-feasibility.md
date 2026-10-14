# Build Feasibility: IdeaForge Lab

**Assessment Type:** Build Feasibility Assessment (Build Lens)  
**Date:** 2026-10-13  
**Linked Idea:** [ideas/evaluated/2026-10-13-ideaforge-lab.md](../evaluated/2026-10-13-ideaforge-lab.md)  
**Assessor:** Cory  
**Status:** assessed

> **Scope:** Can we build a chat and a card that runs the two scorers and keeps the outcome?  
> **Out of scope:** Whether an entrepreneur will pay. That is the opportunity spike.

---

## 🎯 One-Line Technical Thesis

One user, one thread, one card. The model may call web search and the two existing scorers. The card stores the mechanism, the scores, and the outcome. A question list is retrieved before the model answers.

### Core Mechanism

```
Message → retrieve question list + similar cards → model replies, with search when it cites the world
→ card fields update from the reply
→ "run the paces" calls evaluate.py and assess.py
→ outcome is written on the card
```

### Hard Constraints

- [x] Must run on homelab (Proxmox / 10.92.3.0/24) for the pilot
- [x] Must use existing stack: FastAPI, a web UI, Postgres, the Python scorers
- [ ] Latency / uptime requirement: a single user, best effort
- [x] Data residency / compliance: one person's lab on the homelab. No second tenant in the spike.

---

## ✅ Will It Work?

### Approach Summary

| Component | Proposed solution | Confidence (H/M/L) |
|-----------|-------------------|---------------------|
| Data layer | Postgres: threads, messages, cards, questions, outcomes | H |
| Application | Chat page with the card beside it | H |
| Integrations | Strong model API, web search, shell-out to the two scorers | M |
| Background jobs | None in the spike. The reply is one request. | H |

### Unknowns Requiring Proof

1. A reply will challenge the mechanism, cite a live source, and refuse to score the opening sentence.
2. The card can be updated from that reply without a person editing markdown by hand.

### Spike Plan

| Unknown | Spike task | Time box | Pass criteria |
|---------|------------|----------|---------------|
| Critique quality | One fresh idea, model plus web search, no UI required | 1 day | Transcript names who pays, cites a source, withholds the score until the mechanism is clear, and ends with a first spend. Fail if it matches the generic scorer list. |
| Card update | Write the resulting card as structured fields | 1 day | Who pays, arrival path, both scores, and the pass test are stored without hand-editing the template. |

The UI waits on the first row. A chat box in front of a weak reply is the failure this spike is there to catch.

---

## 🔨 Build Complexity

### MVP Scope (minimum shippable)

- [x] Feature 1: thread and card for one user
- [x] Feature 2: Stock returns three starts; On the books reopens a card
- [x] Feature 3: run both scorers on request and store the outcome

**Explicitly NOT in MVP:**

- Many tenants
- A private model
- Other apps calling the service
- Sharing idea text across labs
- Billing

### Effort Estimate

| Phase | Duration | Notes |
|-------|----------|-------|
| Spike / POC | 2 days | Transcript first. UI only if the transcript passes. |
| MVP | 4–8 weeks | One user, chat, card, Stock, outcomes |
| Production-hardening | later | A second person, billing, model swap |

### Skills & Stack

| Area | Match (1–10) | Gap / learning needed |
|------|--------------|------------------------|
| Backend | 8 | Tool calls and the scorer process |
| Frontend | 7 | A thread and a card, not a dashboard |
| Infra / deploy | 7 | Homelab plus two external APIs |
| Domain-specific | 6 | The question list and the retrieval, which are the product |

---

## 🏗️ Infrastructure

### MVP Architecture

```
Browser → homelab app → Postgres
                     → model API
                     → web search
                     → evaluate.py / assess.py
```

### Components

| Component | Technology | Host / location | New? |
|-----------|------------|-----------------|------|
| App | FastAPI + web UI | Homelab LXC | Yes |
| Database | Postgres | CT131 | Tables are new |
| Cache / queue | None for the spike | | |
| Object storage | None | | |
| Reverse proxy | NPM or HAProxy | Existing | Route only |

### Homelab Leverage

- [ ] Blue-green deploy via MCP — personal pilot, not a fleet app yet
- [x] Existing Postgres on CT131
- [ ] qa-01 testing pattern
- [ ] Monitoring stack (CT150) when live
- [x] Other: the idea files and both scorers already in this repo

### Monthly Infra Cost (operational, not revenue)

| Item | MVP $/mo | At scale $/mo |
|------|----------|---------------|
| Compute | 0 | A larger host only if a private model is added |
| Storage | 0 | Small |
| External APIs | Tens of dollars for one user | Grows with sessions, not with a private GPU |
| **Total** | Tens of dollars | Dominated by the model |

---

## 📈 Scale Path (Operational)

### Bottleneck Analysis

| Load tier | Expected load | First bottleneck | Mitigation |
|-----------|---------------|------------------|------------|
| Prototype | 1 user, a few sessions | Critique quality | The spike |
| Early | ~100 sessions | Model latency and cost | Same service, usage watched |
| Growth | Many labs | Case retrieval and question quality | Patterns shared. Idea text stays in the lab. |

### Scaling Actions (in order)

1. One user, transcript spike
2. That user, chat and card
3. A second person only after a session is worth paying for

### What Does NOT Scale Cheaply

- Hosting a private model before the critique is good
- A person inside every thread

---

## ⚠️ Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| The model scores the first sentence | H | H | Spike pass criteria forbid it |
| Search citations are vague or wrong | M | H | The transcript must name the source. A miss fails the spike. |
| Scorer output overwrites the critique | M | H | Numbers come from the scripts. The reply still has to say what to do next. |

---

## 🔧 Ops & Maintainability

- **Deploy path:** manual on the homelab for the pilot
- **Monitoring:** read the transcript. A generic reply is an outage even if the server is up.
- **Backup strategy:** Postgres backup of cards and outcomes
- **Expected steady-state ops:** a weekly pass over outcomes to add a question when a score was wrong

---

## 📊 Build Feasibility Scores

### Technical Viability: 6 / 10
**Notes:** The parts are proven. The unknown is whether the reply meets the MRI bar. That is the spike.

### Build Complexity: 5 / 10
**Notes:** The full one-user lab is about one to two months. The matrix band for a 5 is that range. The spike is two days and is the only work authorized now.

### Infrastructure Fit: 7 / 10
**Notes:** Homelab, Postgres, and the scorers are already here. The model and the search API are the new dependencies.

### Scale Architecture: 7 / 10
**Notes:** One service, more sessions. The private model is a later box, not the path to the second user.

### Technical Risk: 5 / 10
**Notes:** The product fails if the model is weak or if search is sloppy. Both sit outside the homelab.

### Ops Maintainability: 6 / 10
**Notes:** The app is small. The question list is the living part, and it needs a weekly look.

---

## 🎬 Verdict & Next Steps

**Build Feasibility Score:** 60.0 / 100  
**Verdict:** spike_first

### Recommended Next Steps

1. Run the one-day transcript spike on a fresh idea.
2. Keep the UI unbuilt if the transcript fails the MRI comparison.
3. Build the thread and the card only after the transcript passes.

### Gate to Development

- [x] Build Feasibility ≥ 60 (or spike completed successfully) — score 60, spike still required
- [x] Opportunity evaluation completed separately (`evaluate.py`) — 60.0, Validate Market
- [ ] Both scores reviewed before `/build` or repo promotion — do not promote. Do not build the lab yet.

---

## 📝 Assessment Log

| Date | Event | Notes |
|------|-------|-------|
| 2026-10-13 | Created | Scored with the opportunity file |
