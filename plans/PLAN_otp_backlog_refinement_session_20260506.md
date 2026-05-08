# OTP Backlog Refinement Session — Agenda

- **Date proposed:** 2026-05-08 (Thu) or 2026-05-09 (Fri)
- **Duration:** 90 minutes (extend to 120 if Chippens needs deep split)
- **Attendees:** Ramon (PO), Grace (sole assignee / scribe)
- **Goal:** Cut PI7 refinement debt from 42% → ≥70% and clear DoR gaps in active 7.3, then queue 7.4 + critical PI8 features.
- **Source review:** see `ado_otp/audit/` history (last A13, 2026-03-22) and backlog snapshot in this session

---

## Pre-Session Checklist (Ramon, day-of)

- [ ] Browser: open ADO OTP project, "Backlog" view, group by Feature
- [ ] Confirm Grace's calendar block 90 min, no daily-driver interrupts
- [ ] Pre-read this agenda + flagged work item IDs below
- [ ] Have BRD/PRD references for Chippens (highest BV) on hand

---

## Timebox

| Block | Min | Topic |
|------:|----:|-------|
| 1 | 5 | Context + intent: why we're refining today |
| 2 | 15 | 7.3 DoR fixes (in-flight) |
| 3 | 25 | Refine #201708 Chippens Inventory (highest BV, PI7, zero stories) |
| 4 | 15 | Refine #199535 Adam H1B/Green Card (immigration timeline) |
| 5 | 10 | Refine #200075 Due Process / sister to #200073 (DOLE legal) |
| 6 | 10 | Stale-epic decisions: #178743, #191886, #191943 |
| 7 | 10 | Iteration 7.4 commit list + capacity sanity check |

---

## Block 1 — Context (5 min)

- PI7 status: 7.3 mid-flight (Day 3/14). PI7 needs 7.4–7.6 plans.
- Refinement debt: 5 of 12 PI7 features have any refined stories. Target by end of session: 8/12.
- Single-assignee model: Grace. All splits sized for her 1.5 hr/day capacity.

---

## Block 2 — 7.3 DoR Fixes (15 min)

3 active stories have weak Acceptance Criteria. Patch in-place, no scope change.

| ID | Title | SP | Current AC | Target AC additions |
|----|-------|---:|-----------|---------------------|
| #202912 | Fabrication of Signage | 2 | "Safety measures…; brgy compliant" | (a) Materials BOM signed; (b) brgy permit reference number; (c) photo evidence of safety gear |
| #202913 | Installation of Street Signage | 2 | "Installed Street signage" | (a) GPS pin of install; (b) photo before/after; (c) JIT marketing sign-off |
| #203589 | Akira Letter of Invitation | 2 | "Accomplished invitation letter for Japan Embassy" | (a) Required fields list (sponsor company, dates, purpose, financial guarantor); (b) signed PDF; (c) embassy submission receipt |

**Outcome:** DoR moves 4/7 → 7/7 stories on 7.3.

---

## Block 3 — #201708 Chippens Inventory System (25 min)

- **Feature:** #201708 (PI7, Pri 2, BV **15** — highest in OTP)
- **State:** New, zero stories, zero refinement
- **Risk:** Highest-value feature in PI7 currently invisible to delivery

### Discovery questions

1. Who is the user/owner of Chippens inventory? (Operations? Procurement?)
2. What's tracked? (SKUs, location, cost basis, supplier)
3. Build vs buy? (Custom app, Excel-graduation, off-the-shelf SaaS)
4. Integration: does it talk to FINOPS or stand alone?
5. Hard deadline?

### Proposed story split (draft — adjust live)

- **S1:** Inventory schema + master SKU list (define data model) — 2 SP
- **S2:** Initial stock count + baseline upload — 3 SP
- **S3:** Daily stock-in/stock-out workflow + form — 3 SP
- **S4:** Re-order alerts + threshold rules — 2 SP
- **S5:** Monthly reconciliation report (Grace-runnable) — 2 SP

**Total:** ~12 SP across 3 iterations. Anchor S1 in 7.4, S2–S3 in 7.5, S4–S5 in 7.6.

---

## Block 4 — #199535 Adam H1B / Green Card Renewal (15 min)

- **Feature:** #199535 (PI8, BV 10), zero stories
- **Risk:** Immigration filings have non-negotiable USCIS deadlines. PI8 starts 2026-06-29 — only 8 weeks out. Lawyer engagement lead-time ≥4 weeks.

### Discovery questions

1. Filing window opens / closes when?
2. Existing H1B expiration date?
3. Attorney already engaged? Which firm?
4. Premium processing or standard?
5. Documents already collected vs still pending from Adam?

### Proposed story split

- **S1:** Confirm USCIS filing window + lock attorney — 1 SP
- **S2:** Collect Adam's documents (passport, I-94, employment letters) — 2 SP
- **S3:** Employer support docs (LCA, I-129, RFE response template) — 3 SP
- **S4:** File petition + premium processing fee — 2 SP
- **S5:** Track receipt notice + biometrics — 1 SP

**Action:** Pull S1 forward into 7.4 (this PI) — don't wait for PI8. Visa lead-time risk is high.

---

## Block 5 — #200075 Due Process Legal Phase (10 min)

- **Feature:** #200075 (PI7, BV 9), zero stories
- **Sister story:** #200073 already pinned to 7.4 — covers Notice/RKS Form 5/COE
- **Question:** Is #200075 redundant with #200073, or does it cover separate scope (e.g., severance computation, quitclaim execution, post-separation grievance)?

**Decision needed:** Merge #200075 into #200073 OR split #200075 into 2-3 distinct stories (severance calc, quitclaim signing, grievance protocol).

---

## Block 6 — Stale Epic Decisions (10 min)

3 epics still "Active" but anchored to expired iterations.

| Epic | Last Iter | Decision Required |
|------|-----------|-------------------|
| #178743 Holy Trinity Back Lot | PI 3 (2024) | Rebase to PI7 (one live child #178746→#203864 in 7.6) **OR** close epic, lift child to standalone |
| #191886 Mabolo Occupancy Permit | PI4 | Close — verify no open obligation **OR** add story to revive |
| #191943 Employee 201 File Digitization | PI 4 | **Pri 1** — either decompose into PI7/PI8 or downgrade priority |

---

## Block 7 — Iteration 7.4 Commit (10 min)

- **Window:** 2026-05-18 → 2026-05-31 (need to create iteration in ADO)
- **Capacity:** Grace 1.5 hr/day × 10 working days = ~15 hr
- **Sprint goal candidate:** *"Close DOLE redundancy due-process without litigation exposure; unblock H1B filing track."*

### Commit candidate list (target ≤ 12 hr task work, ~10 SP)

- ✅ #200073 Notice & Due Process (2 SP, already pinned to 7.4)
- ✅ NEW Chippens S1: Inventory schema (2 SP) — from Block 3
- ✅ NEW H1B S1: USCIS window + attorney (1 SP) — from Block 4
- ➕ Carry-over from 7.3 if any unfinished
- 🔁 Pull #203864 TCT Release forward only if room

---

## Outputs (post-session, Grace's action items)

- [ ] Update AC on #202912, #202913, #203589 in ADO
- [ ] Create stories for #201708 (5 stories, S1–S5)
- [ ] Create stories for #199535 (5 stories, S1–S5)
- [ ] Decide & execute on #200075 (merge or split)
- [ ] Close/rebase 3 stale epics
- [ ] Create Iteration 7.4 path in ADO (May 18 – May 31)
- [ ] Move S1-Chippens + S1-H1B + #200073 into 7.4
- [ ] Schedule 7.4 planning meeting on 2026-05-15 (Fri)

---

## Success Criteria

- PI7 feature refinement: ≥ 8/12 features have ≥ 1 refined story (was 5/12)
- 7.3 DoR: 7/7 stories pass (was 4/7 = 57%)
- 7.4 sprint goal stated, commit list set, capacity ≤ 80% loaded
- Zero "Active" epics anchored to PI3/PI4 (clean rebase or close)

---

## References

- Audit history: `ado_otp/CLAUDE.md` (A1–A13)
- Last closing audit: `ado_otp/audit/AUDIT_20260322_232928.md`
- Backlog analysis: `ado_otp/BACKLOG_ANALYSIS_20260503.md`
- Skill authority: `.claude/skills/ado_safe_audit.md`
