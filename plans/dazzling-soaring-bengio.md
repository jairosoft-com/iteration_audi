# JIT Operation Team — Backlog Grooming & Refinement Plan

## Context

JIT is at Iter 7.3 Day 4, scoring **79.5 (Moderate Risk)** — 0.5 pts below Low Risk threshold. The audit series shows steady improvement (72.1 → 75.2 → 76.7 → 79.5). The team's story-level DoR compliance is strong (100%), but **feature/goal-level refinement is weak**: 56% of features lack BusinessValue, 5 features are anchored to stale PI6, and 2 items sit at root with no iteration. This grooming session addresses the feature-level debt while preserving 7.3 momentum.

**Source data:** Live ADO snapshot 2026-05-07. Audit: `ado_jit/audit/AUDIT_20260507_2308.md`.

---

## Deliverable

Write `plans/PLAN_jit_backlog_grooming_session_20260507.md` — a timeboxed grooming agenda (modeled on `plans/PLAN_otp_backlog_refinement_session_20260506.md`).

---

## Session Structure (75 min proposed)

### Block 1 — Quick 7.3 Fixes (10 min)
Two immediate actions that cross the Low Risk threshold:

| Action | Impact |
|--------|--------|
| Add SP to #203250 (Claude 4 Spike, Armelita) — set 1–2 SP | D3 → 100.0; Overall → ~80.0 (Low Risk) |
| Define Iteration 7.3 Goal | Closes persistent R3 risk across all JIT audits |

Suggested sprint goal: *"Complete CSS NC II Server Training modules (DHCP→Server Security); execute EBET scholarship implementation; run May marketing campaigns for Bubble MCC, Python, CSS Batch 4; deliver Claude 4 AI tech talk."*

### Block 2 — Feature BusinessValue Assignment (20 min)
15 of 27 features/goals lack BV. This is the biggest refinement gap.

**Missing BV — PI7 features (9 items, prioritize):**

| ID | Title | Suggested BV Range | Rationale |
|----|-------|--------------------|-----------|
| #202217 | UIC Partnership for MCC | 8–13 | Institutional partnership; recurring value |
| #202549 | ChatGPT TESDA MCC | 8–13 | New course offering; market demand |
| #202966 | HCDC Partnership for MCC | 8–13 | Same as UIC — institutional |
| #203163 | TESDA EBET Scholarship | 8–13 | Government funding channel |
| #203223 | Produce New TESDA MCC | 8–13 | Core business expansion |
| #203369 | DNS jit.edu.ph | 5–8 | Infrastructure enabler |
| #203765 | CSS Batch 4 Class | 13–21 | Direct revenue (compare Batch 3 @ BV 21) |
| #202192 | UM Main Interns April 2026 | 2–5 | Intern cohort — lower standalone BV |
| #202202 | MMCM Interns April 2026 | 2–5 | Same category |

**Missing BV — PI8/PI6/Root (6 items):**

| ID | Title | Iter | Action |
|----|-------|------|--------|
| #196224 | ODOO OpenEduCat | PI8 | Assign BV (strategic SIS platform) |
| #191565 | SAFe AI Native Courseware | PI6 stale | Assign BV + AC, or close |
| #198640 | UM CPE Interns Feb 2026 | PI6 stale | Assign BV; likely close (cohort ended) |
| #198641 | HCDC Interns Feb 2026 | PI6 stale | Same — cohort ended |
| #191543 | Rust Language Programming | Root | Assign BV + iteration, or close |
| #203368 | TESDA AI NC II | Root | Assign BV + AC + iteration |

### Block 3 — PI6 Stale Feature Decisions (15 min)
5 features still anchored to PI6 (closed PI). Each needs: close, rebase to PI7/PI8, or archive.

| ID | Title | State | BV | Recommendation |
|----|-------|-------|---:|----------------|
| #200104 | UM-Digos Interns | Active | 2 | Close if cohort completed; child #200771 in 7.5 covers remaining ceremony |
| #200610 | UM-Matina Interns | Active | 2 | Close if cohort completed |
| #198640 | UM CPE Interns Feb 2026 | Active | — | Close — Feb 2026 cohort is over |
| #198641 | HCDC Interns Feb 2026 | Active | — | Close — Feb 2026 cohort is over |
| #191565 | SAFe AI Native Courseware | New | — | Rebase to PI8 if still planned; add AC + BV. Or close. |

### Block 4 — Root / Unassigned Items (5 min)

| ID | Title | Action |
|----|-------|--------|
| #191543 | Intro to Rust Language Programming | Changed Feb 2026 — stale. Close or assign PI8+ with BV. |
| #203368 | TESDA AI Full-Qualification NC II | Fresh (May 6) but missing AC + BV + iteration. Assign PI7 or PI8. Add AC. |

### Block 5 — 7.4 Pipeline Review (15 min)
7.4 is pre-loaded with 12 items (~25 SP). Confirm readiness:

**Stories (3 items, 6 SP):**
- #200767 UM Matina Intern Demo (2 SP, DoR ✓)
- #200768 HCDC Intern Demo (2 SP, DoR ✓)
- Plus #203243 Tech Talk Spike (2 SP, DoR ✓)

**Teofilo Training Chain (5 items, 15 SP):**
- #203805 → #203806 → #203807 → #203808 → #203809 (Module 4.1-1 through 4.1-5)
- All DoR ✓. Confirm sequential order matches Teofilo's pace (~2 items / 2 days).

**Capacity check:** Teofilo 15 SP training + Armelita stories/spikes + intern ceremonies. Grace/Samantha items TBD.

**Questions for session:**
- Who owns #200767 and #200768 execution? (Armelita assigned — confirm)
- Should #203245 (titled "IT7.6 Tech Talk") move from 7.5 → 7.6 path to match its title?
- Any new items expected for 7.4 from Samantha/Grace?

### Block 6 — Feature AC Gap Fix (5 min)
Only 2 features missing AC — quick patches:

| ID | Title | Action |
|----|-------|--------|
| #191565 | SAFe AI Native Courseware | Add AC if rebasing; skip if closing |
| #203368 | TESDA AI Full-Qualification NC II | Add 2-3 AC bullets (application timeline, required docs, TESDA approval criteria) |

### Block 7 — D1 Backlog Hygiene Discussion (5 min)
D1 = 72.1 (31 current / 43 total visible). The 12 non-current items in future iterations are structural drag. Options:
- Accept D1 drag as planned work (no action — they're legitimately future)
- Move low-confidence items out of visible backlog if they won't execute this PI
- This is informational — D1 is an audit metric, not a grooming failure

---

## Post-Session Outputs

- [ ] **Armelita** — add SP to #203250 (30-sec fix, crosses Low Risk threshold)
- [ ] **Armelita** — define Iter 7.3 Goal in ADO
- [ ] **Armelita + Ramon** — assign BV to 15 features (Block 2 table)
- [ ] **Ramon** — close 4 PI6 intern features (#198640, #198641, #200104, #200610) if cohorts completed
- [ ] **Armelita** — decide #191565 SAFe AI Courseware (close or rebase + AC)
- [ ] **Armelita** — decide #191543 Rust (close or assign PI8)
- [ ] **Armelita** — add AC + BV + iteration to #203368 TESDA AI NC II
- [ ] **Armelita** — confirm 7.4 pipeline (12 items, ~25 SP) and Teofilo's training sequence
- [ ] **Armelita** — fix #203245 iter path if it should be 7.6 not 7.5

---

## Success Criteria

| Metric | Before | Target |
|--------|--------|--------|
| Features with BusinessValue | 12/27 (44%) | ≥22/27 (81%) |
| Features with AC | 25/27 (93%) | 27/27 (100%) |
| PI6-anchored features | 5 | 0 (closed or rebased) |
| Root/unassigned items | 2 | 0 |
| #203250 SP gap | 0 SP | 1–2 SP (D3 → 100%) |
| Iteration Goal defined | No | Yes |
| 7.4 pipeline confirmed | Informal | Reviewed + capacity-checked |

---

## Verification

After session execution:
1. Run `/ado-safe-audit ado_jit` — confirm Overall ≥ 80.0 (Low Risk) if #203250 SP added
2. Re-query `wit_list_backlog_work_items` for FeatureCategory — confirm 0 PI6, 0 root items
3. Spot-check 5 features for BV field populated
4. Confirm 7.4 iteration path exists and contains expected 12 items

---

## Files

| File | Action |
|------|--------|
| `plans/PLAN_jit_backlog_grooming_session_20260507.md` | **Create** — final grooming agenda (copy of this plan, cleaned for session use) |
| `ado_jit/CLAUDE.md` | **Update** — refresh Projects table (Iter 7.3 not 6.4) after session |
