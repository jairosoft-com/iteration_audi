---
title: "CI / Engineering-Health Baseline — Git Teams (Pre-P0)"
type: synthesis
tags: [ci, engineering, hci, git, baseline, branch-protection]
sources:
  - "../synthesis/github-compliance-issues.md"
  - "../synthesis/ups-masking-pattern.md"
  - "../entities/team-git-aa-dev.md"
  - "../entities/team-git-cc-dev.md"
  - "../summaries/audit-git-aa-dev-20260419-1345.md"
  - "../summaries/audit-git-cc-dev-20260419-1345.md"
  - "../summaries/audit-git-aa-dev-20260417-0900.md"
  - "../summaries/audit-git-aa-dev-20260416-0900.md"
  - "../summaries/audit-git-aa-dev-20260413-0900.md"
  - "../summaries/audit-git-aa-dev-20260412-0900.md"
  - "../summaries/audit-git-aa-dev-20260407-1719.md"
  - "../summaries/audit-git-cc-dev-20260417-0900.md"
  - "../summaries/audit-git-cc-dev-20260416-0900.md"
  - "../summaries/audit-git-cc-dev-20260413-0900.md"
  - "../summaries/audit-git-cc-dev-20260408-0900.md"
  - "../summaries/audit-git-cc-dev-20260407-1708.md"
  - "../concepts/scoring-git-ups.md"
created: 2026-04-20
updated: 2026-04-20
---

# CI / Engineering-Health Baseline — Git Teams (Pre-P0)

## Baseline

Closing-Day-14 of Iteration 7.1, the two Git-audited teams sit at **HCI 49 (Auto Allies, 🟠 High / 🔴 Critical under Section 9 math)** and **HCI 74 (Colina Health, 🟡 Moderate)** ([[entities/team-git-aa-dev]] · [[entities/team-git-cc-dev]]). This page is the **pre-P0 snapshot**: the empirical "before" against which the P0 branch-protection policy proposed in [[synthesis/github-compliance-issues]] will be measured once rolled out.

## What HCI measures

HCI is the 0.30-weighted engineering-health component of UPS ([[concepts/scoring-git-ups]]). In the Git audit rubric each sub-component scores `/10`, summed to `/100`. Six sub-signals appear repeatedly in the audit chain:

| Sub-signal | AA 04-19 | CC 04-19 | What moves it |
|------------|---------:|---------:|---------------|
| PR Review | 2/10 | 7–8/10 | % merged PRs with reviewer assigned + approval ([[summaries/audit-git-aa-dev-20260419-1345]]) |
| Branch Protection | 1/10 | 1–2/10 | `protected: true` on `main`/`develop` + required-reviewer rule ([[entities/team-git-cc-dev]]) |
| Capacity Balance | 3/10 | 6–7/10 | Contribution spread across team roster (zero-contributors penalise) |
| Traceability | 7/10 | 10/10 | AB# prefix rate on commits / PR title-or-body ([[entities/team-git-aa-dev]]) |
| Backlog Hygiene | 8/10 | 9/10 | Open-PR aging, stale branches, labelling discipline |
| Sprint Discipline | 6–7/10 | 10/10 | Iteration-path integrity, scope-cleanup, end-of-sprint parking |

Conspicuously **absent from the current rubric: test-coverage reporting and CI pass-rate on PRs.** Audits do flag `CI failures / no CI status on PRs` (3 of 48 audits — [[synthesis/github-compliance-issues]] rank #10) but neither is a first-class HCI sub-score today. That is a gap (see [Related-but-not-P0 fixes](#related-but-not-p0-fixes)).

## Current state — AA Dev (HCI 49)

**Driving sub-signals:** PR Review 2/10, Branch Protection 1/10, Capacity Balance 3/10 ([[summaries/audit-git-aa-dev-20260419-1345]]). Zero formal approvals on ~48 merged sprint PRs; `develop`/`dev`/`staging`/`main` all `protected: false` on both AA repos ([[entities/team-git-aa-dev]]).

**Iteration 7.1 HCI trajectory** — 8 consecutive audits, persistent Critical/High:

| Day | HCI | Band | Source |
|-----|----:|------|--------|
| 04-07 Day 2 | 36 | 🔴 Critical | [[summaries/audit-git-aa-dev-20260407-1719]] |
| 04-12 Day 7 | 36 | 🔴 Critical | [[summaries/audit-git-aa-dev-20260412-0900]] |
| 04-13 Day 8 | 40 | 🔴 Critical | [[summaries/audit-git-aa-dev-20260413-0900]] |
| 04-16 Day 11 | 47 | 🔴 Critical | [[summaries/audit-git-aa-dev-20260416-0900]] |
| 04-17 Day 12 | 49 | 🟠 High | [[summaries/audit-git-aa-dev-20260417-0900]] |
| 04-19 Day 14 | 49 | 🟠 High / 🔴 48 Sec.9 | [[summaries/audit-git-aa-dev-20260419-1345]] |

**UPS masking relationship:** at HCI 49 the engineering-health drag is 49 × 0.30 = 14.7 points, but ICS 99.4 × 0.50 = 49.7 anchors UPS at 68.6 🟡 Moderate. Critical engineering-health never bubbles up as a portfolio-level Critical band ([[synthesis/ups-masking-pattern]]). Retro spike `#202169` (PR reviews / branch protection) has been Active for a full sprint with no practice change ([[summaries/audit-git-aa-dev-20260412-0900]]).

## Current state — CC Dev (HCI 74)

**What keeps CC Moderate (not Low):** branch protection still `protected: false` on `main` and `develop` for both FE and BE ([[entities/team-git-cc-dev]]); review latency is concentrated on two reviewers (`pcoronia` as lead author, `raseniero` as requested reviewer on 3 of 3 currently-open PRs). Sprint Discipline 10/10 and Traceability 11/11 (100%) carry the score — the gap vs. AA is governance, not code review throughput.

**Iteration 7.1 HCI trajectory** — gradual climb Moderate→Moderate:

| Day | HCI | Band | Source |
|-----|----:|------|--------|
| 04-07 Day 2 | 60 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260407-1708]] |
| 04-08 Day 3 | 55 | 🟠 High | [[summaries/audit-git-cc-dev-20260408-0900]] |
| 04-13 Day 8 | 68 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260413-0900]] |
| 04-16 Day 11 | 70 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260416-0900]] |
| 04-17 Day 12 | 73 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260417-0900]] |
| 04-19 Day 14 | 74 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260419-1345]] |

**HIPAA adjacency risk:** BE PR#55 (42 files, PHI audit trail + structured logging) sits 2 days without approval under no-branch-protection conditions ([[summaries/audit-git-cc-dev-20260419-1345]]). If HCI slips further while `hipaa`-adjacent PRs are in-flight, the failure mode stops being "score ding" and becomes a compliance incident ([[synthesis/github-compliance-issues]] ranks #11–#12).

## Metrics to track post-P0

Concrete before/after deltas to capture on each Git audit close:

| Metric | Baseline (04-19) | Target post-P0 | Cadence |
|--------|-----------------:|---------------:|--------|
| % merged PRs with required-reviewer approval | AA ~0% · CC partial | ≥95% both teams | per-iteration |
| % merged PRs with passing CI at merge | not measured | ≥95% | per-iteration, new instrument |
| Mean PR review latency (open → approved, hours) | CC ~48h (BE#55) · AA N/A | <24h non-HIPAA · <4h `hipaa` | per-iteration |
| Count of force-push / direct-to-main events | AA 2 · CC 2 of 48 ([[synthesis/github-compliance-issues]]) | 0 | per-iteration |
| `hipaa`-labeled PR compliance rate (2 reviewers + approved) | 0/2 ([[summaries/audit-git-cc-dev-20260419-1345]]) | 100% | CC-only, per-PR |
| AB# prefix rate on commits | AA ~<50% (20/26 audits flag) | ≥95% | AA-only, per-iteration |

## Expected shifts after P0 adoption

**Will move:**

- **AA PR Review sub-score 2/10 → 7–8/10** once required reviewer rule forces approval gates on both AA repos. Single biggest lever on AA HCI.
- **Branch Protection 1/10 → 8–10/10** both teams immediately on policy apply.
- **Direct-to-main count → 0** mechanically.
- **AA HCI 49 → projected 65–72** — still Moderate, not Low, because Capacity Balance (zero-contributor pattern, [[entities/team-git-aa-dev]]) and CI pass-rate are not addressed by P0.

**Won't move structurally:**

- **AA SGPI** (QA-gating failure mode — [[summaries/audit-git-aa-dev-20260419-1345]] — is a capacity issue, not a CI issue).
- **AA Capacity Balance 3/10** — Jerlyn Ates' 3rd-consecutive zero-contribution sprint is an HR/protocol problem, not a policy one.
- **CC review latency** unless a second named reviewer is added alongside `pcoronia`/`raseniero` ([[synthesis/github-compliance-issues]] open question).
- **Test coverage** — not instrumented in the audit today.

## Related-but-not-P0 fixes

- **Test-coverage reporting** — add `coverage%` as a first-class HCI sub-signal once either repo publishes a coverage artefact from CI. Currently unmeasured.
- **PR-size guardrail** — BE#55 at 42 files ([[summaries/audit-git-cc-dev-20260419-1345]]) is the canonical case. Target avg ≤20 files; enforce via size label + reviewer policy, not hard block.
- **CODEOWNERS configuration for HIPAA areas** — pair with the `hipaa` label rule in P1 ([[synthesis/github-compliance-issues]]) so PHI-touching paths auto-route to `raseniero` + one more named reviewer.
- **CI status as a merge gate** — GitHub Actions required checks for both AA repos and all three CC repos. Currently advisory only ([[entities/team-git-cc-dev]] open question).

## Open questions

- Should HCI be disaggregated in audit reports (report all 6 sub-scores, not just composite) so the P0 delta is attributable to specific sub-signals? See [[synthesis/github-compliance-issues]] methodology section.
- Does `colina-health-ai-agent-code-fixing` need the same P0 rules as production repos — and what's its HCI today? No iteration-level audit currently surfaces it.
- Is the AA HCI floor a **training** problem (devs merging their own PRs because they don't know reviewers are required) or a **protocol** problem (Engineering Manager [[entities/person-bomar]] not enforcing)? Post-P0 noncompliance rate disambiguates.
- Should a **weekly CI-health report** from `ci-health` deltas be routed to [[entities/person-bomar]] as the review-enforcement owner?

## Related

- [[synthesis/github-compliance-issues]] — parent; P0 proposal this page measures
- [[synthesis/ups-masking-pattern]] — why HCI Critical is invisible at the portfolio layer
- [[synthesis/top-compliance-issues]] — portfolio-wide issue ranking
- [[entities/team-git-aa-dev]] · [[entities/team-git-cc-dev]] — per-team detail
- [[entities/person-bomar]] — Engineering Manager, natural owner of HCI remediation
- [[concepts/scoring-git-ups]] — HCI weighting (0.30)
