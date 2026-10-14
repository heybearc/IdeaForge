# IdeaForge Lab

**Date Created:** 2026-10-13  
**Category:** api-services  
**Status:** evaluated  
**Creator:** Cory

This revises the January SaaS sketch in `ideas/brainstorm/2026-01-05-passive-income-lab-as-saas.md`. That file stays as history. This one is the product shaped in the MRI session: a chat, a card, and a lab that remembers.

---

## 🎯 Core Concept

An entrepreneur opens a chat and either types an idea or asks Stock for three starting points. The conversation turns the rough note into a card, checks what already exists, and only then runs the two scores. They leave with a small first spend, or a reason not to spend. The lab keeps the card, the argument, and the outcome for the next session.

### Problem Being Solved

People who are about to put time or money into a business idea stay in a general chat tool because the reply argues with them. The chat forgets the lab. A scored markdown file does not argue. They need one place that does both, and that gets sharper as more ideas die or survive.

### Target Audience

**Who pays**

- An entrepreneur deciding where the next spend goes. They subscribe because the lab remembers and they come back.

**Who uses it**

- The same person, in a chat. Cory is the first user. Other entrepreneurs are the customer only after a session is good enough that Cursor is the worse place to do this.

### Unique Value Proposition

The thread is the product. The card is what remains. Stock deals three starting ideas. On the books reopens a parked one. Scores stay in the existing scorers. The model writes the critique and waits to score until the mechanism is clear.

Three clocks keep it current: a live lookup of what exists now, the case file of outcomes, and a question list that grows when a high score dies on contact with the world.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — the lab is the thing they return to
- [ ] Usage-based pricing — model cost sits underneath; the price the customer sees is the subscription
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

No price yet. The January file guessed $29 and $99. Those numbers are not reused here. A price comes after one entrepreneur who is not Cory finishes a session and says what they would pay to keep the lab.

**Revenue scenario (unvalidated):**

- Month 1: $0. The work is a single critique session judged against the MRI thread.
- Month 3: $0 unless that session is good enough to show someone.
- Month 6: a small number of paying labs, only if strangers complete a session and pay.
- Month 12: still unknown. More labs make the case file better. They do not by themselves create revenue.

---

## 🔧 Technical Requirements

### What the first version is

A chat and a card for one user.

1. Type an idea, or ask Stock for three starts.
2. The reply challenges the mechanism and cites a live lookup.
3. The card updates: who pays, how the thing arrives, the pass test.
4. On request, the existing opportunity scorer and build assessor run, and the numbers land on the card.
5. The outcome of the pass test is written back onto the card.

The question list is a file the critique must run. Past cards are retrieved before the model answers. A private model is a later backend on the same service, not the start.

### Tech Stack

- Backend: FastAPI, with tools for web search and the two Python scorers
- Frontend: a chat thread and a card
- Database: Postgres for cards, messages, outcomes, and the question list
- Infrastructure: homelab for the pilot
- APIs/Integrations: a strong model API and a web search API

### Existing Assets to Leverage

- [x] Proxmox infrastructure
- [ ] QuantShift codebase
- [ ] Trading algorithms
- [x] MCP server framework — later, if other apps call the same critique service
- [x] Multi-agent development tools
- [x] Other: `evaluate.py`, `assess.py`, the idea and feasibility templates, the MRI card as the quality bar

### Development Estimate

- MVP: a spike of a few days, then stop
- Beta: only if the spike matches the MRI thread's standard
- Launch: after a stranger pays
- Total: the full lab is one to two months. That build waits on the spike.

### Infrastructure Costs

- Hosting: about $0 on the homelab
- APIs/Services: model and search calls, on the order of tens of dollars a month at personal volume
- Tools/Software: low
- Total: inside the $0–100 band for a personal pilot, plus API use

---

## 📊 Evaluation Scores

### Market Demand: 6 / 10

**Evidence:**

- [x] Competitor analysis completed (this session, 2026-10-13)
- [ ] Reddit/Discord research done
- [ ] Google Trends analyzed
- [ ] Customer interviews: 0 completed

**Notes:** Cursor and general chat models already win this job. Cory is in Cursor for the conversation. IdeaBuddy, plan generators, and chat products also sit here. Demand for "help me think an idea through" is proven. Demand for a paid lab with a card and a memory is not. No entrepreneur has been asked.

### Technical Feasibility: 6 / 10

**Skills Match:**

- [x] Can build with existing skills
- [x] Requires learning: retrieval of past cards, and a critique that will refuse to score a half-formed idea
- [x] Infrastructure ready for a pilot

**Notes:** A chat, a card, and a call to the existing scorers are ordinary. The product is the quality of the argument. That is a spike, and the full lab is longer than a two-to-four week MVP.

### Time to Revenue: 5 / 10

**Timeline:**

- First customer: Cory, using it. That is not revenue.
- First dollar: after a stranger finishes a session and pays. Three to six months if the spike works. Longer if the chat is merely fine.
- Profitable: unknown.

**Notes:** Matrix band for a 5 is revenue in three to six months. Charging before the critique beats staying in Cursor would be selling the weak version.

### Scalability: 6 / 10

**Automation Level:**

- Current: 0%
- Target: sessions run without a person in the thread
- Timeline: after the question list and the case file exist

**Notes:** A hundred labs do not need a hundred operators. Each session still costs a model call, so marginal cost is not near zero. The case file is the part that improves as labs are added.

### Initial Investment: 8 / 10

**Costs:**

- Development time: days for the spike, one to two months for the lab
- Infrastructure: homelab, about $0
- Marketing: $0 until a stranger is invited
- Total cash: model and search API use, personal volume, tens of dollars a month

**Notes:** The matrix scores cash. Time is already counted under time to revenue and build complexity.

### Competitive Advantage: 5 / 10

**Moats:**

- [x] Unique expertise — the two scorers and the MRI session as a worked example
- [ ] Proprietary data/algorithms — empty until outcomes exist
- [x] Network effects — later, and only for patterns, not for the text of someone's idea
- [ ] First-mover advantage
- [ ] Infrastructure advantage
- [ ] Other:

**Notes:** Cursor can grow a memory of files. A general model can search the web. The lab is defensible after the case file and the question list are thick. On day one they are thin. Competitors can copy a chat and a card.

### Automation Potential: 6 / 10

**Manual Tasks:**

- Customer support: low at personal scale
- Content creation: the question list is edited when an outcome embarrasses a score
- Operations: weekly review of sessions, not a person inside each chat
- Marketing: none until the spike passes

**Notes:** Sessions are the automated part. Judgment about whether the critique is still sharp is a weekly human job. That is short of the 90% goal inside three months.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription
- [ ] Usage-based
- [ ] Repeat purchases
- [ ] One-time

**Notes:** A subscription fits because the value is the lab they return to. The MRI patient paid once. This customer comes back. A 10 would mean the price is already tested. It is not.

---

## 📈 Total Score: 60.0 / 100

**Weighted Score Calculation:**

```
(6 × 0.15) +
(6 × 0.10) +
(5 × 0.15) +
(6 × 0.20) +
(8 × 0.10) +
(5 × 0.15) +
(6 × 0.10) +
(8 × 0.05) = 6.00 → 60.0 / 100
```

**Decision:** Validate Market

Worth a spike. Not worth the full build until that spike beats the MRI thread and someone other than Cory wants to keep the lab.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The chat is a worse Cursor**: The session is pleasant and never challenges the mechanism, or it scores the first sentence.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Judge the spike against the MRI thread. Fail it if it skips the hard question.

2. **Empty memory**: Stock and the case file are dull until outcomes exist. Early users get a thin lab and leave.
   - **Likelihood**: High
   - **Impact**: Medium
   - **Mitigation**: Seed the question list and a few public patterns (luggage shipping, MOMS, the MRI order path) before inviting anyone.

3. **Model cost and model quality move together**: A cheaper model makes the argument worse. A strong model makes every session cost money.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: One strong model for the critique. Do not start by hosting a private model.

---

## 🚀 Opportunity Analysis

### What could make this 10x bigger?

1. **Market Expansion**: Any founder deciding on a first spend, not only homelab-shaped ideas.
2. **Product Evolution**: The question list and the case file become the reason a second year is better than the first.
3. **Partnership Potential**: None required for the pilot.
4. **Platform Play**: Other apps call the same critique service. That waits until IdeaForge itself is sharp.

### Adjacent Opportunities

- A private model as a second backend, for volume and for notes that should stay on the homelab.
- The MRI idea stays its own card. This lab is where that card lives.

---

## ✅ Next Steps

### Validation Phase (this spike)

- [ ] Run one fresh idea through a chat that can search the web and call both scorers
- [ ] Compare the transcript to the MRI session: hard question, live source, score only after the mechanism is clear, a pass test for the first spend
- [ ] Fail the spike if the reply is generic or scores the opening sentence
- [ ] If it passes, show the transcript to one entrepreneur and ask whether they would pay to keep a lab like it

### MVP Phase (only after that)

- [ ] Chat, card, Stock, and On the books for one user
- [ ] Outcome written back on the card
- [ ] Question list editable without a code change

### Launch Phase

- [ ] First paid lab that is not Cory

### Growth Phase

- [ ] Patterns shared across labs, idea text kept inside each lab
- [ ] A newer model swapped in without a rewrite
- [ ] A private model only when volume or privacy requires it

---

## 📝 Research Notes

### Competitor Analysis

| Competitor | Pricing | Features | Strengths | Weaknesses |
|-----------|---------|----------|-----------|------------|
| Cursor, and general chat models | Subscription the user already pays | Conversation that argues | This is why the session happened here | The lab, the scorers, and the outcome are not the product |
| IdeaBuddy and plan generators | Subscription | Business-plan templates and prompts | Founders already pay for structure | The output is a plan, not a kill test |
| The January IdeaForge SaaS sketch | Guessed $29 / $99 | Self-serve scores, then done-for-you builds | Same repo, same scorers | It scores the writeup. It does not hold a conversation or a case file. |

### Customer Insights

No interviews yet. The only evidence is this design session.

### Market Data

- Year 1 target: one paying entrepreneur after the spike.
- National market size is not estimated. The spike is the decision.

---

## 🎓 Lessons Learned

[Update this section as you progress]

### What Worked

- The MRI session is the quality bar: mechanism first, live lookup, score second.

### What Didn't Work

- `evaluate.py` on its own prints the same next steps for every mid-scoring idea.

### What to Do Differently

- The model writes the critique. The scorers keep the numbers.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-13-ideaforge-lab
category: api-services
scores:
  market_demand: 6
  technical_feasibility: 6
  time_to_revenue: 5
  scalability: 6
  initial_investment: 8
  competitive_advantage: 5
  automation_potential: 6
  recurring_revenue: 8
total_score: 60.0
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "Chat plus card plus case file. Spike before the full lab."
```

---

**Last Updated:** 2026-10-13  
**Next Review:** 2026-10-27
