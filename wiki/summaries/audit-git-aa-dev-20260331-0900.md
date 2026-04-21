---
title: "Auto Allies Audit — 2026-03-31 09:00 (Iteration 6.6 Day 7)"
type: summary
tags: [git, git-aa-dev, audit, backfill, iteration-6.6]
sources: ["../../git_aa_dev/audit/AUDIT_20260331_0900.md"]
created: 2026-04-19
updated: 2026-04-19
---

# Auto Allies Audit — 2026-03-31 09:00 (Iter 6.6 Day 7)

Source: [AUDIT_20260331_0900.md](../../git_aa_dev/audit/AUDIT_20260331_0900.md) · 2026-03-31 09:00 · Iteration 6.6 IP (2026-03-23 → 2026-04-05)

## TL;DR

Day 7 (70%): SGPI **42.9%** (+14.3) — 5 items Closed (12 SP). But **2 items regressed Ready-for-QA → Back-to-Dev** (#201111, #201110 = 6 SP) — QA found issues. ICS 64.3% (+0.1 flat). HCI 28/100 (+2). 39 iteration PRs.

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | — | — (pre-UPS; ICS 64.3% 🔴) |
| ICS (×0.50) | 64.3% | 🔴 Red |
| HCI (×0.30) | 28/100 | 🔴 Critical |
| SGPI (×0.20) | 42.9% | 🟠 |

## Top issues

- **Two rework regressions (6 SP)** — #201111 and #201110 pushed Ready-for-QA → Active (rework); must be re-fixed AND re-tested in remaining 3 WDs.
- QA pipeline shrank from 4 items (Day 6) to 1 item (2 SP) after the two regressions.
- 0 code reviews, 0 branch protection, 0 formal ADO-GitHub traceability persist.
- Iteration Compliance score essentially flat (+0.1) despite 2 new closures — anchored by structural gaps.
- Positive: #201112 (Super Admin Confirm Payment, 3 SP) and #201118 (T&C Link, 1 SP) both closed; #199007 advanced to Ready for QA.

## Delta vs prior

Previous: [[summaries/audit-git-aa-dev-20260330-0900]] — ICS 64.2%, SGPI 28.6%, HCI 26; this: ICS 64.3% (+0.1), SGPI 42.9% (+14.3), HCI 28 (+2).

## Linked concepts / entities

- [[entities/team-git-aa-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
