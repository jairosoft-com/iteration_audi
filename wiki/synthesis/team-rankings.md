---
title: "Team Rankings — Current Score, Momentum, and Forward Outlook"
type: synthesis
tags: [rankings, portfolio, trend, momentum, volatility, forward-look]
sources:
  - "../synthesis/portfolio-trend.md"
  - "../synthesis/iteration-7.1-close.md"
  - "../synthesis/pi7-plan.md"
  - "../synthesis/ups-masking-pattern.md"
  - "../synthesis/service-model-scoring.md"
  - "../synthesis/scoring-artifacts.md"
  - "../synthesis/top-compliance-issues.md"
created: 2026-04-20
updated: 2026-04-28
---

# Team Rankings — Current Score, Momentum, and Forward Outlook

Composite ranking of all 10 portfolio teams as of **2026-04-19 close** (Iteration 7.1). Combines three signals: **current score** (snapshot health), **7-day slope** (momentum), and **volatility σ** (reliability of the reading). Built from a programmatic scan of 270 audit summaries; the math is reproducible — see *Methodology* at the bottom.

## 2026-04-28 snapshot — Iter 7.2 Day 9 (superseding table below)

Current live rankings from Day 9 audits (2026-04-28). **Shared Services achieves Low Risk for the first time ever (84.6, +17.0)** — a portfolio milestone. **LS Dev enters Day 2 of High Risk (47.9, −2.8)** — continued decline, reactive-only sprint. **JIT DP reset to 0.0** — formula change exposed structural gap. Net portfolio mean +1.7 (70.8→72.5). The 2026-04-19-close tier structure further down is historical context and should not be used for current decisions.

| # | Team | Type | Score (Day 9) | Δ vs D8 | Band | Direction |
|--:|------|:----:|-------------:|--------:|------|:---------:|
| 1 | [[entities/team-ado-shared]] Shared Services | ADO | **84.6** | **+17.0** | 🟢 Low | ↑↑ **FIRST EVER LOW RISK** |
| 2 | [[entities/team-ado-hr]] HR Recruitment | ADO | **81.4** | 0.0 | 🟢 Low | → |
| 3 | [[entities/team-ado-fin]] Finance | ADO | 77.9 | 0.0 | 🟡 Mod | → |
| 4 | [[entities/team-ado-otp]] Office of the President | ADO | 74.8 | 0.0 | 🟡 Mod | → |
| 5 | [[entities/team-ado-fl-dev]] Flawless Wedding | ADO | 74.0 | +3.8 | 🟡 Mod | ↑ |
| 6 | [[entities/team-ado-admin]] Administration | ADO | 73.4 | +1.3 | 🟡 Mod | ↑ |
| 7 | [[entities/team-git-aa-dev]] Auto Allies | Git | UPS 71.0 | +2.7 | 🟡 Mod | ↑ |
| 8 | [[entities/team-ado-jit]] JIT Operation | ADO | 70.4 | −5.6 | 🟡 Mod | ↓ (DP reset 0.0) |
| 9 | [[entities/team-git-cc-dev]] Colina Health | Git | UPS 69.4 | +0.90 | 🟡 Mod | ↑ |
| 10 | [[entities/team-ado-ls-dev]] Life Style Help | ADO | **47.9** | **−2.8** | **🟠 High Risk** | ↓ **Day 2 High Risk** |

**Band distribution:** 2 Low · 7 Moderate · 1 High · 0 Critical.

### Noteworthy shifts vs 2026-04-27 (Day 8)

- **Shared Services reaches Low Risk (84.6, +17.0)** — first time ever in the portfolio. Fastest single-day gain of PI7.2. Milestone; sustainability monitoring warranted.
- **LS Dev Day 2 High Risk (47.9, −2.8)** — continued decline; reactive-only sprint with no structural recovery steps taken. Recovery path unchanged: add ≥1 User Story, estimate #203247 Spike SP, close #203239 Defect. **Ike must activate #195727 FIRST to avoid BR trap** (see [[wiki/TODO]]).
- **JIT DP reset to 0.0** — Audit #44 formula change exposed structural gap; 9 closed items exited visible board. Previously appeared at 76.0 (+2.1 on Day 8); real structural state now visible. Watch Day 10 trajectory.
- **Flawless ↑ +3.8** and **Admin ↑ +1.3** — both continue steady climb.
- **AA Dev ↑ +2.7** — positive momentum; UPS masking pattern still live (see below).
- **Colina ↑ +0.90** — incremental progress.
- **HR and Finance → flat** — holding steady at Low and Moderate respectively.
- **OTP → flat** — no movement; slow-bleed concern from prior analyses unchanged.

### Auto Allies masking pattern — still live

UPS 71.0 continues to mask underlying component deficiencies. Branch protection remains the single highest-ROI action for this team — see [[synthesis/ups-masking-pattern]] option (B) "composite-masks-component override" proposal, which would downgrade AA's displayed band to the worst component.

---

## 2026-04-27 snapshot — Iter 7.2 Day 8 (historical)

LS Dev entered High Risk for the first time in PI7.2 (50.7, −10.4, WIB collapse). Shared Services upgraded 56.1→67.6 (+11.5). Portfolio mean 70.8. Superseded by 2026-04-28 snapshot above.

| # | Team | Type | Score (Day 8) | Δ vs 4/26 | Band |
|--:|------|:----:|-------------:|----------:|------|
| 1 | HR Recruitment | ADO | 81.4 | −2.3 | 🟢 Low |
| 2 | Finance | ADO | 77.9 | 0.0 | 🟡 Mod |
| 3 | JIT Operation | ADO | 76.0 | +2.1 | 🟡 Mod |
| 4 | Office of the President | ADO | 74.8 | 0.0 | 🟡 Mod |
| 5 | Administration | ADO | 72.1 | +1.1 | 🟡 Mod |
| 6 | Flawless Wedding | ADO | 70.2 | 0.0 | 🟡 Mod |
| 7 | Auto Allies | Git | 70.7 | +2.4 | 🟡 Mod |
| 8 | Colina Health | Git | 68.49 | +0.30 | 🟡 Mod |
| 9 | Shared Services | ADO | 67.6 | +3.4 | 🟡 Mod |
| 10 | Life Style Help | ADO | 50.7 | −10.4 | 🟠 High |

---

## 2026-04-24 snapshot — Iter 7.2 Day 5 (historical)

Current live rankings from [[summaries/portfolio-20260424-0935]] at time of Day 5. **Critical band cleared for the first time in PI7.2**; 2 upward band crossings overnight; portfolio mean **+5.3 in one snapshot** (64.6 → 69.9). Superseded by 2026-04-27 snapshot above.

| # | Team | Type | UPS (Day 5) | Δ vs 4/23 PM | Band | Direction |
|--:|------|:----:|------------:|-------------:|------|:---------:|
| 1 | [[entities/team-ado-hr]] HR Recruitment | ADO | **83.7** | +0.4 | 🟢 Low | steady (4-audit Low streak) |
| 2 | [[entities/team-ado-fin]] Finance | ADO | 77.9 | 0.0 | 🟡 Mod | qualitative ↑ (all 3 items Active) |
| 3 | [[entities/team-ado-jit]] JIT Operation | ADO | 74.0 | +0.8 | 🟡 Mod | ↑ |
| 4 | [[entities/team-ado-admin]] Administration | ADO | 71.0 | 0.0 | 🟡 Mod | ➡️ 4-audit stasis |
| 5 | [[entities/team-git-cc-dev]] Colina Health | Git | 70.9 | +2.3 | 🟡 Mod | ↑ (GitHub restored) |
| 6 | [[entities/team-ado-fl-dev]] Flawless Wedding | ADO | **69.5** | **+11.1** | 🟡 Mod ↑ | 🔺 High→Moderate |
| 7 | [[entities/team-ado-otp]] Office of the President | ADO | 68.7 | +3.5 | 🟡 Mod | ↑ |
| 8 | [[entities/team-git-aa-dev]] Auto Allies | Git | 65.7 | −1.7 | 🟡 Mod ↓ | mixed (first closure, but scope added) |
| 9 | [[entities/team-ado-ls-dev]] Life Style Help | ADO | **61.1** | **+21.4** | 🟡 Mod ↑↑ | 🔺 Critical→Moderate (LARGEST PI7.2 gain) |
| 10 | [[entities/team-ado-shared]] Shared Services | ADO | 56.1 | +15.0 | 🟠 High | ↑↑ (exits 6-audit TC zero-streak) |

**Band distribution:** 1 Low · 8 Moderate · 1 High · 0 Critical (prior day: 1 / 6 / 2 / 1).

---

## Historical context — 2026-04-19 close rankings

## Top takeaways

- **Portfolio leader:** [[entities/team-ado-fin]] at **93.7**, with +1.71/d momentum.
- **Cleanest trajectory:** [[entities/team-git-cc-dev]] — UPS 90.6, σ 13.58, no artifact events.
- **Highest momentum:** [[entities/team-ado-fl-dev]] at **+4.72/d** — but from a deep rubric-era floor; treat with caution.
- **Only genuine negative trend:** [[entities/team-ado-otp]] — slow bleed (−0.88/d) with stable σ 4.01 (high confidence in the decline).
- **Hidden decline:** [[entities/team-git-aa-dev]] — UPS looks stable (+1.14/d) but **HCI 49 + SGPI 21.2% are Critical/Red**; composite math hides it ([[synthesis/ups-masking-pattern]]).
- **Shared Services** has 1 data point (baseline 32.2); not a ranking participant until trend data accumulates.

## Overall ranking table

| # | Team | Type | Latest | Δ prev | 7d slope | σ | Mean | Range | Direction |
|--:|------|:----:|------:|-------:|---------:|----:|------:|-------|:---------:|
| 1 | [[entities/team-ado-fin]] Finance | ADO | **93.7** | 0.0 | **+1.71/d** | 14.49 | 75.1 | 35.0 – 93.7 | ⬆️ |
| 2 | [[entities/team-git-cc-dev]] Colina Health | Git | **90.6** | +0.3 | +1.24/d | 13.58 | 78.6 | 51.9 – 90.6 | ⬆️ |
| 3 | [[entities/team-ado-admin]] Administration | ADO | 87.0 | −1.6 | +1.53/d | 16.21 | 58.4 | 22.9 – 88.6 | ⬆️ |
| 4 | [[entities/team-ado-hr]] HR Recruitment | ADO | 87.0 | +8.6 | +1.58/d | **22.56** | 66.9 | 20.0 – 90.8 | ⬆️ (volatile) |
| 5 | [[entities/team-ado-ls-dev]] Life Style Help App | ADO | 82.4 | +71.2 | +3.21/d | 14.04 | 59.3 | 11.2 – 82.4 | ⬆️ (artifact-boosted) |
| 6 | [[entities/team-ado-fl-dev]] Flawless Wedding App | ADO | 79.3 | +10.5 | **+4.72/d** | 20.85 | 44.2 | 6.1 – 79.3 | ⬆️ (from floor) |
| 7 | [[entities/team-ado-otp]] Office of the President | ADO | 71.2 | 0.0 | **−0.88/d** | 4.01 | 75.7 | 66.9 – 81.5 | ⬇️ |
| 8 | [[entities/team-ado-jit]] JIT Operation | ADO | 68.8 | **−9.6** | −0.32/d | 20.03 | 69.0 | 4.5 – 86.8 | ➡️ (recent drop) |
| 9 | [[entities/team-git-aa-dev]] Auto Allies | Git | UPS 68.6 | −0.3 | +1.14/d ⚠️ | 5.05 | 61.3 | 53.0 – 68.9 | ⚠️ masked |
| 10 | [[entities/team-ado-shared]] Shared Services | ADO | 32.2 | — | — | — | — | 32.2 | — (baseline) |

## Tier groupings

### Tier 1 — Healthy and climbing (sustained performers)

High current score · positive momentum · manageable volatility. These teams should sustain into PI7.2 without heavy intervention.

- **[[entities/team-ado-fin]] Finance (93.7, +1.71/d).** Portfolio leader; came from a Feb baseline of 35.0. Only caveat: the eAFS/BIR #201448 is compliance-decoupled — scoring can't verify completion. See [[synthesis/compliance-misalignment]].
- **[[entities/team-git-cc-dev]] Colina Health (UPS 90.6, +1.24/d).** Cleanest Git-side trajectory. Risk: HIPAA PR #BE55 carrying into 7.2 without required-reviewer branch protection. [[synthesis/top-compliance-issues]] rank #5.

### Tier 2 — Healthy with historical wobble

Strong current score · positive slope · but the σ says a score artifact could whip it around. Watch for PI boundaries and close-day formula events.

- **[[entities/team-ado-admin]] Administration (87.0, +1.53/d, σ 16.21).** Δ −1.6 since prior audit is noise; real risk is **bus-factor-1** masked by clean execution ([[entities/person-mark-colina]], 67% burst-delivery on Apr 17).
- **[[entities/team-ado-hr]] HR Recruitment (87.0, +1.58/d, σ 22.56).** **Highest volatility in the portfolio.** Driven by rubric transitions + 2026-04-01 perfect-sprint artifact (−63.4). 7.2 overbook (30 SP vs 22 SP capacity) could trigger another swing; see [[synthesis/capacity-planning]].

### Tier 3 — Mid-score with strong climb (trajectory beats snapshot)

Slope is more compelling than current position. But check for artifact-inflation before trusting the trend.

- **[[entities/team-ado-ls-dev]] Life Style Help App (82.4, +3.21/d, σ 14.04).** ⚠️ **Slope inflated by 2026-04-17 sprint-close-formula artifact** (77.1 → 11.2 then recovered to 82.4). Excluding the artifact, true slope is much shallower. Chronic tax: #187240 at 244 days ([[synthesis/stale-work-items]]).
- **[[entities/team-ado-fl-dev]] Flawless Wedding App (79.3, +4.72/d, σ 20.85).** **Highest momentum in portfolio,** but climbing from a pre-SAFe-rubric 6.1 floor. Real climb is genuine; [[entities/person-carol]] absent from capacity config is the remaining structural gap.

### Tier 4 — Mid-score with negative or flat momentum

Visible issues in the audit layer are pulling these down. Active intervention candidates.

- **[[entities/team-ado-otp]] Office of the President (71.2, −0.88/d, σ 4.01).** **Only team with genuine negative 7-day slope AND low volatility** — highest-confidence declining signal in the portfolio. #198587 signage-install not closed in ADO is a direct Delivery Predictability drag.
- **[[entities/team-ado-jit]] JIT Operation (68.8, flat slope, Δ −9.6 last audit).** Fresh tank: **Delivery Predictability 0.0** at 7.1 close (Grace's #201504/#201514 untouched 16 days; see [[entities/person-grace]]). Flat 7-day slope masks the −9.6 audit-to-audit drop because a prior rise cancels it.
- **[[entities/team-git-aa-dev]] Auto Allies (UPS 68.6, +1.14/d on paper).** ⚠️ **UPS composite is hiding Critical components** — HCI 49 (Critical), SGPI 21.2% (Red). Moderate UPS + low σ look stable; engineering reality is not. Jerlyn zero-contribution 3 straight sprints ([[entities/person-jerlyn]]). See [[synthesis/ups-masking-pattern]].

### Tier 5 — Baseline only

- **[[entities/team-ado-shared]] Shared Services (32.2, no trend data).** One audit on record. Score is partly real (capacity 0.0, DP 0.0) and partly service-model rubric artifact (WIB −70 penalty). Tier-aware rubric ([[synthesis/service-model-scoring]]) would re-score to ~55–60 Moderate.

## Trending-down calls (from different angles)

### Genuine negative momentum (7d slope < 0)

| Team | Slope | Note |
|------|------:|------|
| [[entities/team-ado-otp]] | −0.88/d | Slow bleed; stable σ 4.01; high confidence it's real |
| [[entities/team-ado-jit]] | −0.32/d | Flat slope hiding fresh −9.6 audit-to-audit drop; will decline further unless Grace's items unblock |

### Hidden decline (headline stable, components falling)

| Team | Signal | Citation |
|------|--------|----------|
| [[entities/team-git-aa-dev]] | UPS Moderate steady, but HCI Critical + SGPI Red | [[synthesis/ups-masking-pattern]] |

### Volatility risk (not falling now, but artifact-prone)

| Team | σ | Past artifact event |
|------|--:|---------------------|
| [[entities/team-ado-hr]] | 22.56 | 2026-04-01 perfect-sprint −63.4 |
| [[entities/team-ado-fl-dev]] | 20.85 | Rubric-era baseline collapse (floor 6.1) |
| [[entities/team-ado-jit]] | 20.03 | Peaked at 86.8 on 04-04, now 68.8 (−18) |

## Historical comparison (current vs. own mean)

| Team | Mean | Latest | Δ vs mean | Verdict |
|------|-----:|------:|----------:|---------|
| Flawless Wedding App | 44.2 | 79.3 | +35.1 | Most improved ✓ |
| Administration | 58.4 | 87.0 | +28.6 | Much better than history ✓ |
| Life Style Help App | 59.3 | 82.4 | +23.1 | Big improvement (some artifact) |
| HR Recruitment | 66.9 | 87.0 | +20.1 | Better than history ✓ |
| Finance | 75.1 | 93.7 | +18.6 | Better than history ✓ |
| Colina Health | 78.6 | UPS 90.6 | +12.0 | Better than history ✓ |
| Auto Allies | 61.3 | UPS 68.6 | +7.3 | Better on paper; masked ⚠️ |
| JIT Operation | 69.0 | 68.8 | −0.2 | Flat; peaked at 86.8 (04-04) |
| Office of the President | 75.7 | 71.2 | **−4.5** | **Below own historical mean** ✗ |
| Shared Services | — | 32.2 | — | Baseline |

Only [[entities/team-ado-otp]] is currently performing below its own historical average.

## Forward outlook — PI7.2

Buckets for [[entities/person-ramon]] / [[entities/person-karl]] planning review:

- **Strong bets (sustain with light coaching):** Finance · Colina Health · Administration (**if bus-factor-1 backup assigned**) · HR (**if capacity rebaselined**).
- **Watch closely (intervention likely needed mid-PI):** JIT (blocker-driven; reassignment of Grace's items the single-biggest lever) · OTP (slow bleed; needs root-cause dive) · Life Style (artifact-prone close days; chronic #187240).
- **Structural intervention needed (not PI-coachable alone):** Auto Allies (UPS reporting fix to surface Critical components) · Shared Services (tier-aware rubric to avoid baseline mislabel as performance failure).

See [[synthesis/pi7-plan]] for per-team forward-asks and [[synthesis/top-compliance-issues]] for the common-issue driver behind each team's position.

## Open questions

- **When do we expect [[entities/team-git-aa-dev]]'s UPS masking to break?** Currently HCI 49 / SGPI 21.2%. If SGPI drops further, the composite math could finally pull UPS below 60 Moderate — at which point the dashboard would finally reflect the engineering reality.
- **OTP's −0.88/d slope is genuine — what's the root cause?** The page doesn't have a confident diagnosis. Needs a drill-in audit.
- **Can we safely exclude artifact events from the ranking?** If we rebuild the 7-day slope excluding the 3 artifact events documented in [[synthesis/scoring-artifacts]], the ranking order changes for Life Style and HR. Future versions of this page should offer both views.
- **Shared Services trend will appear after the next iteration.** Entry to Tier rankings is blocked on data; baseline is visible but direction isn't yet known.

## Methodology

Reproducible via the data layer:

1. For each team slug, enumerate all `wiki/summaries/audit-<slug>-*.md` chronologically.
2. Extract the Overall (ADO) or UPS (Git) score from the `## Scores` table in each summary.
3. Compute: **latest** (most recent), **Δ prev** (latest − second-most-recent), **7-day slope** (delta vs. nearest audit ≥ 7 days earlier, annualized per day), **mean** (all audits), **σ** (standard deviation), **min/max** range.
4. Bucket by slope sign + volatility band.

Band colors and thresholds come from [[concepts/risk-bands]]; scoring definitions from [[concepts/scoring-ado-rubric]] and [[concepts/scoring-git-ups]].

**Rebuild cadence:** refresh after every iteration close, or whenever [[synthesis/portfolio-trend]] gets a new set of snapshots. Artifact events from [[synthesis/scoring-artifacts]] should be annotated (currently noted inline).

## Related

- [[synthesis/portfolio-trend]] — multi-PI context
- [[synthesis/iteration-7.1-close]] — per-team forward asks
- [[synthesis/pi7-plan]] — consolidated planning checklist
- [[synthesis/top-compliance-issues]] — what's driving each team's position
- [[synthesis/ups-masking-pattern]] · [[synthesis/service-model-scoring]] · [[synthesis/scoring-artifacts]] — the three "trust the score with caveats" pages
