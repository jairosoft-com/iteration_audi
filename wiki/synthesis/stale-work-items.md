---
title: "Stale Work Items — Chronic Backlog Debt"
type: synthesis
tags: [stale, backlog, debt, refinement, portfolio]
sources:
  - "../entities/team-ado-ls-dev.md"
  - "../entities/team-ado-jit.md"
  - "../entities/team-ado-fl-dev.md"
  - "../entities/team-ado-admin.md"
  - "../summaries/backlog-analysis-ado-admin-20260505.md"
  - "../entities/person-grace.md"
  - "../summaries/audit-ado-ls-dev-20260419-1345.md"
  - "../summaries/audit-ado-ls-dev-20260417-0900.md"
  - "../summaries/audit-ado-ls-dev-20260407-0900.md"
  - "../summaries/audit-ado-ls-dev-20260404-0900.md"
  - "../summaries/audit-ado-jit-20260419-1345.md"
  - "../summaries/audit-ado-jit-20260325-0849.md"
  - "../summaries/audit-ado-fl-dev-20260419-1345.md"
  - "../summaries/audit-ado-fl-dev-20260412-0900.md"
  - "../summaries/audit-ado-fl-dev-20260416-0900.md"
  - "../summaries/audit-ado-admin-20260419-1345.md"
  - "../summaries/audit-ado-otp-20260419-1345.md"
  - "../summaries/portfolio-20260406-0900.md"
  - "../summaries/portfolio-20260401-0900.md"
  - "../concepts/scoring-ado-rubric.md"
  - "../synthesis/dor-leakage.md"
  - "../synthesis/capacity-planning.md"
created: 2026-04-20
updated: 2026-05-05
---

# Stale Work Items — Chronic Backlog Debt

Cross-cutting synthesis of the work items that age in the backlog across audits, never closing and never advancing. Distinct from [[synthesis/dor-leakage]] (items commit without readiness) and [[synthesis/capacity-planning]] (items don't fit the owner) — these items simply **sit**, and each audit they sit costs a team rubric points.

## Headline

**At least 6 chronic stale items across 4 ADO teams are actively penalizing PI7.1 Backlog Refinement scores.** The worst offender — [[entities/team-ado-ls-dev]] **#187240 "Evaluate Deployment and Distribution Options"** Enabler — has been unchanged since **2025-08-18 (244 days stale)** and has triggered a `stale_180` −20 penalty on **9 consecutive audits** ([[summaries/audit-ado-ls-dev-20260419-1345]], [[entities/team-ado-ls-dev]]). That single item alone drags Life Style Help App's Backlog Refinement dimension from ~98 to **18.3 (Critical)** every audit ([[summaries/audit-ado-ls-dev-20260419-1345]]).

## The list

| Work Item | Team | Age (days) | Type | Status | Owner | Citation |
|-----------|------|-----------:|------|--------|-------|----------|
| **#187240** Evaluate Deployment and Distribution Options | LS Dev | **244** | Enabler | New | Ike Yana | [[summaries/audit-ado-ls-dev-20260419-1345]] |
| #194082 | LS Dev | >90 (PI5/Nov–Dec 2025 cohort) | — | — | — | [[entities/team-ado-ls-dev]] |
| #194084 | LS Dev | >90 (PI5/Nov–Dec 2025 cohort) | — | — | — | [[entities/team-ado-ls-dev]] |
| #195229 | LS Dev | >90 (PI5/Nov–Dec 2025 cohort) | — | — | — | [[entities/team-ado-ls-dev]] |
| #194386 | LS Dev | >90 (PI5/Nov–Dec 2025 cohort) | — | — | — | [[entities/team-ado-ls-dev]] |
| **#201569** Netlify/GitHub Transfer | Flawless | 14+ (Ready since Day 3 of 7.1) | Spike | Ready | Carol Cuison | [[summaries/audit-ado-fl-dev-20260419-1345]], [[synthesis/dor-leakage]] |
| **#201504** School Engagement & Flyering | JIT | 16 (untouched since Apr 3) | User Story | — | [[entities/person-grace]] | [[summaries/audit-ado-jit-20260419-1345]] |
| **#201514** Free Discovery Day | JIT | 16 (untouched since Apr 3) | User Story | — | [[entities/person-grace]] | [[summaries/audit-ado-jit-20260419-1345]] |
| #202219 armelita marketing | JIT | 11 (last touched Apr 8) | User Story | — | armelita | [[summaries/audit-ado-jit-20260419-1345]] |
| #202237 armelita marketing | JIT | 11 (last touched Apr 8) | User Story | — | armelita | [[summaries/audit-ado-jit-20260419-1345]] |
| **#202894** Goverment payables for | Admin | born-stale (created Apr 19 with no DoR) | User Story | New | — | [[summaries/audit-ado-admin-20260419-1345]] |
| **#175921–175927** FamDay Field Day (4 tasks) | Admin | ~15 mos (xPI1\Iter 1.4, Feb 2025) | Task | Active | **Roche Casipong** | [[summaries/backlog-analysis-ado-admin-20260505]] |
| **#175958–175964** PHILHEALTH/tax certs (4 tasks) | Admin | ~15 mos (xPI1\Iter 1.3, Jan 2025) | Task | Active/New | **Almera K. Tayao** | [[summaries/backlog-analysis-ado-admin-20260505]] |
| **#193234** Grass cutting Day 2 | Admin | ~7 mos (PI4\Iter 4.3, Oct 2025) | Task | New | Mark Colina | [[summaries/backlog-analysis-ado-admin-20260505]] |
| **#199736** CADAC training Day 1 | Admin | ~2 mos (PI6\Iter 6.5, Mar 2026) | Task | New | Mark Colina | [[summaries/backlog-analysis-ado-admin-20260505]] |
| #202229 Akira letter | OTP | 9 (last ChangedDate Apr 10) | User Story | Active | Grace | [[summaries/audit-ado-otp-20260419-1345]] |
| #192303 | JIT | 159 (reported 2026-03-25) | — | broader backlog | — | [[summaries/audit-ado-jit-20260325-0849]] |

Earlier portfolio snapshots confirm the pattern held for **weeks** before PI7.1 close: LS Dev carried **30 items >180 days stale** into PI7 with Backlog Refinement **0.0 for 11 consecutive audits** ([[summaries/portfolio-20260406-0900]], [[summaries/portfolio-20260401-0900]]); Flawless held **78 of 167 items stale_90 / 58+ stale_180** as late as Apr 12 ([[summaries/audit-ado-fl-dev-20260412-0900]]).

## Root-cause categories

### 1. Abandoned enablers

**#187240** is the archetype. Enabler work (deployment evaluation, infra research) loses priority in feature-heavy sprints; nobody is actively driving it, nobody schedules it, and it accumulates staleness month after month. The 9-audit streak of being flagged without action ([[entities/team-ado-ls-dev]]) is the signature — the item is **known**, not **hidden**, but no owner is accountable for closing or archiving it.

### 2. Low-capacity-owner gridlock

[[entities/person-grace]]'s JIT items **#201504** and **#201514** are configured against a **1 h/day Documentation allocation**; a 2-item sprint commitment exceeds 14h per iteration, so the items simply cannot progress. The 16-day freeze isn't Grace idling — it's structural ([[synthesis/capacity-planning]] Mode 3). Grace also owns OTP's stuck **#202229** (9-day stall, Akira dependency).

### 3. Spike-ready, never-done

**#201569** Netlify/GitHub Transfer Spike has been Ready/Active since Day 3 of 7.1 and is still open at Day 14 without progress ([[summaries/audit-ado-fl-dev-20260419-1345]], [[synthesis/dor-leakage]] §Pattern observations). The Spike form-factor is the problem: Ready is a terminal state until someone writes an acceptance criterion that can "pass." Carol Cuison was reassigned Carol → Ramon → Carol across the sprint without the item ever moving states ([[entities/person-carol]]).

### 4. Born-incomplete

**#202894** was **created Apr 19, Day 14 of 7.1**, with a typo'd title ("Goverment payables for"), no Story Points, no Description, no Acceptance Criteria ([[summaries/audit-ado-admin-20260419-1345]]). It entered the backlog already non-compliant. Without an intervention gate these items age into category 1 within a PI. Same pathology is called out in [[synthesis/dor-leakage]] as "new-items-mid-iteration."

## Impact on scoring

Per [[concepts/scoring-ado-rubric]], Backlog Refinement (dimension 6) compounds stale penalties: a base freshness percentage plus up to **two −20 penalties** (`stale_90` share > 25%, `stale_180` presence).

| Team | Stale driver | Backlog Refinement | Net drag on Overall (/7) | Citation |
|------|--------------|-------------------:|-------------------------:|----------|
| LS Dev | #187240 (244d) + 4 PI5 stragglers | **18.3 🔴 Critical** | ≈ −11.7 points | [[summaries/audit-ado-ls-dev-20260419-1345]] |
| JIT | #201504 + #201514 (16d, Grace) | **80.0 🟢** (−20 untouched penalty) | ≈ −2.9 points | [[summaries/audit-ado-jit-20260419-1345]] |
| Flawless | #201569 + 58+ legacy (Apr 12 read) | **100.0** (recovered from 26.9 post-groom) | dim held; Spike stalls Delivery Predictability instead | [[summaries/audit-ado-fl-dev-20260419-1345]], [[summaries/audit-ado-fl-dev-20260412-0900]] |
| Admin | #202894 (born-stale, 7.2 pipeline) | 100.0 today; will degrade if unresolved | pre-emptive | [[summaries/audit-ado-admin-20260419-1345]] |

Closing/archiving #187240 alone lifts LS Dev Backlog Refinement from 18.3 → ~98 in one grooming pass — a single-item remediation worth **~+11 Overall points** ([[entities/team-ado-ls-dev]] §Structural notes).

## Proposed quarterly amnesty & triage

A standing end-of-PI process to drain the backlog of chronic debt rather than carrying it audit-to-audit:

1. **PI-close amnesty sweep.** Any item with `ChangedDate > 90 days` at PI close enters a **triage session** with three outcomes:
   - **Close as obsolete** (default if no owner defends it in 10 minutes)
   - **Re-scope** — rewrite title/Description/AC and re-estimate; if it re-enters a sprint it resets the clock
   - **Reassign** if the current owner is capacity-blocked (category 2)
2. **Capacity-blocked items** (Grace's #201504/#201514, OTP's #202229) escalate to the **owner's manager** for reassignment before the amnesty default-closes them — the problem is allocation, not the item ([[synthesis/capacity-planning]]).
3. **Spike-ready-never-done** (#201569 pattern) triggers a **30-day acceptance-criteria deadline** from the day the Spike enters Ready. If no written AC by deadline, the Spike auto-closes as **superseded** and a replacement work item must be written if the investigation is still needed.
4. **Born-incomplete** (#202894 pattern) auto-flags **`provisional`** at creation and auto-ejects from iteration path at kickoff + 2 days unless groomed — the same gate already proposed in [[synthesis/dor-leakage]] §Proposed DoR Gate. Unifies the two anti-patterns under one mechanic.

## Dashboard addition

Add a **Top 10 Stalest Items** portfolio widget — one row per item, columns `Work Item · Team · Age (days) · Type · Owner · Root cause category`, sorted descending by age, refreshed daily. Same pattern as the DoR dashboard addition in [[synthesis/dor-leakage]] and the UPS composite row in [[synthesis/ups-masking-pattern]]. At the top of the list today would sit LS Dev #187240 at 244 days — a single cell that would have been red on 9 consecutive dashboards.

## Related

- [[entities/team-ado-ls-dev]] · [[entities/team-ado-jit]] · [[entities/team-ado-fl-dev]] · [[entities/team-ado-admin]]
- [[entities/person-grace]] · [[entities/person-carol]]
- [[synthesis/dor-leakage]] — companion anti-pattern; `provisional` flag unifies born-incomplete handling
- [[synthesis/capacity-planning]] — category 2 root cause (Grace Mode 3)
- [[synthesis/iteration-7.1-close]] — 7.1 retrospective surface for proposed remediations
- [[concepts/scoring-ado-rubric]] — Backlog Refinement dimension definition
