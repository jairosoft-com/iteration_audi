---
title: "Flawless Wedding App Audit — 2026-04-22 0646"
type: summary
tags: [ado, ado-fl-dev, iteration-7.2, audit]
sources: ["../../ado_fl_dev/audit/AUDIT_20260422_0646.md"]
created: 2026-04-22
updated: 2026-04-22
---

# Flawless Wedding App Audit — 2026-04-22 0646

Source: [AUDIT_20260422_0646.md](../../ado_fl_dev/audit/AUDIT_20260422_0646.md) · 2026-04-22 06:46 UTC / 14:46 PHT · Iteration 7.2 (Day 3 of 14 — early-sprint) · Live-data run; prior audit #34 at 0900 held 59.6 (High) in degraded mode.

## TL;DR

**62.5/100 (🟡 Moderate, Δ +2.9 vs #34 / +2.9 vs prior ingest)** — **band promotion High → Moderate** driven by Luke's Day-3 Defect closures. Luke closed #202072 (Vendor Login Error, 2 SP) and #202119 (Blank Dashboard, 2 SP) → first non-zero Delivery Predictability of sprint (0 → 28.6). Untouched-current drops 72.7% → 25.0% as 9 of 12 items refreshed post-iter-start. **Negatives:** DoR slips 100 → 91.7 (#202827 Spike Description is **29 non-WS chars — 1 char below threshold**); Estimation slips 100 → 90.0 as new Defect #203230 enters sprint with 0 SP. **Structural ceiling:** Work Item Balance stuck at 30.0 (zero User Stories, 10 Defects + 2 Spikes). Adding one US is the highest-leverage single action (+5.7 to Overall).

## Scores

| Dimension | Score | Band | Δ vs 4/21 0800 |
|-----------|------:|------|---------------:|
| **Overall** | 62.5 | 🟡 Moderate | **+2.9** (band promotion) |
| Iteration Planning | 7.4 | 🔴 Critical | +0.3 (12/162) |
| Team Capacity | 100.0 | 🟢 Low | 0.0 (Luke + Ressa both configured + active) |
| Estimation | 90.0 | 🟢 Low | **−10.0** (#203230 added 0 SP) |
| DoR Compliance | 91.7 | 🟢 Low | **−8.3** (#202827 Desc = 29 chars) |
| Work Item Balance | 30.0 | 🔴 Critical | 0.0 (no US; −40+−30 double penalty) |
| Backlog Refinement | 90.0 | 🟢 Low | **+10.0** (untouched 72.7% → 25.0%) |
| Delivery Predictability | 28.6 | 🟠 High | **+28.6** (4 SP closed — first non-zero) |

## Top issues

- **Work Item Balance 30.0 — structural ceiling.** 10 Defects (83.3%) + 2 Spikes (16.7%) + 0 User Stories → −40 no-US penalty stacked with −30 dominant-type. Adding one US from 7.3 backlog eliminates −40, lifts WIB to 70.0 and Overall to 68.2. Highest-leverage action available.
- **#202827 Spike Description 29 chars** ("Reports and Iteration Team Events") — 1 character below 30-char DoR threshold. Trivially fixable (one more descriptive word → restores DoR to 100.0). Easiest DoR fix anywhere in the portfolio.
- **#203230 unestimated** — new "Vendor users unable to login — deleted flag" Defect added mid-sprint with 0 SP. Won't contribute to Delivery Predictability when closed. Assign ≥1 SP restores Estimation to 100.0.
- **QA queue loading up** — 3 items on Ressa (#202569 QA Testing 1 SP, #202723 + #200791 Ready for QA 2 SP each = 5 SP) plus 2 active Spikes. QA-pipeline throughput is the Day 4–6 critical path; closing all 3 QA items takes Delivery Predictability to ~64% (Low band).
- **3 pre-iteration Defects in Ready-for-Dev queue** — #190892, #191079, #201326 last touched Apr 15 (pre-sprint). Advancing any to Active removes the untouched flag and maintains Backlog Refinement at 90.0.

## Strongest positive signal

**Luke's Day-3 delivery.** Two Defects closed = 28.6% of committed 14 SP. Per the rubric's "early-sprint — low delivery expected" annotation, this is well above baseline. QA pipeline is loaded (5 SP awaiting) and a Day 4–6 closure wave would land total at 9/14 (64.3%, Low-band Delivery Predictability) mid-sprint.

## Delta vs prior ingest

Previous wiki ingest: [[summaries/audit-ado-fl-dev-20260421-0800]] — 59.6 (High, 7.2 Day 2 sprint-open). This: 62.5 (Moderate, Day 3). Δ **+2.9** — band promotion **High → Moderate**. The scoring artifact note: prior ingest's headline Overall called out this was the only ADO team in High band on 7.2 open. That claim is now superseded.

**Projection:** adding 1 US (WIB 30→70) + fixing #202827 Desc (DoR 91.7→100) + estimating #203230 (Est 90→100) → Overall ~71.2 (solid Moderate). Plus closing all 3 QA items by Day 6 → Delivery Pred 28.6→64.3 → Overall ~76.3 (approaching Low).

## Linked concepts / entities

- [[entities/team-ado-fl-dev]]
- [[concepts/scoring-ado-rubric]]
- [[concepts/risk-bands]]
- [[synthesis/service-model-scoring]]
- [[synthesis/dor-leakage]]
