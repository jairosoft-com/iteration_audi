---
title: "Compliance Misalignment — Regulatory Work Decoupled from ADO"
type: synthesis
tags: [compliance, finance, audit-evidence, misalignment]
sources:
  - "../concepts/compliance-deadlines.md"
  - "../entities/team-ado-fin.md"
  - "../entities/person-grace.md"
  - "../summaries/audit-ado-fin-20260419-1345.md"
  - "../summaries/audit-ado-fin-20260416-0900.md"
  - "../summaries/audit-ado-fin-20260413-0900.md"
  - "../summaries/audit-ado-fin-20260412-0900.md"
  - "../summaries/portfolio-20260419-1953.md"
  - "../synthesis/iteration-7.1-close.md"
created: 2026-04-20

## updated: 2026-04-20

# Compliance Misalignment — Regulatory Work Decoupled from ADO

Regulatory compliance work runs against external deadlines on external portals. The ADO board does not see the submission, does not see the confirmation receipt, and — because that is the only surface the audit skill reads — scores the work as undelivered even when the regulator already has the filing. This page pulls the pattern together and proposes a policy so the rubric stops under-reporting compliance delivery.

## Headline

**Finance's Apr 15 BIR eAFS deadline cannot be verified from the ADO board.** Work item [#201448 (eAFS Portal Submission, 2 SP)](../../ado_fin/audit/AUDIT_20260419_1345.md) was still `Active` at the 2026-04-19 13:45 audit, four days past the filing deadline, with last ChangedDate of Apr 10 — a 9-day inactivity window straddling the regulatory event ([[summaries/audit-ado-fin-20260419-1345]]). Finance scored 93.7 Low anyway, because 4 of 5 other items closed; the compliance miss is the single open question in the team's otherwise cleanest iteration ([[entities/team-ado-fin]]).

## The eAFS/BIR incident

Timeline of #201448 across the iteration ([[concepts/compliance-deadlines]], [[entities/team-ado-fin]]):

| Date | State | Evidence in ADO |
|------|-------|-----------------|
| 2026-04-06 | Committed to Iteration 7.1 (Day 1), DoR pass (Desc ≥30 chars, AC ≥20 chars) | [[summaries/audit-ado-fin-20260406-0900]] |
| 2026-04-10 | Last ChangedDate on record | [[summaries/audit-ado-fin-20260419-1345]] |
| 2026-04-12 | Day 7 midpoint; audit flags "BIR eAFS deadline 3 days away" | [[summaries/audit-ado-fin-20260412-0900]] |
| 2026-04-13 | Day 8; audit flags "deadline tomorrow (Apr 14/15); #201448 still Active" | [[summaries/audit-ado-fin-20260413-0900]] |
| **2026-04-15** | **BIR eAFS regulatory deadline** | not reflected on ADO board |
| 2026-04-16 | Day 11; audit flags "deadline passed with #201448 still Active" | [[summaries/audit-ado-fin-20260416-0900]] |
| 2026-04-19 | Day 14 / sprint close; state still Active, no Transaction Number, no receipt attachment | [[summaries/audit-ado-fin-20260419-1345]] |

What the audit said: Delivery Predictability 85.7 (12 of 14 SP), one item open, filing status "unconfirmed in ADO" ([[summaries/audit-ado-fin-20260419-1345]]). What likely happened in the real world: Grace submitted through the eAFS portal on or before Apr 15 and the confirmation email is in her Outlook, not on #201448. The audit has no way to know.

## Why ADO can't see compliance work

The practitioner's workflow sits entirely outside the system of record the auditor reads:

1. **Prep** happens on the ADO work item (DoR, AC, SP) — visible.
2. **Submission** goes through the BIR eAFS portal — external; no ADO hook.
3. **Confirmation** is a portal receipt plus an email (Transaction Number, timestamp) — delivered to the practitioner's inbox, not to ADO.
4. **Archive** requires the practitioner to paste the receipt back into ADO as a comment or attachment — this is the step that is skipped.

The audit skill reads `System.State`, `System.ChangedDate`, and Story Point closure flags. None of those change when an eAFS filing succeeds. The item stays `Active` because the human closure step is manual post-facto work that competes with the next regulatory task in the practitioner's queue.

## How audits handle it today

The current convention is defensive, not corrective ([[concepts/compliance-deadlines]] §"Convention for audit evidence"):

- Note the deadline in the summary TL;DR.
- Label the Delivery Predictability impact as **"compliance-decoupled"** rather than a regression.
- Surface the evidence-gap in the audit's Open questions so the next iteration's audit reopens it.

This is informational, not structural. The rubric still scores #201448 as `Active = not delivered` — Finance lost ~14.3 Delivery Predictability points against a filing that almost certainly completed. Same shape as the scoring artifacts catalogued in [[synthesis/scoring-artifacts]]: the number is reproducible, but it doesn't describe reality.

## Other compliance tracks to consider

The pattern is not Finance-only. Administration owns a parallel regulatory portfolio and the same decoupling risk applies:

- **[[entities/team-ado-admin]] Administration** scope explicitly covers "government compliance (BFP, PhilGeps, DOLE, EGOV)"; one DOLE WAIR filing (#202364, 1 SP) was visible on Admin's 2026-03-18 audit ([[summaries/audit-ado-admin-20260318-2253]]) and a BIR tax item (#201210) appeared as a mid-sprint scope addition with same-day closure. These closed cleanly, but the pattern — regulator-facing items closed without a receipt trail in ADO — is identical to #201448's failure mode.
- **SSS / PhilHealth / Pag-IBIG** (employer contributions) and **SEC GIS** (annual general information sheet) fall under the same owner profile — monthly and annual cadences, portal-based submission, receipt delivered by email. No ADO work items detected for these in the current audit window, which is itself a gap worth confirming.
- **Colina Health HIPAA PR BE#55** is the Git-side analogue: compliance-relevant code sitting unreviewed at sprint close, no regulatory receipt to attach ([[synthesis/iteration-7.1-close]] §"What didn't").

Cross-check recommended: list every ADO work item whose title contains `BIR`, `BFP`, `DOLE`, `SEC`, `SSS`, `PhilGeps`, `EGOV`, `HIPAA`, `eAFS`, `AFS`, or `ITR` and audit them against this policy, not the generic rubric.

## Proposed policy

Promote the informational convention in [[concepts/compliance-deadlines]] into a rubric rule:

1. **Introduce a `compliance` tag in ADO.** Any work item that ends in a regulator-facing submission must carry the tag.
2. **Require a `deadline` field.** An item tagged `compliance` cannot enter an iteration until the ADO `deadline` custom field (or a normalized Due Date) is set. Audit skill refuses to score the item otherwise.
3. **Evidence-based closure, not state-based.** For items tagged `compliance`, the audit skill scores on **evidence attached** (regulatory receipt: Transaction Number, portal confirmation PDF, or submission email saved to the item) rather than `System.State`. An `Active` item with a receipt attached scores as delivered; a `Closed` item without a receipt scores as an evidence gap.
4. **Deadline-aware penalty.** If `today > deadline` and no receipt is attached, the item contributes a distinct **"compliance at risk"** flag to the team's open-questions block — not a Delivery Predictability penalty. Compliance misses are a separate category from iteration delivery misses.
5. **Audit skill query.** The ADO audit workflow queries for `Tags contains 'compliance'` alongside its iteration query, parses comments and attachments for a regulatory-receipt signature (`FRN`, `Transaction Number`, `eAFS Reference`, etc.), and emits a dedicated section in the audit report.
6. **Portfolio dashboard widget.** Compliance items at risk this iteration surface as a standalone widget, not folded into Delivery Predictability. Prevents the [[synthesis/scoring-artifacts]] pattern of a real red flag being invisible inside a green composite.

## Dashboard additions

Concrete changes for the next [[summaries/portfolio-20260419-1953]] iteration:

- **"Compliance at risk" card** on the portfolio HTML dashboard, top row next to Critical band count. Counts items where `compliance` tag is set and `deadline < today` and no receipt is attached. For 2026-04-19, this would have read `1` (Finance #201448) even though portfolio mean was 76.1 and Finance was green.
- **Deadline timeline** on each ADO team entity panel: a strip of upcoming 30-day compliance deadlines with owner, deadline, and receipt-status ball (green / amber / red). Pulls from the `deadline` field introduced by the policy.
- **Audit-report evidence badge.** On the per-item row in the summary, render a receipt badge (`FRN:…`, `TxID:…`) if the comment/attachment scrape found one. Auditors and the CEO can then tell "Active but filed" apart from "Active and late" at a glance.
- **Cross-team compliance calendar.** [[synthesis/iteration-7.1-close]] forward-ask section gets a new row: every team with a `compliance`-tagged item in the next PI, deadline, receipt status. Replaces the per-team scatter of the information today.

## Related

- [[concepts/compliance-deadlines]] — definition of eAFS/BIR/AFS and the current convention
- [[entities/team-ado-fin]] — Finance entity; 93.7 Low despite #201448 uncertainty
- [[entities/team-ado-admin]] — parallel compliance scope (BFP, PhilGeps, DOLE, EGOV)
- [[entities/person-grace]] — practitioner on both the Finance eAFS filing and the JIT Documentation blocker
- [[synthesis/iteration-7.1-close]] — Finance forward asks include reconciling #201448 before 7.2 planning
- [[synthesis/scoring-artifacts]] — same "scoring doesn't capture reality" theme (rubric transitions, close-day formula effects)
- [[summaries/audit-ado-fin-20260419-1345]] · [[summaries/audit-ado-fin-20260416-0900]] · [[summaries/audit-ado-fin-20260413-0900]] · [[summaries/audit-ado-fin-20260412-0900]]
