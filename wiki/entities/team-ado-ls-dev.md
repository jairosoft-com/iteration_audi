---
title: "Team — Life Style Help App (ADO)"
type: entity
tags: [team, ado, ls-dev, life-style-help-app, safe]
sources:
  - "../../ado_ls_dev/audit/AUDIT_20260426_2205.md"
  - "../../ado_ls_dev/audit/AUDIT_20260425_1533.md"
  - "../../ado_ls_dev/audit/AUDIT_20260424_0834.md"
  - "../../ado_ls_dev/audit/AUDIT_20260423_1510.md"
  - "../../ado_ls_dev/audit/AUDIT_20260422_0900.md"
  - "../../ado_ls_dev/audit/AUDIT_20260421_1400.md"
  - "../../ado_ls_dev/audit/AUDIT_20260419_1345.md"
  - "../../ado_ls_dev/CLAUDE.md"
  - "../../portfolio_report/PORTFOLIO_20260419_1953.html"
created: 2026-04-19
updated: 2026-04-26
---

# Life Style Help App Team (ADO)

Product team delivering **LifeStyleHelpApp.com** (mobile/web membership, workout, blog, and admin tooling) inside ADO project `Life Style Help App`. Small squad — Samantha Babael (Dev), Ike Yana (Dev), Luzmibel Paculanang (Test) — with mixed User Story and Defect work and a recurring ownership-concentration risk on Samantha.

## Latest (Iteration 7.2 Day 7 EOD — 2026-04-26 22:05 PHT / A33)

**Overall 61.1 🟡 Moderate — Δ 0.0 · 4th consecutive flat.** 69+ hour ADO silence. **BR trap risk**: if #203239 (Samantha) closes before Ike activates #195727, untouched ratio hits 33.3% → BR collapses 24.3→4.3 → overall ~57 (High Risk). #187240 Enabler now **253 days stale** (17th consecutive audit flag — Ike to dispose). #203247 SP still null → Est 75.0. See [[summaries/audit-ado-ls-dev-20260426-2205]].

## Previous (Iteration 7.2 Day 6 — 2026-04-25 15:33 PHT) — riskiest Moderate team

**Overall 61.1 🟡 Moderate — unchanged from Day 5.** Zero sprint closures; DP 0.0 annotation removed (now real penalty). #187240 Enabler now **251 days stale** (15th consecutive audit flag — Ike to dispose). Ike's #195727 untouched 8 calendar / 6 sprint days; untouched ratio 1/4 = 25% — one more untouched item triggers −20 BR penalty and drops LS Dev into High Risk. #203247 SP still null → Est 75.0. See [[summaries/audit-ado-ls-dev-20260425-1533]].

## Previous (Iteration 7.2 Day 5 — 2026-04-24 08:34 PHT) — band crossing, record gain

**Overall 61.1 🟡 Moderate — Δ +21.4 (Critical→Moderate) · LARGEST single-session gain in PI7.2.** Two breakthroughs overnight: (1) **Team Capacity CONFIGURED for 7.2** — Samantha 1h/day Dev, Luzmibel 1h/day Test, Ike 1h/day Dev → TC 0.0 → 100.0 (+14.3 overall); (2) **#203239 + #203247 DoR remediated** Apr 24 00:56–01:09 UTC (DoR 75 → 100); #203247 also advanced New → Active. Structural headwinds remain: IP 28.6, BR 24.3, DP 0.0. #187240 Enabler now **250 days stale** (12th+ audit flag — Ike to dispose). See [[summaries/audit-ado-ls-dev-20260424-0834]].

## Current state (Iteration 7.2 Day 3 — 2026-04-22 09:00 PHT / A27, degraded)

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | **41.0** | 🟠 High |
| Iteration Planning | 16.7 | 🔴 Critical (2/12) |
| Team Capacity | 0.0 | 🔴 Critical (NOT configured for 7.2, 3 days in) |
| Estimation | 100.0 | 🟢 Low |
| DoR Compliance | 100.0 | 🟢 Low |
| Work Item Balance | 70.0 | 🟡 Moderate (2 US, 100% dominance) |
| Backlog Refinement | 0.0 | 🔴 Critical (3 penalties stacked) |
| Delivery Predictability | 0.0 | 🔴 Critical (Day 3; 0/5 SP) |

Source: [[summaries/audit-ado-ls-dev-20260423-0900]] (live). **Plateau confirmed — 4 consecutive audits at 41.0.** Zero ADO activity between A27 and A28. #187240 Enabler now **248 days stale** (12th audit flag). #195727 untouched **6 consecutive days** (longest single-item streak in workspace PI7 history). All four P0 recoveries (capacity, #195727 touch, sprint planning, #187240 disposition) unactioned — < 2 hours total effort for ~60 Overall.

## Historical (Iter 7.1 close — 2026-04-19, 82.4 Low)

Iteration 7.1 closed at **82.4 (Low)** — 7 of 7 committed items Closed, 10/10 SP delivered. Δ −41.4 sprint-open regression is compound: no capacity config (−100), under-scoped sprint, Backlog Refinement collapse (stale_90 + stale_180 + untouched all triggered), DP reset. See [[summaries/audit-ado-ls-dev-20260419-1345]].

## Real fixable issues

1. **#187240 "Evaluate Deployment and Distribution Options"** Enabler is 244 days stale (unchanged since 2025-08-18, assigned to Ike, still New at root path). Triggers −20 `stale_180` penalty every audit; has now done so for 9 consecutive audits.
2. **4 PI5/Nov–Dec 2025 items** (#194082, #194084, #195229, #194386) remain >90d stale with no triage. Combined with #187240 they push `stale_90` share to 41.7%, triggering a second −20 penalty.
3. **Luzmibel's 1h/day Testing capacity went unassigned** across all of Iter 7.1 — no QA task was scoped to her on the 7 sprint items.
4. **Ownership concentration on Samantha Babael** — delivered 6 of 7 items (9 of 10 SP) this sprint; delivery risk persists if she is unavailable.
5. **#195716 and #201334** have lingered in Iter 6.5 paths (Ready for Dev / New) for 4+ weeks without being pulled into a sprint or explicitly rescheduled.

## Structural / context notes

- **Backlog Refinement 18.3** is mostly mechanical: base freshness is 58.3% (7/12 fresh), but the two stale penalties (−20 each) dominate. Closing/archiving the stale cohort lifts this dimension to ~98 in a single grooming pass.
- **Iteration Planning 58.3** is flagged "healthy for team size" in the audit — 7 of 12 visible root items were in the current sprint, the remainder were correctly future-iteration or carryover research items.
- **Delivery Predictability formula rewards descoping** — #196380 and #195727 were moved to Iter 7.2 on Apr 17; the rubric counts only items still on Iter 7.1, so 10/10 = 100% is the correct rubric output but masks a small descope.
- **A24 formula artifact** (Day 12 audit reported 11.2 Critical) was caused by current_iteration_root_items transiently = 0 while closures rolled off the visible board; A24's own caveat estimated actual performance ~74.0 Moderate, which A25 (82.4) confirms and improves on.

## ADO references

- Project: `Life Style Help App` (`0f447778-7156-4451-ab21-27be3c4a5888`)
- Team: `Life Style Help App Team` (`a2a805bc-0b30-4ef3-9a8a-b7f3081157a6`)
- Iteration 7.1 ID: `28c6ab66-a3cb-4700-a497-36cbb54dcb92`
- Board: [Stories and Deliverables](https://jairo.visualstudio.com/Life%20Style%20Help%20App/_boards/board/t/Life%20Style%20Help%20App%20Team/Stories%20and%20Deliverables)
- Workspace: [../../ado_ls_dev/](../../ado_ls_dev/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Ramon Aseniero Jr | Project Owner | <ramon@jairosoft.com> |
| Samantha Babael | Developer (primary delivery) | — |
| Ike Yana | Developer | — |
| Luzmibel Paculanang | Tester | — |

Team roster beyond Ramon is captured from ADO assignees / capacity; emails TBD at next audit.

## Linked concepts

- [[concepts/scoring-ado-rubric]] — 7-dimension rubric used above
- [[concepts/risk-bands]] — Low ≥ 80

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-26 22:05** — [[summaries/audit-ado-ls-dev-20260426-2205]] · [raw](../../ado_ls_dev/audit/AUDIT_20260426_2205.md) (A33 — Day 7 EOD)
- **2026-04-25 15:33** — [[summaries/audit-ado-ls-dev-20260425-1533]] · [raw](../../ado_ls_dev/audit/AUDIT_20260425_1533.md) (A31 — Day 6)
- **2026-04-24 08:34** — [[summaries/audit-ado-ls-dev-20260424-0834]] · [raw](../../ado_ls_dev/audit/AUDIT_20260424_0834.md) (A30 — Day 5)
- **2026-04-23 09:00** — [[summaries/audit-ado-ls-dev-20260423-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260423_0900.md) (live)
- **2026-04-22 09:00** — [[summaries/audit-ado-ls-dev-20260422-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260422_0900.md) (degraded-mode)
- **2026-04-21 14:00** — [[summaries/audit-ado-ls-dev-20260421-1400]] · [raw](../../ado_ls_dev/audit/AUDIT_20260421_1400.md)
- **2026-04-19 13:45** — [[summaries/audit-ado-ls-dev-20260419-1345]] · [raw](../../ado_ls_dev/audit/AUDIT_20260419_1345.md)
- **2026-04-17 09:00** — [[summaries/audit-ado-ls-dev-20260417-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260417_0900.md)
- **2026-04-16 09:00** — [[summaries/audit-ado-ls-dev-20260416-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260416_0900.md)
- **2026-04-13 09:00** — [[summaries/audit-ado-ls-dev-20260413-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260413_0900.md)
- **2026-04-12 09:00** — [[summaries/audit-ado-ls-dev-20260412-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260412_0900.md)
- **2026-04-09 09:00** — [[summaries/audit-ado-ls-dev-20260409-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260409_0900.md)
- **2026-04-08 15:32** — [[summaries/audit-ado-ls-dev-20260408-1532]] · [raw](../../ado_ls_dev/audit/AUDIT_20260408_1532.md)
- **2026-04-07 09:00** — [[summaries/audit-ado-ls-dev-20260407-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260407_0900.md)
- **2026-04-06 09:00** — [[summaries/audit-ado-ls-dev-20260406-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260406_0900.md)
- **2026-04-05 09:00** — [[summaries/audit-ado-ls-dev-20260405-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260405_0900.md)
- **2026-04-04 09:00** — [[summaries/audit-ado-ls-dev-20260404-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260404_0900.md)
- **2026-04-02 09:00** — [[summaries/audit-ado-ls-dev-20260402-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260402_0900.md)
- **2026-04-01 09:00** — [[summaries/audit-ado-ls-dev-20260401-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260401_0900.md)
- **2026-03-31 09:00** — [[summaries/audit-ado-ls-dev-20260331-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260331_0900.md)
- **2026-03-30 10:00** — [[summaries/audit-ado-ls-dev-20260330-1000]] · [raw](../../ado_ls_dev/audit/AUDIT_20260330_1000.md)
- **2026-03-30 09:00** — [[summaries/audit-ado-ls-dev-20260330-0900]] · [raw](../../ado_ls_dev/audit/AUDIT_20260330_0900.md)
- **2026-03-27 00:04** — [[summaries/audit-ado-ls-dev-20260327-0004]] · [raw](../../ado_ls_dev/audit/AUDIT_20260327_0004.md)
- **2026-03-26 16:20** — [[summaries/audit-ado-ls-dev-20260326-1620]] · [raw](../../ado_ls_dev/audit/AUDIT_20260326_1620.md)
- **2026-03-25 02:49:06** — [[summaries/audit-ado-ls-dev-20260325-024906]] · [raw](../../ado_ls_dev/audit/AUDIT_20260325_024906.md)
- **2026-03-22 16:27:42** — [[summaries/audit-ado-ls-dev-20260322-162742]] · [raw](../../ado_ls_dev/audit/AUDIT_20260322_162742.md)
- **2026-03-18 21:06:43** — [[summaries/audit-ado-ls-dev-20260318-210643]] · [raw](../../ado_ls_dev/audit/AUDIT_20260318_210643.md)
- **2026-03-16 22:54:15** — [[summaries/audit-ado-ls-dev-20260316-225415]] · [raw](../../ado_ls_dev/audit/AUDIT_20260316_225415.md)
- **2026-03-16 21:34:41** — [[summaries/audit-ado-ls-dev-20260316-213441]] · [raw](../../ado_ls_dev/audit/AUDIT_20260316_213441.md)
- **2026-03-12 15:50:24** — [[summaries/audit-ado-ls-dev-20260312-155024]] · [raw](../../ado_ls_dev/audit/AUDIT_20260312_155024.md)
- **2026-03-11 23:41:11** — [[summaries/audit-ado-ls-dev-20260311-234111]] · [raw](../../ado_ls_dev/audit/AUDIT_20260311_234111.md)
- **2026-03-11 19:52:54** — [[summaries/audit-ado-ls-dev-20260311-195254]] · [raw](../../ado_ls_dev/audit/AUDIT_20260311_195254.md)

## Open questions

- Will Ike close or archive **#187240** before Iter 7.2 kickoff? Unblocking it removes a −20 Backlog Refinement penalty that has persisted for 9 consecutive audits.
- What is Luzmibel's actual sprint role? Capacity is configured at 1h/day Testing but she had zero Iter 7.1 root assignments — either under-utilized or working at task-level below audit visibility.
- Should Iter 7.2 be right-sized to 8–10 SP (matching realized 7.1 velocity) rather than scope-inflated at kickoff?
