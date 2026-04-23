---
title: "Auto Allies Audit — 2026-04-05 09:00 (Iteration 6.6 Sprint Close)"
type: summary
tags: [git, git-aa-dev, audit, backfill, iteration-6.6, sprint-close]
sources: ["../../git_aa_dev/audit/AUDIT_20260405_0900.md"]
created: 2026-04-19

## updated: 2026-04-19

# Auto Allies Audit — 2026-04-05 09:00 (Iter 6.6 Sprint Close)

Source: [AUDIT_20260405_0900.md](../../git_aa_dev/audit/AUDIT_20260405_0900.md) · 2026-04-05 09:00 · Iteration 6.6 IP (2026-03-23 → 2026-04-05)

## TL;DR

Sprint End: **UPS 58.9 Orange**. ICS corrected to **81.6% Yellow** (+17.3) after excluding unestimated spikes. HCI 31/100 Critical (flat), SGPI 42.9% At Risk (flat). **Process-gap discovery**: 7 items (16 SP) closed April 6 — post-sprint-boundary — so not counted. If counted, SGPI would be 100%.

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | 58.9 | 🟠 Orange (High Risk) |
| ICS (×0.50) | 81.6% | 🟡 Yellow |
| HCI (×0.30) | 31/100 | 🔴 Critical |
| SGPI (×0.20) | 42.9% | 🟠 At Risk |

## Top issues

- **Process discipline failure**: 7 items / 16 SP closed April 6 (post-boundary) — team did the work but failed to update ADO states in the sprint window.
- 5/14 parent items closed in sprint (12 SP of 28 committed); 2 Spikes still Active (#201470, #201597).
- Mid-sprint collapse Day 7: 6 SP regressed Ready-for-QA → Active, never recovered within boundary.
- 0 formal code reviews across all 43 PRs — critical engineering practice gap persists.
- ICS methodology correction: unestimated spikes excluded per scoring rules; not a data change.

## Delta vs prior

Previous: [[summaries/audit-git-aa-dev-20260404-0845]] — UPS 53.0 (headline), ICS 64.3%; this: UPS 58.9 (+8.9 after correction), ICS 81.6% (+17.3 Yellow, methodology correction), HCI 31, SGPI 42.9%.

## Linked concepts / entities

- [[entities/team-git-aa-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
