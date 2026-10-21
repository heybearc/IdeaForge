# Proxmox Management SaaS

**Date Created:** 2026-10-14
**Category:** infrastructure-tools
**Status:** evaluated
**Creator:** Cory

This revises `ideas/evaluated/2026-01-04-proxmox-management-saas.md`. That file stays as the January score. This one is the check against what exists now. The January prices and the month-12 revenue are not reused.

---

## 🎯 Core Concept

A paid control plane on top of Proxmox: deploy guests, watch them, schedule backups, and keep the setup as code. The January card sold that to homelabbers and small businesses as a subscription.

### Problem Being Solved

Proxmox is still a steep interface when the fleet is more than one cluster. That pain is real. It is no longer an empty shelf. The official datacenter manager, free homelab monitors, and at least two paid panels already do this job.

### Target Audience

**Who would have to pay**

- A homelabber, for a nicer dashboard than the free ones. That buyer already self-hosts.
- A VPS host or MSP, for provisioning, tenants, and backups. That buyer is who the paid panels are built for.

**Who uses it**

- The same person who runs the Proxmox nodes. Cory already operates a cluster with scripts and an MCP server. That is personal tooling, not a customer.

### Unique Value Proposition

January claimed a Proxmox-specific SaaS did not exist, and that production scripts were the moat. Both claims fail the lookup. What remains is familiarity with this cluster. Familiarity is not a product someone else lacks.

---

## 💰 Revenue Model

**Primary Revenue Stream:**

- [x] Subscription (monthly/annual) — only if a stranger pays to avoid the free tools
- [ ] Usage-based pricing
- [ ] One-time purchase
- [ ] Freemium model
- [ ] Marketplace/commission
- [ ] Licensing/white-label
- [ ] Other:

**Pricing Strategy:**

No new price. January guessed $19, $49, and $99. Virtualize Pro already posts a flat $12 a month for unlimited clusters and VMs. Proxmox Datacenter Manager does not need its own subscription key. A price above the paid panel, or any price against the free official tool, needs a buyer to say so. None has.

**Revenue scenario (unvalidated):**

- Month 1: $0. Nine months after "Build MVP" the outcome is still not started.
- Month 3: $0 on the January product. The shelf it was going to fill is occupied.
- Month 6: still $0 unless a different job is named, one these tools do not do, for someone who already pays.
- Month 12: unknown, and not the old $8,000 figure.

---

## 🔧 Technical Requirements

### What a first version would be

Not a wrap of the existing scripts. A stranger's cluster means API tokens, tenancy, backups that must not be wrong, and a support load when a migrate or a delete misfires. The MCP server and `proxmox-automation-scripts.py` stay operator tools.

### Tech Stack

- Backend: FastAPI, talking to the Proxmox API
- Frontend: a dashboard
- Database: PostgreSQL
- Infrastructure: the existing cluster, for dogfooding only

### Existing Assets to Leverage

- [x] Proxmox infrastructure
- [ ] QuantShift codebase
- [ ] Trading algorithms
- [x] MCP server for this cluster — operator interface, not a multi-tenant product
- [ ] Multi-agent development tools
- [x] Other: automation scripts already in use here

### Development Estimate

- A credible panel against Datacenter Manager and the paid panels: months, not the January four-week MVP
- Total cash to start: low. Time is the cost, and it would be spent into an occupied category

### Infrastructure Costs

- Hosting: about $0 on the existing cluster
- APIs/Services: small
- Total cash: tens of dollars a month until a customer exists

---

## 📊 Evaluation Scores

### Market Demand: 5 / 10

**Evidence:**

- [x] Competitor analysis completed
- [x] Public product pages and project docs checked on 2026-10-14
- [ ] Google Trends not re-run. The January "40% YoY" figure is not reused
- [ ] Customer interviews: 0 completed, same as January

**Notes:** Easier Proxmox operations are a real category. Proxmox Datacenter Manager shipped as a stable product on 2025-12-04 and manages many clusters, guests, and backup servers from one interface, with no separate subscription key. Pulse (community build, plus a paid Pro tier) and ProxMenux cover homelab monitoring, and ProxMenux 1.2 targets VE 8 and VE 9. Vormox sells a hosted Proxmox panel to VPS providers. Virtualize Pro sells the control-panel version at $12 a month. Coolify, installed from the Proxmox community scripts, is the one-click app deploy path, via Docker. Demand for the category is proven by other people's products. Demand for a new entrant with this offer is not. The homelab buyer self-hosts. The hoster buyer already has vendors.

### Technical Feasibility: 7 / 10

**Skills Match:**

- [x] Can build with existing skills (FastAPI, the Proxmox API, this cluster)
- [x] Requires learning: multi-tenant control of someone else's cluster, not another personal script
- [x] Infrastructure ready for dogfooding

**Notes:** Building a panel is feasible. "Wrap the scripts" was the January underestimate. The bar is now Datacenter Manager plus the paid panels, not an empty UI.

### Time to Revenue: 5 / 10

**Timeline:**

- First customer: not week 6. A hoster who will switch tools is a months-long sale. A homelabber may never pay.
- First dollar: three to six months only if the buyer is a hoster and the offer is narrower than "a dashboard"
- Profitable: not estimated

**Notes:** Matrix band for a 5 is revenue in three to six months. That is the optimistic path, and only after the offer changes. The week-8 public launch does not survive contact with the current shelf.

### Scalability: 6 / 10

**Automation Level:**

- Current: 0% as a product. Personal scripts are not the product.
- Target: customers operate their own nodes
- Timeline: not three months to a hands-off control plane

**Notes:** Customers would run Proxmox on their hardware, so the compute cost per customer is low. The support cost is not. A tool that can migrate, delete, or mis-schedule backups does not sit untouched for a week. Marginal cost is low. Attention cost is not.

### Initial Investment: 9 / 10

**Costs:**

- Development time: months for a panel that is not embarrassing next to Datacenter Manager
- Infrastructure: about $0
- Marketing: $0 until there is an offer that is not already free or $12
- Total cash: tens of dollars a month

**Notes:** The matrix scores cash. Starting cash is still in the top band. That is not a reason to spend the time.

### Competitive Advantage: 3 / 10

**Moats:**

- [x] Unique expertise — this cluster, these scripts, the MCP server
- [ ] Proprietary data/algorithms
- [ ] Network effects
- [ ] First-mover advantage — gone. Datacenter Manager is the official layer. Vormox and Virtualize Pro are the paid layer.
- [x] Infrastructure advantage — dogfooding only
- [ ] Other:

**Notes:** Production experience is credibility. It is not a feature a customer cannot get from Proxmox itself or from the panels already selling. The scripts are easy to copy and already duplicated in kind by community scripts.

### Automation Potential: 6 / 10

**Manual Tasks:**

- Customer support: high the moment the tool touches a stranger's cluster
- Content creation: low
- Operations: onboarding API tokens, networks, and trust stays manual
- Marketing: none until an offer exists

**Notes:** Provisioning can be automated. Break/fix on someone else's hypervisor cannot, not at the 90% bar inside three months.

### Recurring Revenue: 8 / 10

**Model:**

- [x] Subscription
- [ ] Usage-based
- [ ] Repeat purchases
- [ ] One-time

**Notes:** A subscription is the right shape for a control plane. The price is untested, and a posted comp is $12 flat against a free official tool. A 10 would mean someone already renewed.

---

## 📈 Total Score: 57.5 / 100

**Weighted Score Calculation:**

```
(5 × 0.15) +
(7 × 0.10) +
(5 × 0.15) +
(6 × 0.20) +
(9 × 0.10) +
(3 × 0.15) +
(6 × 0.10) +
(8 × 0.05) = 5.75 → 57.5 / 100
```

**Decision:** Refine Idea

The January 87.5 does not hold. Do not build the general management SaaS. Do not interview 20 homelabbers about a dashboard they can install for free. Refine only if one job can be named that Datacenter Manager, Pulse, ProxMenux, Vormox, Virtualize Pro, and Coolify do not already do, for a buyer who already pays for that job. If that job cannot be named, archive this card.

The scorer will print a success probability above 57.5 because `infrastructure-tools` gets an expertise multiplier. That multiplier is not evidence of demand.

---

## ⚠️ Risk Assessment

### Top 3 Risks

1. **The shelf is occupied**: The product is a second client for a hypervisor whose vendor now ships the multi-cluster view, while paid panels and free monitors cover the rest.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not build a general panel. Archive unless a missing job is named in one sentence.

2. **The buyer self-hosts**: Homelabbers adopted Proxmox to avoid a vendor dashboard. A SaaS that reaches into their cluster fights the reason they are here.
   - **Likelihood**: High
   - **Impact**: High
   - **Mitigation**: Do not aim the next test at r/homelab signups.

3. **Support is the product**: The first broken migrate becomes the business.
   - **Likelihood**: Medium
   - **Impact**: High
   - **Mitigation**: No remote control of a stranger's cluster until a paid design partner accepts that risk in writing.

---

## 🚀 Opportunity Analysis

### What could make a related idea larger?

1. **Market Expansion**: Not "also VMware." The management category is already crowded on Proxmox alone.
2. **Product Evolution**: Only a job the current tools skip. The January "Vercel for self-hosting" line is Coolify's position, and Coolify already has a Proxmox community-script install.
3. **Partnership Potential**: None. Proxmox shipped the official layer instead of leaving the gap.

### Adjacent ideas that are not this card

- Keep the MCP server and the scripts as private operator tools.
- A hosting panel is a different company, and Vormox and Virtualize Pro are already that company.
- One-click app deploy is Coolify and Dokploy, not a new Proxmox SaaS.

---

## ✅ Next Steps

### Refine (this card)

- [ ] Name one paid job that Datacenter Manager, Pulse, ProxMenux, Vormox, Virtualize Pro, and Coolify do not do
- [ ] If it cannot be named in one sentence, archive this idea
- [ ] If it can, write that sentence as a new brainstorm card. Do not reuse the 87.5 or the $19 tiers

### Do not do

- [ ] Do not start a dashboard, a landing page, or 20 homelab interviews for the January offer
- [ ] Do not treat the expertise multiplier from the scorer as a reason to build

---

## 📝 Research Notes

### Competitor Analysis

Checked 2026-10-14.

| Competitor | Pricing | Features | Strengths | Weaknesses |
|-----------|---------|----------|-----------|------------|
| Proxmox Datacenter Manager | No separate subscription key. Stable release 2025-12-04 | One interface for many VE clusters and Backup Server instances. Guest power actions, cross-cluster migration, updates | Official. Free to run. The January "no Proxmox-specific layer" claim | Does not replace the per-cluster UI. Aimed at fleets more than a single homelab |
| Pulse | Community build is free. A Pro tier exists; its price was not copied here | Monitoring for VE, PBS, and PMG, plus alerts and backup visibility. Installs as an LXC | What homelab monitoring actually looks like in 2026 | Not a provisioning SaaS |
| ProxMenux | Free | Menu-driven VE toolkit and a web monitor. 1.2 covers VE 8 and VE 9 | Homelab post-install, storage, GPU, backups | A toolkit, not a multi-tenant product |
| Vormox | Hosted SaaS. Public tiers target VPS providers; exact dollars not copied | Agentless API panel: provision KVM and LXC, backups, customer panel, billing | The hoster version of this idea, already for sale | Independent of Proxmox. Not a homelab toy |
| Virtualize Pro | $12/month flat, unlimited VMs and clusters, on their pricing page | Multi-cluster panel, tenant VDCs, PBS backup schedules, self-service | Posted price undercuts the January $19 tier | Marketing site. Depth not tested in this review |
| Coolify | Free self-hosted. Also a paid cloud | One-click apps via Docker and SSH. Community script runs it on Proxmox | Occupies "Vercel for hardware" | Docker, not a Proxmox fleet manager |

### Customer Insights

No interviews in January. No interviews since. The nine months of not starting are the customer insight: the pain was not urgent enough to build, and the gap closed while the card sat.

### Market Data

- January's 100,000 installations, 20,000 serviceable users, and 400 paying customers are not reused.
- The relevant facts are the products above, not a year-1 share of an invented base.

---

## 🎓 Lessons Learned

### What Worked

- The assets are real: the cluster, the scripts, and the MCP server. They are worth keeping as operator tools.

### What Didn't Work

- Scoring "no Proxmox-specific SaaS" as a moat without a fresh lookup.
- Treating homelab enthusiasm as willingness to pay a vendor.
- Leaving 87.5 on the open list for nine months after the decision to build was not acted on.

### What to Do Differently

- A high infrastructure score still gets a live lookup before it is called a build.
- If the official vendor ships the layer, the card is stale the day that release is stable.

---

## 📊 ML Training Data

```yaml
idea_id: 2026-10-14-proxmox-management-saas
category: infrastructure-tools
scores:
  market_demand: 5
  technical_feasibility: 7
  time_to_revenue: 5
  scalability: 6
  initial_investment: 9
  competitive_advantage: 3
  automation_potential: 6
  recurring_revenue: 8
total_score: 57.5
outcome: not_started
actual_revenue_30d: $0
actual_revenue_90d: $0
actual_revenue_1y: $0
time_invested_hours: 0
customer_count: 0
automation_achieved: 0%
lessons_learned: "January 87.5 does not hold. Official and paid panels occupy the general management SaaS. Refine only with a job those tools do not do."
```

---

**Last Updated:** 2026-10-14
**Next Review:** Only if a one-sentence gap is written. Otherwise archive.
