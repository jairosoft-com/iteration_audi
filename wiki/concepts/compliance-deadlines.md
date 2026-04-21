---
title: "Compliance Deadlines — eAFS / BIR / regulatory calendar"
type: concept
tags: [compliance, finance, deadline, bir, eafs, regulatory]
sources:
  - "../../ado_fin/audit/AUDIT_20260419_1345.md"
  - "../../ado_fin/CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Compliance Deadlines

Recurring regulatory deadlines that drive Finance-team work and occasionally constrain other teams' iteration plans. Mentioned 40+ times across Finance audits; consolidated here so summaries can link rather than re-define.

## Core terms

| Term | Full name | Owner | Meaning |
|------|-----------|-------|---------|
| **BIR** | Bureau of Internal Revenue (Philippines) | [[entities/team-ado-fin]] | National tax authority; sets filing deadlines for corporate tax documents |
| **eAFS** | Electronic Audited Financial Statements Portal | [[entities/team-ado-fin]] | BIR's electronic submission portal for audited financial statements |
| **AFS** | Audited Financial Statements | Finance + external auditor | The document eAFS submits; required annually |

## Known deadline events in the audit window

| Date | Event | Status at audit |
|------|-------|-----------------|
| **2026-04-15** | BIR eAFS submission deadline | Passed without ADO confirmation. Finance work item **#201448** ("eAFS Portal Submission") was still in `Active` status on 2026-04-19, per [[summaries/audit-ado-fin-20260419-1345]]. |

This is the canonical example of a **compliance deadline decoupled from the ADO board**: the actual filing may have happened outside ADO, but the audit can't verify because the work item wasn't closed. This is a repeatable systemic issue flagged in [[synthesis/iteration-7.1-close]].

## Why this matters for audits

- **Hidden done work.** An Active ADO item on Day 14 usually scores as "not delivered", but if the underlying regulatory filing actually completed, the score under-reports. Auditors should ask: *was this a paperwork gap, or a real miss?*
- **Cross-team scheduling.** Quarterly compliance deadlines (BIR, SEC, DOLE) often fall mid-iteration. Teams with compliance-owner members (e.g., [[entities/person-grace]]) should protect capacity in those iterations.
- **Non-standard audit trail.** eAFS and similar portals have their own confirmation emails/receipts — consider attaching them as `comments` on the ADO work item so the audit skill can detect completion.

## Convention for audit evidence

When an audit can't confirm closure from ADO alone:

1. Note the regulatory deadline in the summary's TL;DR.
2. In the Delta vs prior section, label the Delivery Predictability impact as **"compliance-decoupled"** rather than a regression.
3. Escalate the evidence-gap in the audit's Open questions so it surfaces in the next iteration's audit.

## Related

- [[entities/team-ado-fin]] · [[entities/person-grace]]
- [[synthesis/iteration-7.1-close]] — Apr 15 eAFS deadline featured in the PI7.2 forward asks
- [[concepts/scoring-ado-rubric]] — Delivery Predictability definition

## Open questions

- Is there an authoritative jairosoft compliance calendar we should cite by reference? (Currently inferred from Finance audit context.)
- Should the audit skill auto-annotate work items tagged `compliance` with their regulatory deadline?
- Who in Jairosoft owns the compliance calendar end-to-end? (Candidate: Finance lead; [[entities/person-grace]] is the practitioner, not the owner-of-calendar.)
