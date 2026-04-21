---
title: "Service-Model Scoring — Tier-Aware Rubric Proposal"
type: synthesis
tags: [scoring, rubric, service-model, shared-services]
sources:
  - "../entities/team-ado-shared.md"
  - "../summaries/audit-ado-shared-20260419-1947.md"
  - "../concepts/scoring-ado-rubric.md"
  - "../concepts/risk-bands.md"
  - "../summaries/portfolio-20260419-1953.md"
created: 2026-04-20
updated: 2026-04-20
---

# Service-Model Scoring — Tier-Aware Rubric Proposal

## Headline

The 7-dimension ADO rubric ([[concepts/scoring-ado-rubric]]) was designed for product-delivery teams and **over-penalizes service-model teams** whose output surfaces on consuming teams' boards. On Shared Services' baseline 32.2 ([[summaries/audit-ado-shared-20260419-1947]]), only ~10 points reflect real discipline gaps — the remaining **~22 points are rubric artifacts** from applying a product-team rubric to a cross-cutting services team.

## The case — Shared Services Iter 7.1 baseline

Overall **32.2 / 100 (Critical)** on Iteration 7.1 close ([[entities/team-ado-shared]]). Per-dimension decomposition:

| Dimension | Score | REAL / ARTIFACT | Notes |
|-----------|------:|-----------------|-------|
| Iteration Planning | 15.6 | MIXED | 5 committed-without-DoR items is **real**; denominator of 32 root-backlog items is **artifact** — services work is absorbed onto consuming teams' boards ([[summaries/audit-ado-shared-20260419-1947]]) |
| Team Capacity | 0.0 | REAL | Capacity simply not configured for Iter 7.1 — deterministic zero, fixable ([[entities/team-ado-shared]] §Real fixable issues) |
| Estimation | — | see raw | Per [[summaries/audit-ado-shared-20260419-1947]] |
| DoR Compliance | — | REAL (mostly) | 3 of 5 items in Grooming with no SP / Description / AC — genuine discipline gap |
| Work Item Balance | −70 penalty | ARTIFACT | 80% Enabler share is **structurally correct** for UIUX/IT/DevOps; penalty is a rubric misfit ([[summaries/audit-ado-shared-20260419-1947]]) |
| Backlog Refinement | 100 | — | Fine |
| Delivery Predictability | 0.0 | REAL | 0 SP closed of 3 SP committed on Day 14 — genuine delivery miss |

**Rough split:** ~10 points of the 32.2 trace to real issues (Team Capacity zero, DoR gaps, Delivery Predictability zero). The other ~22 points come from applying product-team scoring to structural service-model characteristics.

## Why a product-team rubric doesn't fit service teams

- **Output location mismatch.** Shared Services (UIUX / IT / DevOps) delivers onto *consuming* teams' boards — Flawless, OTP, Life Style, etc. Their own iteration board under-reports real delivery by design ([[entities/team-ado-shared]]).
- **Enabler-heavy mix is correct.** Platform / ops / infra work is natively Enabler. Penalizing low User Story share (Work Item Balance −70) punishes the service-model shape itself, not a discipline gap.
- **User Story isn't the primary work type.** The rubric's User-Story-centric denominator (e.g., Iteration Planning 5/32) treats absence of stories as incompleteness. For a services team, absence of stories is expected.
- **Baseline carve-out already exists.** [[concepts/risk-bands]] already flags first-time service-team audits as baselines not regressions — but the overall score is still calculated against the product rubric, so the carve-out is annotation-only.

## Tier-aware rubric proposal

### 1. Add `team_type` to each workspace CLAUDE.md

Values: `product | service | hybrid`. Initial assignment:

- `product` — `ado_fl_dev`, `ado_ls_dev`, `git_aa_dev`, `git_cc_dev`, `ado_fin`, `ado_hr`, `ado_admin`, `ado_jit`, `ado_otp` (verify OTP)
- `service` — `ado_shared`
- `hybrid` — candidates: `ado_fl_dev` / `ado_ls_dev` if they formally own platform work (see Open questions)

### 2. Reweight for `service` teams

| Dimension | Product rubric | Service rubric |
|-----------|----------------|----------------|
| Iteration Planning | items-on-iter / root-backlog | items-on-iter / **items actively in progress** (drop stale-root denominator) |
| Team Capacity | as-is | **as-is** — real discipline signal |
| Estimation | as-is | **as-is** — real discipline signal |
| DoR Compliance | as-is | **as-is** — real discipline signal |
| Work Item Balance | Feature/Story/Bug/Spike/Enabler mix | Mix **within Enabler subtypes** (Platform vs. Ops vs. UX); no User-Story-share penalty |
| Backlog Refinement | as-is | as-is |
| Delivery Predictability | as-is | **as-is** — real discipline signal |
| **NEW** Cross-Team Delivery | — | # consuming teams whose iteration cites this team's work this iter (requires cross-board query) |

### 3. Extend [[concepts/risk-bands]] with a service-tier floor

Proposed rule: a `service` team **cannot score Critical (<40) unless both Team Capacity AND Delivery Predictability are 0.0**. Otherwise floor the composite at 40.0 (High) and surface the structural vs. discipline breakdown on the team entity page.

## Estimated re-scoring

Applied retroactively to Shared Services Iter 7.1:

- Team Capacity 0.0 → unchanged (real)
- Delivery Predictability 0.0 → unchanged (real)
- DoR Compliance → unchanged
- Estimation → unchanged
- Iteration Planning 15.6 → **~60** (items-actively-in-progress denominator)
- Work Item Balance −70 → **~70–80** (Enabler-subtype mix score)
- Backlog Refinement 100 → unchanged
- Cross-Team Delivery (NEW) → **unscored at baseline** (requires cross-board audit)

Rough overall: **~55–60 (High/Moderate)** — still flags the real issues (capacity, DP, DoR) without Critical-on-structural-grounds. Matches Ramon's footnote framing ([[summaries/portfolio-20260419-1953]]) that 32.2 is a baseline, not a regression.

## Open design questions

1. **Hybrid teams.** Do Flawless / Life Style qualify as `hybrid` given their platform work, and what's the weighting between product and service dimensions? Default assumption: 70/30 product/service until team-level data says otherwise.
2. **Cross-Team Delivery automation.** Can this be pulled from ADO queries (`wit_search_workitem` for cross-iteration citations / linked work items pointing at Shared Services items)? Needs a spike.
3. **Grandfathering.** When `team_type` is added, does it backdate across audit history? Default: **no backdate** — historical scores stay on the product rubric; next audit is the first service-rubric score, clearly labeled.
4. **Score comparability across tiers.** Portfolio mean/median already spans ADO + Git (different rubrics). Adding a service tier widens the gap. Keep risk bands ([[concepts/risk-bands]]) as the cross-tier comparator; don't publish raw cross-tier score arithmetic as "portfolio health."

## Related

- [[entities/team-ado-shared]] — baseline team
- [[concepts/scoring-ado-rubric]] — current 7-dim rubric
- [[concepts/risk-bands]] — band thresholds + baseline carve-out
- [[summaries/audit-ado-shared-20260419-1947]] — source audit
- [[summaries/portfolio-20260419-1953]] — 10-team recomposition, Ramon's baseline footnote
- [[synthesis/portfolio-trend]] — recomposition shock (04-19 19:53) and § Open questions #2
