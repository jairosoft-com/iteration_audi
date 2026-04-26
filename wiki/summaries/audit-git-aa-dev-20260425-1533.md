---
title: "Auto Allies Audit — Iteration 7.2 Day 6 (2026-04-25)"
type: summary
tags: [safe, git, audit, iteration-7-2, ups, auto-allies]
sources: ["../../git_aa_dev/audit/AUDIT_20260425_1533.md"]
created: 2026-04-25
updated: 2026-04-25
---

# Auto Allies Audit — Iteration 7.2 Day 6 (2026-04-25)

**Sprint:** Iteration 7.2 (Apr 20 – May 3) · **Day 6** · 43% elapsed · 8 working days remaining (after May 1 Labor Day)
**Data mode:** `partial` — raseniero GitHub token 404 active since 2026-04-21; HCI dims 1–6 carried forward from Day 2 baseline

## Scores

| Metric | Value | Band | Δ vs Day 5 |
|--------|------:|------|-----------|
| **ICS** — Iteration Compliance | 96.0% | Green | unchanged |
| **HCI** — Engineering Health | 59/100 | Critical | unchanged (carry-forward) |
| **SGPI** — Sprint Goal Progress | 0.0% | Red | unchanged |
| **UPS** | **65.7** | Moderate | unchanged |

UPS formula: ICS × 0.50 + HCI × 0.30 + SGPI × 0.20 — see [[concepts/scoring-git-ups]]
Risk band definitions: [[concepts/risk-bands]]

> UPS headline (Moderate 65.7) masks Critical HCI (59) — see [[synthesis/ups-masking-pattern]]

## Key findings

### ADO state (no transitions since Day 5)
- No work item state changes between Day 5 audit (09:02 Apr 24) and Day 6 (15:33 Apr 25)
- Three items in `New` state without iteration assignment: #203281, #203287, #203289 (Joseph Gerona) — unclassified mid-sprint scope additions, no planning ceremony
- #203118 (Earl Carino, QA Testing, 2 SP) — only item with a clear path to closure this week

### Critical: Earl Carino direct commit to `dev` (Apr 24, 14:33 UTC)
- Commit: `CreateLawyerCommand` enhancements
- No AB# reference · No PR · No reviewer
- Second consecutive sprint with sensitive backend changes (lawyer/attorney domain logic) committed directly to `dev` without review gate
- Branch protection remains 0 on both repos — action unfulfilled since Day 1 of 7.2

### SGPI trajectory
- 0/27 SP closed on Iteration 7.2 path after 6 days (43% elapsed)
- Team needs ~21 SP closure in remaining 8 working days to reach 75% SGPI target
- No items in QA-ready or mergeable state as of this audit
- May 1 Labor Day removes one capacity day from calculation

## Project exceptions in effect
- Jerlyn Ates (QA/Requirements) and Mary Secusana (Documentation): GitHub absence not penalized per 2026-04-23 LPM Review decision — not developers. Filed in `git_aa_dev/CLAUDE.md`.

## Data integrity notes
- HCI dims 1–6 carry-forward from Day 2 baseline (Apr 21) — GitHub token 404 blocks live reads
- ICS 96.0% unchanged — 3 New-state items (#203281, #203287, #203289) cause the −4.0 deduction from 100%

## Linked pages
- [[entities/team-git-aa-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
- [[synthesis/ups-masking-pattern]]
- Prior audit: [[summaries/audit-git-aa-dev-20260424-0902]] (Day 5, UPS 65.7)
