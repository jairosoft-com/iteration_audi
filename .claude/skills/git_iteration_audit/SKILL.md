---
name: git-iteration-audit
description: Run a standardized GitHub + ADO iteration audit for a single `git_*` workspace or for `all-git-projects`. This skill is the authority for Git audit workflow, scoring, evidence rules, report structure, output policy, and batch behavior.
argument-hint: [project-folder] or [all-git-projects]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, Agent
---

# Git Iteration Audit Skill

Use this skill for standardized GitHub + ADO iteration audits for `git_*` workspaces in this repository.

Do not use this skill for:

- `ado_*` workspaces
- ADO-only SAFe audits
- PDF generation or report packaging workflows
- separate `SCORECARD_*.md` outputs

## Authority and precedence

This skill is the authoritative source for:

- audit workflow
- evidence precedence
- scoring rules
- integrated report structure
- output policy
- batch behavior

Each project `CLAUDE.md` remains the local source of truth for:

- project scope
- ADO team and backlog context
- GitHub repository scope
- people and glossary
- audit history
- explicit `Project Exceptions`

If a project `CLAUDE.md` conflicts with this skill on workflow, scoring, evidence, or output policy, this skill wins unless the conflicting item is explicitly documented under `Project Exceptions`.

## Accepted inputs

This skill accepts exactly two invocation styles:

- `git_iteration_audit [project-folder]`
- `git_iteration_audit all-git-projects`

### Single-project mode

When given a single project folder:

- the folder must be a top-level `git_*` workspace
- the folder must contain `CLAUDE.md`
- write exactly one report to that folder's `audit/` directory

### Batch mode

When given `all-git-projects`:

- enumerate only top-level folders matching `git_*`
- keep only folders that contain `CLAUDE.md`
- process folders in alphabetical order
- generate one integrated report per project in that project's `audit/` directory
- never include `ado_*` folders in the batch

## Required workflow

For each target project:

1. Load the project's `CLAUDE.md`.
2. Read project-local context from that file only:
   - ADO organization, project, team, and backlog scope
   - GitHub repository scope
   - people and glossary
   - audit history
   - explicit `Project Exceptions`
3. Resolve the current active iteration from the scoped ADO team context.
4. Review the most recent prior audit report in that project's `audit/` folder.
   - Use the prior audit for delta context only.
   - Never use the prior audit as a substitute for current evidence.
5. Collect scoped ADO evidence from the current iteration and scoped GitHub evidence from the repository set.
6. Compute the three standard scores described below:
   - `Iteration Compliance Score`
   - `SGPI`
   - `HCI`
7. Write exactly one integrated Markdown report to `./audit/AUDIT_<date>_<time>.md`.

## Evidence precedence

Use this order of precedence:

1. Current ADO iteration and team settings from the scoped team
2. Current ADO parent backlog items in the scoped `Stories and Deliverables` backlog
3. ADO revisions, relations, capacity, and change history
4. Scoped GitHub PR, branch, commit, review, and merge evidence within the iteration window
5. Latest prior audit for delta comparison only

Never broaden scope beyond:

- the ADO project named in the local `CLAUDE.md`
- the ADO team named in the local `CLAUDE.md`
- the scoped `Stories and Deliverables` backlog
- the GitHub repositories named in the local `CLAUDE.md`

## Standard scoring rubric

Every Git audit report must contain these three explicit named scores:

- `Iteration Compliance Score`
- `SGPI`
- `HCI`

### 1. Iteration Compliance Score

Use the deterministic SAFe compliance model from the canonical `git_aa_dev` standard.

#### Dimensions and weights

- `Alignment` = 25
- `Estimation` = 20
- `Quality / DoD` = 35
- `Iteration Integrity` = 20

#### Scope boundary

- Score only current-iteration parent backlog items in the scoped `Stories and Deliverables` backlog
- Exclude child tasks and task-category items

#### Calculation

- `dimension_score = compliant_eligible_items / eligible_items * 100`
- `overall_score = sum(dimension_score * weight) / 100`
- round the final percentage to 1 decimal place

#### Risk bands

- `Green` = `>= 90`
- `Yellow` = `75 - 89.9`
- `Red` = `< 75`

#### Preserve from the canonical Git SAFe model

- alignment parent-link logic
- schema-gap handling
- eligible-item rules
- evidence-gap reporting
- score table columns:
  - `Dimension`
  - `Eligible Items`
  - `Compliant Items`
  - `Failed Items`
  - `Score %`
  - `Weight`
  - `Weighted Contribution`
  - `Evidence`
  - `Reason`

### 2. SGPI

Use `SGPI` as the sprint goal predictability score.

#### Official headline score

- `Committed Scope SGPI = Closed Story Points / Total Committed Story Points`

#### Supporting context metrics

- `Original Scope SGPI = Closed Story Points / Original Planned Story Points`
- `Delivered Proxy SGPI = (Closed Story Points + Passed QA Story Points) / Total Committed Story Points`

#### Reporting rule

- The label `SGPI` always means `Committed Scope SGPI`
- The other two formulas appear only as supporting context

### 3. HCI

Use `HCI` as the engineering health score.

#### Dimensions

- `PR Review Compliance`
- `Branch Protection & Enforcement`
- `CI/CD Gate Quality`
- `Code Ownership`
- `Merge Hygiene & Churn`
- `Work Item ↔ GitHub Traceability`
- `Sprint Discipline`
- `Defect Triage & Velocity`
- `Backlog & Story Hygiene`
- `Capacity Balance & Ownership Distribution`

#### Calculation

- each dimension is scored from `0` to `10`
- `HCI = sum(10 dimension scores)` and is reported as a `/100` score

#### Preserve from the current Git engineering health scorecard

- dimension tables
- category summaries
- remediation style

## Required report structure

Every report must be Markdown only and include these sections in this order:

1. `Audit Metadata`
2. `Executive Summary`
3. `Iteration Scope and Methodology`
4. `Scorecard Summary`
5. `Sprint Goal Predictability (SGPI)`
6. `Developer Productivity Findings`
7. `SAFe Compliance Findings`
8. `Iteration Compliance Score`
9. `Engineering Health Index (HCI)`
10. `ADO-to-GitHub Traceability Analysis`
11. `Collaboration and Review Analysis`
12. `Repository Hygiene`
13. `Risks and Bottlenecks`
14. `Prioritized Remediation Actions`
15. `Evidence Gaps and Limitations`

### Required report content

Near the top of the report, include:

- current iteration name
- current iteration start and finish dates
- scoped ADO team and backlog
- scoped GitHub repositories
- all three named scores

The integrated report must absorb scorecard content directly into the main audit.
Do not emit a separate `SCORECARD_*.md`.

## Visualization policy

Use Mermaid when visualization adds value.

At minimum, include one Mermaid visualization when enough evidence exists, using one of:

- score summary
- state distribution
- SGPI trend
- HCI dimension summary
- traceability breakdown

Do not use `xychart-beta`.

## Output policy

- Write source reports as Markdown only
- Save reports under the target project's `audit/` directory
- Use `AUDIT_<date>_<time>.md`
- Do not generate PDFs
- Do not generate `SCORECARD_*.md`
- Do not write final source reports to `report/` or `temp/`
- Historical scorecards may remain in the repo as legacy artifacts, but new audits must not create them

## Failure behavior

### Single-project mode

If required ADO or GitHub context cannot be resolved:

- stop
- report the failure explicitly
- do not improvise missing scope

### Batch mode

If one project fails:

- continue processing remaining valid `git_*` projects
- record failed or skipped projects in the final batch summary
- do not let one failed project block the rest of the batch

### Missing evidence

When some evidence is missing but the audit can still proceed:

- continue in degraded mode
- record the missing evidence in `Evidence Gaps and Limitations`
- avoid fabricated conclusions

## Completion checklist

Before finishing, verify all of the following:

- the target is a `git_*` workspace or `all-git-projects`
- the local `CLAUDE.md` was read
- the current active iteration was resolved
- the latest prior audit was reviewed
- all three named scores were computed exactly once
- `SGPI` headline value is committed-scope SGPI
- the report used the required section order
- the output is Markdown only
- no PDF or `SCORECARD_*.md` artifacts were generated
- batch mode never touched `ado_*` workspaces
