---
title: "Life Style Help App Audit — 2026-04-21 1400"
type: summary
tags: [ado, ado-ls-dev, iteration-7.2, audit]
sources: ["../../ado_ls_dev/audit/AUDIT_20260421_1400.md"]
created: 2026-04-21
updated: 2026-04-21
---

# Life Style Help App Audit — 2026-04-21 1400

Source: [AUDIT_20260421_1400.md](../../ado_ls_dev/audit/AUDIT_20260421_1400.md) · 2026-04-21 14:00 PDT · Iteration 7.2 (Day 2 of 14 — early-sprint)

## TL;DR

**41.0/100 (High, Δ −41.4)** — Lowest score in workspace's PI7 series. Four compounding sprint-start failures: (1) **no team capacity configured for 7.2** (API returns `No team capacity assigned`), (2) only 2 items / 5 SP committed (severe under-scope), (3) Backlog Refinement collapses to 0.0 (stale_90 + stale_180 + untouched_current all trigger), and (4) **#187240 Enabler now 246 days stale — 10th consecutive audit**.

## Scores

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | 41.0 | 🟠 High |
| Iteration Planning | 16.7 | 🔴 Critical |
| Team Capacity | 0.0 | 🔴 Critical (not configured) |
| Estimation | 100.0 | 🟢 Low |
| DoR Compliance | 100.0 | 🟢 Low |
| Work Item Balance | 70.0 | 🟡 Moderate |
| Backlog Refinement | 0.0 | 🔴 Critical |
| Delivery Predictability | 0.0 | 🔴 Critical (early-sprint — low delivery expected) |

## Top issues

- **#187240 (Enabler) stale for 246 days — 10th consecutive audit.** Still untouched since Aug 18, 2025. Drives −20 stale_180 penalty; baseline P0 recommendation not actioned.
- **No team capacity configured for Iteration 7.2** — deterministic 0 on the dimension. 7.1 had Samantha+Luzmibel+Ike configured; none cloned to 7.2.
- **Sprint under-scoped at 2 items / 5 SP** (#196380 Default Pinned Post, #195727 Meal Time Filter). 2/12 visible items in-sprint → Iteration Planning 16.7.
- **4 PI5 stale User Stories persist** (#194082, #194084, #195229, #194386) — drives stale_90 (41.7% > 25%) → −20.
- **#195727 untouched since Apr 17** → untouched_current 50% > 30% → −20 Backlog Refinement.

## Delta vs prior

Previous: [[summaries/audit-ado-ls-dev-20260419-1345]] — 82.4 (Low); this: 41.0 (High); Δ −41.4 (compound sprint-open failures: Team Capacity −100, Iteration Planning −41.6, Backlog Refinement −18.3, Delivery Predictability −100, partially offset by Work Item Balance dropping only −30).

## Linked concepts / entities

- [[entities/team-ado-ls-dev]]
- [[concepts/scoring-ado-rubric]]
- [[concepts/risk-bands]]
- [[synthesis/stale-work-items]]
- [[synthesis/capacity-planning]]
