---
title: "Team — Flawless Wedding App (ADO)"
type: entity
tags: [team, ado, flawless-wedding-app, product-dev, safe]
sources:
  - "../../ado_fl_dev/audit/AUDIT_20260422_0646.md"
  - "../../ado_fl_dev/audit/AUDIT_20260421_0800.md"
  - "../../ado_fl_dev/audit/AUDIT_20260419_1345.md"
  - "../../ado_fl_dev/CLAUDE.md"
  - "../../portfolio_report/PORTFOLIO_20260419_1953.html"
created: 2026-04-19
updated: 2026-04-22
---

# Flawless Wedding App Team (ADO)

Product development team delivering the Flawless Wedding App (FlawlessWeddingApp.com) inside its own ADO project `Flawless Wedding App`. Primary contributors: Luke Colina (Dev), Ressa Paracuelles (Test). Mixed work composition — defects dominate, with User Stories and Spikes in the mix. Sprint 7.1 delivered a large, substantive backlog refresh that moved the team out of Moderate-Risk bottom tier.

## Current state (Iteration 7.2 Day 3 — 2026-04-22 06:46 UTC, live-data)

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | **62.5** | 🟡 Moderate |
| Iteration Planning | 7.4 | 🔴 Critical (12/162 — structural) |
| Team Capacity | 100.0 | 🟢 Low (Luke + Ressa active) |
| Estimation | 90.0 | 🟢 Low (−10 for #203230 added 0 SP) |
| DoR Compliance | 91.7 | 🟢 Low (#202827 Desc = 29 chars, 1 char short) |
| Work Item Balance | 30.0 | 🔴 Critical (0 US; −40 + −30 double penalty) |
| Backlog Refinement | 90.0 | 🟢 Low (untouched 25%; −10) |
| Delivery Predictability | 28.6 | 🟠 High (4 / 14 SP closed — first non-zero) |

Source: [[summaries/audit-ado-fl-dev-20260423-0910]]. 63.5 Moderate at Day 4 (Δ +1.0 vs 4/22). **5 SP delivered** — 3 Defects closed by Ressa (#202072, #202119, #202569). Delivery Predictability 35.7% (first meaningful). 2 items regressed to Back-to-Dev (#200791, #202723, 4 SP rework). Structural WIB ceiling 30.0 persists (0 User Stories, 4th audit).

## Historical (Iter 7.1 close — 2026-04-19, 79.3 Moderate)

Iteration 7.1 closed at **79.3 (Moderate, 0.7 from Low)** with 13/13 SP delivered; Overall jumped +10.5 from Day 12 (68.8 → 79.3) — largest single-audit improvement in workspace history. Driver was Apr 13–17 substantive backlog refresh (Backlog Refinement 26.9 → 100.0, +73.1). See [[summaries/audit-ado-fl-dev-20260419-1345]].

## Real fixable issues

1. **#201569 Netlify/GitHub Transfer Spike (Carol Cuison) still Ready at Day 14** — sole open sprint item; orphan risk at close. Either close today or move to 7.2 with a capacity-configured assignee.
2. **Carol Cuison not in ADO capacity config** — Team Capacity held at 66.7 for 8+ consecutive audits; closing #201569 or adding Carol to capacity would push Overall to ~84.1 (Low Risk).
3. **DoR failures on closed Spikes #202381 (~29 nws Desc) and #202150 (~13 nws Desc)** — closed without description updates; pattern of closure-without-remediation.
4. **Dashboard cluster #202837, #202838, #202839, #202840, #202873 unestimated** (0 SP) — need SP before 7.2 commitment.
5. **7.3 stories #201787, #201788, #201789 unestimated** (0 SP) — countdown/event details/vendor list; related to the dashboard cluster.

## Structural / context notes

- **Iteration Planning 6.7 is structural** — visible backlog of 164 items includes ~50 forward-planned items (7.2 through PI8.5); rubric does not distinguish good forward planning from stale inventory.
- **Backlog refresh was substantive, not ceremonial** — Day 12 audit flagged the Apr 17 #202150 CleanUp Spike closure as suspect; today's data shows PI3/PI4 legacy defects now have ChangedDates Apr 13–16. Credit to Ressa Paracuelles.
- **Work Item Balance 100.0** — 6 Defects (54.5%) + 2 User Stories (18.2%) + 3 Spikes (27.3%); clean distribution.
- **PI8 planning pipeline already populated** with 13 items in 8.1/8.2/8.5 — unusually strong forward-planning discipline.
- **Team capacity configured**: Luke 6h/day Dev + Ressa 3h/day Test + Luzmibel 3h/day Test + Ike 1h/day Dev (13h/day total).

## ADO references

- Project: `Flawless Wedding App` (`92b967dc-5ec7-4874-b8f5-e43b00d88339`)
- Team ID: `7d90ecbf-d272-4b0c-b33b-c66d96a790ac`
- Iteration 7.1 ID: `4b3e976b-ec9c-43bd-83ec-d9aec2199d30`
- Scoped backlog: `Microsoft.RequirementCategory` (board: `Stories and Deliverables`)
- Workspace: [../../ado_fl_dev/](../../ado_fl_dev/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Luke Colina | Dev — primary sprint delivery (8/10 closed items) | — |
| Ressa Paracuelles | Test / Spike owner — backlog CleanUp and Iteration Spike | — |
| Carol Cuison | Netlify/GitHub specialist — #201569 (not in capacity config) | — |
| Luzmibel | Test — capacity-configured | — |
| Ike | Dev — capacity-configured | — |
| Ramon Aseniero Jr | Project owner / audit requestor | <ramon@jairosoft.com> |

## Linked concepts

- [[concepts/scoring-ado-rubric]] — 7-dimension rubric used above
- [[concepts/risk-bands]] — Moderate 60–79.9

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-23 09:10** — [[summaries/audit-ado-fl-dev-20260423-0910]] · [raw](../../ado_fl_dev/audit/AUDIT_20260423_0910.md)
- **2026-04-22 06:46** — [[summaries/audit-ado-fl-dev-20260422-0646]] · [raw](../../ado_fl_dev/audit/AUDIT_20260422_0646.md)
- **2026-04-21 08:00** — [[summaries/audit-ado-fl-dev-20260421-0800]] · [raw](../../ado_fl_dev/audit/AUDIT_20260421_0800.md)
- **2026-04-19 13:45** — [[summaries/audit-ado-fl-dev-20260419-1345]] · [raw](../../ado_fl_dev/audit/AUDIT_20260419_1345.md)
- **2026-04-17 09:00** — [[summaries/audit-ado-fl-dev-20260417-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260417_0900.md)
- **2026-04-16 09:00** — [[summaries/audit-ado-fl-dev-20260416-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260416_0900.md)
- **2026-04-13 09:00** — [[summaries/audit-ado-fl-dev-20260413-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260413_0900.md)
- **2026-04-12 09:00** — [[summaries/audit-ado-fl-dev-20260412-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260412_0900.md)
- **2026-04-09 09:00** — [[summaries/audit-ado-fl-dev-20260409-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260409_0900.md)
- **2026-04-08 09:00** — [[summaries/audit-ado-fl-dev-20260408-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260408_0900.md)
- **2026-04-07 09:00** — [[summaries/audit-ado-fl-dev-20260407-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260407_0900.md)
- **2026-04-06 09:00** — [[summaries/audit-ado-fl-dev-20260406-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260406_0900.md)
- **2026-04-05 09:00** — [[summaries/audit-ado-fl-dev-20260405-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260405_0900.md)
- **2026-04-04 09:00** — [[summaries/audit-ado-fl-dev-20260404-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260404_0900.md)
- **2026-04-02 09:00** — [[summaries/audit-ado-fl-dev-20260402-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260402_0900.md)
- **2026-04-01 09:00** — [[summaries/audit-ado-fl-dev-20260401-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260401_0900.md)
- **2026-03-31 09:00** — [[summaries/audit-ado-fl-dev-20260331-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260331_0900.md)
- **2026-03-30 10:30** — [[summaries/audit-ado-fl-dev-20260330-1030]] · [raw](../../ado_fl_dev/audit/AUDIT_20260330_1030.md)
- **2026-03-30 09:00** — [[summaries/audit-ado-fl-dev-20260330-0900]] · [raw](../../ado_fl_dev/audit/AUDIT_20260330_0900.md)
- **2026-03-27 00:04** — [[summaries/audit-ado-fl-dev-20260327-0004]] · [raw](../../ado_fl_dev/audit/AUDIT_20260327_0004.md)
- **2026-03-26 16:21** — [[summaries/audit-ado-fl-dev-20260326-1621]] · [raw](../../ado_fl_dev/audit/AUDIT_20260326_1621.md)
- **2026-03-26 15:43** — [[summaries/audit-ado-fl-dev-20260326-1543]] · [raw](../../ado_fl_dev/audit/AUDIT_20260326_1543.md)
- **2026-03-25 09:48:18** — [[summaries/audit-ado-fl-dev-20260325-094818]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-25_094818.md)
- **2026-03-22 23:29** — [[summaries/audit-ado-fl-dev-20260322-2329]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-22_2329.md)
- **2026-03-18 17:39:43** — [[summaries/audit-ado-fl-dev-20260318-173943]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-18_173943.md)
- **2026-03-16 23:04:02** — [[summaries/audit-ado-fl-dev-20260316-230402]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-16_230402.md)
- **2026-03-12 00:30:43** — [[summaries/audit-ado-fl-dev-20260312-003043]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-12_003043.md)
- **2026-03-11 19:33:16** — [[summaries/audit-ado-fl-dev-20260311-193316]] · [raw](../../ado_fl_dev/audit/AUDIT_2026-03-11_193316.md)

## Open questions

- Was the Apr 13–17 refresh a bulk re-iteration-path operation or item-by-item grooming? Revision history would confirm.
- Should the default backlog view exclude PI8 items until PI8 planning begins, to raise Iteration Planning closer to actual performance?
- Is Carol Cuison an internal contributor (should be added to capacity) or external (should be removed from sprint scope)?
