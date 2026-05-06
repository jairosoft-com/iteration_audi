# Finance Team — Full Backlog Analysis
**Date:** May 5, 2026 (refreshed live May 5 PHT) | **Iteration:** 7.3 (Day 2 of 14) | **Analyst:** Claude Code

---

## Inventory Summary

| Category               | Backlog Level | Count  | Total SP / Effort  |
| ---------------------- | ------------- | ------ | ------------------ |
| PI Objectives          | Epic          | 2      | —                  |
| Features               | Feature       | 7      | 66 Effort pts      |
| Stories / Deliverables | Requirement   | 7      | 14 SP              |
| Tasks / Bugs           | Task          | 18     | 27.0 hrs remaining |
| **TOTAL**              |               | **34** |                    |

---

## 1. PI Objectives (EpicCategory)

| ID     | Title                                                      | Type         | State  | Iteration           | Notes                                          |
| ------ | ---------------------------------------------------------- | ------------ | ------ | ------------------- | ---------------------------------------------- |
| 202535 | Audit-Ready Financial Consolidation & Reporting Compliance | PI Objective | Active  | 2026-PI7 / Iter 7.1 | Correctly scoped to PI7; strong AC matrix                       |
| 200425 | End-to-End Automated Payroll System                        | PI Objective | **Closed** | **2026-PI6**     | ✅ **RESOLVED May 5 PHT** — PI6 stale artifact now closed       |

**Finding:** #200425 was a PI6 stale artifact (previously Active). **Closed May 6 00:33 UTC (= May 5 PHT).** PI6 PI Objective backlog debt cleared. Only #200431 (Feature) remains as the outstanding PI6 carryover.

---

## 2. Features (FeatureCategory)

| ID     | Title                                                    | State        | PI      | Effort | Tags               | Notes                                                                        |
| ------ | -------------------------------------------------------- | ------------ | ------- | ------ | ------------------ | ---------------------------------------------------------------------------- |
| 197064 | Jairosoft & JIT — BIR Annual Financial Report Compliance | Active       | PI7     | 10     | Gov't requirement  | Touched May 5 PHT (May 6 00:27 UTC); children active in sprint               |
| 200431 | Automated Gross-to-Net Calculation Logic                 | Active       | **PI6** | 10     | Payroll Automation | **STALE** — PI6 feature, not closed at PI boundary; last changed Mar 18      |
| 202410 | AutoAllies Overdue Invoice Payment                       | Active       | PI7     | 10     | —                  | No child stories in current sprint; risk of no-progress; last changed Apr 10 |
| 203033 | Set-up Employees Payroll Automation in PowerApp          | Active       | PI7     | 9      | Payroll Automation | Well-documented; #203677 child in sprint; last changed May 4                 |
| 203037 | Rates exploration with the new AI Roles and Titles       | Active       | PI7     | 9      | —                  | Touched May 5 PHT (May 6 00:25 UTC); active investigation                    |
| 203042 | Employees Annual Increase Proposal                       | **Approved** | PI7     | 9      | —                  | Ready to activate; child #203043 in sprint; last changed May 4               |
| 203697 | Jairosoft Autopay Set-up                                 | **Approved** | PI7     | 9      | —                  | Ready to activate; child #203704 in sprint; last changed May 4               |

**Findings:**
- **5 Active features simultaneously** — all assigned to Grace alone → high WIP at Feature level
- **#200431 (PI6 carryover):** Feature not closed at PI6 boundary. Still Active. Creates planning debt.
- **#202410 (AutoAllies):** No sprint children. Grace cannot make progress on this feature in Iter 7.3.
- **#203697 and #203042:** In Approved state; children are in active sprint — feature state should advance to Active.

---

## 3. Stories & Deliverables (RequirementCategory — Iter 7.3 Sprint)

| ID | Title | Type | State | SP | DoR | Changed | Notes |
|---|---|---|---|---|---|---|---|
| 203043 | Signed Annual Performance Evaluation Summary | User Story | Ready | 2 | PASS* | May 4 | *AC thin — 1 criterion only |
| 203638 | Submission of Cadac Policy | Spike | Ready | 1 | PASS | May 4 | Scope concern: HR/social item in Finance sprint |
| 203665 | AFS Portal Access | Spike | **Active** | 2 | PASS | **May 5** | **Grace started — Day 2 first mover** |
| 203677 | Attendance Integration | User Story | Ready | 3 | PASS | May 4 | System dependency risk; AC missing data source |
| 203684 | SEC AFS Submission | User Story | Ready | 2 | PASS | May 4 | External compliance deadline unconfirmed |
| 203704 | Set-up Payment Gateway | Enabler | Ready | 2 | PASS | May 4 | Tech enabler for Autopay Feature |
| 203719 | Salary Increase Implementation | User Story | New | 2 | PASS | May 4 | Staged to Iter 7.4 — correct |

**Sprint SP committed:** 12 (Iter 7.3) | **Closed:** 0 | **First Active:** #203665 (Day 2)

**Scope concern — #203638:**
Spike title is "Submission of Cadac Policy to Barangay Cabantian" (drug intervention program). This is an HR/compliance/social program item, not a Finance Team deliverable. Tagged "feedback." Warrants review: is this correctly parented under Finance, or should it be under HR Recruitment Team?

---

## 4. Tasks (TaskCategory — 18 items)

### 4a. Current Sprint Tasks (Iter 7.3 — 11 tasks)

| ID | Title | State | Remaining | Parent Context | Notes |
|---|---|---|---|---|---|
| 203044 | Compute and submit proposal for salary increase | New | 2 hrs | US #203043 / Feature #203042 | Straightforward |
| 203599 | Complete Claude CPN 4 Courses and get Certification | New | **10 hrs** | No parent story | **Training task — 10 hrs is largest task in sprint** |
| 203660 | Access and attached reference to BOD Proposal for Review | New | 0.5 hrs | Feature #203042 | Quick; do first |
| 203666 | Check with BIR Portal credentials | **Active** | 2 hrs | Spike #203665 | Grace in progress — correct state |
| 203667 | Upload AFS Document to AFS BIR Portal | New | 1 hr | Spike #203665 | Sequentially after #203666 |
| 203678 | Review and generate data in the portal | New | 3 hrs | US #203677 | Attendance system dependency |
| 203679 | Validate generated report for accuracy | New | 3.5 hrs | US #203677 | Largest task for #203677 |
| 203685 | Submit AFS Report 2026 to SEC | New | 1 hr | US #203684 | Deadline-sensitive |
| 203686 | Upload and file Docs (hard copy + SharePoint) | New | 1 hr | US #203684 | File management |
| 203705 | Review SB Account for payment | New | 1 hr | Enabler #203704 | Pre-payment gateway check |
| 203706 | Apply for Gcash Business Account | New | 2 hrs | Enabler #203704 | PH payment rail setup |

**Total Iter 7.3 task remaining work:** 27.0 hrs
**Grace capacity remaining (14-day sprint, 3 hrs/day):** 42 hrs total — ~36 hrs remaining on Day 2

**Capacity check:** 27 hrs task work + 12 SP story effort → within Grace's 36 hrs remaining. Feasible if no blockers.

**Concern — #203599 (Claude CPN 4 Courses, 10 hrs):**
- Training task with no parent story link
- 10 hrs = 37% of Grace's total sprint capacity (assuming 27 task hrs)
- No DoR linkage (TaskCategory items don't require DoR)
- Should be tracked separately or under a dedicated Learning Spike — not buried in TaskCategory

### 4b. Ghost / Stale Tasks (7 tasks — old iterations, never closed)

| ID | Title | State | Iteration | Last Changed | Age |
|---|---|---|---|---|---|
| 24391 | Encode data in excel file for Internal FS | New | xPI2\Sprint 3 | 2020-05-17 | **~6 yrs** |
| 24392 | Check and balance FS generated | New | xPI2\Sprint 3 | 2020-05-17 | **~6 yrs** |
| 24393 | Submit to Ma'am Karylle for checking and approval | New | xPI2\Sprint 3 | 2020-05-17 | **~6 yrs** |
| 24394 | Send approved FS to Bookkeeper for reference | New | xPI2\Sprint 3 | 2020-05-17 | **~6 yrs** |
| 158585 | Update resume of each billable employee | New | xPI13\Sprint 2 | 2024-02-17 | ~15 mos |
| 192750 | Review reports | Active | PI4\Iteration 4.4 | 2025-10-22 | ~6 mos |
| 194280 | Presentation | New | PI5\Iteration 5.3 | 2025-12-29 | ~4 mos |

**Action required:** All 7 should be closed or formally cancelled. #192750 is Active in PI4 — a ghost in active state is a data integrity issue.

---

## 5. Feature–Story Hierarchy Map

```
PI Objective #202535 (Audit-Ready Financial Consolidation)
└── Feature #197064 (BIR Annual Financial Report Compliance)
    ├── Spike #203665 (AFS Portal Access) ← ACTIVE Day 2
    │   ├── Task #203666 (BIR Portal credentials) ← ACTIVE
    │   └── Task #203667 (Upload AFS Document)
    └── User Story #203684 (SEC AFS Submission)
        ├── Task #203685 (Submit AFS Report to SEC)
        └── Task #203686 (Upload/file Docs)

Feature #203042 (Employees Annual Increase Proposal) [Approved]
├── User Story #203043 (Signed Annual Performance Evaluation) ← Iter 7.3
│   └── Task #203660 (BOD Proposal for Review)
├── Task #203044 (Compute salary increase proposal)
└── User Story #203719 (Salary Increase Implementation) ← Iter 7.4

Feature #203697 (Jairosoft Autopay Set-up) [Approved]
└── Enabler #203704 (Set-up Payment Gateway) ← Iter 7.3
    ├── Task #203705 (Review SB Account)
    └── Task #203706 (Apply for Gcash Business Account)

Feature #203033 (Payroll Automation in PowerApp)
└── User Story #203677 (Attendance Integration) ← Iter 7.3
    ├── Task #203678 (Review/generate data in portal)
    └── Task #203679 (Validate generated report)

Spike #203638 (Submission of Cadac Policy) ← SCOPE CONCERN
[No parent feature — possibly misrouted from HR team]

Task #203599 (Claude CPN 4 Courses) ← No parent story
[Training task — orphaned]

PI Objective #200425 (End-to-End Automated Payroll System) [PI6 — STALE]
└── Feature #200431 (Automated Gross-to-Net Calculation) [PI6 — STALE]

Feature #202410 (AutoAllies Overdue Invoice Payment) [PI7 — No sprint children]
Feature #203037 (Rates exploration — AI Roles) [PI7 — No sprint children]
```

---

## 6. Key Findings & Risks

| # | Finding | Severity | Item(s) |
|---|---|---|---|
| 1 | Ghost tasks 6 years old still in backlog as "New" | High | #24391–24394 |
| 2 | PI6 artifact #200431 still Active (PI closed) | High | #200431 | ~~#200425 closed May 5 PHT~~ |
| 3 | Feature #203042 and #203697 in Approved state but children are in Active sprint | Medium | #203042, #203697 |
| 4 | #203638 scope mismatch — HR/drug policy item in Finance sprint | Medium | #203638 |
| 5 | #203599 training task (10 hrs) orphaned — no parent story, eats 37% capacity | Medium | #203599 |
| 6 | #202410 (AutoAllies) has no Iter 7.3 children — zero sprint progress possible | Medium | #202410 |
| 7 | #192750 "Review reports" stuck Active in PI4 (Oct 2025) | Medium | #192750 |
| 8 | 5 Active features simultaneously, all assigned to Grace — Feature WIP too high | Medium | #197064, #200431, #202410, #203033, #203037 |
| 9 | #203677 AC missing attendance system name/data source | Low | #203677 |
| 10 | #203043 AC has only 1 criterion | Low | #203043 |

---

## 7. Live Refresh Delta (vs Initial Analysis)

| Item | Initial Fetch | Live Re-fetch | Delta |
|---|---|---|---|
| #200425 End-to-End Automated Payroll System | Active (PI6 STALE) | **Closed** | ✅ PI6 artifact resolved May 5 PHT |
| #197064 BIR Annual Financial Report Compliance | No note | Changed May 5 PHT (May 6 00:27 UTC) | Feature touched — likely linked to sprint activity |
| #203037 Rates exploration — AI Roles | Changed note | Changed May 5 PHT (May 6 00:25 UTC) confirmed | Active investigation |
| #203665 AFS Portal Access | Ready | Active | Grace started Day 2 (unchanged) |
| #203666 BIR Portal credentials | Task | Active | In progress (unchanged) |
| All other 29 items | — | No state change | Confirmed stable |

**D7 update:** Still 0 SP closed. #203665 Active is positive signal. No D7 impact until first closure.
**PI hygiene improvement:** #200425 closed removes one High-severity finding from the backlog.

---

## 8. Prioritized Action Items

1. **[Immediate] Close ghost tasks #24391–24394** — 6-year-old xPI2 tasks serve no purpose. Close with comment "Legacy — completed in 2020."
2. **[This week] Resolve remaining PI6 artifact** — ✅ #200425 closed May 5 PHT. Feature #200431 (Automated Gross-to-Net) still Active in PI6; merge scope into #203033 (Payroll PowerApp) or formally close.
3. **[Day 3] Advance Feature #203042 and #203697 to Active** — children are in active sprint; Feature state should match.
4. **[Day 3] Clarify #203638 scope** — Confirm if Cadac Policy spike belongs to Finance or HR Recruitment Team. Reroute if misassigned.
5. **[Day 3] Link #203599 (Claude training) to a Spike parent** — 10-hr training item needs proper hierarchy. Create a Learning Spike or attach to Feature #203037 (AI Rates exploration) if relevant.
6. **[Day 5] Confirm #203677 attendance system name** — Update AC with specific system (e.g., "HRIS portal") to unblock task execution.
7. **[Mid-sprint] Plan Iter 7.4 children for Feature #202410** — AutoAllies invoice feature has no sprint delivery path.
