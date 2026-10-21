# Crypto Micro-Investing App

**Date Created:** 2026-10-14
**Category:** automation-services
**Status:** evaluated
**Creator:** Cory

This revises `ideas/brainstorm/2026-01-05-crypto-micro-investing-app.md`. That file stays as the January score of 81.5. The open list had drifted to 78. The January prices are not reused.

---

## 🎯 Core Concept

Round everyday card purchases up to the next dollar and buy bitcoin with the spare change. January called it Acorns for crypto, at a few dollars a month, after Plaid and a mobile app.

### Problem Being Solved

People will not open an exchange and buy $0.50 of bitcoin. Spare-change investing is a real behavior. Acorns already does it for ETFs. Direct bitcoin on spend is already Fold and Lolli.

### Target Audience

**Who would have to pay**

- A consumer who wants bitcoin from ordinary spending and will trust a new app with a linked card or bank.

**Who already does this**

- Acorns customers, with round-ups into ETFs and only a small bitcoin-futures ETF sleeve, not direct bitcoin.
- Fold customers, with bitcoin round-ups, Auto-Stack, and rewards cards. Custody and exchange sit at BitGo, which is how Fold reaches all 50 states without collecting its own money-transmitter licenses.
- Lolli customers. On 2026-05-19 Lolli launched automatic bitcoin back on linked Visa and Mastercard purchases across a merchant network. The Block reported more than 600,000 accounts.

### Unique Value Proposition

January said Coinbase had dropped round-ups and Acorns would not do crypto, so a fast app could be first. Acorns still does not sell direct bitcoin. That did not leave the shelf empty. Fold and Lolli took the direct-bitcoin version. Education and gamification are not a substitute for a license.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — the Acorns shape
- [ ] Usage-based pricing
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

No new price. A subscription of a few dollars a month only works after the app can legally pull dollars from a bank and convert them. January's $625 budget was app-store fees and a Plaid sandbox. It was not the license, the sponsor bank, or custody.

**Revenue scenario (unvalidated):**

- Month 1: $0
- Month 6: $0. There is no partner and no license
- Month 12: $0 on a solo build. Not the January 1,000-customer path

---

## 🔧 Technical Requirements

### What a first version would be

Not a React Native screen. Pulling spare change from a bank and buying bitcoin is money transmission and custody. "The user holds their own keys" does not remove that. Someone still moves the dollars and buys the coin before the user can hold it.

The known way through, which Fold uses, is a chartered custody partner such as BitGo, plus a bank for the spending account. That is a vendor relationship and a compliance program, not an MVP.

### Tech Stack

- Mobile app and Plaid, only after a licensed buyer and a bank exist
- QuantShift does not buy $0.50 of bitcoin for a consumer

### Existing Assets to Leverage

- [ ] QuantShift
- [ ] A money-transmitter license or a chartered partner
- [ ] A sponsor bank
- [x] The ability to build a screen, which is the small part

### Development Estimate

- A demo that round-ups a fake purchase: weeks
- A product that moves customer money: not estimated here, because the gate is legal

### Infrastructure Costs

- January: about $625
- Actual start: legal and a custody partner. That is thousands at the low end, and state licensing is the expensive path Fold paid BitGo to avoid. No quote is invented here

---

## 📊 Evaluation Scores

### Market Demand: 4 / 10

**Evidence:**

- [x] Acorns, Fold, Lolli, and BitGo checked on 2026-10-14
- [ ] Customer interviews: 0. January's four evidence boxes were unchecked

**Notes:** Round-ups work. Acorns is the proof, and Acorns round-ups buy ETFs. Direct bitcoin on everyday spend is Fold (round-ups and recurring buys, BitGo custody) and Lolli (card-linked bitcoin back, May 2026). The behavior is taken. A new app has no interview and no reason for those users to move.

### Technical Feasibility: 3 / 10

**Skills Match:**

- [x] Can build an app screen
- [ ] Can legally convert customer dollars to bitcoin
- [ ] Plaid plus QuantShift is not that capability

**Notes:** The matrix asks for an MVP in two to four weeks with skills already in hand. This MVP is a financial institution. Three is "only with a partner that is not on the card."

### Time to Revenue: 2 / 10

**Timeline:**

- First dollar: past a year on a solo license path
- Faster only if a chartered partner accepts the app, which is a sales process with no lead

**Notes:** Between "6 to 12 months" and "12+ months," and the longer side is the honest one without a sponsor.

### Scalability: 5 / 10

**Automation Level:**

- Current: 0%
- Target: round-ups without a clerk, after the rails exist
- Bank-link failures are a support queue

**Notes:** Consumer fintech can scale after it is allowed to operate. The score is not January's 9, because the marginal cost includes the partner, Plaid, and failed links.

### Initial Investment: 3 / 10

**Costs:**

- App stores: about $125, which is what January mostly counted
- Custody partner, bank, counsel: the real bill, in the thousands before a user
- State-by-state licensing: the bill Fold structured itself to avoid

**Notes:** Matrix band for a 3 is $2,000 to $10,000. A self-licensed transmitter can clear the top of the next band. Three is the charitable reading.

### Competitive Advantage: 2 / 10

**Moats:**

- [ ] First mover — Fold and Lolli
- [ ] Acorns does not sell spot bitcoin — true, and not enough
- [ ] Lower fees, education, gamification — not a license

**Notes:** A public bitcoin rewards company with a chartered custodian is the moat. A new screen is not.

### Automation Potential: 5 / 10

**Manual Tasks:**

- The round-up, once legal: automatic
- Compliance, bank exceptions, and support: not a weekly check-in
- Marketing: none

**Notes:** January's 95% automation skipped the regulated parts, which are the product.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription
- [ ] Usage-based
- [ ] Repeat purchases
- [ ] One-time

**Notes:** Acorns proves a subscription can fit spare-change investing. This card has not charged one. A 10 would mean a renewal.

---

## 📈 Total Score: 37.0 / 100

**Weighted Score Calculation:**

```
(4 × 0.15) +
(3 × 0.10) +
(2 × 0.15) +
(5 × 0.20) +
(3 × 0.10) +
(2 × 0.15) +
(5 × 0.10) +
(8 × 0.05) = 3.70 → 37.0 / 100
```

**Decision:** Archive

The January 81.5 does not hold. This is a licensed consumer-finance product, and Fold and Lolli already sell the bitcoin version. Do not build a round-up app. Do not interview people about spare change until a chartered partner is a real option, which is a different and larger company than this lab is for.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **Moving the dollars is the regulated act**: A disclaimer does not cover pulling spare change from a bank and buying bitcoin.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Archive. Do not prototype with live bank links.

2. **The shelf is occupied by funded companies**: Fold's path is BitGo. Lolli already links cards for bitcoin back.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not try to out-ship them with a solo app.

3. **Failed bank links become the job**: Consumer round-up support is a call center, not a dashboard.
   - **Likelihood**: High
   - **Impact**: Medium
   - **Mitigation**: No users, because there is no product.

---

## 🚀 Opportunity Analysis

### What would have to be true

Nothing inside this lab. A chartered partner asking for a distribution app would be their project, with their license. That is not a card to build toward from here.

### Adjacent ideas that are not this card

- QuantShift is stocks at a broker, not spare-change bitcoin.
- The DCA bot is the exchange's recurring-buy button. It was re-scored separately and is also not a build.

---

## ✅ Next Steps

### Archive

- [x] Re-score against Fold, Lolli, Acorns, and the custody path
- [ ] Leave the January file as history
- [ ] Do not start Plaid, a mobile app, or a waitlist

---

## 📝 Research Notes

### Competitor Analysis

Checked 2026-10-14.

| Competitor | What they actually do | Why it matters |
|-----------|----------------------|----------------|
| Acorns | Round-ups from a linked funding source into ETF portfolios. Bitcoin exposure is a futures ETF, capped around 5% of the portfolio, not spot bitcoin | Proves round-ups. Does not leave spot bitcoin open |
| Fold | Bitcoin round-ups, Auto-Stack, debit and credit rewards. BitGo provides custody and exchange and the nationwide charter path | The January product, with the license rented |
| Lolli | Card-linked bitcoin back on Visa and Mastercard via Kard, announced 2026-05-19. 600,000+ accounts reported by The Block | Everyday spend already turns into bitcoin without a new round-up app |

### Customer Insights

Zero interviews. The January "Coinbase left a hole" note was not rechecked, because Fold and Lolli fill the hole either way.

### Market Data

January's 9 million Acorns users are an Acorns fact, not a forecast for this app. They are not reused as a year-1 target.

---

## 🎓 Lessons Learned

### What Worked

- The risk section in January already named money-transmitter licenses. The score did not listen to it.

### What Didn't Work

- Treating Plaid and React Native as the hard parts.
- Treating "Acorns doesn't do spot bitcoin" as an empty market.

### What to Do Differently

- If the product moves customer money into crypto, score the license before the screen.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-14-crypto-micro-investing-app
category: automation-services
scores:
  market_demand: 4
  technical_feasibility: 3
  time_to_revenue: 2
  scalability: 5
  initial_investment: 3
  competitive_advantage: 2
  automation_potential: 5
  recurring_revenue: 8
total_score: 37.0
outcome: archived
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "January 81.5 does not hold. Spare-change bitcoin is Fold and Lolli plus a custody charter. Archive."
```

---

**Last Updated:** 2026-10-14
**Next Review:** None. Archived.
