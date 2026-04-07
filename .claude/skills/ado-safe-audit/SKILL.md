---
name: ado-safe-audit
description: Run a standardized ADO SAFe iteration audit for a single `ado_*` workspace or for `all-projects`. This skill is the authority for ADO audit workflow, scoring, evidence rules, and output policy.
argument-hint: [project-folder] or [all-projects]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, Agent
---

# ADO SAFe Audit Skill

Use this skill for standardized Azure DevOps SAFe audits for `ado_*` workspaces in this repository.

Do not use this skill for:
- `git_*` workspaces
- mixed GitHub + ADO EngProd audits
- PDF generation or report packaging workflows

## Authority and precedence

This skill is the authoritative source for:
- audit workflow
- scoring rubric
- evidence precedence
- report structure
- output policy
- batch behavior

Each project `CLAUDE.md` remains the local source of truth for:
- project, team, and board metadata
- people and glossary
- audit history
- explicit project exceptions

If a project `CLAUDE.md` conflicts with this skill on workflow, scoring, evidence, or output policy, this skill wins unless the difference is explicitly documented under `Project Exceptions`.

## Accepted inputs

This skill accepts exactly two invocation styles:

- `ado-safe-audit [project-folder]`
- `ado-safe-audit all-projects`

### Single-project mode

When given a single project folder:
- the folder must be a top-level `ado_*` workspace
- the folder must contain `CLAUDE.md`
- write exactly one report to that folder's `audit/` directory

### Batch mode

When given `all-projects`:
- enumerate only top-level folders matching `ado_*`
- keep only folders that contain `CLAUDE.md`
- process folders in alphabetical order
- generate one report per project in that project's `audit/` directory
- never include `git_*` folders in the batch

## Required workflow

For each target project:

1. Load the project's `CLAUDE.md`.
2. Read project-local context from that file only:
   - project/team/board identifiers
   - people and glossary
   - audit history
   - explicit `Project Exceptions`
3. Resolve the current active iteration from the scoped ADO team context.
4. Review the most recent prior audit report in that project's `audit/` folder.
   - Use the prior audit for delta context only.
   - Never use the prior audit as a substitute for current evidence.
5. Inspect the current iteration backlog and required ADO evidence.
6. Compute the same seven-dimension SAFe audit score described below.
7. Write exactly one Markdown report to `./audit/AUDIT_<date>_<time>.md`.

## Evidence precedence

Use this order of precedence:

1. Current iteration/team settings from the scoped ADO team
2. Current backlog and work item fields from the scoped Stories and Deliverables backlog
3. Work item revisions, change history, and iteration history
4. Team capacity data for the resolved current iteration
5. Prior audit report for delta comparison only

Never broaden scope beyond:
- the project named in the local `CLAUDE.md`
- the team named in the local `CLAUDE.md`
- the Stories and Deliverables backlog for that team

## Standard scoring rubric

Use one deterministic ADO SAFe v1 rubric for all `ado_*` audits.

### Core definitions

Use these definitions consistently:

- `visible_root_backlog_items`
  - Root-level items returned from the scoped Stories and Deliverables backlog in the current project, regardless of iteration
  - Exclude child tasks and Task-category children

- `current_iteration_root_items`
  - Subset of `visible_root_backlog_items` whose `IterationPath` equals the active iteration

- `contributors_with_current_work`
  - Distinct non-empty assignees on `current_iteration_root_items`

- `contributors_with_capacity`
  - Contributors from `contributors_with_current_work` who have positive capacity or at least one configured activity in the active iteration

- `point_eligible_current_items`
  - `current_iteration_root_items` whose type exposes a Story Points field

- `estimated_current_items`
  - `point_eligible_current_items` with `Story Points > 0`

- `dor_compliant_current_items`
  - `current_iteration_root_items` whose Description and Acceptance Criteria are both present after trimming markup
  - Description minimum: `>= 30` non-whitespace characters
  - Acceptance Criteria minimum: `>= 20` non-whitespace characters

- `fresh_visible_root_items`
  - `visible_root_backlog_items` with `ChangedDate` within the last `45` days

- `stale_90_visible_root_items`
  - `visible_root_backlog_items` with `ChangedDate` older than `90` days

- `stale_180_visible_root_items`
  - `visible_root_backlog_items` with `ChangedDate` older than `180` days

- `untouched_current_items`
  - `current_iteration_root_items` whose `ChangedDate` is earlier than the active iteration start date

- `dominant_type_share`
  - The largest single work-item-type share among `current_iteration_root_items`

- `spike_share`
  - Share of `Spike` items among `current_iteration_root_items`

- `committed_story_points`
  - Sum of Story Points on `estimated_current_items`

- `closed_story_points`
  - Sum of Story Points on `estimated_current_items` whose State is `Closed` or `Done`

### Exact formulas

Score each dimension on `0-100`.

#### 1. Iteration Planning

- If `visible_root_backlog_items = 0`, score `0`
- Otherwise:
  - `Iteration Planning = round(current_iteration_root_items / visible_root_backlog_items * 100, 1)`

#### 2. Team Capacity

- If `contributors_with_current_work = 0`, score `0`
- Otherwise:
  - `Team Capacity = round(contributors_with_capacity / contributors_with_current_work * 100, 1)`

#### 3. Estimation

- If `point_eligible_current_items = 0`, score `0`
- Otherwise:
  - `Estimation = round(estimated_current_items / point_eligible_current_items * 100, 1)`

#### 4. DoR Compliance

- If `current_iteration_root_items = 0`, score `0`
- Otherwise:
  - `DoR Compliance = round(dor_compliant_current_items / current_iteration_root_items * 100, 1)`

#### 5. Work Item Balance

- If `current_iteration_root_items = 0`, score `0`
- Otherwise start from `100` and subtract penalties:
  - no `User Story` items in `current_iteration_root_items`: `-40`
  - `dominant_type_share > 60%`: `-30`
  - `spike_share > 40%`: `-20`
- `Work Item Balance = max(0, 100 - penalties)`

#### 6. Backlog Refinement

- If `visible_root_backlog_items = 0`, score `0`
- Otherwise start from:
  - `base = round(fresh_visible_root_items / visible_root_backlog_items * 100, 1)`
- Then subtract penalties:
  - if `stale_90_visible_root_items / visible_root_backlog_items > 25%`: `-20`
  - else if `stale_90_visible_root_items / visible_root_backlog_items > 10%`: `-10`
  - if `stale_180_visible_root_items >= 1`: `-20`
  - if `current_iteration_root_items > 0` and `untouched_current_items / current_iteration_root_items > 30%`: `-20`
  - else if `current_iteration_root_items > 0` and `untouched_current_items / current_iteration_root_items > 10%`: `-10`
- `Backlog Refinement = max(0, base - penalties)`

#### 7. Delivery Predictability

- If `committed_story_points = 0`, score `0`
- Otherwise:
  - `Delivery Predictability = round(closed_story_points / committed_story_points * 100, 1)`
- Early-sprint note: When the iteration is in its first 5 days (Day 1–5 of a 14-day sprint), annotate the dimension findings with "early-sprint — low delivery expected". No formula adjustment.

### Overall score and risk band

- `Overall Score = round((Iteration Planning + Team Capacity + Estimation + DoR Compliance + Work Item Balance + Backlog Refinement + Delivery Predictability) / 7, 1)`

Use these fixed risk bands:
- `Low Risk` = `>= 80`
- `Moderate Risk` = `60 - 79.9`
- `High Risk` = `40 - 59.9`
- `Critical` = `< 40`

### Evidence gaps

If a required field is unavailable:
- note the gap explicitly in the report
- do not invent missing values
- keep the score deterministic using only visible evidence
- when a dimension denominator becomes `0` because the evidence is missing or no eligible items exist, keep that dimension at `0`

## Required report structure

Every report must be Markdown only and include these sections in this order:

1. `Audit Metadata`
2. `Executive Summary`
3. `Previous Audit Delta`
4. `Current Iteration Snapshot`
5. `Work Item Analysis`
6. `SAFe Compliance Scorecard`
7. `Dimension Findings`
8. `Risks and Bottlenecks`
9. `Prioritized Recommendations`
10. `Evidence Gaps and Limitations`

### Required report content

Near the top of the report, include:
- project name
- team name
- workspace folder
- current iteration name
- current iteration start and finish dates
- audit date with timezone
- previous audit reference
- overall score and risk band

The `SAFe Compliance Scorecard` must include a table with:
- Dimension
- Score
- Evidence
- Notes

The recommendations section must be prioritized and actionable.

## Visualization policy

Use Mermaid when visualization adds value.

At minimum, include one Mermaid visualization when enough evidence exists, using one of:
- score breakdown
- state distribution
- backlog age / refinement trend
- audit-to-audit delta summary

Do not create chart image files.

## Output policy

- Write source reports as Markdown only
- Save reports under the target project's `audit/` directory
- Use `AUDIT_<date>_<time>.md`
- Do not generate PDFs
- Do not generate chart image artifacts
- Do not write source reports to `report/` or `temp/`

## Failure behavior

### Single-project mode

If the required ADO context cannot be resolved:
- stop
- report the failure explicitly
- do not improvise missing scope

### Batch mode

If one project fails:
- continue processing remaining valid `ado_*` projects
- record failed or skipped projects in the final batch summary
- do not let one failed project block the rest of the batch

### Missing evidence

When some evidence is missing but the audit can still proceed:
- continue in degraded mode
- record the missing evidence in `Evidence Gaps and Limitations`
- avoid fabricated conclusions

## Completion checklist

Before finishing, verify all of the following:
- the target is an `ado_*` workspace or `all-projects`
- the local `CLAUDE.md` was read
- the current active iteration was resolved
- the latest prior audit was reviewed
- the seven-dimension rubric was applied exactly once
- the report used the required section order
- the output is Markdown only
- no PDF or chart-image artifacts were generated
- batch mode never touched `git_*` workspaces
