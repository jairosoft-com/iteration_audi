---
title: "GitHub Compliance Issues — Git-audited Teams (Auto Allies + Colina Health)"
type: synthesis
tags: [github, git, compliance, engineering, auto-allies, colina, branch-protection, traceability]
sources:
  - "../entities/team-git-aa-dev.md"
  - "../entities/team-git-cc-dev.md"
  - "../synthesis/ups-masking-pattern.md"
  - "../synthesis/top-compliance-issues.md"
  - "../entities/person-jerlyn.md"
  - "../concepts/scoring-git-ups.md"
created: 2026-04-20
updated: 2026-04-20
---

# GitHub Compliance Issues — Git-audited Teams

Cross-cutting ranking of GitHub/Git-workflow compliance issues across the two teams whose audits use the UPS rubric ([[concepts/scoring-git-ups]]): [[entities/team-git-aa-dev]] (Auto Allies, 26 audits) and [[entities/team-git-cc-dev]] (Colina Health, 22 audits). Derived from a keyword-frequency scan of all 48 Git audit summaries.

**Headline:** the two teams fail in **completely different ways**. Auto Allies exhibits **engineering-health degradation** (traceability gaps, HCI Critical, branch protection); Colina Health exhibits a **review-discipline gap with HIPAA exposure** (reviewer bottleneck, unreviewed merges, large compliance-sensitive PRs). A single "GitHub compliance" policy should address both failure modes.

## Ranked issue table

| # | Issue | Total / 48 | AA | CC | Kind | Wiki cross-ref |
|--:|-------|-----:|---:|---:|------|----------------|
| 1 | Sprint Goal Progress Index — commits/PRs not linked to the sprint goal | 48 (100%)⚠ | 26 | 22 | SGPI component | [[concepts/scoring-git-ups]] |
| 2 | Branch protection gaps / missing required reviewers | 27 (56%) | 16 | 11 | universal | — |
| 3 | Low commit-to-PR ratio / missing AB# traceability | 22 (46%) | **20** | 2 | AA-dominant | [[entities/team-git-aa-dev]] |
| 4 | HCI (Health Check Index) Critical/Red | 15 (31%) | **12** | 3 | AA-dominant | [[synthesis/ups-masking-pattern]] |
| 5 | Unreviewed PRs merged / auto-merge | 4 (8%) | 1 | **3** | CC-dominant | [[entities/team-git-cc-dev]] |
| 6 | PR review latency / reviewer bottleneck | 4 (8%) | 0 | **4** | CC-only | [[entities/team-git-cc-dev]] |
| 7 | Zero-contribution pattern (team member silent N sprints) | 4 (8%) | 3 | 1 | AA-dominant | [[entities/person-jerlyn]] |
| 8 | Mid-sprint scope addition affecting ICS | 4 (8%) | 3 | 1 | AA-dominant | — |
| 9 | Direct-to-main commits / skipped PR | 4 (8%) | 2 | 2 | universal | — |
| 10 | CI failures / no CI status on PRs | 3 (6%) | 2 | 1 | AA-dominant | — |
| 11 | HIPAA compliance-sensitive PR unreviewed | 2 (4%) | 0 | **2** | CC-only (high stakes) | [[entities/team-git-cc-dev]] |
| 12 | Large PR size / high file count | 1 (2%) | 0 | 1 | CC — BE#55 (42 files) | [[summaries/audit-git-cc-dev-20260419-1345]] |
| 13 | Stale feature branch / long-running branch | 1 (2%) | 1 | 0 | AA | — |
| 14 | Blank / low-quality PR description | 1 (2%) | 0 | 1 | CC | — |

⚠ **Caveat on #1:** The 48/48 count reflects that SGPI is computed in *every* audit (the metric name appears universally). The actual *problem* is concentrated on Auto Allies — **SGPI 21.2% (Red) at 04-19 close** — while Colina Health's SGPI is routinely 100% 🟢. Treat #1 as "AA-dominant" in practice.

## Two distinct failure modes

### Auto Allies — Engineering-health degradation

**Dominant issues:** #3 (traceability), #4 (HCI Critical), #7 (zero-contribution), #10 (CI gaps).

**Profile:** The composite UPS has been **Moderate** (68.6 latest) for weeks while the engineering-health component (HCI) has been **Critical** (49 latest). The math of UPS = ICS·0.50 + HCI·0.30 + SGPI·0.20 smooths the signal: ICS 99.4% × 0.50 = 49.7 alone carries the composite above 60. See [[synthesis/ups-masking-pattern]] for full treatment.

Specific signatures in the audit chain:
- **Traceability:** 20 of 26 AA audits flag AB# missing on a majority of commits/PRs. ADO → GitHub audit can't run on those PRs.
- **HCI Critical:** 12 of 26 audits flag HCI in the Critical band. Driven by unreviewed merges + stale PR aging + branch-protection gaps.
- **Zero-contribution:** 3 audits explicitly call out [[entities/person-jerlyn]]'s zero artifacts across 3 consecutive sprints.
- **Positive outlier:** Joseph Gerona's multi-scope PRs (FE #122, BE #83) maintain 4-items-per-PR AB# traceability. A template that could be adopted team-wide.

**Root cause:** No forcing function (branch protection) + no convention enforcement (pre-commit hook for AB#) + one silent contributor unmanaged for 3 sprints.

### Colina Health — Review-discipline gap with HIPAA exposure

**Dominant issues:** #5 (unreviewed merges), #6 (review latency), #11 (HIPAA PRs unreviewed), #12 (large PRs).

**Profile:** The composite UPS is strong (90.6 latest, 🟢 Low), **but** the component mix hides a review-discipline gap that's higher-stakes than the headline implies because Colina handles healthcare data (EMR). One large unreviewed PR at the wrong time could be a compliance incident, not just a score ding.

Canonical case: **BE#55 HIPAA PR (42 files)** — carrying into 7.2 without required reviewers ([[summaries/audit-git-cc-dev-20260419-1345]]).

Specific signatures:
- **Review latency:** 4 of 22 CC audits flag reviewer bottleneck (Paul Coronia is the primary reviewer; `pcoronia`).
- **Unreviewed merges:** 3 of 22 CC audits flag merges proceeding without required approval.
- **HIPAA-adjacent PRs unreviewed:** 2 flagged. These are higher-risk per mention than raw count suggests.

**Root cause:** Small team + no required-reviewer branch protection + no HIPAA-specific review SLA.

## Remediation proposal

A **single GitHub compliance policy** addressing both failure modes. Priority-ordered by impact vs. effort:

### P0 — Apply across all 5 repos

| Repo | Team | Recommended rule |
|------|------|------------------|
| `jairosoft-com/autoallies-version2` | [[entities/team-git-aa-dev]] | Required reviewer ≥1 · passing CI · no force push on `main` |
| `jairosoft-com/autoallies-api-core` | AA | Same |
| `jairosoft-com/colinahealth-fe` | [[entities/team-git-cc-dev]] | Required reviewer ≥1 · passing CI · no force push |
| `jairosoft-com/colinahealth-be` | CC | Same **+ `hipaa` label requires ≥2 reviewers** (see P1) |
| `jairosoft-com/colina-health-ai-agent-code-fixing` | CC | Standard P0 rules |

Addresses ranks 2 (branch protection), 5 (unreviewed merges), 9 (direct-to-main) in one change.

### P1 — Colina-specific: HIPAA review gate

Define a `hipaa` GitHub label. Any PR touching colinahealth-fe/be that changes patient-data-handling files auto-applies the label. Labeled PRs require **2 reviewers** and cannot be merged without both approvals. Addresses ranks 11 and 12 directly.

### P2 — Auto Allies: AB# traceability enforcement

Add a **pre-commit hook** that rejects commits lacking an `AB#\d+` prefix. Mirror the convention in a PR template. Addresses rank 3. Joseph Gerona's PR style is the template.

### P3 — Auto Allies: sprint-goal linking in PR descriptions

Planning-time requirement: PR descriptions must reference the iteration's goal keyword (manual for now; can be auto-checked once goal strings are standardized). Addresses rank 1 on the AA side.

### P4 — Capacity-silence alert for zero-contribution

Weekly automated report: any team member with 0 commits + 0 PR reviews for 14 days surfaces in [[synthesis/top-compliance-issues]] dashboard. Addresses rank 7 ([[entities/person-jerlyn]] pattern).

## Dashboard additions (portfolio-level)

Changes to how Git teams appear in [[summaries/portfolio-20260419-1953]]-style dashboards:

1. **Component-breakdown row** next to UPS (per [[synthesis/ups-masking-pattern]]): show ICS / HCI / SGPI with individual band pills.
2. **Min-component band** as a second pill next to UPS composite.
3. **"Open unreviewed PRs (compliance-sensitive)"** widget — specifically tracks `hipaa`-labeled PRs across Colina repos.
4. **"Silent contributors"** widget — anyone in the Git team roster with 0 artifacts over the last iteration.

## Why GitHub compliance matters beyond scoring

The Git audits are the **only place the engineering-practice layer gets measured** in this portfolio. ADO audits capture planning, capacity, DoR, delivery discipline — but not code review quality, CI hygiene, branch protection, or commit traceability. For the 2 Git teams (and arguably any future team using GitHub), the Git audit is the engineering-conscience record. Weakening it ripples: HIPAA incidents on Colina, production regressions on AA.

## Open questions

- **Should HIPAA review policy also apply to the AI-agent repo** (`colina-health-ai-agent-code-fixing`)? That code fixes the main codebase — a compromise there could bypass the main repo's protections.
- **Is the HCI Critical on Auto Allies primarily review-driven or test-coverage-driven?** Current audits don't cleanly disaggregate. Future audits could report HCI sub-components.
- **Can we seed a `synthesis/ci-health` page once the P0 policy is in place and we have before/after data?** That was the queued follow-up from [[synthesis/top-compliance-issues]].
- **Does CC's review-bottleneck pattern improve if we add a second reviewer explicitly?** Paul Coronia is currently the concentration; low-cost test is to add another named reviewer.

## Methodology

Reproducible:

1. Enumerate `wiki/summaries/audit-git-*-*.md` (48 files as of 2026-04-20).
2. For each, run keyword-frequency match against 14 issue-family patterns (branch protection, traceability, HCI Critical, review latency, HIPAA, zero-contribution, etc.).
3. Tally total and per-team (AA / CC).
4. Split issues into three buckets: **universal** (both teams, ≥50% of audits), **AA-dominant**, **CC-dominant**.
5. Derive distinct failure modes by clustering the dominant issues per team.

**Rebuild cadence:** after every Git audit close (each team's latest audit replaces prior; the 48-audit scan expands monotonically).

## Related

- [[synthesis/top-compliance-issues]] — portfolio-wide view (this page is the Git-specific drill-in; rank #5 there is the branch-protection flag)
- [[synthesis/ups-masking-pattern]] — why AA's UPS hides the component Criticals
- [[synthesis/team-rankings]] · [[synthesis/score-streaks]] — where Git teams land on composite scoring
- [[entities/team-git-aa-dev]] · [[entities/team-git-cc-dev]] — per-team drill-ins
- [[entities/person-jerlyn]] — zero-contribution case
- [[concepts/scoring-git-ups]] — UPS formula
