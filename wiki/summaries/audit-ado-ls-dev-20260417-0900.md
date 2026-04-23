---
title: "Life Style Help App Audit — 2026-04-17 09:00"
type: summary
tags: [ado, ado-ls-dev, audit, backfill]
sources: ["../../ado_ls_dev/audit/AUDIT_20260417_0900.md"]
created: 2026-04-19

## updated: 2026-04-19

# Life Style Help App Audit — 2026-04-17 (board-state artifact)

Source: [AUDIT_20260417_0900.md](../../ado_ls_dev/audit/AUDIT_20260417_0900.md) · 2026-04-17 09:00 PHT · Iteration 7.1 (Apr 6 – Apr 19, 2026), Day 12

## TL;DR

Day 12 score reads **11.2 (Critical Risk)** — but this is a **formula artifact, not a regression**. All 9 prior sprint items were either Closed and removed from the visible backlog or moved to Iter 7.2; current_iteration_root_items = 0 triggers zero-floor rules across most dimensions. Estimated actual sprint delivery: ~57% (8 SP / 14 SP).

## Scores

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | 11.2 | 🔴 Critical |
| Iteration Planning | 0.0 | 🔴 Critical |
| Team Capacity | 0.0 | 🔴 Critical |
| Estimation | 0.0 | 🔴 Critical |
| DoR Compliance | 0.0 | 🔴 Critical |
| Work Item Balance | 60.0 | 🟡 Moderate |
| Backlog Refinement | 18.3 | 🔴 Critical |
| Delivery Predictability | 0.0 | 🔴 Critical |

> ⚠️ Formula artifact. Audit explicitly flags that the Critical score reflects successful sprint closure (all items Closed or moved to 7.2), not a process failure. A25 (2026-04-19 13:45) treats A23 (77.1) as the real prior reading.

## Top issues

- #195715, #201162, #198775 formally Closed — estimated ~8 SP delivered (57.1%).
- #196380 and #195727 responsibly moved to Iteration 7.2.
- #187240 (Enabler, 242 days stale) drives remaining Backlog Refinement penalty.
- Four Dec 2025 items still >90 days stale.

## Delta vs prior

Previous: [[audit-ado-ls-dev-20260416-0900]] — 77.1 Moderate; this: 11.2 Critical; Δ −65.9 (board-state formula artifact, not real regression).

## Linked concepts / entities

- [[entities/team-ado-ls-dev]]
- [[concepts/scoring-ado-rubric]]
- [[concepts/risk-bands]]
