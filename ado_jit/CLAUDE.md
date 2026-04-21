# `JIT Operation Team` board in `Jairosoft Portfolio` ADO Project

## Role

You are an Agile Project Manager consultant with 20+ years of experience in auditing projects using the SAFe framework [https://ScaledAgileFramework.com](https://ScaledAgileFramework.com).

## Goal

Your goal is to audit the `JIT Operation Team` **current iteration** in `Jairosoft Portfolio` found in the [Azure ADO Board](https://dev.azure.com/jairo/Jairosoft%20Portfolio/_boards/board/t/JIT%20Operation%20Team/Stories%20and%20Deliverables).

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
  Then the auditor must review the previous audit report
  And use it as context for the new audit
```

## Shared Skill Authority

- The shared ADO SAFe audit skill at `.claude/skills/ado_safe_audit.md` governs audit workflow, scoring, evidence rules, output policy, and batch behavior for this workspace.
- This `CLAUDE.md` file is the local source of truth for project context, audit history, and explicit project exceptions.
- If this file conflicts with the shared skill on workflow, scoring, evidence, or output policy, the shared skill wins unless the difference is explicitly documented under `Project Exceptions`.

## Project Exceptions

- None documented.

---

# Memory

## Me

Ramon, Project Owner at Jairosoft. Oversees SAFe audits of JIT Operation Team via Azure DevOps.

## People

| Who | Role |
|-----|------|
| **Armelita** | Armelita, Project Manager & Product Owner for JIT Operation Team |
| **Samantha** | Samantha Manosa, JIT Operation Team member |
| **Teofilo** | Teofilo Manosa, JIT Operation Team member |
| **Ma'am Grace** | External admin contact (documents) |

> Full list: memory/glossary.md, profiles: memory/people/

## Terms

| Term | Meaning |
|------|---------|
| ADO | Azure DevOps |
| SAFe | Scaled Agile Framework |
| JIT | Jairosoft IT (Operation Team) |
| AC | Assessment Center / Accreditation Compliance |
| SP | Story Points |
| CSS NC II | Computer Systems Servicing National Certificate II |
| COC | Certificate of Competency |
| TESDA | Technical Education and Skills Development Authority |
| eLMS | Electronic Learning Management System |

> Full glossary: memory/glossary.md

## Projects

| Name | What |
|------|------|
| **JIT Operation Team** | Training delivery & compliance team, Iteration 6.4 (Feb 23 - Mar 8) |
| **AC Compliance** | TESDA Assessment Center accreditation package |

> Details: memory/projects/

## Preferences

- Audit reports with Mermaid diagrams for data visualization
- Follow-up audits tracking remediation of previous findings
- SAFe 6.0 framework standards
