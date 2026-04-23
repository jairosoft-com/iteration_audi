---
title: "Colina Health Audit — 2026-04-06 0900"
type: summary
tags: [git, git-cc-dev, audit, backfill]
sources: ["../../git_cc_dev/audit/AUDIT_20260406_0900.md"]
created: 2026-04-19

## updated: 2026-04-19

# Colina Health Audit — 2026-04-06

Source: [AUDIT_20260406_0900.md](../../git_cc_dev/audit/AUDIT_20260406_0900.md) · 2026-04-06 09:00 · Iteration 7.1 (2026-04-06 → 2026-04-19, Day 1 of 14)

## TL;DR

Iteration 7.1 opens as a defect-stabilization sprint — 9 defects / 17 SP, zero user stories. Day 1 baseline sets UPS 53.8 High Risk (Orange) with ICS 71.4% Red due to data-completeness gaps.

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | 53.8 | 🟠 High |
| ICS (×0.50) | 71.4% | 🔴 Red |
| HCI (×0.30) | 57/100 | 🟠 Needs Improvement |
| SGPI (×0.20) | 17.6% | — (Day 1 proxy) |

## Top issues

- HIGH — ICS Red 71.4% driven by Quality/DoD gap; Description/AC fields missing across most committed defects.
- HIGH — 3 new project-root defects (202269, 202273, 202274) already triaged but unassigned to 7.1 path.
- MEDIUM — Luzmibel (Testing) on leave Apr 9–10; reduced QA capacity; Jaszmeine removed from capacity model.
- MEDIUM — carryover defects 199113, 199117 (Active) are persistent dashboard date-input bugs across iterations.
- LOW — positive Day 1: 3 defects already at Passed QA (183896, 191153, 200826) — rapid carryforward turnaround.

## Delta vs prior

Previous: [[summaries/audit-git-cc-dev-20260405-0900]] — UPS 80.5 (Low, 6.6 close); this: UPS 53.8 (High, 7.1 Day 1 baseline); ICS 85.0 → 71.4 (-13.6), HCI 60 → 57 (-3), SGPI 100 → 17.6 (new iteration); Δ UPS -26.7 (expected sprint-start reset).

## Linked concepts / entities

- [[entities/team-git-cc-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
