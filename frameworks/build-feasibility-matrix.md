# Build Feasibility Matrix

Use this framework to score whether an idea is **technically buildable and operable** — separate from opportunity / passive-income evaluation.

**Build Lens answers:** Can we build it? How hard? What infra? How does it scale operationally?

**It does NOT answer:** market size, pricing, revenue, or passive-income fit (see `evaluation-matrix.md`).

---

## Scoring System

Each criterion is scored **1–10** (10 = best). Weighted total: **0–100**.

| Dimension | Weight | 10 means | 1 means |
|-----------|--------|----------|---------|
| **Technical Viability** | 25% | Approach is proven; core path is clear | Fundamental unknowns; may not work |
| **Build Complexity** | 25% | MVP in days–2 weeks with existing skills | Multi-month; major new skills or research |
| **Infrastructure Fit** | 15% | Runs on existing homelab patterns | Entirely new stack or cloud-only deps |
| **Scale Architecture** | 20% | Clear horizontal path; bottlenecks known | Single-node only; scale path unclear |
| **Technical Risk** | 10% | Low dependency on externals; few unknowns | Heavy third-party / compliance / research risk |
| **Ops Maintainability** | 5% | Low touch; observable; easy rollback | High on-call; fragile; hard to debug |

---

## Dimension Prompts

### 1. Technical Viability — ___ / 10

- Does the core mechanism work with known technology?
- Are there blocking unknowns (algorithms, latency, data access)?
- Is a spike needed to prove the approach?

**Evidence:**
- [ ] Similar systems exist (reference architecture)
- [ ] Core data/API access confirmed
- [ ] Performance envelope estimated

---

### 2. Build Complexity — ___ / 10

- MVP scope bounded and definable?
- Matches your stack (Next.js, FastAPI, Postgres, Proxmox)?
- What must be learned vs reused?

**Effort bands (guide):**
- 10 = ≤2 weeks solo MVP
- 7 = 2–4 weeks
- 5 = 1–2 months
- 3 = 3+ months
- 1 = research project

---

### 3. Infrastructure Fit — ___ / 10

- Uses `10.92.3.0/24` / existing blue-green patterns?
- New services required (queue, object store, GPU, etc.)?
- Homelab vs cloud-only constraints?

**Leverage checklist:**
- [ ] Proxmox LXC
- [ ] Existing Postgres / Redis
- [ ] HAProxy / NPM patterns
- [ ] MCP deploy tooling

---

### 4. Scale Architecture — ___ / 10

- What breaks first under load (DB, API, jobs, storage)?
- Stateless app tier? Background workers? Caching?
- Cost/complexity curve as usage grows (not revenue)

**Scale tiers to sketch:**
- Tier 1: solo / prototype
- Tier 2: ~100 users or equivalent load
- Tier 3: 10× that load

---

### 5. Technical Risk — ___ / 10

- Third-party API availability, rate limits, ToS
- Security boundary (auth, multi-tenant, secrets)
- Data durability, backup, disaster recovery

---

### 6. Ops Maintainability — ___ / 10

- Monitoring, alerts, runbooks
- Deploy/rollback path (MCP blue-green?)
- Expected weekly maintenance hours at steady state

---

## Calculation

```
Build Feasibility Score =
  (Technical Viability × 0.25) +
  (Build Complexity × 0.25) +
  (Infrastructure Fit × 0.15) +
  (Scale Architecture × 0.20) +
  (Technical Risk × 0.10) +
  (Ops Maintainability × 0.05)
```

Each dimension × weight × 10 → sum to 100.

---

## Interpretation

| Score | Verdict | Action |
|-------|---------|--------|
| **80–100** | **Buildable** | Proceed to MVP / implementation planning |
| **60–79** | **Spike first** | Time-boxed prototype on unknowns, then reassess |
| **40–59** | **Defer** | Resolve listed blockers before committing build time |
| **0–39** | **Not buildable** (now) | Archive or pivot architecture; do not start MVP |

---

## Relationship to Opportunity Score

| Opportunity Score (Idea Evaluation) | Build Feasibility Score | Suggested action |
|-----------------------------------|-------------------------|------------------|
| High | High | Strong candidate — build |
| High | Low | Promising market, bad engineering fit — redesign or defer |
| Low | High | Easy build, weak bet — park or use as learning project |
| Low | Low | Archive |

**Never merge into one number.** Track both scores on the idea record.

---

## ML Training Data

```yaml
assessment_id: YYYY-MM-DD-idea-name-build-feasibility
linked_idea: ideas/evaluated/YYYY-MM-DD-idea-name.md
scores:
  technical_viability: X
  build_complexity: X
  infrastructure_fit: X
  scale_architecture: X
  technical_risk: X
  ops_maintainability: X
build_feasibility_score: XX
verdict: [buildable|spike_first|defer|not_buildable]
outcome: [pending|mvp_shipped|spike_failed|abandoned]
actual_build_weeks: X
lessons_learned: "..."
```

Stored separately from opportunity training data in `ml-engine/models/build_feasibility_training.json`.
