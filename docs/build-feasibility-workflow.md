---
description: Build Feasibility Assessment (Build Lens) workflow
---

# Build Feasibility Workflow

**Build Lens** is IdeaForge's engineering assessment — separate from passive-income **Opportunity Evaluation**.

| Lens | Question | Tool |
|------|----------|------|
| **Opportunity** | Should I pursue this? | `evaluate.py` + `idea-template.md` |
| **Build Feasibility** | Can we build and run it? | `assess.py` + `build-feasibility-template.md` |

**Never merge scores.** Track both on serious ideas.

---

## When to Use Build Lens

- Before committing weeks to an MVP
- When an idea is technically interesting but engineering path is unclear
- After opportunity score ≥ 60, **or** as a quick sniff test on a brainstorm item
- When promoting an idea to a real repo (`/promote-idea`)

**Skip Build Lens** for pure market-validation-only work (landing pages, interviews).

---

## Pipeline

### Standard path (recommended)

```
Brainstorm → Opportunity Evaluate → Build Feasibility → Develop
```

### Technical-first path

```
Brainstorm → Build Feasibility (sniff) → Opportunity Evaluate → Develop
```

### Gates to development

Proceed to MVP when **both** are true (adjust thresholds to taste):

- Opportunity score ≥ 60 (`evaluate.py`)
- Build Feasibility ≥ 60 or spike completed successfully (`assess.py`)

Either lens can veto independently.

---

## Step 1: Create assessment

From an existing idea file:

```bash
./scripts/new-build-feasibility.sh 2026-01-05-passive-income-lab-as-saas
# or
./scripts/new-build-feasibility.sh ideas/evaluated/2026-01-29-bni-chapter-toolkit.md
```

Output: `ideas/feasibility/<slug>-build-feasibility.md`

---

## Step 2: Fill in the template

Focus sections:

1. **Will it work** — core mechanism, unknowns, spike plan
2. **Build complexity** — MVP scope, effort, stack match
3. **Infrastructure** — homelab components, new services, cost to operate
4. **Scale path** — bottlenecks at 1×, 100×, 1000× load
5. **Scores** — six dimensions in `build-feasibility-matrix.md`

**Do not fill:** revenue model, pricing, TAM, passive-income criteria.

---

## Step 3: Run assessment

```bash
python3 ml-engine/build-feasibility/assess.py ideas/feasibility/YYYY-MM-DD-idea-build-feasibility.md
```

### Verdicts

| Score | Verdict | Meaning |
|-------|---------|---------|
| 80–100 | `buildable` | Proceed to MVP planning |
| 60–79 | `spike_first` | Time-box proof on unknowns |
| 40–59 | `defer` | Fix blockers before build |
| 0–39 | `not_buildable` | Do not start MVP now |

---

## Step 4: Rank build-feasible ideas

```bash
python3 ml-engine/build-feasibility/assess.py rank
```

Compares **Build Feasibility Score** only — not opportunity rank.

---

## Step 5: Link back to opportunity evaluation

On the source idea file, add (optional):

```markdown
## Build Feasibility
- Assessment: [ideas/feasibility/...](../feasibility/...)
- Score: XX/100 — verdict
- Date: YYYY-MM-DD
```

Opportunity template stays unchanged; this is a cross-link only.

---

## ML training data

Build assessments append to:

`ml-engine/models/build_feasibility_training.json`

Opportunity data remains in `ml-engine/models/training_data.json`.

---

## Quick commands

| Command | Action |
|---------|--------|
| `./scripts/new-build-feasibility.sh <slug>` | Create assessment from idea |
| `python3 ml-engine/build-feasibility/assess.py <file>` | Score one assessment |
| `python3 ml-engine/build-feasibility/assess.py rank` | Rank all in `ideas/feasibility/` |
| `python3 ml-engine/idea-scorer/evaluate.py <idea>` | Opportunity score (unchanged) |

---

## Related docs

- [build-feasibility-matrix.md](../frameworks/build-feasibility-matrix.md) — scoring criteria
- [build-feasibility-template.md](../frameworks/build-feasibility-template.md) — assessment template
- [passive-income-workflow.md](./passive-income-workflow.md) — opportunity pipeline (unchanged core)
