---
title: "Auto Allies Audit — 2026-04-01 09:00 (Iteration 6.6 Day 8)"
type: summary
tags: [git, git-aa-dev, audit, backfill, iteration-6.6]
sources: ["../../git_aa_dev/audit/AUDIT_20260401_0900.md"]
created: 2026-04-19
updated: 2026-04-19
---

# Auto Allies Audit — 2026-04-01 09:00 (Iter 6.6 Day 8)

Source: [AUDIT_20260401_0900.md](../../git_aa_dev/audit/AUDIT_20260401_0900.md) · 2026-04-01 09:00 · Iteration 6.6 IP (2026-03-23 → 2026-04-05)

## TL;DR

Day 8 (80%): FLAT. ICS 64.3%, SGPI 42.9%, HCI 29/100 (+1). Only 2 WDs remain. Realistic SGPI ceiling 57–64% if #199007 + both rework items close; worst case 42.9% (current). 43 iteration PRs.

## Scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | — | — (pre-UPS; ICS 64.3% 🔴) |
| ICS (×0.50) | 64.3% | 🔴 Red |
| HCI (×0.30) | 29/100 | 🔴 Critical |
| SGPI (×0.20) | 42.9% | 🟠 |

## Top issues

- Headline scores flat — no closures in 24h; 2 rework items (#201111, #201110, 6 SP) still Active, no new PRs.
- 1 item (#199007, 2 SP) in QA Testing from April 1, awaiting validation.
- #200184 (Ticket/Case Migration, 5 SP) the largest uncommitted Active item with no new PR activity.
- 0 code reviews across 43 PRs, 0% formal traceability, no branch protection — persistent.
- 2 WDs remain — closure risk high for rework items requiring both dev and QA cycles.

## Delta vs prior

Previous: [[summaries/audit-git-aa-dev-20260331-0900]] — ICS 64.3%, SGPI 42.9%, HCI 28; this: ICS 64.3% (flat), SGPI 42.9% (flat), HCI 29 (+1).

## Linked concepts / entities

- [[entities/team-git-aa-dev]]
- [[concepts/scoring-git-ups]]
- [[concepts/risk-bands]]
