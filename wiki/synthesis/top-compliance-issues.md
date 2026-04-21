---
title: "Top Compliance Issues — Portfolio-wide Ranking"
type: synthesis
tags: [compliance, issues, ranking, portfolio, safe, rubric]
sources:
  - "../synthesis/dor-leakage.md"
  - "../synthesis/service-model-scoring.md"
  - "../synthesis/stale-work-items.md"
  - "../synthesis/capacity-planning.md"
  - "../synthesis/ups-masking-pattern.md"
  - "../synthesis/compliance-misalignment.md"
  - "../synthesis/scoring-artifacts.md"
  - "../synthesis/iteration-7.1-close.md"
  - "../synthesis/pi7-plan.md"
created: 2026-04-20
updated: 2026-04-20
---

# Top Compliance Issues — Portfolio-wide Ranking

A cross-cutting ranking of the most frequent compliance issues across the 10-team portfolio, derived from a frequency scan of all 326 wiki pages + triangulation with the synthesis layer. Issues are grouped by **kind** (team discipline · engineering practice · scoring artifacts · measurement gaps), not by score impact, so readers can see where discipline gaps end and rubric edge cases begin.

**Top takeaway:** DoR gaps + Work Item Balance + stale items + bus-factor-1 + capacity misconfig together account for ~60% of compliance-issue mentions across the wiki. All five are addressed by the four systemic changes in [[synthesis/pi7-plan]].

## Ranking table (by wiki mention frequency)

| # | Issue | Frequency | Kind | Primary source |
|--:|-------|----------:|------|----------------|
| 1 | DoR leakage — items committed without Description / AC / SP | 257 | discipline | [[synthesis/dor-leakage]] |
| 2 | Work Item Balance penalty — distribution out of expected range | 238 | discipline (often artifact on service teams) | [[synthesis/service-model-scoring]] |
| 3 | Stale chronic items (>90 days untouched) | 57 | discipline | [[synthesis/stale-work-items]] |
| 4 | Bus factor 1 — single-point delivery dependency | 49 | discipline | [[entities/person-mark-colina]] |
| 5 | Branch protection / CI hygiene gaps | 43 | engineering | [[entities/team-git-cc-dev]] (HIPAA PR BE#55) |
| 6 | Delivery Predictability collapse (0 SP Day 12→14) | 37 | discipline | [[entities/team-ado-jit]] |
| 7 | No Iteration Goal / PI Objectives documented | 34 | discipline | [[entities/team-ado-hr]] legacy audits |
| 8 | Compliance deadlines decoupled from ADO boards | 28 | measurement gap | [[synthesis/compliance-misalignment]] |
| 9 | Bulk-add / denominator artifacts | 22 | scoring artifact | [[synthesis/scoring-artifacts]] |
| 10 | UPS composite masks Critical components | 18 | measurement gap | [[synthesis/ups-masking-pattern]] |
| 11 | Capacity overbooked (commitment > configured) | 17 | discipline | [[synthesis/capacity-planning]] |
| 12 | PI boundary / Holy Week / IP week evacuation | 13 | scoring artifact | [[synthesis/scoring-artifacts]] |
| 13 | Zero-contribution pattern (14+ days, no artifacts) | 11 | engineering | [[entities/person-jerlyn]] |
| 14 | Sprint-close formula artifact (Day-14 drop 50+ pts) | 11 | scoring artifact | [[synthesis/scoring-artifacts]] |
| 15 | Capacity not configured at all | 10 | discipline | [[synthesis/capacity-planning]] |
| 16 | Items created mid-iteration without DoR | 7 | discipline | [[synthesis/dor-leakage]] |

## Category 1 — Team discipline (the real fixables)

These are actual compliance gaps, not rubric artifacts. Improving these raises scores AND delivery quality.

### DoR leakage (1 · 257 mentions)

Items committed to an iteration without meeting Definition of Ready. Shared Services committed 3 of 5 items in Grooming state on Iter 7.1; Flawless DoR Compliance sat at 28.6 Critical as late as 04-12; Admin spawned #202894 on Day 14 with no SP / Description / AC.
**Remediation:** DoR gate at planning close — items missing Description + AC + SP auto-tag `provisional` and eject at kickoff+2d unless groomed. Closures with thin DoR tagged `closed-with-debt`. See [[synthesis/dor-leakage]].

### Work Item Balance penalty (2 · 238 mentions)

Two distinct phenomena collapsed under one rubric dimension:

- **Real imbalance** — e.g., [[entities/team-ado-admin]]'s 100% User Story dominance (no Spike/Enabler) drives a −30 penalty; one Spike in 7.2 would remove it.
- **Structural artifact** — e.g., [[entities/team-ado-shared]]'s 80% Enabler share + 0 User Stories is *correct* for a cross-cutting services team but triggers a −70 penalty.
**Remediation:** Tier-aware rubric per [[synthesis/service-model-scoring]] — `team_type` attribute; service teams drop the User-Story-share penalty; product teams retain it.

### Stale / chronic items (3 · 57 mentions)

LS Dev #187240 "Evaluate Deployment and Distribution Options" is the stalest at **244 days** with a 9-audit `stale_180` penalty streak. JIT #201504/#201514 (Grace's items, 16 days untouched) are the same pattern at a younger age.
**Remediation:** Quarterly PI-close amnesty sweep — items >90 days `ChangedDate` default to close-as-obsolete unless an owner defends in a 10-minute triage window. See [[synthesis/stale-work-items]].

### Bus factor 1 (4 · 49 mentions)

[[entities/team-ado-admin]] is the canonical case — [[entities/person-mark-colina]] is the sole assignee for 27 SP. Clean execution (18 SP Apr 17 burst) masks the structural risk.
**Remediation:** Pair-assign a backup; reset 5h/day capacity to reflect reality; flag bus-factor-1 teams in portfolio dashboard.

### Delivery Predictability collapse (6 · 37 mentions)

[[entities/team-ado-jit]] closed **0 SP out of 3 SP committed** on Iter 7.1 (Days 12→14) — Grace's #201504/#201514 untouched 16 days. [[entities/team-ado-shared]] hit the same 0/3 on baseline.
**Remediation:** Track blocked-owner pattern; reassign when owner capacity is sub-threshold. Tied to the capacity wrong-mix failure mode in [[synthesis/capacity-planning]].

### No Iteration Goal / PI Objectives (7 · 34 mentions)

[[entities/team-ado-hr]] had this flagged for **12 consecutive audits** pre-PI7; several other teams occasionally flagged. Goals aren't required-field in ADO.
**Remediation:** Planning-gate requirement — iteration cannot start without a goal entered.

### Capacity problems (11 + 15 · 27 mentions combined)

Three failure modes documented in [[synthesis/capacity-planning]]:

- **Not configured** (Shared Services Team Capacity 0.0 — deterministic zero)
- **Overbooked** (HR 7.2: 30 SP committed vs. 22 SP capacity; Admin 7.2: 32 vs 27)
- **Wrong mix** (JIT Grace at 1h/day for 2 items; Admin 5h/day fiction masking the 18-SP burst; Flawless 66.7 stuck because Carol absent from config)

**Remediation:** Capacity-discipline pre-planning gate. No iteration starts without capacity config; commitment-vs-capacity check at planning close.

### Mid-iteration created items (16 · 7 mentions)

[[entities/team-ado-admin]]'s #202894 is the canonical example — created 2026-04-19 (Day 14 of 7.1) with no SP, no Description, no AC. Drags the denominator and the DoR score simultaneously.
**Remediation:** Mid-iteration additions auto-tag `provisional`; don't count in current iteration's Iteration Planning denominator until fully groomed.

## Category 2 — Engineering practice (Git-side)

### Branch protection / CI hygiene (5 · 43 mentions)

[[entities/team-git-cc-dev]] Colina's BE#55 HIPAA PR (42 files) carrying into 7.2 without required-reviewer branch protection. Several teams also show missing CI status on PRs, unreviewed merges.
**Remediation:** Queued for a future `synthesis/ci-health` synthesis.

### Zero-contribution pattern (13 · 11 mentions)

[[entities/person-jerlyn]] on Auto Allies — 3 consecutive sprints with zero GitHub artifacts; traceable back to March. [[synthesis/ups-masking-pattern]] explains why this doesn't drop UPS below Moderate despite being clearly Critical on the engineering side.
**Remediation:** Reassignment or capacity re-baseline conversation; separately, surface as a dashboard flag via the ups-masking fix.

## Category 3 — Scoring artifacts (not real team issues)

These **look** like compliance failures but are rubric edge cases. All cited in [[synthesis/scoring-artifacts]] with proposed carve-outs.

| Artifact | Typical signature | Proposed carve-out |
|----------|-------------------|---------------------|
| Bulk-add denominator (9) | Day 14 Iteration Planning drops 50+ pts after new 7.x items added | **Day-14 T-1 fallback** — substitute T-1 value with close-window flag |
| PI boundary / Holy Week (12) | −40 to −60 pt score moves on PI transition + holiday overlap | **Rubric-version baseline** — first post-boundary audit is baseline, no cross-boundary deltas |
| Sprint-close formula (14) | Day-14 score drops 50+ pts vs. T-1 on a clean-execution team | **Perfect-sprint hold** — freeze Overall at close-day value for remainder of iteration |

See also [[synthesis/pi6-close]] for how these interacted at the PI6 close (03-31) projection-vs-reality gap.

## Category 4 — Measurement gaps (system-level)

### Compliance deadlines decoupled (8 · 28 mentions)

[[synthesis/compliance-misalignment]]: Finance #201448 eAFS Portal Submission sat Active for 9 days across the Apr 15 BIR deadline. Finance scored 93.7 Low; the regulator likely already has the filing. Audit can't verify.
**Remediation:** `compliance` tag + mandatory `deadline` field + scoring on attached regulatory receipt rather than ADO `System.State`. Standalone dashboard widget for compliance-at-risk.

### UPS masking (10 · 18 mentions)

[[synthesis/ups-masking-pattern]]: Auto Allies UPS 68.6 (Moderate) hides HCI 49 (Critical) + SGPI 21.2% (Red). The portfolio-level dashboard already hacks around it via color override (2026-04-17) — a signal the composite is untrustworthy on its own.
**Remediation:** Show all 3 components per row; surface min-component band as a second pill next to UPS.

## Remediation consolidation

Every issue above maps to at least one of the four systemic changes proposed in [[synthesis/pi7-plan]]:

1. **Capacity-discipline pre-planning gate** — addresses issues #11, #15, and part of #4 (bus factor).
2. **DoR gate at planning close** — addresses #1, #16, and indirectly #6 (DP collapse driven by un-DoR'd items).
3. **UPS component-breakdown in every dashboard row** — addresses #10 and #13 (masking + zero-contribution invisibility).
4. **Rubric carve-outs (perfect-sprint hold + rubric-version baseline + Day-14 T-1 fallback)** — addresses #9, #12, #14.

Residual items needing their own fix:

- **#5 branch protection** — queued for `synthesis/ci-health`.
- **#8 compliance deadlines** — the `compliance` tag policy in [[synthesis/compliance-misalignment]].
- **#2 Work Item Balance** — the tier-aware rubric in [[synthesis/service-model-scoring]].
- **#3 stale items** — the quarterly amnesty in [[synthesis/stale-work-items]].
- **#7 Iteration Goal** — needs a planning-gate rule (currently no dedicated synthesis).

## Open questions

- **Frequency ≠ impact.** This page ranks by wiki-mention count, which skews toward issues that show up in many summaries (chronic, broad) vs. those that spike on one team in one iteration. A score-weighted ranking (by how many score points each issue costs) could invert the order. Worth producing when portfolio-trend data is richer.
- **Cross-issue correlations.** E.g., bus-factor-1 teams tend to have clean execution scores that mask capacity fragility. Is there a reliable signature for detecting this?
- **Before/after measurement.** If PI7.2 adopts the 4 systemic changes from [[synthesis/pi7-plan]], which of these 16 issues do we expect to see drop in frequency? Set a baseline.

## Related

- [[synthesis/iteration-7.1-close]] — retrospective that seeded many of the issue flags above
- [[synthesis/pi7-plan]] — the consolidated forward-look; every systemic change maps back to issues in this ranking
- [[synthesis/portfolio-trend]] — cross-date context
- [[concepts/scoring-ado-rubric]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]
- All [[entities/team-*]] pages — per-team drill-in for any issue cited
