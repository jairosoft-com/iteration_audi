# Colina Health — Backlog Grooming Session Agenda

- **Date proposed:** 2026-05-08 (Fri) or 2026-05-11 (Mon)
- **Duration:** 90 minutes (extend to 120 if PI6 rebase decisions stack)
- **Attendees:** Ramon (PO), Karl (PM / Dev Lead), Paul Coronia (Dev), Asnari Pacalna (Dev), Luzmibel (QA), Jaszmeine (Design)
- **Goal:** Close DoR gaps in active 7.3, drain PI7-root unassigned, decide PI6/PI3/PI4 stale items, queue 7.4 commit list, fix DoD gaps from Day 3 audit.
- **Source review:** `git_cc_dev/audit/AUDIT_20260506_0909.md` (Iter 7.3, Day 3, UPS 69.1, Yellow); live ADO backlog snapshot 2026-05-06.

---

## Pre-Session Checklist (Ramon, day-of)

- [ ] Browser: open ADO Jairosoft Portfolio, "Stories and Deliverables" backlog, group by Iteration Path
- [ ] Confirm Karl + dev pair (Paul, Asnari) calendar block
- [ ] Pre-read this agenda + flagged work item IDs
- [ ] Pull current ADO roster to reconcile `Kyaa-A` / `pcoronia` membership (audit R2)
- [ ] Confirm 7.4 iteration path exists in ADO (`Jairosoft Portfolio\2026-PI7\Iteration 7.4`); create if missing

---

## Backlog State Snapshot (2026-05-06, top 50 reviewed)

| Bucket | Count | Notes |
|------:|------:|-------|
| Active 7.3 | 14 | In-flight — audit-tracked |
| PI7 root, no iteration | 3 | AB#200194, AB#202676, AB#202677 — must assign 7.4–7.6 |
| 2026-PI6 stale | 8 | AB#187405–#200334 — rebase or close |
| PI 3 / PI 4 / Iter 2.6 | 6 | AB#182486, #183185, #185860, #191145, #191239, #192218 — ancient |
| Unassigned (portfolio root) | 31 | No PI tag — many High Prio Defects |
| Missing SP | 36 | Largest DoR gap |
| Missing Description | 15 | DoD blocker |
| Missing AC | 7 | DoD blocker |

---

## Timebox

| Block | Min | Topic |
|------:|----:|-------|
| 1 | 5 | Context + intent |
| 2 | 15 | 7.3 DoD fixes (in-flight gap from audit Day 3) |
| 3 | 15 | PI7-root triage — AB#200194, AB#202676, AB#202677 |
| 4 | 20 | High-Prio Defect drain (10 unassigned, no SP) |
| 5 | 15 | PI6 stale-rebase decisions (8 items) |
| 6 | 10 | Ancient PI3 / PI4 / Iter 2.6 decisions (6 items) |
| 7 | 10 | 7.4 commit list + capacity sanity check |

---

## Block 1 — Context (5 min)

- **Iter 7.3 status:** Day 3 of 14, UPS 69.1 (Yellow). ICS 95.0 (Green). HCI 72 (Yellow).
- **Backlog debt:** 31 items at portfolio root with no iteration. 36 of top 50 lack SP. 15 lack Description.
- **Roster gap (R2 from audit):** `Kyaa-A` and `pcoronia` are active GitHub authors but not in ADO team roster. `kcaumban` has zero 7.3 GitHub activity. Reconcile before 7.4 commit.
- **GitHub token issue:** Resolved per Day 3 audit (data_mode: full). Carry-forward concession lifted.

---

## Block 2 — 7.3 DoD Fixes (15 min)

Audit flagged Day 2 remediation not acted on. Patch in-place, no scope change.

| ID | Title | Missing | Action |
|----|-------|---------|--------|
| AB#197582 | [MAR][View Reports] Slow loading of medications | `System.Description` | Add 1-2 sentence description summarizing perf scope (table size, render path) |
| AB#198096 | [MAR Report][Calendar] Filters persist after closing | `System.Description` | Add description summarizing filter-state-on-close behavior |

**Outcome:** ICS DoD dimension lifts from 85.7% → 100%. UPS gains ~+2.5 pts.

**Side fixes (parallel):**

- AB#202592 — move iter path 7.2 → Closed (PR#174 merged Apr 30)
- AB#203672 — assign iter 7.3 OR move to backlog
- FE#191 PR title — change `[Ticket: 197582]` → `[AB#197582]` before merge

---

## Block 3 — PI7-Root Triage (15 min)

3 items live at PI7 root with no iteration assignment. Must land in 7.4–7.6 or get downgraded.

| ID | Title | Type | State | SP | Decision |
|----|-------|------|------|---:|----------|
| AB#200194 | [Workflow][Update Medication Log] First letter remains in Administered field | Defect | New | 2 | High Prio (Pri 1). Assign 7.4. Add Description. |
| AB#202676 | Timezone Based on User Preference or Location | User Story | New | — | Estimate SP, split if >5. Assign 7.4 or 7.5. Owner: pcoronia. |
| AB#202677 | Frontend Weekly Medication Generation with Deferred Saving | User Story | New | — | Estimate SP. Likely 8+ (split required). Assign 7.5. Owner: pcoronia. |

### Discovery questions

- AB#202676: scope = browser-detected vs explicit user pref vs admin-set? Server-side conversion of stored timestamps?
- AB#202677: "deferred saving" = client-side state + bulk POST? Conflict resolution if MAR table mutated by another session?

### Proposed split for AB#202677 (likely needed)

- S1: Local weekly grid state model (hold edits before commit) — 3 SP
- S2: Bulk POST endpoint + idempotency — 3 SP
- S3: Conflict resolution UI on stale read — 2 SP
- S4: Discard/reset path — 1 SP

---

## Block 4 — High-Prio Defect Drain (20 min)

10+ defects tagged `High Prio Defects` sit at portfolio root with no iteration, no SP, often no Description.

### Triage table (estimate SP live; assign or close)

| ID | Title | Has Desc | Has AC | Recommended |
|----|-------|:--------:|:------:|-------------|
| AB#197814 | Add New Medication / Dietary Order — no validation indicator | ✗ | ✓ | Add desc; SP=1; assign 7.4 |
| AB#197834 | Orders > Med View History — Dosage without unit | ✗ | ✓ | Add desc; SP=1; assign 7.4 |
| AB#197858 | MAR Scheduled — pagination missing scheduled meds | ✗ | ✓ | Add desc; SP=2; assign 7.4 |
| AB#198094 | MAR Scheduled — deleted med orders still visible | ✗ | ✓ | Add desc; SP=3; assign 7.4 (data integrity) |
| AB#198098 | MAR PRN — no warning on daily admin exceed | ✓ | ✓ | SP=2; assign 7.4 |
| AB#198115 | MAR — frequency change not reflected after Orders edit | ✗ | ✓ | Add desc; SP=3; assign 7.4 (parent of AB#199309 family) |
| AB#198365 | Lab/Imaging — inconsistent Delete modal label | ✗ | ✓ | Add desc; SP=1; assign 7.5 (cosmetic) |
| AB#200246 | Admin Orders — Med/Status dropdown not responsive (iPad) | ✓ | ✓ | SP=2; assign 7.5 |
| AB#184114 | Orders > Dietary — first letter not capitalized | ✗ | ✓ | SP=1; assign 7.5 OR close (cosmetic, age 2024) |
| AB#185152 | Lab Results — unsupported file type validation | ✗ | ✓ | Add desc; SP=2; assign 7.5 |

**Working rule:** ≤5 min description per item. Defer cosmetic-only to 7.6 if 7.4–7.5 fills.

---

## Block 5 — PI6 Stale Rebase (15 min)

8 items still tagged `2026-PI6` despite PI7 being current. Decide: rebase to 7.4–7.6, downgrade priority, or close.

| ID | Title | Type | State | SP | Recommended |
|----|-------|------|-------|---:|-------------|
| AB#187405 | Delete Functionality for all tables | User Story | New | — | Split (per-table). Estimate. Rebase 7.5–7.6. |
| AB#187406 | MAR — Generate MAR Report | User Story | New | — | High value (Prio-hotfix tag). Rebase 7.4. Estimate. |
| AB#192275 | Workflow — Scheduled Frequency Restriction Warning | User Story | New | 3 | Add Description. Rebase 7.4. |
| AB#193926 | Automatic Date Formatting on Input Fields | User Story | New | 5 | Rebase 7.5. Confirm scope across all date pickers. |
| AB#196454 | Colina Intake/Output Tab | Design | Grooming | — | Jaszmeine: complete grooming. Rebase to 7.5 once design ready. |
| AB#197981 | Colina — Task Feature Enhancement | Design | Grooming | — | Same — design-led. Rebase post-grooming. |
| AB#199506 | MAR — PRN Med Interval & Max Dose Enforcement | User Story | New | 2 | Rebase 7.4. Companion to AB#198098. |
| AB#200334 | MAR Workflow — View Schedule in Custom Date | User Story | Grooming | 3 | Rebase 7.5. |

**Outcome:** Zero `2026-PI6` items still anchored to closed PI.

---

## Block 6 — Ancient Items (PI3 / PI4 / Iter 2.6) (10 min)

| ID | Title | Last Iter | Decision |
|----|-------|-----------|----------|
| AB#182486 | Plotting Data — Add Reminders Feature | PI 3 | Close OR rebase 7.6 (CR-Unicorn P1 tag — verify still wanted) |
| AB#183185 | Orders — Tab-Specific PDF list | Iter 2.6 (IP) | Tag says "ClosedbutnotyetQA" — verify and close |
| AB#185860 | Dashboard — Total Orders Donut Chart | PI 3 | Close (UI may already redesigned) OR rebase |
| AB#191145 | Timezone — Tab PDFs | PI 4 | Sister to AB#202676 timezone story — merge OR close |
| AB#191239 | All Pages — Time picker retain current time | PI 3 | Confirm still buggy; rebase 7.5 OR close |
| AB#192218 | CSAT / NPS Spike | PI 4 | Spike — close if no longer pursuing measurement effort |

**Working rule:** if no live customer pain in last 6 months → close. Tag "stale-grooming-2026-05" before bulk close for audit trail.

---

## Block 7 — Iteration 7.4 Commit (10 min)

- **Window:** 2026-05-18 → 2026-05-31 (verify path in ADO; create if missing)
- **Capacity:** 2 active devs (Kyaa-A, pcoronia). Assume 8 hr/day × 10 working days × 2 = 160 hr → ~25–30 SP committed.
- **Sprint goal candidate:** *"Close MAR data-integrity defect cluster, ship timezone foundation, drain unassigned high-prio defects."*

### Commit candidate list (target ≤ 30 SP, ≤ 80% capacity)

- ✅ AB#200194 — Med Log first-letter defect (2 SP) — from Block 3
- ✅ AB#202676 — Timezone foundation (estimate Block 3) — likely 5 SP
- ✅ AB#187406 — Generate MAR Report (Block 5; rebase + estimate)
- ✅ AB#192275 — Frequency Restriction Warning (3 SP) — Block 5
- ✅ AB#199506 — PRN Interval & Max Dose (2 SP) — Block 5
- ✅ AB#197858 — MAR pagination defect (2 SP) — Block 4
- ✅ AB#198094 — Deleted med orders persist (3 SP) — Block 4
- ✅ AB#198098 — PRN daily-admin warning (2 SP) — Block 4
- ✅ AB#198115 — Frequency change not reflected (3 SP) — Block 4
- ➕ Carry-over from 7.3 if any unfinished (likely Enabler 29 SP if not started)
- ⚠ Enabler debt: AB#202584–AB#202603 (29 SP across 8 items) — if 7.3 doesn't start them, queue earliest as 7.4 cap-room allows OR descope 2 lowest-value enablers

---

## Outputs (post-session, owner action items)

- [ ] **Karl** — reconcile ADO roster (add Kyaa-A, pcoronia OR document contractor relationship)
- [ ] **Asnari** — patch Description on AB#197582, AB#198096, plus 7+ defect descs from Block 4
- [ ] **Paul** — estimate SP on AB#202676, AB#202677; split AB#202677 into 4 stories
- [ ] **Ramon** — close-or-rebase 6 ancient items (Block 6); tag with `stale-grooming-2026-05`
- [ ] **Ramon** — rebase 8 PI6 items to 7.4/7.5/7.6 paths (Block 5)
- [ ] **Jaszmeine** — finish design on AB#196454, AB#197981 before re-anchor
- [ ] **Karl** — create iteration path 7.4 in ADO (May 18 – May 31) if missing
- [ ] **Karl** — move 7.4 commit list (Block 7) into iteration 7.4 path
- [ ] **Ramon** — schedule 7.4 planning meeting on 2026-05-15 (Fri)

---

## Success Criteria

- 7.3 DoD gap: 0 (was 2) — AB#197582 + AB#198096 patched
- PI7-root items: 0 (was 3) — all assigned to 7.4–7.6
- 2026-PI6 anchored items: 0 (was 8)
- Ancient PI 2/3/4 items: closed or rebased — bucket count = 0
- 7.4 sprint goal stated, ≤ 30 SP committed, ≤ 80% capacity
- ADO roster reconciled with GitHub identities (R2 closed)

---

## References

- Last audit: `git_cc_dev/audit/AUDIT_20260506_0909.md` (Day 3, UPS 69.1)
- Skill authority: `.claude/skills/git_iteration_audit/SKILL.md`
- Local context: `git_cc_dev/CLAUDE.md`
- ADO Project ID: `666bb99a-6acd-4999-bb34-efd0e4ea90dc`
- ADO Team ID: `66cdeb09-df38-4c3e-9418-0ed0d68c39f2`
- Backlog: `Microsoft.RequirementCategory` — Stories and Deliverables
