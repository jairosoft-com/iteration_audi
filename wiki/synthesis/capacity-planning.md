---
title: "Capacity Planning — Portfolio's Consistent Weak Spot"
type: synthesis
tags: [capacity, planning, portfolio, pi7, weakness]
sources:
  - "../entities/team-ado-shared.md"
  - "../entities/team-ado-hr.md"
  - "../entities/team-ado-jit.md"
  - "../entities/team-ado-admin.md"
  - "../entities/team-ado-fl-dev.md"
  - "../entities/person-grace.md"
  - "../summaries/audit-ado-hr-20260419-1345.md"
  - "../summaries/audit-ado-jit-20260419-1345.md"
  - "../summaries/audit-ado-shared-20260419-1947.md"
  - "../summaries/audit-ado-admin-20260419-1345.md"
  - "../summaries/audit-ado-fl-dev-20260419-1345.md"
  - "../summaries/portfolio-20260419-1953.md"
  - "../synthesis/iteration-7.1-close.md"
  - "../synthesis/portfolio-trend.md"
  - "../concepts/scoring-ado-rubric.md"
created: 2026-04-20
updated: 2026-04-20
---

# Capacity Planning — Portfolio's Consistent Weak Spot

Cross-cutting synthesis of the PI7.1-close capacity signals. Capacity is the one dimension where a clean delivery sprint still leaves a structural debt, because PI7.2 was being **committed while PI7.1 was still closing** — and the commitment math does not reconcile with the configured capacity. See [[synthesis/iteration-7.1-close]] for the cross-team retrospective this synthesis drills into.

## Headline

**Four of ten teams carried an unresolved capacity issue at PI7.1 close** — Shared Services (not configured at all), HR (30 SP committed vs 22 SP empirical capacity for 7.2), Admin (32 SP pipeline vs 27 SP ceiling), and Flawless (Team Capacity stuck at 66.7 for 8+ consecutive audits) ([[summaries/audit-ado-shared-20260419-1947]], [[summaries/audit-ado-hr-20260419-1345]], [[summaries/audit-ado-admin-20260419-1345]], [[summaries/audit-ado-fl-dev-20260419-1345]]). Killer fact: Shared Services scored a deterministic **Team Capacity 0.0** this iteration purely because the config step was skipped ([[entities/team-ado-shared]]).

## The pattern — three failure modes

### Mode 1 — Not configured (baseline)

[[entities/team-ado-shared]] scored **Team Capacity 0.0** on its first audit because team capacity was never wired for Iteration 7.1. This is deterministic, not analytic — a zero on a simple pre-planning step. The rubric can't distinguish "low capacity" from "unconfigured capacity," so the team takes a full −14 point hit on Overall without any underlying performance signal ([[summaries/audit-ado-shared-20260419-1947]], [[concepts/scoring-ado-rubric]]).

### Mode 2 — Overbooked at planning

[[entities/team-ado-hr]] committed **30 SP into PI7.2 against an empirical 22 SP capacity** (the same ceiling demonstrated by 22/22 SP delivered in 7.1) ([[summaries/audit-ado-hr-20260419-1345]]). [[entities/team-ado-admin]] built a **32 SP 7.2 pipeline against a 27 SP ceiling** ([[summaries/audit-ado-admin-20260419-1345]]). In both cases Team Capacity scored 100.0 for 7.1 because the *config* was correct; the *commitment* broke against it. The rubric's Team Capacity dimension measures configuration, not commitment-fit, so these overbooks are invisible to the score until delivery fails.

### Mode 3 — Structurally wrong mix

Configuration is correct but the underlying allocation does not support a realistic sprint commitment.

- **[[entities/team-ado-jit]]:** [[entities/person-grace]] is configured at **1 h/day Documentation** and owns 2 untouched sprint items (#201504, #201514, 16 days idle) ([[summaries/audit-ado-jit-20260419-1345]]). A 2-item Documentation commitment exceeds 14h per iteration — the 1h/day allocation was the blocker, not Grace's throughput ([[entities/person-grace]]).
- **[[entities/team-ado-admin]]:** [[entities/person-mark-colina]] is configured at **5 h/day** but absorbed 18 of 27 SP (67% of sprint load) in a single Apr 17 burst. The configured hours are a fiction; the actual 7.1 hours exceeded the 5h/day ceiling. Bus-factor-1 at 27 SP is not a capacity configuration — it is a resourcing fault dressed up as capacity ([[summaries/audit-ado-admin-20260419-1345]]).
- **[[entities/team-ado-fl-dev]]:** Team Capacity **66.7 for 8+ consecutive audits** because Carol Cuison is the assigned owner of #201569 but is not in the ADO capacity config — the team is delivering against a denominator that excludes a real contributor ([[summaries/audit-ado-fl-dev-20260419-1345]]).

## Team-by-team audit

| Team | Latest capacity issue | Dimension impact | Citation |
|------|------------------------|------------------:|----------|
| [[entities/team-ado-shared]] | Not configured for 7.1 | Team Capacity 0.0 → −14 to Overall | [[summaries/audit-ado-shared-20260419-1947]] |
| [[entities/team-ado-hr]] | 30 SP committed vs 22 SP empirical for 7.2 | Team Capacity 100.0 (config correct); commitment-vs-capacity mismatch invisible to rubric | [[summaries/audit-ado-hr-20260419-1345]] |
| [[entities/team-ado-admin]] | 32 SP pipeline vs 27 SP ceiling; 5h/day fiction vs Apr 17 18-SP burst | Team Capacity 100.0 but bus-factor-1 on 27 SP | [[summaries/audit-ado-admin-20260419-1345]] |
| [[entities/team-ado-fl-dev]] | Carol Cuison not in capacity config | Team Capacity 66.7 stuck across 8+ audits; adding Carol or closing #201569 = +~4.8 Overall | [[summaries/audit-ado-fl-dev-20260419-1345]] |
| [[entities/team-ado-jit]] | Grace 1h/day owning 2 sprint items | 16-day freeze on #201504/#201514 drives Delivery Predictability 0.0 | [[summaries/audit-ado-jit-20260419-1345]], [[entities/person-grace]] |

Five of 8 ADO teams show at least one capacity-related drag. The other three (Finance, Life Style, OTP) carry capacity at 100.0 without an overbook, confirming the issue is not universal — it is persistent on teams with service-model shape, bus-factor-1 resourcing, or late-sprint commitment pressure.

## Why this keeps happening

Inferred from the cross-team data, not conjecture:

1. **Capacity config is a pre-planning step easily skipped.** Shared Services' 0.0 is the archetype: the capacity step precedes sprint planning, has no "commit" button that forces it, and produces a deterministic zero on the rubric without a visible error on the board ([[entities/team-ado-shared]]).
2. **Commitment ≠ capacity check at planning close.** HR and Admin both ran clean 7.1 deliveries (22/22 SP and 27/27 SP), then committed 7.2 volumes above their own empirical ceiling — no automated gate flags a 30-vs-22 or 32-vs-27 mismatch before planning closes ([[summaries/audit-ado-hr-20260419-1345]], [[summaries/audit-ado-admin-20260419-1345]]).
3. **Bus-factor-1 hides behind configured capacity.** Admin's 5h/day is accurate as a configuration but fictional as a constraint when one person absorbs 18 SP in a day ([[summaries/audit-ado-admin-20260419-1345]]). HR's Almera is the same pattern at 22 SP ([[entities/team-ado-hr]]); OTP is Grace-only by accepted exception ([[synthesis/iteration-7.1-close]]).
4. **Service-model teams under-represent capacity.** [[synthesis/service-model-scoring]] argues Shared Services' 0.0 is partly rubric mismatch, but the "not configured" fact itself is real — a tier-aware rubric still needs the capacity config populated.
5. **Fractional allocations are not scrutinized.** Grace's 1h/day is a signal the team treats as capacity without checking that a 2-item sprint commitment is mathematically feasible against 14h total iteration time ([[entities/person-grace]], [[summaries/audit-ado-jit-20260419-1345]]).

## Proposed "Capacity Discipline" for PI7.2

Concrete, each tied to one of the failure modes above.

1. **Pre-planning capacity-config gate.** Before PI7.2 sprint planning opens for any team, verify ADO team capacity is populated (every active contributor with an hours/day allocation, days off subtracted). Targets: [[entities/team-ado-shared]] (Mode 1), [[entities/team-ado-fl-dev]] (add Carol Cuison).
2. **Commitment-vs-capacity guardrail at planning close.** Planning cannot close if `committed_SP > (team_capacity_hours × historical SP/hour)` without an explicit written override. Targets: HR (prune 30 → ≤22 SP), Admin (prune 32 → ≤24 SP) ([[summaries/audit-ado-hr-20260419-1345]], [[summaries/audit-ado-admin-20260419-1345]]).
3. **Quarterly review of 1h/day-style allocations.** Any contributor at ≤2h/day must either (a) be reassigned as a stakeholder (non-committer), or (b) carry at most 1 small item per iteration. Targets: [[entities/person-grace]] on JIT — reassign #201504/#201514 or drop JIT commitment to ≤1 item.
4. **Bus-factor-1 alert.** Any team where a single assignee owns ≥75% of committed SP triggers a retrospective entry on the forward risk. Targets: Admin (Mark Colina, 27 SP sole), HR (Almera, 22 SP sole), OTP (Grace-only, by exception), Life Style (Samantha 9 of 10 SP) ([[synthesis/iteration-7.1-close]]).
5. **Perfect-sprint carry-forward.** Teams that deliver 100% of commitment should not be penalized by a 7.2-pipeline overbook in the *same* Day-14 audit — instead surface the overbook as a planning-quality flag on the 7.2 pre-opening portfolio, decoupled from 7.1's Team Capacity score. Complements [[synthesis/scoring-artifacts]] § Proposed carve-outs.

## Dashboard additions

What [[summaries/portfolio-20260419-1953]] could surface explicitly:

- **Capacity-configured Y/N indicator** per team — a visible green/red dot that makes Mode 1 fail-fast rather than hiding inside a 0.0 on an averaged dimension.
- **Overbook ratio column** — `committed_SP / empirical_capacity_SP` for the *next* iteration; flag > 1.10 as Red, 1.00–1.10 as Yellow. Would have surfaced HR 1.36 and Admin 1.19 at 7.1 close.
- **Bus-factor flag column** — top-assignee share of committed SP; flag > 75% as Yellow and > 90% as Red. Would flag Admin, HR, OTP, and Life Style simultaneously.
- **Fractional-allocation watch list** — contributors at ≤2h/day with any open committed SP on the current iteration. Would surface Grace-on-JIT without needing a person page.

## Related

- [[synthesis/iteration-7.1-close]] — cross-team retrospective where capacity is named the portfolio's weakest spot
- [[synthesis/portfolio-trend]] — PI6 close → PI7.1 close context
- [[synthesis/service-model-scoring]] — tier-aware rubric proposal (Shared Services)
- [[synthesis/scoring-artifacts]] — close-day / rubric-transition carve-outs this synthesis dovetails with
- [[concepts/scoring-ado-rubric]] — 7-dimension rubric, Team Capacity definition
- [[entities/team-ado-shared]] · [[entities/team-ado-hr]] · [[entities/team-ado-jit]] · [[entities/team-ado-admin]] · [[entities/team-ado-fl-dev]]
- [[entities/person-grace]] · [[entities/person-mark-colina]]
