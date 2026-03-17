# Administration Team board in Jairosoft FINOPS ADO Project

## Role

You are an Agile Project Manager consultant with 20+ years of experience in auditing projects using the SAFe framework [https://ScaledAgileFramework.com](https://ScaledAgileFramework.com).

## Goal

Your goal is to audit the `Administration Team Board` current iteration in `Jairosoft FINOPS` found in the [Azure ADO Board](https://dev.azure.com/jairo/Jairosoft%20FINOPS/_boards/board/t/Administration%20Team/Stories%20and%20Deliverables).

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

---

# Memory

## Me
Ramon (ramon@jairosoft.com). SAFe audit consultant for Jairosoft FINOPS Administration Team.

## People
| Who | Role |
|-----|------|
| **Mark** | Mark Colina (mcolina@jairosoft.com), sole Admin Team member, handles all work items |
| **Ramon** | Ramon, project owner / audit requestor |
-> Full list: memory/glossary.md, profiles: memory/people/

## Terms
| Term | Meaning |
|------|---------|
| FINOPS | Jairosoft FINOPS — the ADO project |
| Admin Team | Administration Team (ADO team ID: a38a9c02) |
| PI | Program Increment (SAFe cadence unit, ~5-6 iterations) |
| IP Sprint | Innovation & Planning sprint at end of each PI |
| WSJF | Weighted Shortest Job First — SAFe prioritization |
| CADAC | Training certification program at UIC |
| BFP FSIC | Bureau of Fire Protection - Fire Safety Inspection Certificate |
| PhilGeps | Philippine Government Electronic Procurement System |
| VECO | Visayan Electric Company (Cebu power utility) |
| JIT | Jairosoft IT (subsidiary/brand) |
| TESDA | Technical Education and Skills Development Authority |
| BIR | Bureau of Internal Revenue (PH tax authority) |
-> Full glossary: memory/glossary.md

## Projects / ADO IDs
| Name | What |
|------|------|
| **PI 6** | Current Program Increment (Jan-Apr 2026), Iterations 6.1-6.6 |
| **Iteration 6.4** | Current sprint (Feb 23 - Mar 8, 2026) |
| **ADO Project ID** | e0bb302f-40f9-46c3-8164-6f1acb317d63 |
| **Admin Team ID** | a38a9c02-07ab-483d-a1e3-aff54e19e603 |
-> Details: memory/projects/

## Teams in FINOPS
| Team | ID |
|------|-----|
| FINOPS Program Team | da58789d-dfdf-4cc3-880d-8a2091bced9b |
| Finance Team | 1f4b45fa-82e8-4a36-aedc-6c1bc8f51070 |
| Administration Team | a38a9c02-07ab-483d-a1e3-aff54e19e603 |
| HR Recruitment Team | 248f59a6-372c-4b74-8129-9eaf260f211e |

## Backlog Levels
| Level | ADO Category | Work Item Types |
|-------|-------------|-----------------|
| Epics & Objectives | Microsoft.EpicCategory | Epic |
| Features & Goals | Microsoft.FeatureCategory | Feature |
| Stories & Deliverables | Microsoft.RequirementCategory | User Story, Defect, Issue |
| Tasks | Microsoft.TaskCategory | Task, Bug |

## Recurring Audit Findings (Persistent Issues)
- ~~No capacity planning configured~~ **RESOLVED** (Mar 9, 2026) — Mark set 8h/day "Documentation" activity. Note: activity type could be broader.
- No Story Points on User Stories (every audit)
- Single assignee (Mark Colina) on all items — bus factor risk
- Features lack Business Value / Effort for WSJF
- Stories lack acceptance criteria
- Typos in work item titles
- Overall SAFe compliance: ~42/100

## Audit History
| # | File | Date |
|---|------|------|
| 1 | AUDIT_20260225_2104 | Feb 25, 2026 |
| 2 | AUDIT_20260304_0000 | Mar 4, 2026 |
| 3 | AUDIT_20260304_2157 | Mar 4, 2026 |
| 4 | AUDIT_20260305_2132 | Mar 5, 2026 |
| 5 | AUDIT_20260306_2216 | Mar 6, 2026 |
| 6 | AUDIT_20260309_1556 | Mar 9, 2026 |
| 7 | AUDIT_20260309_1730 | Mar 9, 2026 |
| 8 | AUDIT_20260316_0226 | Mar 16, 2026 |

## Preferences
- Audit reports saved to `./audit/` folder
- Mermaid diagrams for data visualization
- SAFe 6.0 framework standards
