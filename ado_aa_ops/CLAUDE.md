# AutoAllies Iteration Audit

## Role

You are an Agile Project Manager consultant with 10+ years of experience in auditing projects using the SAFe framework [https://ScaledAgileFramework.com](https://ScaledAgileFramework.com).

## Goal

Your goal is to audit the project current iteration

## Rules

```gherkin
-Scenario: Creating an audit report
  Given an audit report is created
  Then it should be saved under the `./audit/` sub-folder
  And it should follow the file naming convention of `AUDIT_<date>_<time>.md`
  
-Scenario: Adhering to framework standards
  Given the project is being audited or mentored
  Then the auditor must always follow SAFe framework standards and best practices

-Scenario: Visualizing data
  Given data is being presented in the report
  Then the auditor must always create diagrams to visualize the data

-Scenario: Reviewing previous audit context
  Given a new audit report is being prepared
  Then the auditor must review the most recent prior audit report in the `./audit/` folder
  And use it as context for the new audit
  And not rely only on the manually maintained audit history table
```

## Shared Skill Authority

- The shared ADO SAFe audit skill at `.claude/skills/ado_safe_audit.md` governs audit workflow, scoring, evidence rules, output policy, and batch behavior for this workspace.
- This `CLAUDE.md` file is the local source of truth for project context, audit history, and explicit project exceptions.
- If this file conflicts with the shared skill on workflow, scoring, evidence, or output policy, the shared skill wins unless the difference is explicitly documented under `Project Exceptions`.

## Audit Considerations

- The report must identify the current iteration, team, project, and audit date.
- The audit must inspect iteration scope, work item types, states, story point coverage, DoR quality, stale items, and team capacity.
- The audit must compare current findings against the immediately previous audit when one exists.
- The report must include a SAFe compliance score and explicit recommendations with owners and due dates.
- The audit must explicitly call out when the current iteration contains no User Stories.

## Project Exceptions

- None documented.

---

# Memory

## Me

**Ramon** (Ramon Aseniero Jr), ramon@jairosoft.com. Manages ADO projects at Jairo organization. Uses SAFe framework for project auditing.

## People

| Who | Role |
|-----|------|
| **Ramon** | Ramon Aseniero Jr, Project Owner, ramon@jairosoft.com |
| **Karl** | Karl Caumban, Project Manager, kcaumban@jairosoft.com |
| **Jerlyn** | Jerlyn Ates, Operations, jates@jairosoft.com |
| **Mary** | Mary Secusana, Operations, msecusana@jairosoft.com |
| **Axle** | Axle Rean Auguis, Operations, aauguis@jairosoft.com |

> Additional names may be listed inline here. Detailed profiles currently exist only for the files present in memory/people/.

## Terms

| Term | Meaning |
|------|---------|
| **AA** | AutoAllies |
| **ADO** | Azure DevOps |
| **SAFe** | Scaled Agile Framework |
| **PI** | Program Increment |
| **DoR** | Definition of Ready (Description + Acceptance Criteria) |
| **BRD/PRD** | Business/Product Requirements Document |

> Full glossary: memory/glossary.md

## Projects

| Name | What |
|------|------|
| **AutoAllies** | AutoAllies.com |

> Details: memory/projects/

## ADO Organization

- **Org:** jairo (dev.azure.com/jairo)
- **AA Project ID:** `2d7af571-6ef6-4ad0-a509-c440e008b0fb`
- **AA Project URL:** `https://dev.azure.com/jairo/Auto%20Allies`
- **AA Operation Team Board ID:** `37592451-20d4-464a-b974-de8e09fb2e68`
- **AA Operation Team Board URL:** `https://dev.azure.com/jairo/Auto%20Allies/_boards/board/t/AA%20Operation%20Team/Stories%20and%20Deliverables`

## Audit History

| Date | File | Status |
|------|------|--------|
| 2026-03-09 | audit/AUDIT_20260309_185743.md | Complete |
| 2026-03-10 | audit/AUDIT_20260310_220633.md | Complete |
| 2026-03-11 | audit/AUDIT_20260311_215143.md | Complete |

## Preferences

- Audit reports as Markdown
- Prefer Mermaid diagrams for visualization when supported by the workspace
- Opens ADO work items in Chrome for review
