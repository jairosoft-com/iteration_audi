---
title: "Portfolio Meeting Agenda — 2026-04-21 (Iter 7.2 Day 2 sprint-open review)"
type: summary
tags: [portfolio, meeting-agenda, iteration-7.2]
sources: ["../../portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260421.html"]
created: 2026-04-21
updated: 2026-04-21
---

# Portfolio Meeting Agenda — 2026-04-21

Source: [PORTFOLIO_MEETING_AGENDA_20260421.html](../../portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260421.html) · 30-minute review · Iter 7.2 Day 2 sprint-open · Facilitator: Ramon · Attendee: Karl Caumban.

## TL;DR

Day-2 sprint-open review covering all 10 teams with focus on 3 at-risk (Shared, LS-Dev, Flawless) and 7 Quick Wins mapped to specific owners. Based on [[summaries/portfolio-20260421-0130]] data (mean 63.9 / median 67.2 / 1·6·2·1 dist). Strong structural risk section naming Admin/HR/JIT/Colina bus-factor cluster and the Auto Allies branch-protection persistent gap.

## Structure

- **Portfolio Snapshot & Scorecard** — mean/median/trend chart, all-10 scores, Git UPS-without-SGPI variants.
- **Critical & High Risk Deep Dive** — Shared Services, LS-Dev, Flawless (each with root-cause + quick win).
- **Quick Wins & Escalations** — 9 P0 items mapped to specific owners:
  - Flawless: add 1 User Story (Luke, pull from 7.3)
  - LS-Dev: configure capacity (Ramon/Team Lead, clone 7.1); comment #195727 (Ike)
  - Shared: configure capacity (Carol/Ramon); DoR on #202687 (Jaszmeine)
  - OTP: DoR on 3 items (Grace, post-return Apr 23) — #175360, #202911, #202913
  - Admin: DoR on #202898, #202909 (Mark, by Day 3)
  - JIT: comment #199092 + #198615 (armelita)
  - AA: fix PR#123 compile errors (Cliff, TS2304+TS2307)
- **Structural Risks** — Backlog Debt (LS-Dev, Shared) · Engineering Gaps (AA HCI 53, Colina, Shared) · Bus Factor (AA, Admin, HR, JIT).
- **Decisions Needed — PDM Sign-Off** — Shared Services rubric exception; LS-Dev "is 7.2 intentional or deferred"; Admin de-scope 12 SP.
- **Action Items & Owners** — P0 (today) + P1 (before Day 5) checklist.

## Key decisions flagged for PDM sign-off

1. **Shared Services rubric exception** — should Work Item Balance drop the no-User-Story penalty for service teams?
2. **LS-Dev 7.2 planning intent** — 2 items / 5 SP is either deferred planning or intentional light load; which?
3. **Admin over-commit de-scope** — 12 SP to remove from sprint to hit 27 SP ceiling.

## Follow-up visibility (P1 / Before Day 5 Apr 24)

- Configure branch protection on develop/dev/staging/main both AA repos (Cliff + Earl).
- Size 3 unsized Design items (#202553, #202687, #202724).
- Assign sub-iterations to 12 PI7-parent User Stories (#202059–202071).

## Linked

- [[summaries/portfolio-20260421-0130]] (data source)
- [[summaries/meeting-agenda-20260423-1600]] (next agenda in series)
- [[synthesis/capacity-planning]] · [[synthesis/bus-factor]] · [[synthesis/dor-leakage]] · [[synthesis/github-compliance-issues]]

## Follow-up outcome tracking

By 4/23 morning ingests (2 days post-meeting):
- ✅ **HR closed 3 items Day 2** (Verano/Pabatao/Fernandez = 5 SP) — first DP signal.
- ✅ **OTP DoR fixes pending** — Grace returned Apr 23 but P0 overdue; not complete.
- ✅ **AA PR#123 fix** — inferred merged via #202530 → QA Testing on 4/22 evening.
- ✅ **AA DoR gaps remediated** — #194753 Description, #199106 AC both fixed Apr 22.
- ✅ **AA sprint-lock complete** — all 5 Estimation items transitioned.
- ❌ **Shared capacity** — still unconfigured Day 4 (4 consecutive audits).
- ❌ **LS-Dev capacity + #187240 + #195727** — all still unactioned Day 4 (12-audit streak on #187240).
- ❌ **Admin DoR on #202898/#202909** — deadline missed; both executing without Desc/AC.
- ❌ **Flawless add 1 US** — still 0 User Stories in 7.2 at Day 4 (4-audit persistence).
- ✅ **AA branch protection** — still P1; gap to HCI Moderate now only +2.
