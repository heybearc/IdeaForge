---
description: Passive Income Lab - Idea to Revenue Workflow
---

# Passive Income Lab Workflow

## Quick Commands

- `/idea` - Create and evaluate a new passive income idea
- `/validate` - Run market validation on an idea
- `/rank` - Rank all ideas by success probability
- `/build` - Start building an MVP for a validated idea

## Workflow Steps

### 1. Brainstorm New Idea

```bash
# Create new idea from template
cp frameworks/idea-template.md ideas/brainstorm/$(date +%Y-%m-%d)-idea-name.md

# Edit the file and fill in all sections
# Focus on: problem, target audience, revenue model, evaluation scores
```

### 2. Evaluate Idea

```bash
# Run ML evaluation
python3 ml-engine/idea-scorer/evaluate.py ideas/brainstorm/YYYY-MM-DD-idea-name.md

# Review the output:
# - Total score (aim for 60+)
# - Success probability
# - Strengths and weaknesses
# - Recommended next steps
```

### 3. Move to Evaluated (if score >= 60)

```bash
# Move to evaluated folder
mv ideas/brainstorm/YYYY-MM-DD-idea-name.md ideas/evaluated/

# Or archive if score < 40
mv ideas/brainstorm/YYYY-MM-DD-idea-name.md ideas/archived/
```

### 4. Market Validation (for ideas scoring 60+)

**Week 1-2 Validation Checklist:**

- [ ] Research 5 competitors
  - Pricing models
  - Feature sets
  - Strengths/weaknesses
  - Revenue estimates

- [ ] Interview 20 potential customers
  - What's their current pain point?
  - What solution are they using now?
  - How much would they pay?
  - What features are must-haves?

- [ ] Validate pricing
  - Survey target market
  - Compare to competitors
  - Test willingness to pay

- [ ] Create landing page
  - Clear value proposition
  - Email signup form
  - Pricing preview
  - Deploy to Proxmox

- [ ] Collect 50+ email signups
  - Post on Reddit (relevant subreddits)
  - Share in Discord communities
  - Product Hunt teaser
  - Twitter/X posts

**Validation Success Criteria:**
- 50+ email signups
- 10+ customer interviews completed
- Pricing validated (3+ people say "I'd pay $X")
- Clear understanding of must-have features

### 5. Build MVP (for validated ideas scoring 80+)

**Week 3-6 Development:**

```bash
# Create project structure
mkdir -p active-projects/project-name/{backend,frontend,docs}

# Set up infrastructure
# - Create LXC container on Proxmox
# - Set up PostgreSQL database
# - Configure reverse proxy

# Development checklist:
# - [ ] Backend API (FastAPI/Django)
# - [ ] Frontend UI (Next.js)
# - [ ] Authentication
# - [ ] Payment processing (Stripe)
# - [ ] Core features (MVP only!)
# - [ ] Documentation
# - [ ] Beta testing with 10 users
```

**MVP Success Criteria:**
- Core features working
- 10 beta users actively testing
- Payment processing functional
- Positive feedback from beta users

### 6. Launch (Week 7-8)

**Launch Checklist:**

- [ ] Public launch announcement
  - Product Hunt
  - Reddit (relevant subreddits)
  - Hacker News
  - Twitter/X
  - LinkedIn

- [ ] Marketing materials ready
  - Demo video
  - Screenshots
  - Case studies/testimonials
  - Documentation

- [ ] Monitoring in place
  - Error tracking
  - Analytics
  - Performance monitoring
  - Customer support system

- [ ] First paying customers
  - Convert beta users
  - Launch discount (optional)
  - Collect feedback

**Launch Success Criteria:**
- 10+ paying customers in first month
- Positive reviews/feedback
- No critical bugs
- Clear path to profitability

### 7. Growth & Optimization (Month 3-6)

**Automation Checklist:**

- [ ] Automate operations
  - Monitoring and alerts
  - Billing and invoicing
  - Customer onboarding
  - Support documentation

- [ ] Scale infrastructure
  - Load testing
  - Performance optimization
  - Backup and disaster recovery

- [ ] Expand features
  - Based on customer feedback
  - Competitive analysis
  - Usage analytics

- [ ] Optimize conversion
  - A/B test pricing
  - Improve onboarding
  - Reduce churn
  - Upsell/cross-sell

**Growth Success Criteria:**
- 90%+ automation achieved
- Profitable (revenue > costs)
- Growing customer base
- Positive unit economics

### 8. ML Feedback Loop

**Update Training Data:**

```bash
# Update idea outcome in ML training data
# Edit: ml-engine/models/training_data.json

# Add actual results:
{
  "idea_id": "YYYY-MM-DD-idea-name",
  "outcome": "launched|profitable|failed",
  "actual_revenue_30d": 1000,
  "actual_revenue_90d": 5000,
  "actual_revenue_1y": 25000,
  "time_invested_hours": 160,
  "customer_count": 50,
  "automation_achieved": 0.85,
  "lessons_learned": "What worked, what didn't, what to do differently"
}
```

**This data trains the ML model to:**
- Predict success more accurately
- Identify your personal success patterns
- Recommend better ideas over time
- Optimize for your strengths

## Ranking Ideas

```bash
# Rank all evaluated ideas
python3 ml-engine/idea-scorer/evaluate.py rank ideas/evaluated/

# Output shows:
# 1. Highest probability ideas first
# 2. Score and category
# 3. Recommended action
```

## Key Principles

1. **Validate Before Building** - Always validate market demand first
2. **Start Small** - MVP should take 4-6 weeks max
3. **Leverage Assets** - Use existing infrastructure and code
4. **Automate Early** - Build automation from day 1
5. **Track Everything** - Feed data back to ML system
6. **Iterate Fast** - Launch, learn, improve

## Common Mistakes to Avoid

- ❌ Building before validating market demand
- ❌ Over-engineering the MVP
- ❌ Ignoring customer feedback
- ❌ Not tracking metrics from day 1
- ❌ Trying to automate too early (before product-market fit)
- ❌ Competing on features instead of solving a real problem

## Success Metrics

Track these for every project:

- **Time to First Dollar**: Days from start to first revenue
- **Customer Acquisition Cost**: Marketing spend / new customers
- **Lifetime Value**: Average revenue per customer
- **Churn Rate**: % of customers who cancel
- **Automation Level**: % of time it runs without you
- **Profitability**: Monthly revenue - monthly costs

## Resources

- Evaluation Matrix: `frameworks/evaluation-matrix.md`
- Idea Template: `frameworks/idea-template.md`
- ML Scorer: `ml-engine/idea-scorer/evaluate.py`
- Success Patterns: `knowledge-base/success-patterns/`
- Active Projects: `active-projects/`
