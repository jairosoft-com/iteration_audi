---
title: "Iteration 7.1 Close — Cross-Team Retrospective"
type: synthesis
tags: [iteration-7.1, retrospective, portfolio, close, safe]
sources:
  - "../summaries/portfolio-20260419-1953.md"
  - "../summaries/portfolio-20260419-1345.md"
  - "../summaries/audit-ado-admin-20260419-1345.md"
  - "../summaries/audit-ado-fin-20260419-1345.md"
  - "../summaries/audit-ado-fl-dev-20260419-1345.md"
  - "../summaries/audit-ado-hr-20260419-1345.md"
  - "../summaries/audit-ado-jit-20260419-1345.md"
  - "../summaries/audit-ado-ls-dev-20260419-1345.md"
  - "../summaries/audit-ado-otp-20260419-1345.md"
  - "../summaries/audit-ado-shared-20260419-1947.md"
  - "../summaries/audit-git-aa-dev-20260419-1345.md"
  - "../summaries/audit-git-cc-dev-20260419-1345.md"
created: 2026-04-20
updated: 2026-04-20
---

# Iteration 7.1 Close — Cross-Team Retrospective

Cross-team retrospective for PI7 Iteration 7.1 (2026-04-06 → 2026-04-19), built from 10 Day-14 audit summaries plus the 13:45 (9-team) and 19:53 (10-team) portfolio snapshots. Scope: what the iteration proved, what it didn't, what to ask of each team before PI7.2 kickoff.

## Headline

- **Portfolio mean 76.1 / median 80.9** at 10-team close ([[summaries/portfolio-20260419-1953]]); mean 81.0 / median 82.4 at the 9-team pre-recomposition peak ([[summaries/portfolio-20260419-1345]]).
- **Distribution (10-team):** 5 Low · 4 Moderate · 0 High · 1 Critical. First full PI7.1 cycle with **zero High Risk** ([[summaries/portfolio-20260419-1345]], [[synthesis/portfolio-trend]]).
- **Iteration arc:** mean 62.0 on PI7 Day 1 (04-06) → 81.0 on Day 14 9-team peak — +19.0 points, the cleanest monotonic climb of PI6 or PI7 in the dataset ([[synthesis/portfolio-trend]]).
- Two standout conclusions: (1) PI7.1 delivered the first zero-Critical, zero-High sprint in the window and sustained it for six consecutive captures (04-13 → 04-19 13:45) ([[synthesis/portfolio-trend]]); (2) **median held** under Shared Services recomposition (82.4 → 80.9) — mean-based portfolio health is brittle at 10 teams; the median is the better headline metric ([[summaries/portfolio-20260419-1953]]).

## Scoreboard

| Team | Overall / UPS | Band | Δ vs prior audit | Descriptor |
|------|--------------:|------|:-----------------|:-----------|
| [[entities/team-ado-fin]] Finance | 93.7 | 🟢 Low | ±0 vs Day 12 ([[summaries/audit-ado-fin-20260419-1345]]) | Steady |
| [[entities/team-git-cc-dev]] Colina Health | 90.6 | 🟢 Low | +0.3 vs Day 12 ([[summaries/audit-git-cc-dev-20260419-1345]]) | Clean |
| [[entities/team-ado-admin]] Administration | 87.0 | 🟢 Low | −1.6 vs Day 12 (88.6) ([[summaries/audit-ado-admin-20260419-1345]]) | Flawless |
| [[entities/team-ado-hr]] HR Recruitment | 87.0 | 🟢 Low | +8.6 vs Day 12 (78.4) ([[summaries/audit-ado-hr-20260419-1345]]) | Promoted |
| [[entities/team-ado-ls-dev]] Life Style | 82.4 | 🟢 Low | +5.3 vs A23 real reading (77.1) ([[summaries/audit-ado-ls-dev-20260419-1345]]) | Recovered |
| [[entities/team-ado-fl-dev]] Flawless | 79.3 | 🟡 Moderate | +10.5 vs Day 12 (68.8) ([[summaries/audit-ado-fl-dev-20260419-1345]]) | Groomed |
| [[entities/team-ado-otp]] OTP | 71.2 | 🟡 Moderate | ±0 vs A30 ([[summaries/audit-ado-otp-20260419-1345]]) | Stalled |
| [[entities/team-ado-jit]] JIT | 68.8 | 🟡 Moderate | −9.6 vs Day 12 (78.4) ([[summaries/audit-ado-jit-20260419-1345]]) | Slumped |
| [[entities/team-git-aa-dev]] Auto Allies | 68.6 | 🟡 Moderate | UPS masks SGPI 21.2 ([[summaries/audit-git-aa-dev-20260419-1345]]) | Masked |
| [[entities/team-ado-shared]] Shared Services | 32.2 | 🔴 Critical | Baseline ([[summaries/audit-ado-shared-20260419-1947]]) | Baseline |

## What worked

- **Zero High Risk for the first time in the dataset** from 04-13 onward ([[synthesis/portfolio-trend]]); the one Critical at close is Shared Services' baseline, not a regression ([[summaries/audit-ado-shared-20260419-1947]]).
- **Four band upgrades across the iteration:** HR Moderate → Low (+8.6), Flawless carried Moderate but +10.5, Colina sustained Low, Life Style recovered Low after A24 artifact ([[synthesis/portfolio-trend]], [[summaries/portfolio-20260419-1345]]).
- **Median 80.9 (Low) at 10-team close** ([[summaries/portfolio-20260419-1953]]) — the portfolio is meaningfully healthier than any prior snapshot in this window ([[synthesis/portfolio-trend]]).
- **Colina Health 90.6 UPS with 21/21 SP delivered** and HCI +1 to 74 on a merged Sprint-Discipline spike — cleanest trajectory of any team this PI ([[summaries/audit-git-cc-dev-20260419-1345]]).
- **HR band upgrade Moderate → Low** (78.4 → 87.0) driven by Delivery Predictability 21.4 → 100.0 after 22/22 SP delivery ([[summaries/audit-ado-hr-20260419-1345]]).
- **Flawless Wedding App +10.5** on a genuine backlog refresh — Backlog Refinement 26.9 → 100.0 across 164 items ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **Administration 100% delivery** (27/27 SP across 11 User Stories, zero state regressions) with zero stale items at any threshold ([[summaries/audit-ado-admin-20260419-1345]]).
- **Finance DoR 100% across 5 sprint items** and 85.7% delivery — only the eAFS filing is open ([[summaries/audit-ado-fin-20260419-1345]]).
- **Colina 100% traceability** — 11/11 committed defects have `AB#` links across 28 merged iteration PRs ([[summaries/audit-git-cc-dev-20260419-1345]]).
- **Backlog Refinement at 100 for five of 10 teams** (Admin, HR, Finance, OTP, Flawless) — concentrated hygiene work during the iteration paid off in the closing audit.

## What didn't

- **Capacity planning misses** are the most common cross-team gap. HR committed 30 SP against 22 SP empirical capacity for 7.2 ([[summaries/audit-ado-hr-20260419-1345]]); Admin 7.2 pipeline 32 SP vs 27 SP ceiling ([[summaries/audit-ado-admin-20260419-1345]]); Shared Services capacity not configured at all, producing deterministic 0.0 ([[summaries/audit-ado-shared-20260419-1947]]); Flawless Team Capacity stuck at 66.7 for 8+ audits because Carol Cuison isn't in the config ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **DoR leakage at sprint edges.** Admin's #202894 created Day-14 with a typo'd title, no SP, no Description, no AC ([[summaries/audit-ado-admin-20260419-1345]]); Shared Services committed 3 of 5 items in Grooming state ([[summaries/audit-ado-shared-20260419-1947]]); Flawless closed #202381 and #202150 without remediation ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **Delivery Predictability collapses on close-day boards.** JIT fell 67.4 → 0.0 on a strict visible-state read (0 of 14 SP closed on 6 remaining items) ([[summaries/audit-ado-jit-20260419-1345]]); OTP held 0.0 with no board movement for 35 hours ([[summaries/audit-ado-otp-20260419-1345]]); Shared Services 0 SP closed of 3 committed ([[summaries/audit-ado-shared-20260419-1947]]).
- **Stale work items** persist across cycles: Life Style #187240 Enabler at 244 days stale drives Backlog Refinement 18.3 ([[summaries/audit-ado-ls-dev-20260419-1345]]); JIT's Grace items #201504 / #201514 untouched 16 days drive a −20 penalty ([[summaries/audit-ado-jit-20260419-1345]]); Colina's AI Agent PR#9 stale 56 days ([[summaries/audit-git-cc-dev-20260419-1345]]).
- **UPS composite masking** at Auto Allies — UPS 68.6 Moderate hides HCI 49 (Critical) and SGPI 21.2% (Red); 14 SP parked in QA Testing at sprint end; zero formal PR reviews on ~48 merged PRs; third consecutive Red-SGPI sprint ([[summaries/audit-git-aa-dev-20260419-1345]], [[synthesis/ups-masking-pattern]]).
- **Audit-internal inconsistency.** Auto Allies audit headline/scorecard cites HCI 49 while Section 9 breakdown computes 48 with Sprint Discipline −1 — same document, two numbers ([[summaries/audit-git-aa-dev-20260419-1345]]).
- **Regulatory commitments missing from ADO.** Finance #201448 (BIR eAFS, 2 SP) inactive 9 days across the Apr 15 filing deadline with no confirmation in ADO ([[summaries/audit-ado-fin-20260419-1345]]); Colina HIPAA PR BE#55 (42 files) unreviewed at close ([[summaries/audit-git-cc-dev-20260419-1345]]).
- **Work Item Balance stuck at 70** on four teams (Admin, Finance, HR, OTP, JIT) — a recurring −30 dominant-type penalty that planning ceremonies have not addressed. OTP is the only team with a documented exception; the others are silent acceptance.
- **State-hygiene lag.** Finance #199347 (Finance Presentation, 5 SP) delivered mid-March but only marked Closed on Apr 17, ~5 weeks late ([[summaries/audit-ado-fin-20260419-1345]]); Auto Allies #201173 Revenue Cat unblocked Day 14 with no merged code ([[summaries/audit-git-aa-dev-20260419-1345]]).

## Team spotlight — winners

- **[[entities/team-ado-fin]] Finance (93.7)** — highest score in the portfolio; 4 of 5 sprint items Closed with 100% DoR pass; only miss is the BIR eAFS item. Apr 17 10-SP burst closure shows the team can clear a long tail fast ([[summaries/audit-ado-fin-20260419-1345]]).
- **[[entities/team-git-cc-dev]] Colina Health (90.6)** — cleanest trajectory in the dataset; UPS held 90+ for the first time since PI7 open; HCI +1 to 74 after Sprint Discipline spike merged; first Claude-Code-assisted PR (BE#55) in team history ([[summaries/audit-git-cc-dev-20260419-1345]], [[synthesis/portfolio-trend]]).
- **[[entities/team-ado-hr]] HR (87.0)** — Apr 18 90-minute burst closed 8 items / 16 SP to deliver 22/22 SP on remaining commitment; Delivery Predictability +78.6 drove the band upgrade ([[summaries/audit-ado-hr-20260419-1345]]).
- **[[entities/team-ado-admin]] Admin (87.0)** — 100% delivery, zero stale items at any threshold, strongest backlog hygiene of all ADO teams this cycle; 1.6-point drop is purely the Day-14 denominator expansion from six new 7.2 items ([[summaries/audit-ado-admin-20260419-1345]]).
- **[[entities/team-ado-ls-dev]] Life Style (82.4)** — recovered cleanly from the A24 close-day formula artifact (11.2 Critical) to a real +5.3 gain vs A23; 7/7 items Closed, 10/10 SP delivered ([[summaries/audit-ado-ls-dev-20260419-1345]]).

## Team spotlight — at-risk

- **[[entities/team-ado-shared]] Shared Services (32.2 baseline)** — the sole Critical at close, but structurally: capacity not configured, 3 Grooming items committed without DoR, −70 Work Item Balance penalty for an Enabler-dominant services mix, 5 of 32 visible items on the current iteration. Requires [[synthesis/service-model-scoring]] tier-aware treatment before scoring against product-team rubric ([[summaries/audit-ado-shared-20260419-1947]]).
- **[[entities/team-git-aa-dev]] Auto Allies (UPS 68.6)** — headline Moderate hides Critical components (HCI 49 / SGPI 21.2%). Healthy code delivery (63.6% proxy SGPI) failing at the QA gate: 14 SP parked in QA Testing at close; two zero-contribution team members for the full 14-day sprint (Jerlyn Ates QA, Mary Secusana Documentation); zero formal PR reviews on ~48 merged PRs ([[summaries/audit-git-aa-dev-20260419-1345]], [[synthesis/ups-masking-pattern]]).
- **[[entities/team-ado-jit]] JIT (68.8, Delivery Predictability 0.0)** — no closures between Apr 17 evening and Apr 19 13:45; Grace's #201504 / #201514 untouched since Apr 3 (16 days). Close-all scenario modeled at Overall 83.1 (Low) — single action could swing the band ([[summaries/audit-ado-jit-20260419-1345]]).
- **[[entities/team-ado-otp]] OTP (71.2, stationary from A30)** — 35 hours of zero board movement; #198587 (3 SP JIT Signage) still Active; #202229 stalled 9 days on Akira dependency. Single closure of #198587 modeled at Overall ~79.8 (near Low) ([[summaries/audit-ado-otp-20260419-1345]]).
- **[[entities/team-ado-fl-dev]] Flawless (79.3, almost Low)** — genuine backlog refresh worked but Iteration Planning 6.7 Critical and Team Capacity 66.7 are both structural rubric artifacts (Carol Cuison not in config; 50+ PI8 items visible). Closing #201569 today would push Overall to ~84.1 ([[summaries/audit-ado-fl-dev-20260419-1345]]).

## Themes

1. **Capacity planning is the portfolio's weakest spot.** Four teams over-committed or under-configured capacity for 7.2 (HR 30 vs 22, Admin 32 vs 27, Flawless 66.7 stuck, Shared Services 0.0). Pattern cuts across ADO tiers — the rubric surfaces it consistently, but the planning ceremony doesn't absorb the feedback.
2. **DoR leakage at sprint edges, not sprint middles.** The items created or closed on Day 14 carry the DoR failures (Admin #202894, Flawless #202381/#202150, Shared Services 3 Grooming items). Mid-sprint DoR held at 100% across most teams. Enforcement belongs at board-entry and closure-review, not at daily standup.
3. **Day-14 close-day formula artifacts remain unreconciled.** JIT Delivery Predictability 0.0, OTP Delivery Predictability 0.0, Admin Iteration Planning 39.3, HR Iteration Planning 39.3, OTP Iteration Planning 28.6, Life Style A24 (11.2 artifact) all share the same root: the rubric reads a board view that has already shed closed items or absorbed 7.2 candidates. Formalize a close-day carve-out — see [[synthesis/scoring-artifacts]] for the same pattern at 04-01 (HR) and 04-17 (Life Style, Auto Allies).
4. **Compliance deadlines live outside ADO.** Finance eAFS Apr 15 (BIR filing) and Colina HIPAA PR BE#55 are both critical-path regulatory items whose status isn't reflected on the ADO board. Portfolio-level risk surfaces from this gap more than from any scoring issue.
5. **Bus-factor-1 risk on top-scoring teams.** HR's Almera sole-contributed all 22 SP delivered and all 30 SP in 7.2 pipeline ([[summaries/portfolio-20260419-1345]]); OTP is Grace-only by accepted exception ([[summaries/audit-ado-otp-20260419-1345]]); Life Style's Samantha Babael delivered 6 of 7 items (9 of 10 SP) ([[summaries/audit-ado-ls-dev-20260419-1345]]); Admin's Apr 17 18-SP single-day burst raises the same sustainability question ([[summaries/audit-ado-admin-20260419-1345]]). Headline scores are healthy; resourcing is fragile.
6. **Burst-closure cadence is the portfolio's dominant delivery mode.** Four separate teams show Day-12–18 clustered closures: Admin 18 SP on Apr 17, HR 16 SP in 90 minutes on Apr 18, Finance 10 SP in 1 minute on Apr 17, Auto Allies near-zero SGPI movement in final 48 hours. The rubric rewards the outcome but the pattern is indistinguishable from over-commitment absorbed by end-of-sprint heroics.

## Forward asks for PI7.2

- **[[entities/team-ado-hr]] HR:** rebalance 7.2 commitment from 30 SP to ≤22 SP empirical capacity; triage #202888 "APE — Caumban — Copy" as duplicate-risk before kickoff ([[summaries/audit-ado-hr-20260419-1345]]).
- **[[entities/team-ado-admin]] Admin:** prune 7.2 pipeline from 32 SP to ≤24 SP; groom #202894 (title/SP/Desc/AC) before sprint start; document PI7-root legacy home for the 8 unassigned items ([[summaries/audit-ado-admin-20260419-1345]]).
- **[[entities/team-ado-jit]] JIT:** unblock Grace's #201504 / #201514 or reassign; re-path PI6 leakage (#200766, #202514–202517) out of the 7.2 denominator ([[summaries/audit-ado-jit-20260419-1345]]).
- **[[entities/team-ado-otp]] OTP:** close #198587 before retrospective (moves band Moderate → near-Low); formally re-path #202229 to 7.2 with status comment; add an Enabler to the solar-install chain to lift Work Item Balance 70 → 100 ([[summaries/audit-ado-otp-20260419-1345]]).
- **[[entities/team-git-cc-dev]] Colina:** review HIPAA PR BE#55 (202696, 42 files) before 7.2 code freeze; enable branch-protection on `main`; triage 11 new project-level defects (202269 … 202483) against 7.2 capacity ([[summaries/audit-git-cc-dev-20260419-1345]]).
- **[[entities/team-git-aa-dev]] Auto Allies:** surface component Criticals in dashboards per [[synthesis/ups-masking-pattern]]; break the QA-gate bottleneck (14 SP parked, third Red-SGPI sprint); activate retro spikes #202168 / #202169; reinstate Jerlyn Ates and Mary Secusana ([[summaries/audit-git-aa-dev-20260419-1345]]).
- **[[entities/team-ado-shared]] Shared Services:** wire team capacity config before 7.2 Day 1; move stories to User Story type where possible to exit −70 Work Item Balance penalty; groom the 3 committed items out of Grooming before kickoff; propose tier-aware rubric adjustment per [[synthesis/service-model-scoring]] ([[summaries/audit-ado-shared-20260419-1947]]).
- **[[entities/team-ado-fin]] Finance:** reconcile #201448 (BIR eAFS) status in ADO before 7.2 planning — record Transaction Number or re-path; right-size 7.2 commitment to 12 SP empirical with 1 SP Spike buffer ([[summaries/audit-ado-fin-20260419-1345]]).
- **[[entities/team-ado-fl-dev]] Flawless:** add Carol Cuison to ADO capacity config before 7.2 kickoff; close #201569 Netlify/GitHub Transfer Spike today for a ~+4.8 Overall lift; hide PI8 items from default backlog view ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **[[entities/team-ado-ls-dev]] Life Style:** archive #187240 Enabler (244d stale) plus 3 of 4 PI5 stragglers — lifts Backlog Refinement 18.3 → ~98 (+~11 Overall); right-size 7.2 commitment to 8–10 SP; schedule Luzmibel Paculanang onto a testing assignment ([[summaries/audit-ado-ls-dev-20260419-1345]]).

## Related

- [[synthesis/portfolio-trend]] — timeline context (PI6 close → PI7.1 close)
- [[synthesis/ups-masking-pattern]] — Auto Allies composite-vs-component pattern
- [[synthesis/scoring-artifacts]] — close-day / rubric-transition exceptions
- [[synthesis/service-model-scoring]] — Shared Services tier-aware scoring
- [[concepts/scoring-ado-rubric]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]
