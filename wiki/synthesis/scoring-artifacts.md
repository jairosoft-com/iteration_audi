---
title: "Scoring Artifacts — Rubric Transitions, Formula Edge Cases, PI Boundaries"
type: synthesis
tags: [scoring, rubric, artifacts, portfolio]
sources:
  - "../summaries/portfolio-20260401-0900.md"
  - "../summaries/portfolio-20260402-0900.md"
  - "../summaries/portfolio-20260405-0900.md"
  - "../summaries/portfolio-20260416-0900.md"
  - "../summaries/portfolio-20260417-0900.md"
  - "../summaries/portfolio-20260419-1345.md"
  - "../summaries/audit-ado-hr-20260401-0900.md"
  - "../summaries/audit-ado-ls-dev-20260416-0900.md"
  - "../summaries/audit-ado-ls-dev-20260417-0900.md"
  - "../summaries/audit-ado-ls-dev-20260419-1345.md"
  - "../summaries/audit-ado-jit-20260428-0203.md"
created: 2026-04-20

## updated: 2026-04-28

# Scoring Artifacts — Rubric Transitions, Formula Edge Cases, PI Boundaries

## Headline

Three distinct events inside the 2026-02-25 → 2026-04-19 window look like portfolio regressions but are scoring artifacts: a rubric dimension-count change, a perfect-sprint empty-commitment collapse, and a Day-14 sprint-close formula edge case. Plus one structural driver — the PI6 → PI7 boundary + Holy Week — which is real but non-performance. **Do not compute slopes across these dates.** Each is evidence of rubric mechanics, not team trajectory, and each needs a formal carve-out in [[concepts/scoring-ado-rubric]] before trend lines can be trusted.

## Artifact 1 — Rubric transition 2026-04-05 (6-dim → 7-dim)

**Cause.** Introduction of Delivery Predictability as the 7th ADO dimension on PI6 final day. Overall score shifts from mean-of-6 to mean-of-7, and Delivery Predictability itself reads low for teams mid-close.

**Signature in data.**

- Portfolio mean 60.4 → **56.9** (−3.5); median 61.4 → 63.1 (+1.7) — mean drops while median rises (penalty concentrates in already-struggling teams).
- **Nadir** of the 19-snapshot window on mean (56.9) and a matching Low-band count of 1 (only Colina at 80.5).
- Source: [[summaries/portfolio-20260405-0900]] explicitly flags "Rubric v2 activated — ADO teams now scored on 7 dimensions including Delivery Predictability. All ADO trends carry a transition artifact."

**Teams affected (selected deltas day-over-day).**

| Team | Δ vs 04-04 | Note |
|------|-----------:|------|
| [[entities/team-ado-jit]] | −22.1 | Lost portfolio-lead status (had been 86.8) |
| [[entities/team-ado-fin]] | −12.1 | Still Moderate but material |
| [[entities/team-ado-otp]] | −8.2 | From Low into Moderate |

**How to detect from data alone.** Compare dimension count in the rubric header across two consecutive audit files for the same team — if dimension_count changes, flag every overall-score delta spanning that boundary as methodology-driven. Every ADO team's deltas across 04-04 → 04-05 carry a transition component.

## Artifact 2 — Perfect-sprint / empty-commitment (HR 2026-04-01)

**Cause.** When a team closes 100% of committed items before the audit runs, `current_iteration_items = 0` drives zero-denominators in 4 of 6 (now 7) dimensions — Iteration Planning, Team Capacity, Estimation, DoR Compliance all collapse to 0.0, and the arithmetic mean drags Overall to near-zero.

**Signature in data.**

- [[entities/team-ado-hr]]: 90.1 Low (03-31) → **26.7 Critical** (04-01) → 83.0 Low (04-02). Δ one-day = **−63.4**, Δ two-day = +56.3. A V-shape across 48 hours on otherwise clean delivery.
- Sprint context: 14/14 items Closed, 27/27 SP — HR's **2nd consecutive perfect sprint**. Source: [[summaries/audit-ado-hr-20260401-0900]] top-line: "Scoring artifact — Overall collapses to 26.7 (Critical) because all 14 sprint items are Closed and 16 unassigned items remain visible."
- [[summaries/portfolio-20260401-0900]] pre-flags the reading as "artifact" in the Critical row.

**How to detect from data alone.** If a team's prior audit shows `closed_items == committed_items` AND the next audit shows `active_items == 0` AND 4+ dimension scores collapse to 0.0 simultaneously — it's this artifact, not a regression. A zero-denominator on three or more dimensions in one snapshot should auto-suppress the overall reading.

## Artifact 3 — Sprint-close formula (Life Style Help App 2026-04-17)

**Cause.** Same family as Artifact 2, but triggered by **mid-close board state**: items Closed and items moved to the next iteration both exit the scoped backlog, leaving a transient window where `current_iteration_root_items = 0`. Iteration Planning / Capacity / Estimation / DoR / Delivery Predictability all zero-floor.

**Signature in data.**

- [[entities/team-ado-ls-dev]]: 77.1 Moderate (04-16) → **11.2 Critical** (04-17) → 82.4 Low (04-19 13:45). Same dataset semantically (one sprint, no new work). Δ one-day = **−65.9**, then +71.2 rebound. See [[summaries/audit-ado-ls-dev-20260416-0900]], [[summaries/audit-ado-ls-dev-20260417-0900]], [[summaries/audit-ado-ls-dev-20260419-1345]].
- The 04-19 audit explicitly states: "Do not interpret the +71.2 delta as sudden improvement." Real gain vs nearest clean reading (A23 = 77.1) is **+5.3**, not +71.2.
- Parallel override same day: [[entities/team-git-aa-dev]] scored 68.6 (band-computed Moderate per [[concepts/risk-bands]]) but color-coded Orange/High Risk per `git_iteration_audit` standard because HCI 49 and SGPI 21.2% Red are masked by composite UPS. Source: [[summaries/portfolio-20260417-0900]].

**How to detect from data alone.** Flag any Day-N (N ≥ Day-12) audit where `active_items == 0` but `closed_items + moved_items ≥ committed_items`. Specifically: if `active_items == 0` AND ≥ 3 dimensions read 0.0 AND prior-day overall was ≥ 60, the reading is a close-window artifact.

## Structural — PI boundary / IP week (2026-04-01 → 04-02)

**Not a scoring artifact, but non-performance.** [[entities/team-ado-admin]] evacuated its entire sprint (9 items; 6 moved to PI7 Iter 7.1, 3 removed) on 04-02 for Holy Week + Innovation Planning. Score 72.3 → **26.7**, Δ −45.6. Source: [[summaries/portfolio-20260402-0900]] frames it as "intentional Holy Week + IP boundary action, not a delivery failure."

The portfolio mean regression across 04-01 → 04-05 (~15 points) is a mix of (a) this structural evacuation, (b) Artifact 1 (rubric transition), and (c) Artifact 2 (HR perfect-sprint). None is team performance.

## Artifact 4 — DP visible-board reset (JIT 2026-04-28)

**Cause.** When all previously-closed sprint items exit the visible backlog (board cleanup), the Delivery Predictability formula computes `0 SP closed / N SP visible = 0.0%` even though real delivery occurred. The DP denominator is scoped to currently-visible board items only — items that closed and exited are invisible to the rubric.

**Signature in data.**

- [[entities/team-ado-jit]]: DP 34.0 → **0.0** (Δ −34.0); Overall 76.0 → **70.4** (Δ −5.6, Moderate band maintained).
- Actual sprint output: **17 SP / 9 items closed** before the audit ran (~1.9 SP/day delivery pace). All 9 closed items exited the visible board prior to the audit window; rubric sees 0/31 SP = 0.0.
- Same class as Artifact 2 (HR perfect-sprint empty-commitment collapse): zero-denominator driven by board state, not delivery failure.
- Source: [[summaries/audit-ado-jit-20260428-0203]] top-line: "Structural reset — 0 SP closed in visible backlog (all 9 closed items exited). Actual sprint output = 17 SP across 9 items."

**Distinguishes from real regression.** Artifact 2 collapses four dimensions simultaneously (zero active items → zero-denominator in IP, Capacity, Estimation, DoR). This artifact collapses DP only — remaining six dimensions score normally. If DP alone drops to 0.0 while all other dimensions are ≥ 70, suspect closed-item board exit, not delivery failure.

**Teams affected.**

| Team | Audit | DP Δ | Overall Δ | Note |
|------|-------|-----:|----------:|------|
| [[entities/team-ado-jit]] | #44 Day 9 2026-04-28 | −34.0 | −5.6 | 9 items exited visible board; real delivery continued |

**Proposed carve-out.** DP denominator should include items **closed-and-exited within the current sprint window**, not only currently-visible board items. Specifically: DP = (SP closed in sprint, including exited items) / (SP committed at sprint start). This preserves the metric's intent (did the team deliver against commitment?) while eliminating the exit-artifact. Add as Proposed Carve-out 6 in [[concepts/scoring-ado-rubric]].

## Detection rules (programmable)

Apply in order. First match wins.

1. **Rubric-version change.** If `rubric.dimension_count` differs between two audits, label the newer audit as a new baseline; do not compute cross-boundary deltas or slopes.
2. **Zero-denominator collapse.** If ≥ 3 dimensions score 0.0 in a single audit AND prior audit was ≥ 60, flag overall as `artifact` and carry forward the prior overall.
3. **Close-window board state.** If `active_items == 0` AND `closed_items + moved_to_next_iteration ≥ committed_items` at Day ≥ 12, flag as `close-artifact`.
4. **Any one-day delta ≥ 40 points.** Treat as artifact candidate pending cause assignment (rubric / close / PI boundary). Never include in slope calculations.
5. **Composite-masks-component.** If a Git team's UPS band ≠ (HCI band ∧ SGPI band) — i.e., either component is Critical while UPS is Moderate — override display band to the worse component band. Already enforced ad-hoc for Auto Allies 04-17; formalize it.

## Proposed carve-outs

Concrete rubric amendments for [[concepts/scoring-ado-rubric]] and [[concepts/scoring-git-ups]]:

1. **Perfect-sprint hold.** If a team closes 100% of committed items before the next audit window, hold the overall score static at the close-day value for the remaining days of the iteration. Resume live scoring when the next iteration's commitment is active.
2. **Rubric-version baseline.** On any dimension-count or formula change, label the first audit post-change as `baseline` per-team; do not report portfolio deltas across the version boundary. Portfolio trend pieces must treat the transition date as a segment break.
3. **Day-14 T-1 fallback.** For Day-12 through Day-14 audits, if computed overall is ≥ 30 points below T-1 AND the drop is caused by zero-denominators (rule 2 above), substitute T-1 value with a `close-window` flag. If the drop is real (failed delivery), report it normally.
4. **UPS component-floor.** Git UPS display band = min(UPS band, HCI band, SGPI band). Composite remains reported numerically; the *color* reflects the worst component.
5. **Service-model / IP-week tag.** Snapshots falling within IP week or immediately after a whole-team evacuation tagged `structural` and excluded from mean/median slope calculations (already semi-applied for Shared Services baseline per [[concepts/risk-bands]]).

## Impact on portfolio trend

Exclude these timestamps from slope and monotonic-trend calculations in [[synthesis/portfolio-trend]]:

- **2026-04-01 09:00** — HR Artifact 2; portfolio mean 64.7 understates by roughly +5.9 points.
- **2026-04-02 09:00** — Admin structural evacuation; mean 59.6 understates.
- **2026-04-05 09:00** — Artifact 1 rubric transition; nadir 56.9 is methodology, not performance.
- **2026-04-17 09:00** — LS Dev Artifact 3 + Auto Allies override; mean 72.1 understates by roughly +7 points.

Valid PI7.1 slope (04-06 → 04-19 13:45) = mean 62.0 → 81.0 over 14 days (+1.36/day), consistent with the pre-carve-out "cleanest trajectory in the dataset" finding. Recomputing with Artifact 3 excluded tightens monotonicity; Artifact 1 exclusion is the primary reason PI6 → PI7 "regression" is not real.

## Related

- [[synthesis/portfolio-trend]]
- [[concepts/scoring-ado-rubric]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]
- [[entities/team-ado-hr]] · [[entities/team-ado-ls-dev]] · [[entities/team-ado-admin]] · [[entities/team-ado-jit]] · [[entities/team-ado-fin]] · [[entities/team-git-aa-dev]]
