# Vonage MFA SMS Relay (Bookkeeping Client)

**Date Created:** 2026-06-02  
**Category:** automation-services  
**Status:** brainstorm  
**Creator:** Cory  
**Client context:** Bookkeeping firm on Vonage VOIP; one shared number receives bank MFA SMS; single gatekeeper manually forwards codes today.

---

## 🎯 Core Concept

Automate delivery of inbound MFA SMS from a Vonage business number to email and/or Microsoft Teams so any authorized staff can act on codes without one person being the bottleneck.

### Problem Being Solved

- Bank institutions send MFA codes as SMS to the firm's Vonage number
- Only one employee can access that inbox today
- Manual copy/paste creates delays and single point of failure

### Target Audience (internal)

- Bookkeeping firm staff who need timely MFA codes for client banking portals

### Unique Value Proposition

- Near-real-time relay to channels the team already monitors (email / Teams)
- Uses existing homelab automation (n8n, Cloudigan Mail) where possible

---

## 🔧 Technical Requirements (high level)

- Inbound SMS capture from Vonage
- Filter/route messages (bank senders, keywords like "code", "verification")
- Deliver to M365 email and/or Teams channel
- Audit trail; minimize secret retention in logs

**Out of scope for v1:** Replacing Vonage; changing how banks send MFA; full client portal integration.

---

## 💰 Revenue Model

Internal/client services project — not evaluated here (see opportunity evaluation separately if productized).

---

## 📊 Evaluation Scores

*(Opportunity evaluation not run — BFA-first for this engagement.)*
