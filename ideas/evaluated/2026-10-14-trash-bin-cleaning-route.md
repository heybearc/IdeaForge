# Trash Bin Cleaning Route

**Date Created:** 2026-10-14
**Category:** local-services
**Status:** evaluated
**Creator:** Cory

Sparked by [Bin Bath's Cleveland pricing](https://binbath.com/cleveland/#pricing). This card is the model, not a plan to open a second Cleveland company.

---

## 🎯 Core Concept

A truck washes trash carts on the city's trash day, on a repeating schedule, and bills the card without a new sale each visit.

### Problem Being Solved

A cart smells, draws pests, and nobody wants to scrub it. The buyer already rolls it to the curb on a day the city chose.

### Target Audience

**Who pays**

- A household, per visit, on a monthly, bi-monthly, or quarterly plan. Two bins are the base. An extra bin is a small add-on because the truck is already stopped.

**Who does the work**

- A driver and a reclaim rig. Not a software product.

### Unique Value Proposition

Bin Bath already runs this in Cleveland and Akron. The worth copying is the offer design. The one-time wash is priced to make the schedule the normal purchase. The truck keeps the wastewater. Signup, reminders, and card renewal are route software, not a custom app.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — a visit plan, billed per stop
- [ ] Usage-based pricing
- [ ] One-time purchase — listed, and priced as the expensive way to get one wash
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

Bin Bath's posted Cleveland prices, checked 2026-10-14:

- Every 4 weeks: $27 a visit for up to 2 bins, 12 visits a year
- Every 8 weeks: $36 a visit, 6 a year
- Every 12 weeks: $41 a visit, 4 a year
- One-time: $79 a visit
- Each extra bin: $10 on any of those

Twelve visits at $27 is $324 a year. Four visits at $41 is $164 a year. The monthly plan is not the cheap plan. It is the full plan, and each visit looks cheaper than showing up once. The truck wants the stop every trash cycle. The extra bin is margin because the stop was already paid for.

**Revenue scenario (unvalidated):**

No year-1 revenue is estimated. Equipment sites publish income charts. Those charts are not used here. A route's revenue is stops times the posted visit price, after fuel, disposal, insurance, and the truck payment. None of that has been counted for a specific town.

---

## 🔧 Technical Requirements

### What the business actually is

A reclaim wash on a trailer or truck, a tow vehicle, wastewater disposal, and a route that follows trash day. [MyRoutePro](https://myroutepro.com/system/) is the software Bin Bath's site runs on: enrollment, reminders, card renewal, and route assignment. Their 1,000-customer plan is $195 a month.

### Existing Assets to Leverage

- [ ] Proxmox, QuantShift, or the scorers — none of these wash a cart
- [ ] A reclaim trailer
- [ ] A filled street on one trash day

### Development Estimate

Not a software build. A compliant hot-water trailer is the start. [The Bin Trailer](https://thebintrailer.com/cost-to-buy-new-trash-bin-cleaning-equipment-trailer/) lists a new single cold-water unit at $29,999 and a double hot-water unit at $45,999, before a tow vehicle, tax, and operating cash. A 2026 roundup puts a trailer business with vehicle and reserve at about $35,000 to $80,000. A franchise package is higher. Those are other people's quotes, not a bid for this lab.

### Infrastructure Costs

- Rig: tens of thousands for the version that keeps the water on the truck
- Route software: about $195 a month once there are customers
- A hose-and-wand test is cheaper and is not this business. Dirty water in a storm drain is the thing the truck exists to avoid

---

## 📊 Evaluation Scores

### Market Demand: 7 / 10

**Evidence:**

- [x] A live local company with posted prices and a suburb list, including Cleveland, Akron, Hudson, Solon, Twinsburg, and Westlake
- [x] The category is a known route business, with trailer makers and route software sold to it
- [ ] No conversations with households that are not already Bin Bath customers

**Notes:** Demand for the service is proven by a company charging for it on this map. Demand for a second brand on the same streets is not.

### Technical Feasibility: 4 / 10

**Skills Match:**

- [ ] This lab's stack does the work
- [x] A person can learn the route
- [ ] The hard part is the rig, the disposal permit, and showing up on trash day

**Notes:** Feasible as a small business someone chooses as a job. Not feasible as a build inside IdeaForge.

### Time to Revenue: 6 / 10

**Timeline:**

- First dollar: after a rig and a few streets, measured in months, not a weekend
- The equipment vendor says there is no guaranteed payback period

**Notes:** Faster than a licensed finance app. Slower than a landing page. The delay is filling one trash day, not writing code.

### Scalability: 3 / 10

**Automation Level:**

- Current: a driver and a truck
- Target: more streets means more driver-days
- A second truck is a hire

**Notes:** This is the weight that decides the card. Revenue tracks labor and equipment. It does not grow while the owner is elsewhere. Route software removes the scheduling chore. It does not remove the wash.

### Initial Investment: 1 / 10

**Costs:**

- The clever rig: about $30,000 to $46,000 for a new trailer, plus a vehicle and reserve
- Matrix band for a 1 is $10,000 or more

**Notes:** Cash is the opposite of the homelab ideas. A cheap wand is a different offer, and it fails the wastewater rule that makes the Cleveland company acceptable on a driveway.

### Competitive Advantage: 3 / 10

**Moats:**

- [ ] Unique expertise from this lab
- [ ] First mover in Cleveland-Akron — Bin Bath is already there
- [x] Route density — a moat only after the stops exist, which is the incumbent's moat

**Notes:** The model is copyable. The filled route is not. Starting here means taking streets from a company that already published the price.

### Automation Potential: 3 / 10

**Manual Tasks:**

- Billing and reminders: MyRoutePro
- The wash, the driving, and the disposal: a person, every trash day
- Marketing: door hangers and a signup page until a street is dense

**Notes:** Half or more of the work stays manual. That is the business.

### Recurring Revenue: 10 / 10

**Model:**

- [x] Subscription — the visit plan
- [ ] Usage-based
- [ ] Repeat purchases
- [ ] One-time — offered, and priced so the plan is the normal buy

**Notes:** This is the part that is actually clever, and it earns the top of the scale. The customer is sold a place on a calendar. The card renews. The one-time price is the penalty for not joining.

---

## 📈 Total Score: 43.0 / 100

**Weighted Score Calculation:**

```
(7 × 0.15) +
(4 × 0.10) +
(6 × 0.15) +
(3 × 0.20) +
(1 × 0.10) +
(3 × 0.15) +
(3 × 0.10) +
(10 × 0.05) = 4.30 → 43.0 / 100
```

**Decision:** Refine Idea

Keep the lesson. Do not start a bin company from this lab, and do not build software for one. Cleveland and Akron already have the operator. The score is low because the work scales with trucks and the rig costs more than $10,000, not because the offer is dumb.

The lesson worth keeping: sell a repeating stop on a calendar the buyer does not control, price a single visit so the plan is the obvious buy, and charge a small amount for the extra unit once the stop exists.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The map is taken**: Bin Bath already publishes Cleveland, Akron, and the suburbs.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not open against them. The card is the pattern, not a launch.

2. **The truck is the company**: Without reclaim, the driveway and the storm drain are the product, and towns can stop that.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not test this with a consumer pressure washer.

3. **Vendor income sheets**: Trailer sellers publish revenue. A thin route still owes the payment.
   - **Likelihood**: High
   - **Impact**: Medium
   - **Mitigation**: No revenue projection on this card.

---

## 🚀 Opportunity Analysis

### What the pattern is worth

1. A filled trash day is the asset. Software is how the card gets charged.
2. The same shape shows up in other route jobs. It does not make those jobs passive.
3. It does not transfer to a national app. The constraint is a municipal trash calendar.

### Adjacent ideas that are not this card

- MRI stays a center-paid booking test. A bin route does not make that true.
- A SaaS for bin companies is MyRoutePro. That shelf is occupied.

---

## ✅ Next Steps

### Do not build

- [x] Name the mechanism: repeating stop, plan priced against a painful one-time visit, extra bin is margin, water stays on the truck
- [ ] Do not buy a trailer, print door hangers, or sketch a competing app
- [ ] If the pattern is reused, reuse it on a card where someone else already does the physical work

---

## 📝 Research Notes

### What Bin Bath posted

Source: [Bin Bath Cleveland pricing](https://binbath.com/cleveland/#pricing), 2026-10-14.

| Plan | Cadence | Visit price, up to 2 bins |
|------|---------|---------------------------|
| Monthly | Every 4 weeks, 12 a year | $27 |
| Bi-monthly | Every 8 weeks, 6 a year | $36 |
| Quarterly | Every 12 weeks, 4 a year | $41 |
| One-time | Once | $79 |

Additional bins are $10 each per visit on every plan. The site says the rig uses 200-degree water at 3,500 psi and hauls the wastewater away. The site is powered by MyRoutePro.

### Equipment, not a quote for us

- New trailer list prices: $29,999 cold, $45,999 hot, from The Bin Trailer. They also say payback is not guaranteed.
- A separate 2026 cost roundup puts trailer plus vehicle plus reserve at about $35,000 to $80,000.
- MyRoutePro: $195 a month for up to 1,000 customers on the plan page checked with this card.

---

## 🎓 Lessons Learned

### What Worked

- The offer is legible in one screen. Plan, visit price, extra bin, and the cities are all visible.

### What Didn't Work

- Reading a clever local route as a software idea, or as passive income.

### What to Do Differently

- When a business looks clever, write down which number is doing the work. Here it is the repeating visit, not the wash recipe.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-14-trash-bin-cleaning-route
category: local-services
scores:
  market_demand: 7
  technical_feasibility: 4
  time_to_revenue: 6
  scalability: 3
  initial_investment: 1
  competitive_advantage: 3
  automation_potential: 3
  recurring_revenue: 10
total_score: 43.0
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "Bin Bath is a real route. The clever part is the repeating paid stop. It is not an IdeaForge build. Cleveland is taken."
```

---

**Last Updated:** 2026-10-14
**Next Review:** None, unless the lesson is being applied to a different card.
