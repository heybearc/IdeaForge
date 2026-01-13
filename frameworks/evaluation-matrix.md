# Idea Evaluation Matrix

Use this framework to score every passive income idea objectively.

## Scoring System

Each criterion is scored 1-10 (10 = best). Total possible: 100 points.

### 1. Market Demand (Weight: 15%)
**Score: ___ / 10**

- Is there proven demand for this solution?
- Are people actively searching for it?
- Do competitors exist and are they profitable?
- Can you validate demand in 1 week?

**Evidence Required:**
- [ ] Reddit/Discord discussions about the problem
- [ ] Competitor revenue estimates
- [ ] Google Trends data
- [ ] 10+ potential customer conversations

---

### 2. Technical Feasibility (Weight: 10%)
**Score: ___ / 10**

- Can you build it with existing skills?
- Are required technologies mature/stable?
- Can you build MVP in 2-4 weeks?
- Do you have infrastructure already?

**Leverage Your Strengths:**
- ✅ Proxmox/LXC/containerization
- ✅ Django/Next.js/FastAPI
- ✅ Trading algorithms/QuantShift
- ✅ Multi-agent development
- ✅ MCP server architecture

---

### 3. Time to Revenue (Weight: 15%)
**Score: ___ / 10**

- 10 = Revenue in 1-2 weeks
- 7 = Revenue in 1-2 months
- 5 = Revenue in 3-6 months
- 3 = Revenue in 6-12 months
- 1 = Revenue in 12+ months

**Target:** First dollar within 30 days of launch

---

### 4. Scalability (Weight: 20%)
**Score: ___ / 10**

- Can revenue grow without proportional time investment?
- Is it software/digital (vs. service-based)?
- Can it serve 100x customers with minimal changes?
- Are marginal costs near zero?

**Passive Income Test:**
- Can it run for 1 week without your involvement?
- Can it handle growth automatically?

---

### 5. Initial Investment (Weight: 10%)
**Score: ___ / 10**

- 10 = $0-100 (use existing infrastructure)
- 7 = $100-500
- 5 = $500-2,000
- 3 = $2,000-10,000
- 1 = $10,000+

**Your Advantage:** Existing Proxmox infrastructure = near-zero hosting costs

---

### 6. Competitive Advantage (Weight: 15%)
**Score: ___ / 10**

- What makes this defensible?
- Do you have unique expertise/data/infrastructure?
- Is there a network effect or lock-in?
- Can competitors easily replicate it?

**Your Moats:**
- Homelab infrastructure expertise
- Trading algorithm knowledge
- Multi-agent development workflows
- MCP server early adoption

---

### 7. Automation Potential (Weight: 10%)
**Score: ___ / 10**

- 10 = 100% automated (no manual work)
- 7 = 90% automated (weekly check-in)
- 5 = 75% automated (daily involvement)
- 3 = 50% automated (significant manual work)
- 1 = Mostly manual labor

**Goal:** 90%+ automation within 3 months

---

### 8. Recurring Revenue (Weight: 5%)
**Score: ___ / 10**

- 10 = Monthly/annual subscriptions
- 7 = Usage-based recurring fees
- 5 = Repeat purchases likely
- 3 = One-time sales with upsells
- 1 = Pure one-time transactions

**Target:** Subscription or usage-based model

---

## Calculation

```
Total Score = (Market Demand × 0.15) + 
              (Technical Feasibility × 0.10) + 
              (Time to Revenue × 0.15) + 
              (Scalability × 0.20) + 
              (Initial Investment × 0.10) + 
              (Competitive Advantage × 0.15) + 
              (Automation Potential × 0.10) + 
              (Recurring Revenue × 0.05)
```

## Interpretation

- **80-100**: Excellent - Prioritize immediately
- **60-79**: Good - Validate market demand this week
- **40-59**: Moderate - Needs refinement or pivot
- **20-39**: Weak - Reconsider or archive
- **0-19**: Poor - Archive and learn from it

## Decision Matrix

| Score | Action |
|-------|--------|
| 80+ | Build MVP this month |
| 60-79 | Validate with 20+ customer conversations |
| 40-59 | Refine idea, re-evaluate in 2 weeks |
| <40 | Archive, document lessons learned |

## Risk Assessment

Document top 3 risks for any idea scoring 60+:

1. **Market Risk**: ___
2. **Technical Risk**: ___
3. **Execution Risk**: ___

**Mitigation Strategies:**
- Risk 1: ___
- Risk 2: ___
- Risk 3: ___

## Opportunity Analysis

What could make this idea 10x bigger?

1. **Market Expansion**: ___
2. **Product Evolution**: ___
3. **Partnership Potential**: ___

## Next Steps Template

Based on score:

**If 80+:**
- [ ] Week 1: Build MVP
- [ ] Week 2: Beta test with 10 users
- [ ] Week 3: Launch publicly
- [ ] Week 4: First paying customers

**If 60-79:**
- [ ] Week 1: 20 customer interviews
- [ ] Week 2: Refine based on feedback
- [ ] Week 3: Re-evaluate score
- [ ] Week 4: Decide: build or pivot

**If 40-59:**
- [ ] Identify core weakness
- [ ] Brainstorm 3 variations
- [ ] Re-evaluate best variation
- [ ] Archive if still <60

## ML Training Data

Every evaluated idea becomes training data:

```yaml
idea_id: YYYY-MM-DD-idea-name
scores:
  market_demand: X
  technical_feasibility: X
  time_to_revenue: X
  scalability: X
  initial_investment: X
  competitive_advantage: X
  automation_potential: X
  recurring_revenue: X
total_score: XX
outcome: [not_started|validated|launched|profitable|failed|archived]
actual_revenue_30d: $X
actual_revenue_90d: $X
actual_revenue_1y: $X
lessons_learned: "..."
```

This data trains the ML model to predict success more accurately over time.
