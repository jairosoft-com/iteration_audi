---
title: "Bus Factor — Single-Point-of-Failure Catalog"
type: synthesis
tags: [bus-factor, risk, concentration, people, portfolio]
sources:
  - "../entities/person-mark-colina.md"
  - "../entities/person-armelita.md"
  - "../entities/person-grace.md"
  - "../entities/person-jerlyn.md"
  - "../entities/team-ado-admin.md"
  - "../entities/team-ado-jit.md"
  - "../entities/team-ado-hr.md"
  - "../entities/team-ado-fin.md"
  - "../entities/team-ado-otp.md"
  - "../entities/team-ado-ls-dev.md"
  - "../entities/team-ado-fl-dev.md"
  - "../entities/team-git-aa-dev.md"
  - "../entities/team-git-cc-dev.md"
  - "../synthesis/capacity-planning.md"
  - "../synthesis/top-compliance-issues.md"
  - "../synthesis/iteration-7.1-close.md"
  - "../concepts/scoring-ado-rubric.md"
created: 2026-04-20
updated: 2026-04-20
---

# Bus Factor — Single-Point-of-Failure Catalog

## Headline

**At PI7.1 close, seven of ten portfolio teams carry a bus-factor-1 or near-1 dependency** on a single delivery contributor or single reviewer. The most severe delivery case is [[entities/team-ado-jit]] ([[entities/person-armelita]] routinely 70–80%+ of SP across 30+ audits); the most recently flagged is [[entities/team-ado-admin]] ([[entities/person-mark-colina]], 27 SP sole assignee with an 18-SP single-day burst on 2026-04-17) ([[summaries/audit-ado-admin-20260417-0900]], [[summaries/audit-ado-jit-20260408-0900]]).

## Definition

"Bus factor 1" in this portfolio means **a team where if a single named individual is unavailable for a sprint, delivery halts or drops >50%.** The signature shows up in the [[concepts/scoring-ado-rubric|7-dimension ADO rubric]] indirectly: Work Item Balance reads the work-type monoculture, Team Capacity reads the configuration but not the concentration, and Delivery Predictability only flags the consequence after the person has already missed. None of the seven dimensions measure concentration directly — it has to be read off assignee shares of committed SP. See [[synthesis/capacity-planning]] § "wrong mix" for how the same failure mode surfaces on the capacity side.

## The catalog

| Team | Individual | Role | SP concentration | Risk signals | Citation |
|------|------------|------|-----------------:|--------------|----------|
| [[entities/team-ado-admin]] | [[entities/person-mark-colina]] | Sole contributor | **100% · 27 of 27 SP** | 18-SP single-day burst Apr 17; Overall 87.0 masks structural fragility | [[summaries/audit-ado-admin-20260419-1345]] |
| [[entities/team-ado-jit]] | [[entities/person-armelita]] | PM + PO + IC | **~77% avg · 20–31 of 28–36 SP** | PM+PO triple-hat; 76% (Feb 26) → 80.6% (Apr 8) concentration arc | [[summaries/audit-ado-jit-20260226-0800]], [[summaries/audit-ado-jit-20260407-0900]], [[summaries/audit-ado-jit-20260408-0900]] |
| [[entities/team-ado-hr]] | Almera Kleer Tayao | Sole contributor | **100% · 22 SP committed + 30 SP in 7.2 pipeline** | Persistent across 33 audits; 16-SP single-day burst Apr 18 | [[entities/team-ado-hr]] |
| [[entities/team-ado-fin]] | [[entities/person-grace]] | Sole contributor | **100% · 12 of 14 SP** | Accepted single-operator model; #201448 eAFS filing lagged unresolved | [[entities/team-ado-fin]] |
| [[entities/team-ado-otp]] | [[entities/person-grace]] | Sole assignee | **100%** | Single-assignee model accepted as project exception | [[entities/team-ado-otp]] |
| [[entities/team-ado-ls-dev]] | Samantha Babael | Primary dev | **~90% · 9 of 10 SP, 6 of 7 items** | Small squad — Ike Yana / Luzmibel carry near-zero delivery share | [[entities/team-ado-ls-dev]] |
| [[entities/team-ado-fl-dev]] | Carol Cuison | Spike owner | **100% of open 7.1 scope (#201569)** | Not in ADO capacity config → Team Capacity stuck 66.7 for 8+ audits | [[entities/team-ado-fl-dev]] |
| [[entities/team-git-cc-dev]] | Paul Coronia | Lead dev | **18 of ~30 PRs (~60%)** | Delivery-side co-dominance; review-side below | [[entities/team-git-cc-dev]] |
| [[entities/team-git-cc-dev]] | `raseniero` (Ramon) | Sole approver | **Requested reviewer on all 3 active open PRs** including BE#55 HIPAA | Review bottleneck — 2-day unreviewed on 42-file HIPAA PR | [[summaries/audit-git-cc-dev-20260419-1345]] |
| [[entities/team-git-aa-dev]] | Joseph / Cliff / Earl | Delivery trio | **3 of 5 produce 100% of GitHub output** | Inverse case — [[entities/person-jerlyn]] and Mary Secusana at zero-contribution does not halt delivery but invalidates capacity math | [[entities/team-git-aa-dev]] |

Teams without a bus-factor-1 signal: [[entities/team-ado-shared]] (baseline unconfigured; roster not yet captured).

## Two kinds of bus factor

- **Delivery bus factor** — one person does the work. Archetype: [[entities/person-mark-colina]] on Admin, [[entities/person-armelita]] on JIT, Almera on HR, Samantha on LS Dev. Score the risk against **committed SP concentration**.
- **Review bus factor** — one person approves the work. Archetype: `raseniero` on all open CC Dev PRs, including the 42-file HIPAA PR BE#55 sitting 2 days unreviewed ([[summaries/audit-git-cc-dev-20260419-1345]]). Score the risk against **distinct reviewer count across a PI's merged PRs**.

Both stall a sprint; they belong on the same dashboard but under different columns.

## Risk scoring

Proposed 0–3 per team, applied to PI7.1-close state:

| Team | Delivery score | Review score | Notes |
|------|---------------:|-------------:|-------|
| [[entities/team-ado-admin]] | **3** | n/a | 100% single contributor |
| [[entities/team-ado-jit]] | **3** | n/a | 70–80%+ concentration + PM/PO/IC triple-hat |
| [[entities/team-ado-hr]] | **3** | n/a | 100% single contributor, 33-audit streak |
| [[entities/team-ado-fin]] | **3** | n/a | Accepted single-operator |
| [[entities/team-ado-otp]] | **3** | n/a | Accepted single-operator exception |
| [[entities/team-ado-ls-dev]] | **2** | n/a | Samantha ~90% but two nominal backups on roster |
| [[entities/team-ado-fl-dev]] | **2** | n/a | Sole open item to out-of-config assignee |
| [[entities/team-git-cc-dev]] | 1 | **3** | Delivery shared pcoronia/Kyaa-A; reviews all flow to `raseniero` |
| [[entities/team-git-aa-dev]] | 1 | 1 | Delivery trio absorbs; zero formal PR reviews (separate issue) |
| [[entities/team-ado-shared]] | — | — | Roster not yet captured |

Score 3 = delivery OR review halts without one named person. Seven of ten teams score 3 on at least one axis; four of those are accepted single-operator functions (Fin, OTP, plus HR and Admin which are structurally single-operator but not formally documented as exceptions).

**Concentration trajectory on JIT** (from the Armelita audit chain — showing the signal is stable, not noise):

| Audit date | Armelita share | Citation |
|------------|---------------:|----------|
| 2026-02-26 | 76% (20 of ~28 SP) | [[summaries/audit-ado-jit-20260226-0800]] |
| 2026-03-03 | 56% of remaining open (19 of 34 SP) | [[summaries/audit-ado-jit-20260303-0700]] |
| 2026-04-07 | 77.5% (31 SP) | [[summaries/audit-ado-jit-20260407-0900]] |
| 2026-04-08 | 80.6% (29 of 36 SP) | [[summaries/audit-ado-jit-20260408-0900]] |
| 2026-04-09 | 72.5% (14 items / 29 SP) | [[summaries/audit-ado-jit-20260409-0900]] |

Six-week mean ≈ 72% — well above the 40% proposed flag threshold and equal-to-or-above the 60% dominant-type threshold every single sprint.

## Why existing rubric doesn't catch this

The [[concepts/scoring-ado-rubric|7-dimension rubric]] measures **consequences** (Work Item Balance, Delivery Predictability, Backlog Refinement) rather than **cause** (concentration). A team can score Low Risk while being bus-factor-1: [[entities/team-ado-admin]]'s **Overall 87.0** at close is the canonical proof — clean 27/27 SP, 100% DoR, 100% Team Capacity, yet Mark is the only person who could deliver it ([[summaries/audit-ado-admin-20260419-1345]]). [[entities/team-ado-fin]] hits **93.7** on the same structural pattern ([[entities/team-ado-fin]]). [[synthesis/top-compliance-issues]] ranks bus factor 1 as issue #4 (49 mentions) precisely because the signal lives in narrative text, not in any score dimension.

## Proposed guardrail

Three additions to the audit + portfolio dashboard:

1. **Per-team concentration flag at planning.** Any assignee owning ≥40% of committed iteration SP triggers a `concentration` flag in the audit. The audit's Open Questions section must include an explicit acknowledgment + one-sentence backup plan ("If Mark is unavailable, #202357 falls to …"). Threshold calibrated from [[synthesis/capacity-planning]] § Dashboard additions which proposed 75%/90%; 40% captures earlier-stage concentration trajectories too (catches JIT's 76% in Feb and Admin's 100% equally).
2. **Per-repo review-bus-factor flag.** Any repo with **<2 distinct reviewers with approval evidence across a PI's merged PRs** triggers a `review-bus-factor` flag. [[entities/team-git-cc-dev]] currently trips this with `raseniero` as the sole requested reviewer on all 3 active open PRs.
3. **Dashboard widget: "Top 5 bus-factor risks at PI open."** Track whether each risk persists sprint-to-sprint; expected natural decay is zero without intervention (see [[entities/team-ado-hr]]'s 33-audit unbroken streak).

## Mitigation options (by severity)

- **Pair-assignment.** Explicitly share ownership of key items. Cheapest move for [[entities/team-ado-admin]] — any single Admin item with a named secondary approver drops delivery-bus-factor from 3 → 2. No hiring required.
- **Cross-training.** [[entities/team-ado-jit]]: Teofilo carries 6h/day configured but regularly idle ([[summaries/audit-ado-jit-20260325-0849]] "Teofilo has capacity but zero items"); explicit cross-training lets him absorb 2 items per iteration off Armelita. [[entities/team-git-cc-dev]]: add a backup reviewer (e.g., Bomar or Paul) to unblock HIPAA PRs when `raseniero` is absent.
- **Role separation.** [[entities/person-armelita]]'s PM+PO+IC triple-hat is the textbook SAFe anti-pattern — she grooms, accepts, and delivers her own stories. Even informal separation (another person accepting her stories) resolves the conflict-of-interest without headcount.
- **Hire / team-grow.** [[entities/team-ado-admin]] (Mark-only), [[entities/team-ado-hr]] (Almera-only), [[entities/team-ado-fin]] (Grace-only) are structural bus-factor-1 that no coaching move resolves. These need a hiring decision or formal acceptance as operating risk.

## Related

- [[synthesis/capacity-planning]] — "wrong mix" failure mode; concentration hides inside configured capacity
- [[synthesis/top-compliance-issues]] — rank #4, 49 mentions
- [[synthesis/iteration-7.1-close]] — retro identified bus-factor-1 on Admin, HR, OTP, Life Style simultaneously
- [[synthesis/pi7-plan]] — capacity-discipline gate partially addresses bus factor
- [[concepts/scoring-ado-rubric]] · [[concepts/risk-bands]] · [[concepts/stakeholder-roles]]
- [[entities/person-mark-colina]] · [[entities/person-armelita]] · [[entities/person-grace]] · [[entities/person-jerlyn]]

## Open questions

- **Is bus-factor-1 actually tolerable** on Admin, Fin, OTP, HR given the headcount constraint? If yes, the portfolio should formally accept it (as OTP already does) and decouple it from the rubric rather than re-flagging every audit.
- **Does the 40% threshold catch too many teams?** On PI7.1 close data, 7 of 10 teams flag. A 60% threshold (matching the dominant-type rubric) catches JIT, Admin, HR, Fin, OTP, LS Dev — still 6 of 10.
- **Is review bus factor primarily a `raseniero` bandwidth issue** rather than a team-structure issue? If so, the mitigation is a review rotation, not team-level change.
