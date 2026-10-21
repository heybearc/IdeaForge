# Trading Signal Aggregator API

**Date Created:** 2026-10-14
**Category:** trading-bots
**Status:** evaluated
**Creator:** Cory

This revises `ideas/evaluated/2026-01-04-trading-signal-aggregator.md`. That file stays as the January score of 85.0. The open list had drifted to 83.5. The January prices are not reused.

---

## 🎯 Core Concept

An API that takes alerts from TradingView, indicator vendors, and custom bots and turns them into webhook or REST calls a broker can trade. January priced that at $29 a month and up, and said no unified API existed.

### Problem Being Solved

A trader with more than one alert source does not want to retype orders. That pipe already exists. TradersPost and SignalStack both accept TradingView and TrendSpider webhooks and send orders to a connected broker or exchange.

### Target Audience

**Who would have to pay**

- An algorithmic trader who wants one webhook in front of their own broker.

**Who already paid someone else**

- That trader. TradersPost Starter is $49 a month for one live account. SignalStack is $27 a month for 50 signals, $97 for 250, and $347 for 1,000, with a free tier of 5 signals a month. Those are their own posted prices.

### Unique Value Proposition

January's moat was QuantShift in production, TradeConfident indicators, and being first. QuantShift can keep consuming its own signals. That does not make a public pipe. TradeConfident was a hoped-for partnership, not a contract on the card. First is gone.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual)
- [x] Usage-based pricing — SignalStack already bills this way
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

No new price. The seat is $27 to $49 a month for the small plan. Matching it means winning a switch from a tool the trader already connected to TradingView. Nothing on the card shows why they would switch.

**Revenue scenario (unvalidated):**

- Month 1: $0
- Month 6: $0 unless QuantShift's private path is mistakenly counted as revenue
- Month 12: unknown. Not the January "40 customers" path

---

## 🔧 Technical Requirements

### What a first version would be

A webhook that places an order. TradersPost's docs already specify that JSON. Building a worse copy is feasible and pointless. A multi-tenant version also inherits broken-alert support.

### Tech Stack

- FastAPI and webhooks
- Broker connections the card assumed would be easy because QuantShift has one broker

### Existing Assets to Leverage

- [x] QuantShift, as a private consumer of signals for its own strategies
- [ ] A marketplace of other people's indicators
- [ ] An exclusive TradeConfident deal

### Development Estimate

- A private webhook for QuantShift: small, and it is not this business
- A public aggregator meant to replace TradersPost: a company, not a six-week port

### Infrastructure Costs

- Hosting: low
- The cost that matters is being on the hook when an alert double-fires into a live account

---

## 📊 Evaluation Scores

### Market Demand: 5 / 10

**Evidence:**

- [x] TradersPost and SignalStack docs and pricing checked on 2026-10-14
- [ ] Customer interviews: 0

**Notes:** Traders pay for this category. TradersPost has been selling the webhook since 2021. Demand for another entrant is not shown. January's "no unified API" line is false.

### Technical Feasibility: 7 / 10

**Skills Match:**

- [x] Can build a webhook and an order with existing skills
- [x] Requires learning: every extra broker, and the failure modes of someone else's Pine script
- [x] QuantShift already runs strategies. That is one user

**Notes:** Feasible as software. The January "just expose QuantShift" skips tenancy, broker coverage, and alert audit logs.

### Time to Revenue: 4 / 10

**Timeline:**

- First dollar: not week 6. The buyer already has a posted vendor at $27 or $49
- Switching cost sits with the incumbent, which January counted as a moat for this card

**Notes:** A private feed inside QuantShift has no customer to charge. A public feed has to take one from TradersPost or SignalStack.

### Scalability: 7 / 10

**Automation Level:**

- Current: 0% as a product
- Target: alerts in, orders out
- A bad alert is still a human incident

**Notes:** An API scales better than a custody app. It does not run unattended when orders hit the wrong account.

### Initial Investment: 7 / 10

**Costs:**

- Hosting: about $0
- Legal: higher if this app originates or republishes someone else's signals as recommendations. Lower if the user only routes their own alert. The card mixed those
- Marketing against an incumbent: not the January $200

**Notes:** A prototype is cheap. A product that republishes TradeConfident is not a disclaimer problem only.

### Competitive Advantage: 2 / 10

**Moats:**

- [x] QuantShift exists — as a user of signals, not a network
- [ ] Proprietary signal quality — not on this card
- [ ] First mover — TradersPost and SignalStack
- [ ] TradeConfident exclusive — not signed
- [ ] Low-latency homelab — not why a trader picks a webhook

**Notes:** The pipe is the easy part to copy, and two companies already run it.

### Automation Potential: 7 / 10

**Manual Tasks:**

- Routing: automatic
- New brokers and bad payloads: manual
- Marketing: none until there is a reason to switch

**Notes:** The happy path is automated. The business is the unhappy path.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription
- [x] Usage-based
- [ ] Repeat purchases
- [ ] One-time

**Notes:** Both shapes are already how this category charges. Untested here. A 10 would mean a trader renewed.

---

## 📈 Total Score: 55.5 / 100

**Weighted Score Calculation:**

```
(5 × 0.15) +
(7 × 0.10) +
(4 × 0.15) +
(7 × 0.20) +
(7 × 0.10) +
(2 × 0.15) +
(7 × 0.10) +
(8 × 0.05) = 5.55 → 55.5 / 100
```

**Decision:** Refine Idea

Do not build the public API. The January 85.0 does not hold. Keep signal handling inside QuantShift. Archive this card unless one sentence names a routing job TradersPost and SignalStack do not do, for a trader who already pays one of them.

The scorer will print a success probability above 55.5 because `trading-bots` gets an expertise multiplier. That multiplier is not a reason to sell webhooks.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The pipe is the whole product, and it is for sale**: A new webhook URL does not change the trader's broker coverage.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not launch a second pipe.

2. **Republishing signals is advice**: Aggregating TradeConfident or a Discord into orders other people follow is a different license question than routing the user's own alert.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: Do not originate or resell signals. QuantShift may keep using the ones it already has.

3. **A live order is an incident**: Double alerts and bad quantity fields lose money immediately.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: No public endpoint.

---

## 🚀 Opportunity Analysis

### What would have to be true

1. A broker or alert source the two incumbents refuse, that a named trader will pay to connect.
2. Not a signal marketplace. That is a publisher business on top of a crowded pipe.
3. Not "add crypto and forex." Both incumbents already list those asset classes.

### Adjacent ideas that are not this card

- QuantShift's own strategies stay on the QuantShift card.
- Backtesting-as-a-service was a January aside. It is not scored here.

---

## ✅ Next Steps

### Refine (this card)

- [ ] Name one paid routing job TradersPost and SignalStack do not do
- [ ] If it cannot be named in one sentence, archive this idea
- [ ] Do not wrap QuantShift's private signals in a public API to test the sentence

---

## 📝 Research Notes

### Competitor Analysis

Checked 2026-10-14.

| Competitor | Pricing | What it does |
|-----------|---------|--------------|
| TradersPost | Starter $49/month, one live account, from their site as checked by PropKoala on 2026-09-28 and their own SignalStack comparison | TradingView, TrendSpider, and custom JSON to a broker. Stocks, options, futures, crypto |
| SignalStack | Free up to 5 signals/month. Basic $27 / 50, Premium $97 / 250, Pro $347 / 1,000. Retail table on their help center. The public pricing page was discounting the first year | Same job, billed per signal. Webhook per connected broker |

### Customer Insights

Zero interviews. The January competitor note said TradingView alerts and Discord bots, and missed the companies whose only job is this webhook.

### Market Data

January's 40-customer month-3 path is not reused.

---

## 🎓 Lessons Learned

### What Worked

- QuantShift having a real signal path is useful for QuantShift.

### What Didn't Work

- "No unified API exists" as a scored moat.
- Counting switching costs as an advantage before having a user.

### What to Do Differently

- Search for the webhook product by the job ("TradingView alert to broker"), not by the word aggregator.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-14-trading-signal-aggregator
category: trading-bots
scores:
  market_demand: 5
  technical_feasibility: 7
  time_to_revenue: 4
  scalability: 7
  initial_investment: 7
  competitive_advantage: 2
  automation_potential: 7
  recurring_revenue: 8
total_score: 55.5
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "January 85 does not hold. TradersPost and SignalStack already route alerts to brokers. Keep signals inside QuantShift."
```

---

**Last Updated:** 2026-10-14
**Next Review:** Only if a one-sentence gap is written. Otherwise archive.
