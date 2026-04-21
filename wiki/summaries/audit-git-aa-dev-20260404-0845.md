---
title: "Auto Allies Audit — 2026-04-04 08:45 (Iteration 6.6 Final Day)"
type: summary
tags: [git, git-aa-dev, audit, backfill, iteration-6.6, sprint-close]
sources: ["../../git_aa_dev/audit/AUDIT_20260404_0845.md"]
created: 2026-04-19
updated: 2026-04-19
---

# Auto Allies Audit — 2026-04-04 08:45 (Iter 6.6 Final Day)

Source: [AUDIT_20260404_0845.md](../../git_aa_dev/audit/AUDIT_20260404_0845.md) · 2026-04-04 08:45 · Iteration 6.6 IP (2026-03-23 → 2026-04-05)

## TL;DR

Sprint final WD (100%). **First UPS score: 53.0 Orange (High Risk)** — but exact formula yields 50.0. ICS 64.3% Red, SGPI 42.9%, HCI 31/100 Critical. All scores flat from Day 9. Sprint closed with 12 of 28 SP (42.9%) — rework items #201111, #201110 never recovered.

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | 53.0 (report) / 50.0 (calc) | 🟠 Orange (High Risk) |
| ICS (×0.50) | 64.3% | 🔴 Red |
| HCI (×0.30) | 31/100 | 🔴 Critical |
| SGPI (×0.20) | 42.9% | 🟠 At Risk |

## Top issues

- UPS report/calculation inconsistency: headline 53.0; verified calc 64.3×0.50 + 31×0.30 + 42.9×0.20 = 50.0.
- Sprint closed under-delivered: 12/28 SP (42.9%); #199007 still QA Testing (not closed); #201111/#201110 still Active.
- 5 items Closed; BE PR #52 (affiliate enabler) still open at sprint end.
- Zero code reviews across 43 PRs; 0% formal traceability; no branch protection (14th audit).
- Two rework items have been Active 7 WDs since Day 7 regression — never recovered.

## Delta vs prior

Previous: [[summaries/audit-git-aa-dev-20260402-0900]] — ICS 64.3%, SGPI 42.9%, HCI 30; this: same ICS/SGPI, HCI 31 (+1). First UPS introduced at 53.0 (headline).

## Linked concepts / entities

- [[entities/team-git-aa-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
