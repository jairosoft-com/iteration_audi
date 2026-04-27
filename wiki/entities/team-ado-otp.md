---
title: "Team — Office of the President (ADO)"
type: entity
tags: [team, ado, otp, office-of-the-president, safe]
sources:
  - "../../ado_otp/audit/AUDIT_20260426_2210.md"
  - "../../ado_otp/audit/AUDIT_20260425_0833.md"
  - "../../ado_otp/audit/AUDIT_20260424_0835.md"
  - "../../ado_otp/audit/AUDIT_20260423_1100.md"
  - "../../ado_otp/audit/AUDIT_20260422_0644.md"
  - "../../ado_otp/audit/AUDIT_20260421_0930.md"
  - "../../ado_otp/audit/AUDIT_20260419_1345.md"
  - "../../ado_otp/CLAUDE.md"
  - "../../portfolio_report/PORTFOLIO_20260419_1953.html"
created: 2026-04-19
updated: 2026-04-26
---

# Office of the President Team (ADO)

Administrative/operations function inside ADO project `OTP`, covering executive correspondence, compliance filings (PhilGeps, H1B, visa paperwork), facility work (fire extinguisher canvassing, JIT signage, solar installation chain), and board-level documentation. Work is 100% User-Story-shaped and, by accepted team exception, executed under a **single-assignee model** with **Grace** as sole owner of every board item.

## Latest (Iteration 7.2 Day 7 Evening — 2026-04-26 22:10 PHT / A39)

**Overall 74.8 🟡 Moderate — Δ +6.1 · LARGEST single-session gain in 7.2 sprint series.** Grace completed all P0s ~23:15–23:29 PHT: #202911 DoR remediated, #202913 DoR+SP fixed, #175360 + #201811 activated. DoR 71.4→100.0, Est 85.7→100.0. DP still 0.0 (no SP closed). Closes wiki TODO `grace-action` item (#202911 + #202913 DoR remediation). See [[summaries/audit-ado-otp-20260426-2210]].

## Previous (Iteration 7.2 Day 6 — 2026-04-25 08:33 PHT)

**Overall 68.7 🟡 Moderate — unchanged from Day 5 (A36).** #202911 and #202913 remain bare-title at Day 6 — zero content added since sprint start (Apr 20). #203026 and #203029 still Active; no closures; DP 0.0 annotation removed (now real penalty). Score ceiling if P0s remediated: ~74.8 (still Moderate). See [[summaries/audit-ado-otp-20260425-0833]].

## Previous (Iteration 7.2 Day 5 — 2026-04-24 08:35 PHT)

**Overall 68.7 🟡 Moderate — Δ +3.5** · Two overnight remediations by Grace at 03:08–03:11 PHT: #175360 DoR remediated (AC added; DoR 57.1 → 71.4) and #201811 touched (BR 90 → 100). #202911 + #202913 remain zero-content DoR failures (sole remaining P0 DoR/Est barrier). Post-P0 ceiling: 75.4. See [[summaries/audit-ado-otp-20260424-0835]].

## Current state (Iteration 7.2 Day 3 — 2026-04-22 06:44 UTC / A35)

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | **65.2** | 🟡 Moderate |
| Iteration Planning | 53.8 | 🟠 High (7/13 committed) |
| Team Capacity | 100.0 | 🟢 Low |
| Estimation | 85.7 | 🟢 Low (6/7 — #202913 no SP) |
| DoR Compliance | 57.1 | 🟠 High (4/7 — #175360 no AC, #202911/#202913 title-only) |
| Work Item Balance | 70.0 | 🟡 Moderate (−30 for 100% User Story, accepted exception) |
| Backlog Refinement | 90.0 | 🟢 Low (−10 for #201811 untouched since Apr 8) |
| Delivery Predictability | 0.0 | 🔴 Critical (Day 3; 0 closed of 14 SP committed) |

Source: [[summaries/audit-ado-otp-20260423-0900]] (first live-data read of 7.2). Δ −1.5 from 4/22 prior. Live surfaces #201811 untouched penalty (BR 100 → 90). A33 "first unassigned item" finding retracted — #202913 was Grace-assigned since Apr 20. DoR remediation overdue for 2nd post-return workday. **Zero board movement at Day 4** — all 6 items still New.

## Historical (Iter 7.1 close — 2026-04-19)

Iteration 7.1 final state remained frozen at **71.2** (Moderate); see [[summaries/audit-ado-otp-20260419-1345]]. Score frozen from A30 — no board movement in the final 35 hours. Historical sprint delivery was ~14 SP (Apr 16 wave of 7 closures) but those items were no longer on the visible board by sprint close, so the rubric could not count them.

## Real fixable issues

1. **#198587 "Installation of JIT Signage Preparation"** (3 SP, Active) — last touched 2026-04-17 23:36 PHT, no formal closure 35 hours later. If the physical install is complete, closing in ADO lifts DP to 60.0 and Overall to ~79.8.
2. **#202229 "Invitation Letter from Akira"** (2 SP, Active) — stalled 9 days on external dependency (Akira's signed letter). Should be formally re-pathed to Iter 7.2 rather than carried into sprint close as an Active artifact.
3. **5 future-iteration items** (#175360, #200073, #201811, #201815, #201820) sit at ChangedDate 2026-04-08 — 11 days without a planning-touch refresh before Iter 7.2 kickoff.
4. **No iteration goal configured** on 7.1 — blocks outcome-based retrospective framing and PI-objective alignment.

## Structural / context notes

- **Iteration Planning 28.6 is a board-view artifact.** The Apr 16–17 closure wave (7 items / 14 SP per A29) removed delivered items from the visible backlog before the rubric could observe them. Actual planning quality was high: team committed 14 items / 33 SP at kickoff.
- **Delivery Predictability 0.0 is strictly mechanical** — formula is `closed / committed on visible 7.1 items`. The Apr 16 closures are invisible to the formula; only the 2 remaining Active items (5 SP) count against it.
- **Work Item Balance 70.0 is an accepted project exception** — 100% User Story composition triggers the −30 dominance penalty. OTP's CLAUDE.md explicitly accepts this as a structural characteristic of an admin/ops team; adding even one Enabler or Spike in 7.2 would lift this to 100.
- **Single-assignee (Grace) model is an accepted exception.** Not a scoring deduction, but amplifies risk at sprint close (zero fallback) and creates a structural ceiling on capacity.
- **Historical full-sprint velocity ~14/33 ≈ 42%** (51.5% if #198587 closes) is lower than prior OTP sprints.

## ADO references

- Project: `OTP` (`e7739905-28a3-4ae1-9173-7f6cd13b3494`)
- Team: `OTP Team` (`64de61f0-1203-4b01-aee2-6b4415aec52b`)
- Iteration 7.1 ID: `ce4205d6-4038-4752-a0b8-dda248031686`
- Workspace: [../../ado_otp/](../../ado_otp/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Ramon Aseniero Jr | Project Owner | <ramon@jairosoft.com> |
| Grace | Sole assignee (accepted project exception) | <grace@jairosoft.com> |
| Karl Caumban | Portfolio Delivery Manager | <kcaumban@jairosoft.com> |
| Akira | External — invitation-letter signer (#202229) | — |

## Linked concepts

- [[concepts/scoring-ado-rubric]] — 7-dimension rubric used above
- [[concepts/risk-bands]] — Moderate 60–79.9

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-26 22:10** — [[summaries/audit-ado-otp-20260426-2210]] · [raw](../../ado_otp/audit/AUDIT_20260426_2210.md) (A39 — Day 7 Evening)
- **2026-04-25 08:33** — [[summaries/audit-ado-otp-20260425-0833]] · [raw](../../ado_otp/audit/AUDIT_20260425_0833.md) (A37 — Day 6)
- **2026-04-24 08:35** — [[summaries/audit-ado-otp-20260424-0835]] · [raw](../../ado_otp/audit/AUDIT_20260424_0835.md) (A36 — Day 5)
- **2026-04-23 09:00** — [[summaries/audit-ado-otp-20260423-0900]] · [raw](../../ado_otp/audit/AUDIT_20260423_0900.md) (first live 7.2 read)
- **2026-04-22 06:44** — [[summaries/audit-ado-otp-20260422-0644]] · [raw](../../ado_otp/audit/AUDIT_20260422_0644.md)
- **2026-04-21 09:30** — [[summaries/audit-ado-otp-20260421-0930]] · [raw](../../ado_otp/audit/AUDIT_20260421_0930.md)
- **2026-04-19 13:45** — [[summaries/audit-ado-otp-20260419-1345]] · [raw](../../ado_otp/audit/AUDIT_20260419_1345.md)
- **2026-04-17 09:00** — [[summaries/audit-ado-otp-20260417-0900]] · [raw](../../ado_otp/audit/AUDIT_20260417_0900.md)
- **2026-04-16 09:00** — [[summaries/audit-ado-otp-20260416-0900]] · [raw](../../ado_otp/audit/AUDIT_20260416_0900.md)
- **2026-04-13 09:00** — [[summaries/audit-ado-otp-20260413-0900]] · [raw](../../ado_otp/audit/AUDIT_20260413_0900.md)
- **2026-04-12 09:00** — [[summaries/audit-ado-otp-20260412-0900]] · [raw](../../ado_otp/audit/AUDIT_20260412_0900.md)
- **2026-04-09 09:00** — [[summaries/audit-ado-otp-20260409-0900]] · [raw](../../ado_otp/audit/AUDIT_20260409_0900.md)
- **2026-04-08 15:32** — [[summaries/audit-ado-otp-20260408-1532]] · [raw](../../ado_otp/audit/AUDIT_20260408_1532.md)
- **2026-04-07 09:00** — [[summaries/audit-ado-otp-20260407-0900]] · [raw](../../ado_otp/audit/AUDIT_20260407_0900.md)
- **2026-04-06 09:00** — [[summaries/audit-ado-otp-20260406-0900]] · [raw](../../ado_otp/audit/AUDIT_20260406_0900.md)
- **2026-04-05 09:00** — [[summaries/audit-ado-otp-20260405-0900]] · [raw](../../ado_otp/audit/AUDIT_20260405_0900.md)
- **2026-04-04 09:00** — [[summaries/audit-ado-otp-20260404-0900]] · [raw](../../ado_otp/audit/AUDIT_20260404_0900.md)
- **2026-04-02 09:00** — [[summaries/audit-ado-otp-20260402-0900]] · [raw](../../ado_otp/audit/AUDIT_20260402_0900.md)
- **2026-04-01 09:00** — [[summaries/audit-ado-otp-20260401-0900]] · [raw](../../ado_otp/audit/AUDIT_20260401_0900.md)
- **2026-03-31 09:00** — [[summaries/audit-ado-otp-20260331-0900]] · [raw](../../ado_otp/audit/AUDIT_20260331_0900.md)
- **2026-03-30 10:15** — [[summaries/audit-ado-otp-20260330-1015]] · [raw](../../ado_otp/audit/AUDIT_20260330_1015.md)
- **2026-03-30 09:00** — [[summaries/audit-ado-otp-20260330-0900]] · [raw](../../ado_otp/audit/AUDIT_20260330_0900.md)
- **2026-03-27 07:01** — [[summaries/audit-ado-otp-20260327-0701]] · [raw](../../ado_otp/audit/AUDIT_20260327_0701.md)
- **2026-03-26 16:30** — [[summaries/audit-ado-otp-20260326-1630]] · [raw](../../ado_otp/audit/AUDIT_20260326_1630.md)
- **2026-03-25 09:48:57** — [[summaries/audit-ado-otp-20260325-094857]] · [raw](../../ado_otp/audit/AUDIT_2026-03-25_094857.md)
- **2026-03-22 23:29:28** — [[summaries/audit-ado-otp-20260322-232928]] · [raw](../../ado_otp/audit/AUDIT_20260322_232928.md)
- **2026-03-18 21:35:00** — [[summaries/audit-ado-otp-20260318-213500]] · [raw](../../ado_otp/audit/AUDIT_20260318_213500.md)
- **2026-03-17 21:11:59** — [[summaries/audit-ado-otp-20260317-211159]] · [raw](../../ado_otp/audit/AUDIT_20260317_211159.md)
- **2026-03-16 22:32:41** — [[summaries/audit-ado-otp-20260316-223241]] · [raw](../../ado_otp/audit/AUDIT_20260316_223241.md)
- **2026-03-12 13:54:39** — [[summaries/audit-ado-otp-20260312-135439]] · [raw](../../ado_otp/audit/AUDIT_20260312_135439.md)
- **2026-03-11 20:51:39** — [[summaries/audit-ado-otp-20260311-205139]] · [raw](../../ado_otp/audit/AUDIT_20260311_205139.md)
- **2026-03-10 20:50:34** — [[summaries/audit-ado-otp-20260310-205034]] · [raw](../../ado_otp/audit/AUDIT_20260310_205034.md)
- **2026-03-09 22:57:51** — [[summaries/audit-ado-otp-20260309-225751]] · [raw](../../ado_otp/audit/AUDIT_20260309_225751.md)
- **2026-03-06 22:17:41** — [[summaries/audit-ado-otp-20260306-221741]] · [raw](../../ado_otp/audit/AUDIT_20260306_221741.md)
- **2026-03-05 21:46:59** — [[summaries/audit-ado-otp-20260305-214659]] · [raw](../../ado_otp/audit/AUDIT_20260305_214659.md)
- **2026-03-04 22:12:09** — [[summaries/audit-ado-otp-20260304-221209]] · [raw](../../ado_otp/audit/AUDIT_20260304_221209.md)
- **2026-02-26 23:16:28** — [[summaries/audit-ado-otp-20260226-231628]] · [raw](../../ado_otp/audit/AUDIT_20260226_231628.md)
- **2026-02-24 22:12:43** — [[summaries/audit-ado-otp-20260224-221243]] · [raw](../../ado_otp/audit/AUDIT_20260224_221243.md)

## Open questions

- Has #198587 actually been installed? A closure today (or Monday before retro) would move OTP into Low Risk band (~85.5).
- Should Iter 7.2 include at least one Enabler or Spike so Work Item Balance can exit the accepted −30 penalty range?
- Is the "visible-state" Iteration Planning / Delivery Predictability behaviour a rubric gap worth addressing (e.g., count closed-and-removed items for these dimensions)? Identical issue affects [[entities/team-ado-shared]] in a different shape.
