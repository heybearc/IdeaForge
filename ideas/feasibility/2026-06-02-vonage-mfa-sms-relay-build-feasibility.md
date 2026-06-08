# Build Feasibility: Vonage MFA SMS Relay (Bookkeeping Client)

**Assessment Type:** Build Feasibility Assessment (Build Lens)  
**Date:** 2026-06-02  
**Linked Idea:** [ideas/brainstorm/2026-06-02-vonage-mfa-sms-relay.md](../brainstorm/2026-06-02-vonage-mfa-sms-relay.md)  
**Assessor:** Cory  
**Status:** assessed — **spike required on Vonage product boundary**

> **Scope:** Can we technically capture Vonage inbound SMS and relay to email/Teams?  
> **Out of scope:** Whether to productize; client pricing; market demand.

---

## 🎯 One-Line Technical Thesis

Public webhook receives inbound SMS (if Vonage exposes it) → n8n on `flows.cloudigan.net` normalizes payload → Cloudigan Mail (`mail.cloudigan.net`) and/or Teams Incoming Webhook posts the message to authorized staff.

### Core Mechanism

```
Bank SMS → Vonage number → [Vonage inbound webhook?] → n8n → Email API / Teams webhook
```

**Critical dependency:** Whether the client's **Vonage Business Communications (VBC)** account exposes programmatic inbound SMS, or only the desktop/mobile Business Inbox app.

### Hard Constraints

- [x] Prefer existing homelab stack (n8n CT188, Cloudigan Mail, NPM/HAProxy)
- [ ] Client Vonage admin must configure webhook or approve API/developer access
- [ ] Must not store MFA codes in long-term logs (security)
- [ ] Low volume (~dozens/day max expected) but high sensitivity

---

## ✅ Will It Work?

### Approach Summary

| Component | Proposed solution | Confidence |
|-----------|-------------------|------------|
| SMS ingress | Vonage Messages/SMS API inbound webhook **if** number is on developer API or linked per Vonage subscription APIs | **L** until account type confirmed |
| Orchestration | n8n workflow (webhook trigger → filter → branch) | **H** — pattern matches Uptime Kuma → Zammad |
| Email egress | `POST https://mail.cloudigan.net/v1/send` (M365 Graph) with `n8n-cron` key | **H** — production today |
| Teams egress | Teams Incoming Webhook URL **or** n8n Microsoft Teams node | **H** — no custom code required |
| Custom API | Optional thin Express/FastAPI receiver only if n8n insufficient for signature verify | **M** |

### Repo / infra relevance (~/Projects scan)

| Asset | Relevance |
|-------|-----------|
| **homelab-nexus** — n8n on CT188, `flows.cloudigan.net` | **Primary** — same webhook pattern as Uptime Kuma → Zammad |
| **cloudigan-mail** — `POST /v1/send` | **Primary** — outbound email without new M365 wiring |
| **chapter-hub** — `x-cron-token` cron pattern | Reference for secured HTTP triggers |
| **cloudigan-api** — Stripe webhook handler | Reference for signature validation, idempotency |
| **cloudigan** — planned Graph MCP for Teams | **Not built** — use Teams Incoming Webhook for v1 |
| **Vonage / SMS code in any repo** | **None** — greenfield integration |

### Unknowns Requiring Proof (BLOCKING)

1. **VBC vs Vonage API:** Client "Vonage VOIP" is almost certainly **Vonage Business Communications**. VBC APIs cover calls/recordings/provisioning — **SMS is NOT in VBC APIs**. SMS is handled via Business Inbox desktop/mobile apps only ([Vonage Business support](https://businesssupport.vonage.com/articles/answer/Vonage-Business-Communications-APIs)).
2. **Can the same LVN get an inbound webhook?** Vonage states subscription-based Communications APIs "operate independently" but may use SMS data from VBC — requires Vonage account review / developer sales path.
3. **10DLC / Business Inbox:** US SMS requires Campaign Registry registration on VBC — changing number routing may affect compliance.
4. **Banks sending to number:** If solution requires a **new** API number, every bank/customer must update MFA destination (high friction).

### Alternative paths if VBC has no webhook

| Path | Effort | Friction |
|------|--------|----------|
| **A. n8n + Vonage Communications API** on same or new number | Medium | Requires Vonage admin + possible number migration |
| **B. Vonage partner (e.g. Telerivet)** web UI + API | Low–medium | Third-party; verify VBC compatibility |
| **C. VBC multi-user Business Inbox** (no automation) | **Lowest** | May solve "one gatekeeper" without code — assign multiple users in VBC admin |
| **D. Dedicated cheap Android phone + SMS forwarder app** | Low | Operational hack; not ideal for firm security |
| **E. Ask banks for email/app-based MFA** | Variable | Often impossible |

### Spike Plan

| Unknown | Spike task | Time box | Pass criteria |
|---------|------------|----------|---------------|
| Account type | Client Vonage admin: screenshot account type, Business Inbox settings, number ownership | 1 hr client call | Confirm VBC vs API; list admin capabilities |
| Webhook feasibility | Open Vonage developer dashboard OR Vonage support ticket: "inbound SMS webhook for existing VBC number" | 2 hrs | Written yes/no + required SKUs |
| n8n Vonage node | n8n test workflow with Vonage sandbox number (if API available) | 4 hrs | Test SMS → n8n → Mail Gateway test email |
| Teams relay | Create Teams Incoming Webhook; n8n HTTP POST test message | 1 hr | Message appears in channel |

---

## 🔨 Build Complexity

### MVP Scope (if Vonage webhook is confirmed)

- [ ] n8n workflow: Vonage inbound webhook → parse `msisdn`, `text`, `to`
- [ ] Filter node: allowlist bank short codes / keywords (`code`, `verification`, `\d{6}`)
- [ ] Email branch: Cloudigan Mail to shared mailbox (`bookkeeping-mfa@clientdomain`)
- [ ] Teams branch: Incoming Webhook to private channel
- [ ] Redact/limit logging (no full message in n8n execution history if possible)

**Explicitly NOT in MVP:**

- Custom web dashboard
- Two-way SMS replies
- Per-client multi-tenant SaaS
- Replacing Vonage phone system

### Effort Estimate (after spike passes)

| Phase | Duration | Notes |
|-------|----------|-------|
| Spike | 1–2 days | Vonage account + sandbox |
| MVP (n8n-only) | 2–4 days | No new repo if n8n sufficient |
| Hardened (signed webhooks, audit) | +3–5 days | Optional Express service on homelab |

### Skills & Stack

| Area | Match (1–10) | Gap |
|------|--------------|-----|
| n8n | 9 | Vonage node config new |
| Email (Cloudigan Mail) | 9 | Already integrated |
| Teams | 7 | Incoming Webhook only; Graph later |
| Vonage / telco | 3 | No prior repo usage |
| Security/compliance | 6 | MFA handling policies needed |

---

## 🏗️ Infrastructure

### MVP Architecture (preferred — n8n-only)

```
Bank → Vonage LVN → HTTPS POST → flows.cloudigan.net/webhook/vonage-mfa-sms
                                      ↓
                                   n8n (CT188)
                                   ├→ mail.cloudigan.net/v1/send → M365 mailbox
                                   └→ Teams Incoming Webhook → private channel
```

### Components

| Component | Technology | Location | New? |
|-----------|------------|----------|------|
| Webhook ingress | n8n Webhook node | CT188 `10.92.3.79` | Workflow only |
| Email | Cloudigan Mail | CT196/197 | No |
| Teams | Incoming Webhook | Microsoft 365 | Client-side config |
| Optional API | Node/Express | New LXC or sandbox | Only if signature verify needed |

### Homelab Leverage

- [x] n8n already public at `https://flows.cloudigan.net` (see homelab-nexus `N8N-WORKFLOW-SUMMARY.md`)
- [x] Cloudigan Mail with `n8n-cron` API key pattern (`.env.example` in homelab-nexus)
- [x] NPM/HAProxy already fronting n8n
- [ ] No new LXC required for n8n-only MVP

### Monthly Infra Cost

| Item | MVP | Notes |
|------|-----|-------|
| Homelab compute | $0 | Existing CT188 |
| Vonage | Client-paid | Possible API subscription if separate from VBC |
| M365 / Teams | Client-paid | Already have M365 |

---

## 📈 Scale Path (Operational)

### Bottleneck Analysis

| Tier | Load | Bottleneck | Mitigation |
|------|------|------------|------------|
| Prototype | <50 SMS/day | Vonage webhook reliability | 200 OK handler; idempotency by `messageId` |
| Growth | N/A for one client | n8n execution history size | Disable verbose logging; external audit store |
| Multi-client | Many firms | Shared n8n workflow | Per-client webhooks + routing keys |

Volume is trivial for infrastructure; **security and compliance** are the real scaling concerns.

### What Does NOT Scale Cheaply

- Productizing across clients with different Vonage account types
- Teams Graph API (app registration per tenant) vs simple Incoming Webhook

---

## ⚠️ Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **VBC cannot webhook inbound SMS** | **High** | **Blocks MVP** | Spike first; fallback Path C (multi-user Inbox) or API number migration |
| MFA codes in n8n logs / email | Medium | High | Short retention; dedicated channel; encrypt; access controls |
| Teams channel too public | Medium | High | Private channel; limited members; consider email-only |
| Bank ToS / security policy | Medium | Medium | Client accepts responsibility; document data flow |
| Vonage retries duplicate posts | Low | Low | Idempotency on `messageId` in n8n |
| SMS sender spoofing | Low | Medium | Allowlist sender numbers where possible |

### Security notes (bookkeeping + banking MFA)

- Treat relayed codes as **credentials** — same handling as passwords
- Prefer **private Teams channel** + **restricted mailbox** over broad distribution
- Avoid printing full SMS body in n8n execution logs (use truncated preview)
- Document client acceptance / risk memo before production

---

## 🔧 Ops & Maintainability

- **Deploy path:** n8n workflow export in homelab-nexus docs; activate on CT188
- **Monitoring:** Uptime Kuma on webhook URL; alert via existing n8n → Zammad chain
- **Backup:** n8n workflow JSON in git (homelab-nexus)
- **Steady-state ops:** ~30 min/month unless Vonage changes routing

---

## 📊 Build Feasibility Scores

### Technical Viability: 5 / 10
**Notes:** Technically straightforward **if** inbound webhook exists on client's Vonage product. VBC-only accounts may not support this without account/product change — largest unknown.

### Build Complexity: 8 / 10
**Notes:** n8n + Mail + Teams is ~2–4 days once webhook confirmed. Vonage account archaeology may take longer than build.

### Infrastructure Fit: 9 / 10
**Notes:** Perfect fit for existing n8n + Cloudigan Mail; no new containers for MVP.

### Scale Architecture: 9 / 10
**Notes:** Trivial volume; architecture adequate.

### Technical Risk: 4 / 10
**Notes:** VBC product boundary + MFA sensitivity drive risk down. Wrong assumption = wasted build.

### Ops Maintainability: 8 / 10
**Notes:** n8n-only is easy to operate; document workflow.

---

## 🎬 Verdict & Next Steps

**Build Feasibility Score:** 72 / 100  
**Verdict:** spike_first — confirm Vonage product/webhook path before building

### Recommended Next Steps

1. **Client call (30 min):** Vonage admin access — VBC Business Inbox vs API; can multiple users access Inbox today (Path C)?
2. **Vonage support ticket:** "Need inbound SMS HTTP webhook for number X on VBC account" — get authoritative answer.
3. **If webhook YES:** 4-hour n8n spike (sandbox number → Mail + Teams).
4. **If webhook NO:** Present Path C (multi-user Inbox) or dedicated API number + customer bank update process.

### Recommended MVP Stack (if spike passes)

**n8n only** — no new repo required. Reuse:

- `homelab-nexus` for workflow documentation
- Cloudigan Mail for email
- Teams Incoming Webhook for chat

Custom API (`cloudigan-api`-style) only if Vonage signed webhooks need verification outside n8n.

### Gate to Development

- [ ] Vonage inbound webhook confirmed for client's number **or** explicit decision to migrate number to Communications API
- [ ] Client security sign-off on email/Teams relay
- [ ] Spike demo: test SMS → team notification in <60 seconds

---

## 📝 Assessment Log

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-02 | BFA created | No Vonage code in ~/Projects; n8n + Mail patterns apply |
