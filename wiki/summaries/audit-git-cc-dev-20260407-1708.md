---
title: "Colina Health Audit — 2026-04-07 1708"
type: summary
tags: [git, git-cc-dev, audit, backfill]
sources: ["../../git_cc_dev/audit/AUDIT_20260407_1708.md"]
created: 2026-04-19

## updated: 2026-04-19

# Colina Health Audit — 2026-04-07

Source: [AUDIT_20260407_1708.md](../../git_cc_dev/audit/AUDIT_20260407_1708.md) · 2026-04-07 17:08 · Iteration 7.1 (2026-04-06 → 2026-04-19, Day 2 of 14)

## TL;DR

Day 2 velocity strong — 2 defects Closed, 3 promoted to Ready for UAT, 2 to Passed QA — but ICS drops further to 63.0% Red due to AC completeness re-evaluation and new untagged scope addition (200885).

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | 51.9 | 🟠 High |
| ICS (×0.50) | 63.0% | 🔴 Red |
| HCI (×0.30) | 60/100 | 🟡 Moderate |
| SGPI (×0.20) | 11.8% | — (Day 2 in-progress) |

## Top issues

- HIGH — ICS 63% Red: AcceptanceCriteria fields absent for all 10 iteration defects (possible ADO rich-text API surface issue, but drives Quality/DoD to 0%).
- HIGH — 200885 added mid-sprint with no Story Points, no Description, no AC — compounds Iteration Integrity deduction.
- MEDIUM — 8 new root-level defects triaged today (202269 / 202273 / 202274 / 202436 / 202439 / 202442 / 202444 / 202448) — backlog pressure.
- LOW — positive delta: 198953 and 198955 fully Closed via passed/qa/* → main promotion pattern; 5/10 defects now production-ready.
- LOW — 199113 (3 SP) + 199117 (5 SP) both advanced to Passed QA — highest-value progress event.

## Delta vs prior

Previous: [[summaries/audit-git-cc-dev-20260406-0900]] — UPS 53.8 (High); this: UPS 51.9 (High); ICS 71.4 → 63.0 (-8.4, data completeness), HCI 57 → 60 (+3), SGPI 17.6 → 11.8 (-5.8 headline but proxy 76.5%), UPS -1.9.

## Linked concepts / entities

- [[entities/team-git-cc-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
