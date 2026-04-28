---
title: "Shared Services Turnaround — Critical to Low Risk in 11 Audits"
type: synthesis
tags: [safe, ado, audit, shared-services, turnaround, iteration-7-2]
sources:
  - "../summaries/audit-ado-shared-20260419-1947.md"
  - "../summaries/audit-ado-shared-20260427-1110.md"
  - "../summaries/audit-ado-shared-20260428-0204.md"
  - "../entities/team-ado-shared.md"
created: 2026-04-28
updated: 2026-04-28
---

# Shared Services Turnaround — Critical to Low Risk in 11 Audits

Shared Services entered Iteration 7.2 with the worst score in the portfolio (32.2 Critical); by Day 9 (A11) the team posted 84.6 Low Risk — the first Low Risk in team history and the largest single-session gain (+17.0) ever recorded for this workspace. The climb from Critical to Low took 11 audits over 9 sprint days.

## Journey

| Audit | Date | Score | Band | Key driver |
|-------|------|------:|------|------------|
| A1 (baseline) | 2026-04-19 | 32.2 | 🔴 Critical | First audit, Iteration 7.1 close; capacity unconfigured, −70 WIB, 0 SP closed |
| A2 | 2026-04-21 | ~35–40 | 🔴 Critical | Capacity still missing; DoR failures persist |
| A3 | 2026-04-22 | 53.1 | 🟠 High | Scoping correction (broader cross-team view); first non-zero DP (8/14 SP) |
| A4 | 2026-04-23 | 35.3 | 🔴 Critical | Team-owned scope only; rubric artifacts re-surface on tight sprint |
| A5/A6 | 2026-04-24 | 56.1 | 🟠 High | **TC configured for first time** (Teofilo 6h, Vicsante 6h, Jaszmeine 3h); TC 0→100 (+14.3 overall) |
| A7 | 2026-04-25 | 56.1 | 🟠 High | Stagnant — all P0 actions from A6 still open |
| A9 | 2026-04-26 | 64.2 | 🟡 Moderate | **First delivery** (5 SP: #202464, #203231, #203266); DP 0→62.5% |
| A10 | 2026-04-27 | 67.6 | 🟡 Moderate | #202687 DoR resolved (11-day stale); #203309 sized; scope 7→8 items |
| **A11** | **2026-04-28** | **84.6** | **🟢 Low** | **Triple structural fix: D1 scope 8→26, D5 US added, D6 #202551 cleared** |

> A2 and A8 scores are approximate; exact values not ingested as wiki summaries. See [[entities/team-ado-shared]] audit history for raw links.

## Structural drivers of the A10→A11 +17.0 jump

### 1. D1 scope tripling — 8→26 work items (+46.8 on Iteration Planning)

The single largest dimension gain in team history. Six AI Enabler User Stories assigned to Vicsante (#200807–#200809, #203372, #203373, #203375) were pulled into the sprint, expanding committed scope from 8 to 26 items. Sprint-to-backlog ratio improved from a critically thin slice to 70.3% (D1 = 70.3). This alone accounts for the majority of the overall jump.

### 2. User Story addition eliminates −40 WIB penalty (+40.0 on Work Item Balance)

The all-Defect/Enabler sprint composition that had plagued the team since A1 (−70 WIB at baseline, −40 WIB in most 7.2 audits) was corrected. Six User Stories now constitute 23.1% of sprint items; Enabler share (57.7%) falls just below the 60% dominant-type threshold. D5 reaches 100.0 for the first time. Maintaining User Story presence in 7.3 is required to preserve this score.

### 3. #202551 refinement touch — D6 90→100 (+10.0 on Backlog Refinement)

Item #202551, flagged as untouched since at least A6, received its first refinement activity on Apr 28. With all 37 backlog items now fresh, D6 clears to 100.0, eliminating the last −20 refinement penalty.

### Teofilo throughput — 20 SP closed in one day

12 items totaling 20 SP closed by Teofilo (DevOps/IT work: #202396, #202464, #203114–#203117, #203229, #203231, #203266, #203296, #203312). Delivery is real, not a scoring artifact. This burst also suppresses D7 (expanded denominator: 20/33 SP = 60.6%) — closing remaining 13 SP would push D7 to 100.0 and overall to 94.4.

## Risks / open questions

| Risk | Impact | Status |
|------|--------|--------|
| 8 items unestimated (Vicsante AI queue: #200807–#200809, #203372, #203373, #203375, #203393, +1) | D3 69.2 → 100.0 if sized (overall +4.4) | Open — all in Estimation state, Day 10 target |
| #202687 in New state (3 SP, Jaszmeine) | High spill risk to 7.3; 9-day New streak | Open |
| D7 dips −1.9 despite more absolute closures | Expanded denominator effect; 13 SP remain open | Manageable if sprint closes clean |
| #186848 backlog age | Old ID suggests pre-2026 creation; ChangedDate unverified; D6 staleness risk | Unverified |
| WIB sustainability | US presence requires active maintenance in 7.3+ | Structural — monitor each sprint |
| Is 84.6 repeatable? | Scope tripling was partly a one-time queue drain; natural 7.3 baseline may regress D1 | Structural — watch 7.3 A1 |

The 84.6 Low Risk score is real but partly driven by a scope catch-up event (pulling Vicsante's AI queue). Sustaining Low Risk in 7.3 requires: (a) deliberate User Story inclusion, (b) full estimation at sprint start, and (c) #202687 closure or formal deferral before 7.3 planning.

## Related pages

- [[entities/team-ado-shared]] — full team profile, audit history, stakeholders
- [[concepts/risk-bands]] — Critical / High / Moderate / Low thresholds
- [[concepts/scoring-ado-rubric]] — 7-dimension rubric used throughout
- [[synthesis/portfolio-trend]] — portfolio-wide context; Shared Services was sole Critical at A1
