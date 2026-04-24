---
title: "Auto Allies Audit — 2026-04-22 0900 (Iteration 7.2 Day 3)"
type: summary
tags: [git, auto-allies, iteration-7.2, audit]
sources: ["../../git_aa_dev/audit/AUDIT_20260422_0900.md"]
data_mode: partial
created: 2026-04-22
updated: 2026-04-22
---

# Auto Allies Audit — 2026-04-22 0900

Source: [AUDIT_20260422_0900.md](../../git_aa_dev/audit/AUDIT_20260422_0900.md) · 2026-04-22 09:00 PHT · Iteration 7.2 (Day 3 of 14 — early-sprint) · **Partial evidence — ADO live; both GitHub repos returned HTTP 404 for all API calls under `raseniero` token. GitHub-dependent HCI dimensions carried from Day 2 audit.**

## TL;DR

**ICS 95.3% · SGPI 0.0% · HCI 53/100 — all unchanged vs Day 2.** Three scores flat. ADO evidence is fresh (18 parents in Iter 7.2, 15 non-spike = 35 SP baseline, 2 DoR gaps persist). GitHub inaccessible today — token scope issue flagged as Critical evidence gap. **Key worsening signal:** Day 2's P1 "lock the 5 Estimation items (10 SP) by Wednesday" was missed — all 5 items remain in Estimation state with ChangedDates from Apr 20–21, no movement. 29% of sprint SP now in commit-ambiguity on Day 3.

## Scores (independent 3-score panel — per Git rubric)

| Score | Value | Band | Δ vs 4/21 Day 2 |
|-------|------:|------|---------------:|
| **ICS — Iteration Compliance** | 95.3% | 🟢 Green | 0 |
| **SGPI — Committed Scope** | 0.0% | (early-sprint annotation) | 0 |
| **HCI — Engineering Health** | 53/100 | 🟠 Critical | 0 (GitHub inaccessible; carried) |

## Top issues

- **GitHub API 404 on both repos** — `raseniero` token authenticated but lacks org read access to private jairosoft-com repos today. Critical evidence gap. HCI scored conservatively at 53 (Day 2 carry). **Investigate token/SSO before next audit.**
- **Estimation sprint-lock missed on 5 items (10 SP)** — #199106, #200233, #201564, #202684, #202926 all still in Estimation state. Day 2 audit recommended Ready-for-Dev transition by today. Delivery risk.
- **2 DoR gaps unchanged** — #194753 (empty Description) + #199106 (no AC). ICS Quality/DoD holds at 86.7%; fixing both restores ICS to 100.0.
- **Branch protection still 0** across all 4 critical branches (`develop`, `main` on FE; `dev`, `main` on BE). 17th+ consecutive audit flagging. Primary HCI lever — configuring on all 4 is +3 to +4 HCI (gap to Moderate is +7).
- **PR#123 CHANGES_REQUESTED (TS2304 + TS2307)** — Cliff's fix to #202530 (3 SP, Active) not confirmed pushed. Blocking item cannot close until resolved.

## Positive signals (carried from Day 2)

- **First human PR review in team history** (Earl → Cliff on PR#123) — preserved.
- **Retro spike #202168 CLOSED** by Jerlyn.
- **`github-code-quality[bot]` active on PR#123** — new CI-gating capability.

## Delta vs prior ingest

Previous wiki ingest: [[summaries/audit-git-aa-dev-20260421-0900]] — ICS 95.3 / SGPI 0.0 / HCI 53 (all Day 2 open state). This: identical 3 scores. Δ 0 across the board.

**Trajectory for HCI path to Moderate (+7):** branch protection (+3 to +4) + second review cycle on PR#123 (+1 to +2) + AB# on direct commits (+1). None of these require GitHub API read access — they require team action in GitHub and ADO.

## Linked concepts / entities

- [[entities/team-git-aa-dev]]
- [[entities/person-jerlyn]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
- [[synthesis/ups-masking-pattern]]
- [[synthesis/github-compliance-issues]]
- [[synthesis/ci-health]]
