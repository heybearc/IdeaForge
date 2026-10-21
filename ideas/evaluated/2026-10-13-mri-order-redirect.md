# MRI Order Redirect

**Date Created:** 2026-10-13  
**Category:** automation-services  
**Status:** evaluated  
**Creator:** Cory

---

## 🎯 Core Concept

A booking platform for MRI orders, built like MOMS (My One Medical Source) is built for blood draws. Imaging centers pay a platform fee to be on the network, plus a per-scan fee, the way a lab pays a draw fee on top of its subscription. The patient books on the web. The scan happens at an independent center instead of a hospital outpatient department.

The luggage move is still the reason it exists: the scan does not need the hospital, and the hospital's facility fee is the toll. MOMS is the business shape.

### Problem Being Solved

Hospital outpatient MRI prices are often two to five times the cash price of the same study at an independent imaging center. The gap is the hospital facility fee. The order is usually written to the hospital scanner, and the patient does not know they can take it elsewhere.

Independent centers want that volume and have empty hours. They do not want to staff a call desk for every redirected order. MOMS already proved that the party who wants the volume will pay to sit on a network, and will pay again per procedure.

### Target Audience

**Who pays**

- The imaging center. Monthly platform fee to receive orders, plus a per-scan fee when the patient is scanned.
- The patient does not subscribe.

**Who uses the web app**

- A patient with an MRI order, to see a center and book.
- The imaging center, to see incoming orders, open slots, and fees owed.

### Unique Value Proposition

Price sites show the gap. MOMS does not do MRI. This platform takes the order onto a center that has already paid to receive it, and charges that center per completed scan.

### Reference: MOMS

[My One Medical Source](https://www.myonemedicalsource.com/) is the blood-draw version of this shape.

- Labs and clients subscribe for access to the collection network. Published tiers are about $999, $2,500, and $5,000 per month, paid annually. Source: [MOMS lab pricing](https://knowledge.myonemedicalsource.com/what-is-the-cost-to-join-the-lab/client-network).
- The draw fee is separate. The lab can pay it, or the patient can pay it. Source: [MOMS draw pricing](https://knowledge.myonemedicalsource.com/maps-connecting-with-labs-setting-prices).
- Collection sites join free. MOMS takes $2.50 per collection, plus card processing. Source: [MAP join cost](https://knowledge.myonemedicalsource.com/what-is-the-cost-to-join-the-map-network).

On MOMS the lab is the subscriber, because the lab needs someone to draw the blood. Here the imaging center is the subscriber, because the center needs the patient. Same two charges: access, then a fee per procedure.

### How an order gets onto the platform

Nothing is intercepted. A hospital order lives in that hospital's chart. The platform sees it only when a person or a contracted clinic sends the patient over. There is no feed to plug into.

MOMS works the same way. A lab joins, then tells its own patients to book a draw on MOMS. The platform does not pull orders out of some other lab's system.

Three ways an MRI order arrives, in the order to attempt them:

1. **Patient-driven.** The doctor hands over an order for an MRI. The patient opens the site, sees an independent center, and requests a time. No contract. This is the pilot. Volume stays small until someone with a stack of orders sends people on purpose.
2. **Contract with the ordering clinic.** The doctor's office agrees that new MRI orders go through the booking page, or staff book the slot before the patient leaves. The doctor still writes the order. The clinic chooses the center. This is the MOMS move: the party who already has the patient points them at the network. Independent clinics are the ones to sign. A hospital imaging department is paid by the facility fee, so it will not send the scan away.
3. **Contract with a health plan or employer.** The plan's rule sends the member to an independent center before the hospital slot is booked. That is the version that catches orders at scale. It is a later sale, after the pilot has completed scans.

A hospital contract is the wrong first door. The hospital is the fee being avoided.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — imaging center platform fee
- [x] Usage-based pricing — per-scan fee, the draw-fee equivalent
- [ ] Marketplace/commission
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Licensing/white-label
- [ ] Other: patient pays the center's scan price, not us

**Pricing Strategy:**

Do not copy MOMS's $999 month as the pilot price. A single-city MRI center has not asked for a national network yet.

- Platform fee: a monthly amount one center will pay to receive orders. Set it in the first sales call. Annual billing can come after the first center stays.
- Per-scan fee: a flat amount owed when the scan is completed. This is the draw fee. It is smaller than the platform fee's job and it scales with volume.
- Patient: $0 to the platform. They pay the center for the MRI, at the center's cash or insured price.

**Revenue scenario (unvalidated):**

- Month 1: $0 until a center signs.
- Month 3: one center's platform fee only, unless scans have started.
- Month 6: one center's platform fee plus per-scan fees. No dollar target until the center names both prices.
- Month 12: a second center, or a second study such as CT, on the same two fees.

---

## 🔧 Technical Requirements

### The front end

Yes. This is a small web app with two sides, not a single brochure page.

1. **Patient side.** City and study. One or more centers that have an open slot. A booking request. v1 confirms the slot by a person at the center, then shows the patient the time.
2. **Center side.** Sign-in, incoming orders, slot list, platform fee status, and a per-scan fee ledger.

No patient subscription and no patient account beyond the booking. The written order stays off the server in v1. The form collects a phone number, the study, and the hospital named on the order. Name, date of birth, and the order itself stay on the call or go center-to-clinic until storage of health information is a deliberate step.

### Tech Stack

- Backend: small API for bookings, centers, and fees
- Frontend: patient booking page and center portal
- Database: centers, slots, booking status, fees. Not the medical order in v1.
- Infrastructure: existing homelab for the pilot
- APIs/Integrations: none until a center asks to push a booking into their own scheduler. Card billing for the two fees comes when a center agrees to pay them.

### Existing Assets to Leverage

- [x] Proxmox infrastructure — hosting the pilot
- [ ] QuantShift codebase
- [ ] Trading algorithms
- [ ] MCP server framework
- [ ] Multi-agent development tools
- [x] Other: MOMS as the fee pattern. Empty scanner time as the inventory.

### Development Estimate

- MVP: 2–4 weeks for patient booking plus a center list of orders
- Beta: after one center agrees to both fees
- Launch: first booked scan under that agreement
- Total: the portal is the build. The center agreement sets the date.

### Infrastructure Costs

- Hosting: about $0 on the homelab while the order stays off the server
- APIs/Services: card processing once fees are charged
- Tools/Software: low
- Total: low until health-information storage is required

---

## 📊 Evaluation Scores

### Market Demand: 8 / 10

**Evidence:**

- [x] Competitor analysis completed (desk research, 2026-10-13)
- [ ] Reddit/Discord research done
- [ ] Google Trends analyzed
- [ ] Customer interviews: 0 completed

**Notes:** The MRI price gap is published. MOMS shows labs will pay a platform fee plus a separate procedure fee for blood draws. No imaging center has been asked if they will pay both for MRI orders.

### Technical Feasibility: 6 / 10

**Skills Match:**

- [x] Can build with existing skills
- [x] Requires learning: how an imaging order is allowed to move, and when a booking becomes stored health information
- [x] Infrastructure ready for a pilot web app

**Notes:** Two screens and a fee ledger are ordinary. The medical rules around the order are the hard part.

### Time to Revenue: 4 / 10

**Timeline:**

- First customer: a center must agree to a monthly fee and a per-scan fee. Unknown week.
- First dollar: the first platform invoice, or the first completed scan, whichever they accept first.
- Profitable: after those fees cover the time to run the bookings. Unknown month.

**Notes:** A subscription asks the center to pay before the volume shows up. The pilot can invoice the platform fee only after the first completed scans, if that is what gets a yes.

### Scalability: 8 / 10

**Automation Level:**

- Current: 10%
- Target: 70% once centers confirm their own slots in the portal
- Timeline: after one center's booking path is repeatable

**Notes:** The same portal takes a second center and a second study. Each hospital's order rules are the part that does not copy cleanly.

### Initial Investment: 7 / 10

**Costs:**

- Development time: about 40–80 hours for both sides of the web app
- Infrastructure: about $0 for the pilot
- Marketing: the first center is a direct conversation, not an ad budget
- Total: mostly time

**Notes:** Higher than a one-page form because the center portal is part of the product. Still small next to a national build.

### Competitive Advantage: 6 / 10

**Moats:**

- [ ] Unique expertise
- [ ] Proprietary data/algorithms
- [x] Network effects — later, if several centers and a stream of orders lock in
- [ ] First-mover advantage
- [ ] Infrastructure advantage
- [x] Other: MOMS proved the fees for blood draws. MRI redirect is the same fees on a scan.

**Notes:** Comparison sites and each center's own scheduler already exist. The opening is hospital orders landing on centers that pay to receive them. A center can still do this with a phone number on a PDF.

### Automation Potential: 5 / 10

**Manual Tasks:**

- Customer support: high until the center confirms slots in the portal
- Content creation: low
- Operations: the first bookings are confirmed by hand
- Marketing: high until orders arrive without a person hunting for them

**Notes:** The platform fee is only honest once orders arrive through the product. Hand-confirm the first ones.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription — center platform fee
- [x] Usage-based — per-scan fee
- [ ] Repeat purchases
- [ ] One-time

**Notes:** Both fees recur. The patient does not.

---

## 📈 Total Score: 65.0 / 100

**Weighted Score Calculation:**

```
(8 × 0.15) +
(6 × 0.10) +
(4 × 0.15) +
(8 × 0.20) +
(7 × 0.10) +
(6 × 0.15) +
(5 × 0.10) +
(8 × 0.05) = 6.50 → 65.0 / 100
```

**Decision:** Validate Market — superseded 2026-10-14 for the booking gap

The 65.0 above assumed a patient could not already book a cheaper MRI at an independent center. RadiologyAssist, Green Imaging, and MDsave already do that. Building another booking page does not fill a gap. Do not make the three center calls to test booking. The only leftover is a fee shape, a center paying a monthly fee plus a per-scan fee, and nothing shows a center paying that.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The order cannot move**: The hospital or the ordering clinic refuses to send the study out, or insurance only pays at the hospital.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Ask one center and one ordering office first. Cash-pay patients are the clean first case.

2. **Health information**: Storing the written order, name, and date of birth makes this a medical-record problem.
   - **Likelihood**: High if the booking form collects the order
   - **Impact**: High
   - **Mitigation**: v1 collects a phone number, the study, and which hospital is on the order. The order itself stays off the server.

3. **The center will not pay twice**: They may want the patients and refuse a monthly fee plus a per-scan fee.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: Ask for both fees in the first call. If they will pay only one, write down which one and do not pretend it is the MOMS model.

---

## 🚀 Opportunity Analysis

### What could make this 10x bigger?

1. **Market Expansion**: CT and ultrasound on the same center subscription, then a second city.
2. **Product Evolution**: Centers publish open slots. A cancellation is offered to someone who already has an order.
3. **Partnership Potential**: Ordering clinics send every hospital MRI through the booking page.
4. **Platform Play**: This is already the platform. More centers and more orders are the growth, the way MOMS added collection sites under one lab subscription.

### Adjacent Opportunities

- The same two fees for a hospital outpatient procedure an ambulatory center already performs.
- A portal login for the ordering clinic, so staff book the center without handing the patient a comparison site.
- The boost-belt idea stays a separate physical product.

---

## ✅ Next Steps

### Validation Phase (Week 1-2)

- [ ] Pick one metro and list independent MRI centers with a published cash price
- [ ] Call three centers with the MOMS shape: a monthly fee to receive orders, plus a per-scan fee
- [ ] Ask which fee they would actually pay, and whether they can take an outside doctor's order
- [ ] Call one ordering office: can the patient take this order to that center?
- [ ] Stop if no center will pay to receive the orders

### MVP Phase (after a center says yes)

- [ ] Patient booking page for that city and MRI only
- [ ] Center portal: incoming bookings and a per-scan ledger
- [ ] Phone number and study only. No order upload.
- [ ] Run the first ten bookings with a person confirming the slot

### Launch Phase

- [ ] First platform fee or first per-scan fee collected
- [ ] Note where the patient came from
- [ ] Only then add a second center or a second study

### Growth Phase

- [ ] Centers manage their own slots
- [ ] Second study on the same subscription
- [ ] Annual billing only after a center has stayed through a few months of scans

---

## 📝 Research Notes

### Competitor Analysis

| Competitor | Pricing | Features | Strengths | Weaknesses |
|-----------|---------|----------|-----------|------------|
| MOMS | Lab subscription about $999–$5,000/mo, plus a separate draw fee. Sites join free. $2.50 per collection. | Labs send patients to draw sites. Patients schedule. The platform bills. | This is the model. Labs already pay both fees. | Blood draw and specialty kits. Not MRI. |
| Getlabs | Partner platform access, price on request. Patients often pay the visit fee, sometimes about $25–$90. | Mobile phlebotomy booked online, specimen goes to Labcorp, Quest, or a specialty lab. | National draw network and a partner portal. | They sell the draw visit, not a cheaper MRI. |
| FairVisitHealth, TreatCompare, MDsave, Sesame | Consumer comparison or a posted cash bundle | Shows a lower imaging price, sometimes a voucher | The MRI price gap is public | They do not charge centers a platform fee to receive a redirected hospital order. |
| The imaging center's own site | Center's cash price | "Same scan, lower cost" pages | The center already wants the patient | Each center only sells itself. |

### Customer Insights

No interviews yet.

### Market Data

- The shoppable unit is one MRI study, one city, one center on a platform fee.
- Year 1 target: one independent center paying both fees.
- MOMS prices are the comparable shape, not the pilot price list.

---

## 🎓 Lessons Learned

[Update this section as you progress]

### What Worked

- ___

### What Didn't Work

- ___

### What to Do Differently

- ___

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-13-mri-order-redirect
category: automation-services
scores:
  market_demand: 8
  technical_feasibility: 6
  time_to_revenue: 4
  scalability: 8
  initial_investment: 7
  competitive_advantage: 6
  automation_potential: 5
  recurring_revenue: 8
total_score: 65.0
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "Fee shape taken from MOMS: platform subscription plus a per-procedure fee."
```

---

**Last Updated:** 2026-10-13  
**Next Review:** 2026-10-27
