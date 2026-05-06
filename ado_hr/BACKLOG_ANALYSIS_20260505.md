# HR Recruitment Team — Full Backlog Analysis
**Date:** May 5, 2026 (live data May 5 PHT) | **Iteration:** 7.3 (Day 2 of 14) | **Analyst:** Claude Code

---

## Inventory Summary

| Category               | Backlog Level | Count  | Total SP / Effort   |
| ---------------------- | ------------- | ------ | ------------------- |
| PI Objectives          | Epic          | 3      | —                   |
| Features               | Feature       | 16     | —                   |
| Stories / Deliverables | Requirement   | 17 + 1 spike | 32 SP         |
| Tasks                  | Task          | 51 + 1 orphan | 28.5 hrs remaining |
| **TOTAL**              |               | **72** |                     |

---

## 1. PI Objectives (EpicCategory)

| ID     | Title                                                                        | Type         | State   | Iteration          | Notes                                                         |
| ------ | ---------------------------------------------------------------------------- | ------------ | ------- | ------------------ | ------------------------------------------------------------- |
| 200673 | Accelerating Market-Ready Velocity through Integrated Engineering & Growth Hiring | PI Objective | **New** | 2026-PI6       | ⚠️ PI6 artifact — never activated; last changed Mar 10, 2026 |
| 200583 | Streamline & Execute Annual Health Screenings                                | PI Objective | **New** | 2026-PI6           | ⚠️ PI6 artifact — never activated; last changed Mar 10, 2026 |
| 200581 | Digital HR Transformation & Workflow Automation                              | PI Objective | **New** | 2026-PI6           | ⚠️ PI6 artifact — never activated; last changed Mar 9, 2026  |

**Finding:** All 3 PI Objectives remain in **"New"** state at PI6 scope. None were activated during PI6 nor closed at PI6 boundary. PI6 has ended and PI7 is in Iteration 7.3. No PI7 PI Objective exists for HR team — the highest planning layer is absent for the current PI.

---

## 2. Features (FeatureCategory)

### 2a. PI6 Features — Stale (9 items)

| ID     | Title                                       | State        | PI           | Last Changed   | Notes                                                                       |
| ------ | ------------------------------------------- | ------------ | ------------ | -------------- | --------------------------------------------------------------------------- |
| 191712 | Employee 2026 Annual Medical Check up       | **Active**   | PI6          | Mar 9, 2026    | PI6 feature; PI7 child #202099 active in sprint — feature not promoted      |
| 195668 | Recruit Bubble Trainer                      | **Active**   | PI6          | **May 4, 2026**| Recently touched; child #201273 in sprint; feature never promoted to PI7   |
| 196947 | Employees 2026 Annual Evaluation            | **Active**   | PI6 Iter 6.2 | Mar 9, 2026    | PI6 feature; 6 APE stories in current sprint — PI transition hygiene missed |
| 197387 | Communication Skills Training               | **Active**   | PI6          | Mar 9, 2026    | PI6 stale; child #197939 in sprint; de-committed in 6.5 but feature left open |
| 197685 | Hire Bubble Developer                       | **Active**   | PI6          | **May 4, 2026**| Recently touched; no sprint children in 7.3                                |
| 197687 | Hire DevOps Engineer                        | **Active**   | PI6          | Mar 16, 2026   | PI6 stale; child #202093 in sprint under this feature                      |
| 197691 | Teof Growth Plan                            | **Estimation**| PI6         | **May 4, 2026**| Recently touched; no AC; no sprint children                                |
| 198053 | Hire Senior Technical Lead for SSI          | **Active**   | PI6          | Mar 9, 2026    | PI6 feature; 3 Sr. Tech Lead stories active in 7.3 sprint                 |
| 200059 | Hire Sales & Mktg. for JIT                 | **Active**   | PI6 Iter 6.4 | Mar 16, 2026   | PI6 stale (Iter 6.4); children #203063 and #203534 in current sprint       |

### 2b. PI7 Features — Active/Approved (5 items)

| ID     | Title                                  | State          | PI      | Effort | Last Changed  | Notes                                                                    |
| ------ | -------------------------------------- | -------------- | ------- | ------ | ------------- | ------------------------------------------------------------------------ |
| 202341 | 2025 Sick Leave Conversion             | **Active**     | PI7     | —      | May 4, 2026   | ✅ Correctly scoped PI7; child #202349 in sprint                        |
| 197048 | Employee Engagement 2nd Quarter 2026   | **Approved**   | PI7     | —      | May 4, 2026   | Spike #203629 (Incentives) semantically linked; Feature not yet Active  |
| 197385 | Hire Tech Sales from Manila            | **Approved**   | PI7     | —      | Apr 6, 2026   | Child #203534 in sprint; Feature state should advance to Active         |
| 203708 | CADAC Compliance                       | **Approved**   | PI7 Iter 7.2 | —  | May 4, 2026   | Approved in 7.2; no 7.3 sprint children; stalled at Approved state     |
| 192163 | Leave Credits Automation               | **Active**     | **None** | —     | Mar 9, 2026   | ⚠️ No PI assignment (root path); floating feature with no planning context |

### 2c. Features in Estimation (2 items)

| ID     | Title             | State          | PI   | Last Changed  | Notes                                          |
| ------ | ----------------- | -------------- | ---- | ------------- | ---------------------------------------------- |
| 197331 | Jerlyn Growth Plan | **Estimation** | PI7  | Apr 6, 2026   | No AC; no sprint children; not ready for work  |
| 197690 | Ressa Growth Plan  | **Estimation** | PI7  | Apr 6, 2026   | No AC; no sprint children; not ready for work  |

**Findings:**
- **9 PI6 features still Active or Estimation** — PI6 is over; these were never promoted to PI7 or formally closed at PI boundary. Creates severe planning debt and inflates WIP at Feature level.
- **10 Active features total** (9 PI6 + 1 PI7), all assigned to Almera alone → Feature WIP = 10 on a 1-person team.
- **#192163 (Leave Credits Automation):** No PI path assignment — scoping artifact that was never prioritized into a PI.
- **#197048 and #197385 in Approved with sprint children** — Feature state should advance to Active.
- **#197691, #197331, #197690:** Features in Estimation with no AC documented. Not ready for planning.

---

## 3. Stories & Deliverables (RequirementCategory — Iter 7.3 Sprint)

| ID     | Title                                              | Type       | State     | SP | DoR   | Changed  | Notes                                            |
| ------ | -------------------------------------------------- | ---------- | --------- | -- | ----- | -------- | ------------------------------------------------ |
| 203825 | Client Interview \| Sr. Tech Lead - Maraon, Belleo | User Story | Ready     | 2  | PASS  | May 5    | New in 7.3; Day 1 addition; 5 tasks             |
| 203829 | APE - Babael, Samantha (2nd Month PEF)             | User Story | Ready     | 1  | PASS  | May 5    | New in 7.3; 3 tasks; deadline May 15            |
| 203533 | Sr. Tech Lead - Beltran, Ken Henson                | User Story | Ready     | 2  | PASS  | May 4    | Technical & hiring decision; 3 tasks            |
| 202887 | Sr. Tech Lead - Barua, Marlo                       | User Story | Ready     | 2  | PASS  | May 4    | 3 tasks; hiring decision pending                |
| 203063 | Sales & Mktg. - Angel Dorothy Abina                | User Story | Ready     | 2  | PASS  | May 4    | 5 tasks; full interview pipeline                |
| 202093 | LinkedIn DevOps Engr. Hiring                       | User Story | Ready     | 2  | PASS* | May 4    | *Description references "Iter 6.5" target — stale |
| 203534 | LinkedIn Tech Sales from Manila Hiring (7.3)       | User Story | Ready     | 1  | PASS* | May 4    | *Description references "Iter 7.1" target — stale |
| 203535 | APE - Caumban, Karl Jordan (Sprint 7.3)            | User Story | Ready     | 2  | PASS  | May 4    | 3 tasks; PEF → 201 file pipeline               |
| 203536 | APE - Tayao, Almera Kleer (Sprint 7.3)             | User Story | Ready     | 2  | PASS  | May 4    | Self-evaluation; 1 task (follow up PEF from manager) |
| 202104 | APE - Rommel Senillo - Summary - PI7               | User Story | Ready     | 2  | PASS  | Apr 30   | 3 tasks; PEF → 201 file pipeline               |
| 203537 | APE - Calvin John Dalino - Summary (7.3)           | User Story | Ready     | 2  | PASS  | May 4    | 3 tasks; PEF → 201 file pipeline               |
| 203538 | APE - Ryan Vince Castillo (Sprint 7.3)             | User Story | Ready     | 2  | PASS  | May 4    | 3 tasks; PEF → 201 file pipeline               |
| 202099 | Annual Medical Check-up \| Cebu Employees - PI7    | User Story | Ready     | 1  | PASS  | Apr 30   | 3 tasks; make-up schedule coordination         |
| 202349 | Finance Reporting & Export                         | User Story | Ready     | 2  | PASS  | Apr 30   | 2 tasks; includes 3-hr SL Conversion finalize  |
| 201273 | LinkedIn Bubble Trainer Hiring - Interview         | User Story | Ready     | 2  | PASS  | Apr 30   | 4 tasks; #195668 Feature still PI6             |
| 197939 | Communication Skills Proposals Summary Presentation| User Story | Ready     | 2  | PASS  | Apr 30   | 1 task (present to BOD); #197387 Feature PI6   |
| 203629 | HR Discussion on Employees Incentives, Scaling of Bonuses | Spike | Ready | 3 | PASS | **May 6 UTC** | Most recently changed; tagged "feedback"; 1 task |

**Sprint SP committed:** 32 SP (17 stories + 1 spike) | **Closed:** 0 | **Active:** 0 | **Day 2 — no story started yet**

**DoR notes:**
- #202093 and #203534: AC passes, SP set, but story descriptions reference past iterations (6.5 and 7.1 respectively). Minor stale description debt.
- #203536 (Almera self-evaluation): Only 1 task; lightweight but valid — supervisor completes PEF.

---

## 4. Tasks (TaskCategory — Iter 7.3)

### 4a. Sprint Tasks by Parent Story

| Parent Story | Tasks | State | Total Remaining | Notes |
|---|---|---|---|---|
| #203825 Client Interview Maraon | 203820, 203821, 203822, 203823, 203824 | All New | 2.75 hrs | Endorse → Schedule → Prepare → Track → Collect Feedback |
| #203533 Sr. Tech Lead Beltran | 202331, 202333, 202334 | All New | 2.25 hrs | Technical + CEO Final interview pipeline |
| #202887 Sr. Tech Lead Barua | 202336, 202338, 202339 | All New | 2.25 hrs | Technical + CEO Final interview pipeline |
| #203063 Sales & Mktg. Angel | 203058, 203059, 203060, 203061, 203062 | All New | 1.25 hrs | Full 5-step interview pipeline |
| #202093 LinkedIn DevOps Hiring | 200558, 200560, 200561 | All New | 2.75 hrs | Resume review + shortlist + job post |
| #203534 LinkedIn Tech Sales Hiring | 200719, 200720, 200721, 200722, 200723 | All New | 3.5 hrs | Full interview pipeline for Manila hire |
| #203535 APE Caumban | 193646, 193647, 200639 | All New | 1.0 hr | PEF create → submit BOD → save 201 |
| #203536 APE Almera | 203065 | New | 0.25 hrs | Follow up PEF from manager |
| #202104 APE Rommel | 200649, 200650, 200651 | All New | 1.0 hr | PEF create → submit BOD → save 201 |
| #203537 APE Calvin | 200663, 200664, 200665 | All New | 1.0 hr | PEF create → submit BOD → save 201 |
| #203538 APE Ryan | 200656, 200657, 200658 | All New | 1.0 hr | PEF create → submit BOD → save 201 |
| #202099 Medical Check-up Cebu | 201253, 201254, 201255 | All New | 0.75 hrs | Notify → Monitor → Confirm completion |
| #202349 Finance Reporting | 202350, 202351 | All New | **3.25 hrs** | Finalize SL list (3 hrs) + email Finance |
| #201273 LinkedIn Bubble Trainer | 200712, 200713, 200715, 200716 | All New | 1.75 hrs | Shortlist → Initial → Final → Decision |
| #197939 Comm Skills Presentation | 199990 | New | 1.0 hr | Present to Grace/BOD |
| #203629 HR Incentives Spike | 203819 | New | 1.0 hr | Discussion with Grace from Finance perspective |
| #203829 APE Babael Samantha | 203826, 203827, 203828 | All New | 1.75 hrs | Prepare PEF → Send to Armie → Collect |

**Total sprint tasks:** 51 tasks | **All New** (0 Active, 0 Done) | **Total remaining: ~28.5 hrs**

### 4b. Orphaned Task

| ID     | Title                                   | State | Remaining | Parent | Notes                                      |
| ------ | --------------------------------------- | ----- | --------- | ------ | ------------------------------------------ |
| 203605 | Complete Claude CPN 4 Courses and get Certification | New | — | **None** | Training task; no parent story; no remaining hrs set; similar to Finance team issue |

**Capacity check:**
Almera capacity (14-day sprint, est. ~3 hrs/day task work): ~42 hrs total, ~40 hrs remaining Day 2.
28.5 hrs task remaining + 32 SP story work → feasible within capacity if no blockers and Almera maintains last PI's velocity (34 SP closed in 6.5).

---

## 5. Feature–Story Hierarchy Map

```
PI Objective #200673 (Market-Ready Velocity Hiring) [PI6 — NEW — STALE]
├── Feature #198053 (Hire Senior Technical Lead for SSI) [PI6 Active — STALE]
│   ├── User Story #202887 (Sr. Tech Lead — Barua, Marlo) ← Iter 7.3
│   │   ├── Task #202338 (Technical Interview w/ Dev. Team)
│   │   ├── Task #202339 (Final Interview with CEO & JP)
│   │   └── Task #202336 (Secure Final hiring decision)
│   ├── User Story #203533 (Sr. Tech Lead — Beltran, Ken Henson) ← Iter 7.3
│   │   ├── Task #202333 (Technical Interview w/ Dev. Team)
│   │   ├── Task #202334 (Final Interview with CEO & JP)
│   │   └── Task #202331 (Secure Final hiring decision)
│   └── User Story #203825 (Client Interview — Maraon, Belleo) ← Iter 7.3 [NEW Day 1]
│       ├── Task #203820 (Endorse Candidates to Client)
│       ├── Task #203821 (Schedule Client Interview)
│       ├── Task #203822 (Notify and Prepare Candidates)
│       ├── Task #203823 (Track Interview Completion)
│       └── Task #203824 (Collect Client Feedback)
├── Feature #197685 (Hire Bubble Developer) [PI6 Active — STALE]
│   └── [No sprint children in 7.3]
├── Feature #195668 (Recruit Bubble Trainer) [PI6 Active]
│   └── User Story #201273 (LinkedIn Bubble Trainer Hiring — Interview) ← Iter 7.3
│       ├── Task #200712 (Shortlist Qualified Candidates)
│       ├── Task #200713 (Conduct Initial Interview)
│       ├── Task #200715 (Facilitate Final Interview with CEO)
│       └── Task #200716 (Secure Final hiring decision)
└── Feature #197690 (Ressa Growth Plan) [PI7 Estimation — No sprint children]

Feature #200059 (Hire Sales & Mktg. for JIT) [PI6 Iter 6.4 Active — STALE]
├── User Story #203063 (Sales & Mktg. — Angel Dorothy Abina) ← Iter 7.3
│   ├── Task #203058 (Coordinate and schedule interview)
│   ├── Task #203059 (Conduct the initial interview)
│   ├── Task #203060 (Endorse for Technical Interview)
│   ├── Task #203061 (Endorse Final Interview with CEO)
│   └── Task #203062 (Secure Final hiring decision)
└── User Story #203534 (LinkedIn Tech Sales from Manila Hiring) ← Iter 7.3
    ├── Task #200719 (Shortlist Qualified Candidates)
    ├── Task #200720 (Conduct Initial Interview)
    ├── Task #200721 (Facilitate Technical Interview)
    ├── Task #200722 (Facilitate Final Interview with CEO)
    └── Task #200723 (Secure Final hiring decision)

PI Objective #200583 (Streamline Annual Health Screenings) [PI6 — NEW — STALE]
└── Feature #191712 (Employee 2026 Annual Medical Check up) [PI6 Active — STALE]
    └── User Story #202099 (Annual Medical Check-up | Cebu Employees — PI7) ← Iter 7.3
        ├── Task #201253 (Send schedule notification to employees)
        ├── Task #201254 (Monitor attendance to make-up schedule)
        └── Task #201255 (Confirm all employees completed check-up)

PI Objective #200581 (Digital HR Transformation) [PI6 — NEW — STALE]
└── Feature #192163 (Leave Credits Automation) [Active — NO PI assignment]
    └── [No sprint children in 7.3]

Feature #196947 (Employees 2026 Annual Evaluation) [PI6 Iter 6.2 Active — STALE]
├── User Story #202104 (APE — Rommel Senillo) ← Iter 7.3
│   ├── Task #200649 (Create PEF interpretation)
│   ├── Task #200650 (Submit to BOD and Managers)
│   └── Task #200651 (Save to 201 files)
├── User Story #203535 (APE — Caumban, Karl Jordan) ← Iter 7.3
│   ├── Task #193646 (Submit to BOD and Managers)
│   ├── Task #193647 (Save to 201 files)
│   └── Task #200639 (Create PEF interpretation)
├── User Story #203536 (APE — Tayao, Almera Kleer) ← Iter 7.3 [Self-eval]
│   └── Task #203065 (Follow up accomplished PEF from Manager)
├── User Story #203537 (APE — Calvin John Dalino) ← Iter 7.3
│   ├── Task #200663 (Create PEF interpretation)
│   ├── Task #200664 (Submit to BOD and Managers)
│   └── Task #200665 (Save to 201 files)
├── User Story #203538 (APE — Ryan Vince Castillo) ← Iter 7.3
│   ├── Task #200656 (Create PEF interpretation)
│   ├── Task #200657 (Submit to BOD and Managers)
│   └── Task #200658 (Save to 201 files)
└── User Story #203829 (APE — Babael, Samantha — 2nd Month PEF) ← Iter 7.3 [NEW Day 1]
    ├── Task #203826 (Prepare PEF of Sam)
    ├── Task #203827 (Send out PEF to Ma'am Armie)
    └── Task #203828 (Collect accomplished PEF)

Feature #197387 (Communication Skills Training) [PI6 Active — STALE]
└── User Story #197939 (Communication Skills Proposals Summary Presentation) ← Iter 7.3
    └── Task #199990 (Present to Ma'am Grace/BOD re: Canvassed vendors)

Feature #197687 (Hire DevOps Engineer) [PI6 Active — STALE]
└── User Story #202093 (LinkedIn DevOps Engr. Hiring) ← Iter 7.3
    ├── Task #200558 (Review resumes based on job requirements)
    ├── Task #200560 (Prepare shortlist of qualified applicants)
    └── Task #200561 (Prepare Job Post Content for DevOps Engr. hiring)

Feature #202341 (2025 Sick Leave Conversion) [PI7 Active] ✅
└── User Story #202349 (Finance Reporting & Export) ← Iter 7.3
    ├── Task #202350 (Finalize the 2025 SL Conversion list and computation) [3 hrs]
    └── Task #202351 (Email to Finance for release)

Feature #197048 (Employee Engagement Q2 2026) [PI7 Approved]
└── Spike #203629 (HR Discussion on Incentives, Scaling of Bonuses) ← Iter 7.3
    └── Task #203819 (Discussion with Ma'am Grace from Finance perspective)

Feature #197385 (Hire Tech Sales from Manila) [PI7 Approved]
[Sprint child is #203534 — also claimed by #200059; ambiguous parent]

Feature #203708 (CADAC Compliance) [PI7 Approved Iter 7.2]
└── [No sprint children in 7.3]

Feature #197331 (Jerlyn Growth Plan) [PI7 Estimation — No sprint children]

Task #203605 (Complete Claude CPN 4 Courses) ← ORPHANED — No parent story
```

---

## 6. Key Findings & Risks

| # | Finding | Severity | Item(s) |
|---|---|---|---|
| 1 | 3 PI Objectives stuck as "New" in PI6 — entire top planning layer is stale | Critical | #200673, #200583, #200581 |
| 2 | 9 PI6 Features still Active/Estimation — PI6 ended months ago; no PI boundary cleanup | High | #191712, #195668, #196947, #197387, #197685, #197687, #197691, #198053, #200059 |
| 3 | No PI7 PI Objective exists for HR — team operates with no PI-level outcome target | High | — |
| 4 | Feature WIP = 10 Active simultaneously, all on Almera alone — extreme overload at Feature level | High | All Active features |
| 5 | #192163 (Leave Credits Automation) — Active Feature with no PI assignment; floating with no delivery context | Medium | #192163 |
| 6 | All 17 sprint stories in "Ready", 0 Active on Day 2 — no story started | Medium | Sprint |
| 7 | #197048 and #197385 in Approved state but sprint children are active — Feature state should advance | Medium | #197048, #197385 |
| 8 | #203605 training task orphaned — no parent story, no remaining work hours set | Medium | #203605 |
| 9 | #202093 and #203534 story descriptions reference old iterations (6.5 and 7.1) — stale target language | Low | #202093, #203534 |
| 10 | #203534 ambiguous parent — could belong to #200059 (PI6 Active) or #197385 (PI7 Approved) | Low | #203534 |
| 11 | 4 APE stories repeat identical 3-task template — PEF interpret → submit BOD → save 201 file; functional but formulaic | Info | #202104, #203535, #203537, #203538 |
| 12 | Bus factor = 1 — Almera handles all 17 stories, 51 tasks, and 1 spike alone | Structural | Ongoing |

---

## 7. Prioritized Action Items

1. **[Immediate] Create PI7 PI Objective for HR team** — Three stale PI6 PI Objectives with no PI7 replacement leaves the team with no outcome target for the current PI. Draft a PI7 objective covering hiring, APE completion, and 2025 SL Conversion.
2. **[This sprint] Close or promote all 9 PI6 features** — Each should either be:
   - Closed (if all work completed): #197685, #191712 (medical check-ups done), #197387 (pending proposal), #196947 (APE in progress — promote to PI7)
   - Promoted to PI7 path: #198053, #195668, #197687, #200059 (still have active sprint stories)
3. **[Day 3] Advance Features #197048 and #197385 to Active** — Children are in active sprint; Feature state should match.
4. **[Day 3] Set iteration path for #192163 (Leave Credits Automation)** — Assign to PI7 or close if de-scoped. Cannot be planned without a PI.
5. **[Day 3] Start first story — set at least 1 story to Active** — All 17 at "Ready" on Day 2 is a yellow signal. Almera should begin the highest-priority item (recommend #203825 Client Interview Maraon — deadline-sensitive as it involves external client scheduling).
6. **[Day 3] Link #203605 (Claude training) to a parent** — Create a Learning Spike or link to a Feature (e.g., #197048 Employee Engagement or #197331 Growth Plans).
7. **[Day 5] Update stale descriptions on #202093 and #203534** — Change "within Iteration 6.5" and "within Iteration 7.1" to "within Iteration 7.3" to maintain DoR quality.
8. **[PI Boundary] Resolve PI6 PI Objectives** — Close #200673, #200583, #200581 with comments noting which work was completed vs. deferred. Clears backlog debt at Epic level.
