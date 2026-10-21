# Crypto Dollar-Cost Averaging Bot

**Date Created:** 2026-10-14
**Category:** trading-bots
**Status:** evaluated
**Creator:** Cory

This revises `ideas/brainstorm/2026-01-05-crypto-dollar-cost-averaging-bot.md`. That file stays as the January score of 87.0. The open list had drifted to 86. The January prices are not reused.

---

## 🎯 Core Concept

A subscription bot that buys crypto on a schedule for people who will not watch the market. January also had it buy dips during the week, rebalance, and spread buys across coins, on Kraken, Gemini, or Coinbase, for $9, $19, or $49 a month.

### Problem Being Solved

People freeze when they try to time a buy. A fixed schedule fixes that. The exchanges already run that schedule.

### Target Audience

**Who would have to pay**

- Someone putting $50 to $500 a month into bitcoin or ether who does not want to press the button.

**Who already has the button**

- That same person, inside Coinbase, River, Strike, Swan, Kraken, or Cash App.

### Unique Value Proposition

January said the bot would be cheaper than Coinbase and smarter than a blind weekly buy. A weekly buy is the product people actually want, and it is already free or close to it. A dip-buying bot is a different product, and 3Commas already sells that one.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — only if someone pays more than the exchange charges to do this
- [ ] Usage-based pricing
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

No new price. Nine dollars a month on a $200 contribution is 4.5% before the exchange fee. On a $50 contribution it is 18%. River and Strike waive the recurring-buy trading fee after the first week and keep a spread of roughly a quarter of a percent or less. That is the comp. A second subscription does not beat it.

**Revenue scenario (unvalidated):**

- Month 1: $0
- Month 3: $0 on this offer
- Month 12: not the January figure. No interviews, no customers, and the feature shipped inside the exchanges while the card sat

---

## 🔧 Technical Requirements

### What a first version would be

Exchange API keys, a schedule, and an order. That is a small program. It is also a request that a stranger trust this app with trade permissions on their account. QuantShift does not shorten that. QuantShift is an Alpaca stock bot.

### Tech Stack

- A scheduler and exchange APIs
- A dashboard only if someone is paying for a view they do not get at the exchange

### Existing Assets to Leverage

- [ ] The QuantShift stock bot — different broker, different asset, different customer
- [x] General ability to call an API
- [ ] Custody, and it should stay that way. Touching customer coins makes this a financial institution

### Development Estimate

- A schedule that places orders: weeks
- A business someone pays for: not a build estimate. The exchanges already did the build

### Infrastructure Costs

- Hosting: about $0
- The real cost is support when an API key is wrong or a dip-rule buys a coin the user hates

---

## 📊 Evaluation Scores

### Market Demand: 4 / 10

**Evidence:**

- [x] Competitor check on 2026-10-14
- [ ] Customer interviews: 0, same as January. The January evidence boxes were unchecked

**Notes:** Recurring buys are a standard exchange feature. Spark's 2026 comparison lists Cash App Auto Invest near 0% (fees and spread removed February 2026), Strike near a 0.15% spread after the first week, River near 0.25% after seven days, Swan near 1% plus a spread, and Coinbase near 1.5% plus a spread. bitcoin.diy's 2026 exchange comparison agrees that River and Strike are the cheap end for automated DCA. 3Commas sells the other thing January mixed in: a bot that averages down and takes profit, connected to many exchanges. Demand for the behavior is real. Demand for a paid third app in front of a free button is not shown.

### Technical Feasibility: 6 / 10

**Skills Match:**

- [x] Can place scheduled orders with existing skills
- [x] Requires learning: keeping someone else's exchange keys safe, and not drifting into advice
- [ ] QuantShift is not a head start on this

**Notes:** The happy path is short. The January "seven weeks from the stock bot" is the wrong map.

### Time to Revenue: 4 / 10

**Timeline:**

- First dollar: not week 7. The substitute is already in the exchange app and costs less than this subscription
- A paying user inside six months would need a job the exchanges do not do

**Notes:** Matrix band between "3 to 6 months" and "6 to 12 months." The build is not the delay. The offer is.

### Scalability: 6 / 10

**Automation Level:**

- Current: 0% as a product
- Target: orders can run unattended
- The support load is keys, missed fills, and "why did it buy that"

**Notes:** Software scales. A consumer who handed over trade keys does not scale like a content site.

### Initial Investment: 7 / 10

**Costs:**

- Hosting: about $0
- A lawyer, if the dip rule is marketed as smarter than the user's own schedule
- January's $200 ad budget does not cover that

**Notes:** Cash to prototype is still low. Cash to sell "we buy the dips for you" is a compliance question the card scored as a disclaimer.

### Competitive Advantage: 2 / 10

**Moats:**

- [ ] Cheaper than Coinbase — River, Strike, and Cash App already are
- [ ] Smart timing — 3Commas already sells that, and it is not DCA
- [ ] Multi-exchange — several bots and the exchanges themselves
- [ ] QuantShift experience — stocks, via Alpaca

**Notes:** Nothing on the January moat list is still unowned.

### Automation Potential: 7 / 10

**Manual Tasks:**

- Order placement: automatic
- Key setup and "the bot did something I dislike": a person
- Marketing: none until the offer changes

**Notes:** The schedule itself is the automated part. The product people would argue about is the dip rule.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription
- [ ] Usage-based
- [ ] Repeat purchases
- [ ] One-time

**Notes:** A subscription is the right shape for a bot. It is untested, and the thing it replaces does not charge one. A 10 would mean renewals.

---

## 📈 Total Score: 51.0 / 100

**Weighted Score Calculation:**

```
(4 × 0.15) +
(6 × 0.10) +
(4 × 0.15) +
(6 × 0.20) +
(7 × 0.10) +
(2 × 0.15) +
(7 × 0.10) +
(8 × 0.05) = 5.10 → 51.0 / 100
```

**Decision:** Refine Idea

Do not build the consumer bot. The January 87.0 does not hold. Archive it unless one sentence names a paid job that Coinbase, River, Strike, Swan, Kraken, Cash App, and 3Commas do not already do. A dip-buying rule is not that sentence.

The scorer's success probability will sit above 51 because `trading-bots` gets an expertise multiplier. That is not demand. QuantShift stays its own card.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The feature is free where the money already sits**: A second app cannot undercut a fee that is already near zero.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not sell a schedule. The exchanges sell the schedule.

2. **Dip-buying is a trading bot wearing a savings costume**: Averaging down is how people blow up accounts, and it is a crowded bot category.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not add a timing rule to rescue the card.

3. **API keys are the custody problem in disguise**: Trade permission on a stranger's exchange account is the business, even if the coins never sit here.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: Do not collect keys for a product that should not be built.

---

## 🚀 Opportunity Analysis

### What would have to be true

1. A job the exchange recurring-buy screen does not do, for someone who already pays for that job.
2. Not "also stocks." That is QuantShift, and it is a broker-dealer's customer, not a crypto key.
3. Not a partnership with an exchange. They already shipped this.

### Adjacent ideas that are not this card

- Leave QuantShift on its own card.
- Leave wallet recovery parked. That market is recovery scams.

---

## ✅ Next Steps

### Refine (this card)

- [ ] Name one paid job the exchange recurring-buy buttons and 3Commas do not do
- [ ] If it cannot be named in one sentence, archive this idea
- [ ] Do not port QuantShift into a retail crypto app to find out

---

## 📝 Research Notes

### Competitor Analysis

Checked 2026-10-14.

| Competitor | What they charge to DCA | What they are |
|-----------|-------------------------|---------------|
| River, Strike | Recurring trading fee waived after the first week. Spread about 0.15% to 0.25% | The cheap version of this card |
| Cash App | Spark's comparison: Auto Invest fees and spread cut to about 0% in February 2026 | Already on the phone |
| Swan Bitcoin | About 0.99% plus a spread. First $10,000 of fees waived on Swan's own terms as reported in that comparison | Bitcoin-only, the "gap" January named |
| Coinbase | About 1.49% plus a spread on recurring buys. Still the expensive button, not an empty shelf | Where the user already is |
| Kraken | Recurring buys around 0.40% on the same comparison | Multi-coin, which January treated as a feature |
| 3Commas | Subscription DCA bots on many exchanges. Price tiers not copied | The dip-averaging product, not a savings plan |

### Customer Insights

Zero interviews. Nine months of not starting, while River, Strike, and Cash App made the paid-app version worse.

### Market Data

January's customer counts are not reused.

---

## 🎓 Lessons Learned

### What Worked

- QuantShift remains a real stock bot. It is not evidence for this card.

### What Didn't Work

- Scoring "Coinbase is expensive" as if no other exchange had shipped recurring buys.
- Calling a dip rule a moat.

### What to Do Differently

- If the exchange app has the button, the card is a feature request to them.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-14-crypto-dollar-cost-averaging-bot
category: trading-bots
scores:
  market_demand: 4
  technical_feasibility: 6
  time_to_revenue: 4
  scalability: 6
  initial_investment: 7
  competitive_advantage: 2
  automation_potential: 7
  recurring_revenue: 8
total_score: 51.0
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "January 87 does not hold. Exchange recurring buys are free or nearly free. Do not build a second subscription in front of them."
```

---

**Last Updated:** 2026-10-14
**Next Review:** Only if a one-sentence gap is written. Otherwise archive.
