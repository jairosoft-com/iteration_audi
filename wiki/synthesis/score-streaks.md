---
title: "Score Streaks — Longest ≥80 Runs per Team"
type: synthesis
tags: [streaks, consistency, low-risk, rankings, scoring]
sources:
  - "../synthesis/team-rankings.md"
  - "../synthesis/portfolio-trend.md"
  - "../synthesis/scoring-artifacts.md"
  - "../synthesis/iteration-7.1-close.md"
created: 2026-04-20
updated: 2026-04-28
---

# Score Streaks — Longest ≥80 Runs per Team

Who has held Low Risk (≥80) the longest? Three different answers depending on what "streak" means:

- 🏆 **Longest single streak in history:** [[entities/team-ado-jit]] — **13 consecutive audits** (2026-03-18 → 2026-04-04).
- 🔥 **Longest currently-active streak:** [[entities/team-ado-hr]] — HR Recruitment (active, 2 consecutive audits at ≥80 as of 2026-04-28; 81.4 Day 9). Colina's 7-run ended Apr 28 (69.4 Moderate — streak broken).
- 📊 **Most cumulative audits at ≥80:** [[entities/team-ado-fin]] — **16 of 33 audits (48%)**.

Each is a legitimate read; pick by the question being asked.

## Full ranking by longest single streak

| Rank | Team | Longest streak (audits) | Span | Current streak | Total ≥80 audits | % of audits |
|-----:|------|---:|------|---:|---:|---:|
| 1 | [[entities/team-ado-jit]] JIT Operation | **13** | 2026-03-18 → 2026-04-04 | 0 | 14 / 38 | 37% |
| 2 | [[entities/team-ado-fin]] Finance | 11 | 2026-03-22 → 2026-04-04 | 0 *(77.9 plateau — 10 consecutive below 80)* | 16 / 33 | **48%** |
| 3 | [[entities/team-ado-hr]] HR Recruitment | 8 | 2026-03-22 → 2026-03-31 | **2 (active)** | 10 / 34 | 29% |
| 4 | [[entities/team-git-cc-dev]] Colina Health | 7 | 2026-04-08 → 2026-04-27 | 0 *(broken Apr 28 — 69.4)* | 8 / 12 | 67% |
| 5 | [[entities/team-ado-admin]] Administration | 3 | 2026-04-16 → 2026-04-19 | 0 | 3 / 34 | 9% |
| 6 | [[entities/team-ado-ls-dev]] Life Style Help App | 1 | 2026-04-19 | 0 *(dropped High Risk Day 8)* | 1 / 20 | 5% |
| 7 | [[entities/team-ado-otp]] Office of the President | 1 | 2026-04-04 | 0 | 2 / 19 | 11% |
| 8 | [[entities/team-ado-fl-dev]] Flawless Wedding App | 0 | — | 0 | 0 / 25 | 0% |
| 9 | [[entities/team-git-aa-dev]] Auto Allies | 0 | — | 0 | 0 / 11 | 0% |
| 10 | [[entities/team-ado-shared]] Shared Services | **1** | **2026-04-28** | **1 (active)** ⭐ | **1 / 9** | **11%** |

## The rubric-transition break event

**Four of the top 5 streaks ended at scoring-artifact events, not real regressions.** Context matters:

| Event | Date | Streaks broken |
|-------|------|----------------|
| Perfect-sprint artifact (HR -63.4) | 2026-04-01 | HR (ended 03-31) |
| Rubric transition 6-dim → 7-dim | **2026-04-05** | **JIT (ended 04-04) · Finance (ended 04-04)** |

Both top streaks fell on the same day — not because teams slipped, but because the rubric itself changed shape. See [[synthesis/scoring-artifacts]] for the proposed **rubric-version baseline** carve-out that would have preserved cross-boundary streaks.

**Implication:** If you exclude the artifact event as a streak-breaker, JIT's real arc is **2026-03-18 → 2026-04-04 (13 audits) + bridge across rubric + short re-entries through April.** The portfolio was more consistently-Low than the raw-streak numbers suggest.

## Why Colina Health's 7-run was impressive

Unlike the top three ADO teams whose streaks were killed by the ADO 7-dim rubric transition, [[entities/team-git-cc-dev]] uses the **Git UPS formula** (ICS·0.50 + HCI·0.30 + SGPI·0.20 per [[concepts/scoring-git-ups]]) — which wasn't affected by the 2026-04-05 change. Colina's streak survived every known artifact event in the window. It was the cleanest Low-Risk run in the dataset.

**Update 2026-04-28 (Day 9):** Colina fell to 69.4 Moderate on Apr 28, breaking the 7-audit streak at 2026-04-08 → 2026-04-27. The streak is now historical.

## Who never made 80

Two teams have **zero** audits at ≥80 across the entire window:

- **[[entities/team-ado-fl-dev]] Flawless Wedding App** — 25 audits, max 79.3 (latest). Close but never crossed the Low threshold. Trajectory is strongly positive; a single ≥80 audit in PI7.2 would end the streak-of-zero.
- **[[entities/team-git-aa-dev]] Auto Allies** — 11 audits, max UPS 68.9. Well below the threshold. The headline UPS masks Critical components (see [[synthesis/ups-masking-pattern]]); even if UPS crossed 80, the engineering reality would not.

**Shared Services graduated from this list on 2026-04-28:** first-ever ≥80 audit (84.6, Day 9 / A11). See milestone callout below.

## Finance structural ceiling

[[entities/team-ado-fin]] Finance holds the portfolio's highest cumulative ≥80 rate (48%) and has now posted **10 consecutive audits at 77.9** — a plateau that sits structurally below the ≥80 threshold without ever crossing it. This is the closest-without-crossing pattern in the dataset: consistent Moderate High performance but a persistent ceiling just short of Low Risk. If Finance breaks through in A12+, it will extend its all-time cumulative lead substantially.

## Shared Services milestone — first ≥80 ever (2026-04-28)

[[entities/team-ado-shared]] Shared Services posted **84.6 (Low Risk)** on 2026-04-28 (Day 9, Audit A11) — the **first time this team has ever reached the ≥80 threshold** in portfolio history. Previously: 1 audit at baseline 32.2 (Critical), with gradual recovery over subsequent audits. The jump to Low Risk is a portfolio-level first for this team.

## What sustained-Low-Risk looks like — patterns from the top 3

Three very different paths to long streaks:

**JIT (13-streak, now broken):** Ramped from 4.5 (Feb) over ~3 weeks, landed at 82.0 on Mar 18, held 82–87 for 13 audits, then the rubric transition reset everyone. Pattern: **built up, held steady, got caught in methodology change.**

**Finance (11-streak, now at Moderate plateau):** Similar ramp + long 89.5 plateau in Iter 6.6, fell on rubric change, recovered in 7.1. As of Day 9 (2026-04-28) Finance is at 77.9 — 10 consecutive audits at that level, just below the ≥80 threshold. Pattern: **long plateau at mid-80s, rubric-resistant to the extent that underlying work never changed; now showing a structural ceiling at 77.9 Moderate.**

**Colina (7-streak, now broken):** Climbed from 51.9 on 04-08 through steady small improvements, crossed 80 on 04-08 and held until 04-27. Fell to 69.4 on Apr 28. Pattern: **no plateau during the run, but streak ended without a gradual fade — single-audit break.**

## Open questions

- **If we add a streak metric to the portfolio dashboard,** does it change how teams behave? Sustained-Low should be rewarded distinct from single-audit Low.
- **Should streaks that span a rubric boundary be credited?** The data argues yes (the underlying work didn't change); the current score-based definition says no. See [[synthesis/scoring-artifacts]] carve-out #2 (rubric-version baseline).
- **Flawless and Auto Allies have never been ≥80.** Is the threshold appropriate for their team type? (Flawless is on a steep climb; Auto Allies is masked.) Revisit with [[synthesis/service-model-scoring]] if team-type weighting is adopted.
- **Is there a post-PI7.2 streak worth tracking** — e.g., once [[synthesis/pi7-plan]] systemic changes are adopted, does the portfolio see a broader sustained-Low era?

## Methodology

1. For each team slug, enumerate `wiki/summaries/audit-<slug>-*.md` in chronological order.
2. Extract Overall (ADO) or UPS (Git) score from each.
3. Count consecutive runs of audits with score ≥ 80.0 (Low Risk band per [[concepts/risk-bands]]).
4. Report: **longest run** (highest consecutive count anywhere in history), **current run** (consecutive from the most recent audit backward while still ≥80), **cumulative count** (total audits at ≥80).

Threshold is a hard 80.0; no smoothing applied. A single 79.9 breaks the streak.

**Rebuild cadence:** recompute after every audit ingest. A team's current run advances or resets on each new audit.

## Related

- [[synthesis/team-rankings]] — who's currently ranked where
- [[synthesis/portfolio-trend]] — multi-PI trajectory context
- [[synthesis/scoring-artifacts]] — the three events that broke most of the streaks
- [[concepts/risk-bands]] — why 80 is the Low threshold
- [[synthesis/iteration-7.1-close]] · [[synthesis/pi7-plan]] — retrospective + forward-look
