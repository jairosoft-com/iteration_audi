# JIT Operation Team — Backlog Grooming & Refinement Session Agenda

- **Date proposed:** 2026-05-09 (Fri) or 2026-05-12 (Mon)
- **Duration:** 75 minutes
- **Attendees:** Ramon (PO), Armelita (PM / Product Owner), Teofilo (Training), Samantha (Ops)
- **Goal:** Assign BusinessValue to 15 unscored features, close/rebase 5 stale PI6 features, confirm 7.4 pipeline, fix #203250 SP gap to cross Low Risk threshold.
- **Source:** `ado_jit/audit/AUDIT_20260507_2308.md` (Iter 7.3, Day 4, Overall 79.5 — Moderate Risk, 0.5 pts below Low Risk)

---

## Pre-Session Checklist (Ramon / Armelita, day-of)

- [ ] Browser: open ADO Jairosoft Portfolio → JIT Operation Team board, backlog view grouped by Iteration Path
- [ ] Confirm Armelita + Teofilo calendar block (75 min)
- [ ] Pre-read this agenda + flagged work item IDs
- [ ] Verify Iteration 7.4 path exists in ADO (`Jairosoft Portfolio\2026-PI7\Iteration 7.4`)

---

## Backlog State Snapshot (2026-05-07)

| Bucket | Count | Notes |
|------:|------:|-------|
| Iter 7.3 stories (in flight) | 31 | 26 open + 5 closed; 63 SP committed; 11 SP closed |
| Iter 7.4 pre-loaded | 9 | 3 stories + 1 spike + 5 training items (~25 SP) |
| Iter 7.5 pre-loaded | 3 | 1 story + 2 spikes (~6 SP) |
| PI8 items | 1 | #200766 ODOO Spike (2 SP) |
| PI7 Features/Goals | 19 | 9 missing BusinessValue |
| PI8 Features | 1 | #196224 ODOO OpenEduCat — missing BV |
| PI6 stale Features | 5 | Intern cohorts + SAFe AI Courseware |
| Root (no iteration) | 2 | #191543 Rust + #203368 TESDA AI NC II |
| **Features missing BV** | **15/27** | **56% — biggest grooming gap** |
| Features missing AC | 2/27 | #191565, #203368 |

---

## Timebox

| Block | Min | Topic |
|------:|----:|-------|
| 1 | 10 | Quick 7.3 fixes — #203250 SP + Iteration Goal |
| 2 | 20 | Feature BusinessValue assignment (15 items) |
| 3 | 15 | PI6 stale feature decisions (5 items) |
| 4 | 5 | Root / unassigned items (2 items) |
| 5 | 15 | 7.4 pipeline review + capacity check |
| 6 | 5 | Feature AC gap fix (2 items) |
| 7 | 5 | D1 backlog hygiene discussion |

---

## Block 1 — Quick 7.3 Fixes (10 min)

Two actions that immediately cross Low Risk threshold:

| Action | Owner | Impact |
|--------|-------|--------|
| Add SP to **#203250** (Claude 4 Course Spike, Armelita) — set 1–2 SP | Armelita | D3 96.8 → 100.0; Overall 79.5 → ~80.0 (Low Risk) |
| Define **Iteration 7.3 Goal** in ADO | Armelita | Closes persistent R3 risk (missing across all JIT audits) |

**Suggested Iteration Goal:**
> *"Complete CSS NC II Server Training modules (DHCP → Server Security); execute EBET scholarship implementation (guidelines, MOU, trainer verification); run May marketing campaigns for Bubble MCC, Python, CSS Batch 4; deliver Claude 4 AI tech talk; maintain TESDA compliance through SAFe MCCs conversion."*

**Outcome:** Overall score crosses 80.0 → Low Risk band.

---

## Block 2 — Feature BusinessValue Assignment (20 min)

15 of 27 features/goals have no BusinessValue. BV drives backlog priority ranking. Assign live during session.

### PI7 Features — Missing BV (9 items, highest priority)

| ID | Title | Suggested BV | Rationale |
|----|-------|------------:|-----------|
| #203765 | CSS Batch 4 Class | 13–21 | Direct revenue; compare Batch 3 @ BV 21 |
| #203223 | Produce New TESDA MCC | 8–13 | Core business — new course offerings |
| #203163 | TESDA EBET Scholarship | 8–13 | Government funding channel |
| #202549 | ChatGPT TESDA MCC | 8–13 | New AI course; market demand |
| #202217 | Jairosoft Partnership with UIC for MCC | 8–13 | Institutional partnership; recurring value |
| #202966 | Jairosoft Partnership with HCDC for MCC | 8–13 | Same — institutional |
| #203369 | DNS jit.edu.ph | 5–8 | Infrastructure enabler, not direct revenue |
| #202192 | UM Main BSIT/BSMMA Interns April 2026 | 2–5 | Intern cohort — lower standalone BV |
| #202202 | MMCM Interns April 2026 | 2–5 | Same category |

### PI8/PI6/Root Features — Missing BV (6 items)

| ID | Title | Iter | Recommended Action |
|----|-------|------|--------------------|
| #196224 | ODOO OpenEduCat | PI8 | Assign BV (strategic SIS platform — likely 8–13) |
| #191565 | SAFe AI Native Courseware | PI6 | Assign BV + AC if rebasing; skip if closing (Block 3) |
| #198640 | UM CPE Interns Feb 2026 | PI6 | Likely close (cohort ended) — BV moot |
| #198641 | HCDC Interns Feb 2026 | PI6 | Same — likely close |
| #191543 | Rust Language Programming | Root | Assign BV + iteration if alive; close if abandoned |
| #203368 | TESDA AI Full-Qualification NC II | Root | Assign BV + AC + iteration (new, fresh May 6) |

**Working rule:** ≤1 min per feature. Ramon states BV; Armelita records in ADO. Use comparables: Batch 3 (BV 21), Assessment Center (BV 13), Python (BV 8), Interns (BV 2).

---

## Block 3 — PI6 Stale Feature Decisions (15 min)

5 features anchored to PI6 (closed PI). Decide: close, rebase, or archive.

| ID | Title | State | BV | Recommendation |
|----|-------|-------|---:|----------------|
| #198640 | UM CPE Interns February 2026 | Active | — | **Close** — Feb 2026 cohort is over |
| #198641 | HCDC Interns February 2026 | Active | — | **Close** — Feb 2026 cohort is over |
| #200104 | UM-Digos Interns | Active | 2 | **Close** if cohort completed; child #200771 (7.5 intern ceremony) covers remaining work |
| #200610 | UM-Matina Interns | Active | 2 | **Close** if cohort completed |
| #191565 | SAFe AI Native Courseware | New | — | **Rebase to PI8** if still planned; add AC + BV. Or **close** if superseded by ChatGPT MCC (#202549). |

**Outcome:** Zero PI6-anchored features. Clean PI6 → PI7 boundary.

---

## Block 4 — Root / Unassigned Items (5 min)

2 items at portfolio root with no iteration path:

| ID | Title | Changed | Decision |
|----|-------|---------|----------|
| #191543 | Introduction to Rust Language Programming | 2026-02-09 | Stale (3 months). Close if abandoned. Or assign PI8 + BV if course creation resumes. |
| #203368 | Apply for TESDA AI Full-Qualification NC II | 2026-05-06 | **Fresh but incomplete.** Missing AC + BV + iteration. Assign PI7 or PI8. Add 2-3 AC bullets: application timeline, required docs, TESDA approval criteria. |

**Outcome:** Zero root/unassigned items.

---

## Block 5 — Iteration 7.4 Pipeline Review (15 min)

7.4 is pre-loaded with 9 items (~25 SP). Review readiness and capacity.

### Pre-loaded Items

**User Stories (3 items, 6 SP):**

| ID | Title | SP | State | Assignee | DoR |
|----|-------|---:|-------|----------|-----|
| #200767 | UM Matina CPE Intern Final Demo & Certificates | 2 | New | Armelita | ✓ |
| #200768 | HCDC Interns Final Demo & Certificates | 2 | New | Armelita | ✓ |

**Spike (1 item):**

| ID | Title | SP | Assignee | DoR |
|----|-------|---:|----------|-----|
| #203243 | IT7.4 Tech Talk — AI Tools Demo | 2 | Armelita | ✓ |

**Teofilo Training Chain (5 items, 15 SP):**

| ID | Title | SP | Sequence |
|----|-------|---:|----------|
| #203805 | 4.1-1 Server Security & Reporting | 3 | First |
| #203806 | 4.1-2 Tools, Equipment & Testing Devices | 3 | Second |
| #203807 | 4.1-3 Personal Computer System & Specification | 3 | Third |
| #203808 | 4.1-4 Occupational Health & Safety Procedures | 3 | Fourth |
| #203809 | 4.1-5 Network Maintenance Task | 3 | Fifth |

**All items DoR ✓** — SP set, Description present, AC present.

### Capacity Check

| Contributor | 7.4 Items | SP | Notes |
|-------------|-------:|---:|-------|
| Teofilo | 5 Training | 15 | ~2 items/2 days pace = completes by Day 5–6 of 7.4 |
| Armelita | 2 US + 1 Spike | 6 | Intern demos are event-based; tech talk is time-boxed |
| Grace | TBD | — | No 7.4 items pre-loaded; confirm if new items expected |
| Samantha | TBD | — | No 7.4 items pre-loaded; social media / intern work likely |

**Total pre-loaded: 25 SP.** With Armelita's likely additions (marketing, enrollment), expect 30–40 SP committed.

### Questions for Session

1. **#203245** (titled "IT7.6 Tech Talk") is in Iter 7.5 path — should it move to 7.6?
2. Any new items expected for Samantha/Grace in 7.4?
3. Sprint goal candidate for 7.4: *"Complete Module 4 training chain (Server Security through Network Maintenance); execute intern cohort final demonstrations; deliver IT7.4 tech talk."*

---

## Block 6 — Feature AC Gap Fix (5 min)

Only 2 features missing Acceptance Criteria:

| ID | Title | Action |
|----|-------|--------|
| #191565 | SAFe AI Native Courseware | Add AC if rebasing (Block 3); skip if closing |
| #203368 | TESDA AI Full-Qualification NC II | Add 2-3 AC bullets: (a) TESDA application form submitted; (b) required documents complete per checklist; (c) TESDA approval confirmation received |

---

## Block 7 — D1 Backlog Hygiene Discussion (5 min)

D1 = 72.1 (31 current items / 43 total visible). 12 non-current items in future iterations are structural drag.

**Options:**
- **Accept drag** — these are legitimately planned future work (7.4/7.5/PI8). D1 improves naturally as 7.3 items close and 7.4 items become current.
- **Move low-confidence items** out of visible backlog if they won't execute this PI.
- **Key insight:** D1 is an audit planning metric, not a grooming failure. The 7.4 pipeline being pre-loaded is actually good practice.

**No action required** unless team wants to descope specific items.

---

## Post-Session Action Items

| Owner | Action | Block |
|-------|--------|-------|
| **Armelita** | Add SP (1–2) to #203250 (Claude 4 Spike) | B1 |
| **Armelita** | Define Iteration 7.3 Goal in ADO | B1 |
| **Armelita + Ramon** | Assign BV to 15 features per Block 2 table | B2 |
| **Ramon** | Close 4 PI6 intern features (#198640, #198641, #200104, #200610) | B3 |
| **Armelita** | Decide #191565 SAFe AI Courseware — close or rebase PI8 + add AC/BV | B3 |
| **Armelita** | Decide #191543 Rust — close or assign PI8 + BV | B4 |
| **Armelita** | Add AC + BV + iteration to #203368 TESDA AI NC II | B4/B6 |
| **Armelita** | Confirm 7.4 pipeline (9 items, ~25 SP) + Teofilo training sequence | B5 |
| **Armelita** | Fix #203245 iter path if should be 7.6 not 7.5 | B5 |
| **Armelita** | Define draft 7.4 Sprint Goal | B5 |

---

## Success Criteria

| Metric | Before | Target |
|--------|--------|--------|
| Overall Score | 79.5 (Moderate) | ≥ 80.0 (Low Risk) |
| Features with BusinessValue | 12/27 (44%) | ≥ 22/27 (81%) |
| Features with AC | 25/27 (93%) | 27/27 (100%) |
| PI6-anchored features | 5 | 0 (closed or rebased) |
| Root/unassigned items | 2 | 0 |
| #203250 SP gap | 0 SP | 1–2 SP → D3 = 100% |
| Iteration Goal defined | No | Yes |
| 7.4 pipeline confirmed | Informal | Reviewed + capacity-checked |

---

## References

- Last audit: `ado_jit/audit/AUDIT_20260507_2308.md` (Audit #53, Day 4, Overall 79.5)
- Skill authority: `.claude/skills/ado_safe_audit.md`
- Local context: `ado_jit/CLAUDE.md`
- ADO Project ID: `666bb99a-6acd-4999-bb34-efd0e4ea90dc`
- ADO Team ID: `b25e3129-6272-4e54-a3ff-f1ef3c8eeb2c`
- Backlog: `Microsoft.RequirementCategory` — Stories and Deliverables
