# OTP Project

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
  Then the auditor must review the previous audit report
  And use it as context for the new audit
```

## Audit Considerations

-The team has accepted that Grace is the single assignee for all work items in this project

---

# Memory

## Me
**Ramon** (Ramon Aseniero Jr), ramon@jairosoft.com. Manages ADO projects at Jairo organization. Uses SAFe framework for project auditing.

## People
| Who | Role |
|-----|------|
| **Ramon** | Ramon Aseniero Jr, project owner, ramon@jairosoft.com |
| **Grace** | Sole assignee for all OTP work items (accepted by team) |
> Full list: memory/glossary.md, profiles: memory/people/

## Terms
| Term | Meaning |
|------|---------|
| **OTP** | Office of the President — ADO project (SAFe audited) |
| **JIT** | JIT — another ADO project in Jairo org |
| **SSI** | SSI — project needing a Principal Software Engineer |
| **ADO** | Azure DevOps |
| **SAFe** | Scaled Agile Framework |
| **PI** | Program Increment |
| **DoR** | Definition of Ready (Description + Acceptance Criteria) |
| **BRD/PRD** | Business/Product Requirements Document |
> Full glossary: memory/glossary.md

## Projects
| Name | What |
|------|------|
| **OTP** | Office of the President, current: Iteration 6.5 (Mar 9 – Mar 22, 2026), SAFe audited |
| **JIT** | Separate ADO project in Jairo org |
| **SSI** | Project hiring a Principal Software Engineer |
> Details: memory/projects/

## ADO Organization
- **Org:** jairo (dev.azure.com/jairo)
- **OTP Project ID:** e7739905-28a3-4ae1-9173-7f6cd13b3494
- **JIT Project ID:** f169a7d0-b2e3-40b1-9e63-9c7e556d5100
- **OTP Team:** OTP Team

## Audit History
| # | Date | File | Iteration | Status |
|---|------|------|-----------|--------|
| A1 | Feb 24, 2026 | AUDIT_20260224_221243 | 6.4 (Day 2) | Initial audit — 10 findings |
| A2 | Feb 26, 2026 | AUDIT_20260226_231628 | 6.4 (Day 4) | Follow-up — 7 resolved, 2 partial, 1 unresolved |
| A3 | Mar 4, 2026 | AUDIT_20260304_221209 | 6.4 (Day 10) | 8 resolved, new scope creep finding (#200069) |
| A4 | Mar 5, 2026 | AUDIT_20260305_214659 | 6.4 (Day 11) | Stalled — 0 SP closed in 2 days, deadline breach risk |
| A5 | Mar 6, 2026 | AUDIT_20260306_221741 | 6.4 (Day 12) | Critical — 3-day stall, AC deadline breached (#199524) |
| A6 | Mar 9, 2026 | AUDIT_20260309_225751 | 6.5 (Day 1) | Opening audit — 10 items stranded in 6.4, capacity -33% |
| A7 | Mar 10, 2026 | AUDIT_20260310_205034 | 6.5 (Day 2) | 9/10 stranded items moved to 6.5, scope explosion (39+ SP vs 28 hrs) |
| A8 | Mar 11, 2026 | AUDIT_20260311_205139 | 6.5 (Day 3) | First 0-critical/0-high audit; 6 findings resolved (best day); DoR 83%; 5 tasks closed |
| A9 | Mar 12, 2026 | AUDIT_20260312_135439 | 6.5 (Day 4) | #199524 2nd deadline breach, #178753 365-day anniversary, 2 HIGH findings |
| A10 | Mar 16, 2026 | AUDIT_20260316_223241 | 6.5 (Day 8) | Mid-sprint: 22 SP effective (63%), #178753 Resolved, #199524 Closed, 6 stories pending closure |
| A11 | Mar 17, 2026 | AUDIT_20260317_211159 | 6.5 (Day 9) | Record day: 5 stories closed, #178753 fully Closed (370 days), 18 SP credited (46%), 100% DoR |
| A12 | Mar 18, 2026 | AUDIT_20260318_213500 | 6.5 (Day 10) | 25 SP credited (64%), 31 SP effective (79%), #199577 + #200074 Closed, 95% sprint goal probability |

## Preferences
- Audit reports as Markdown
- Mermaid diagrams for visualization (rendered via matplotlib)
- Opens ADO work items in Chrome for review
