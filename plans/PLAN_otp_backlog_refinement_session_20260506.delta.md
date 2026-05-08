# OTP Backlog Refresh — Delta vs 2026-05-06 Plan

- **Refreshed:** 2026-05-07
- **Source:** Live ADO snapshot (project `e7739905-28a3-4ae1-9173-7f6cd13b3494`, team `64de61f0-1203-4b01-aee2-6b4415aec52b`, OTP Team)
- **Active iteration:** Iteration 7.3 (May 4 → May 17, 2026) — confirmed unchanged
- **Companion file:** `PLAN_otp_backlog_refinement_session_20260506.md` (still authoritative agenda; this is the diff)

---

## TL;DR — Plan Still ~90% Valid

Most plan blocks survive the refresh. Two material changes:

1. **AB#202913 Installation of Street Signage already moved 7.3 → 7.4** (plan Block 2 listed 3 DoR fixes for 7.3; now 2). AC strengthen still needed but in 7.4 scope.
2. **Two new 7.3 stories appeared** (AB#203588 QA AI Roles, AB#203792 Memorandum). Both arrive DoR-compliant (SP+Desc+AC). No grooming needed; just acknowledge in Block 1 context.

Plan also missed one item: **AB#197093 CEBU Occupancy Permit** — Feature at OTP root, no Desc/AC, no iteration. Add to Block 6 stale-decisions.

---

## Snapshot — OTP Stories + Features + Stale Epics (29 items)

|                                     Bucket | Count | IDs                                                                                      |
| -----------------------------------------: | ----: | ---------------------------------------------------------------------------------------- |
|        Iter 7.3 stories (active in flight) |     4 | #202912, #203588, #203792, #203589                                                       |
|                           Iter 7.4 stories |     2 | #200073, #202913                                                                         |
|                           Iter 7.6 stories |     1 | #203864                                                                                  |
|                           Iter 8.1 stories |     2 | #201815, #201820                                                                         |
| 2026-PI7 Features (no story decomposition) |    10 | #178746, #192486, #197095, #198979, #200071, #203019, #203025, #203346, #200075, #201708 |
|                          2026-PI8 Features |     6 | #198758, #199535, #201710, #194824, #203347, #203348                                     |
|                      Stale Epics (PI3/PI4) |     3 | #178743, #191886, #191943                                                                |
|                    Root OTP (no iteration) |     1 | **#197093 (new finding)**                                                                |

---

## Iter 7.3 — Live State (was 4 items, plan only mentioned 3)

| ID | Title | SP | State | DoR Status | Plan Coverage |
|----|-------|---:|-------|-----------|---------------|
| #202912 | Fabrication of Signage | 2 | New | AC weak (2 bullets, brgy permit ref) | ✅ Block 2 covers — fix AC |
| #203588 | Implementation of QA AI Roles | 4 | Active | DoR ✓ (Desc+AC+SP) | **Not in plan** — already DoR-clean, skip in session |
| #203792 | Release of Memorandum | 2 | Active | DoR ✓ (Desc+AC+SP) | **Not in plan** — already DoR-clean, skip in session |
| #203589 | Akira Letter of Invitation | 2 | New | AC weak (1 bullet, "Accomplished invitation letter") | ✅ Block 2 covers — fix AC |

**Iter 7.3 commit total:** 10 SP across 4 stories (was 6 SP / 3 stories at plan time).

**Block 2 update:** Drop AB#202913 from 7.3 fixes; it lives in 7.4 now. Two AC patches remain (#202912, #203589). DoR moves 2/4 → 4/4 stories on 7.3.

---

## Iter 7.4 Pre-Loaded (plan-relevant)

| ID | Title | SP | State | Notes |
|----|-------|---:|-------|-------|
| #200073 | Notification & Due Process (Story) | 2 | New | DoR ✓ — sister to Feature #200075 (Block 5 still applies — decide merge or split) |
| #202913 | Installation of Street Signage | 2 | Active | DoR weakish (1 bullet AC). Patch AC during session even though 7.4. |

7.4 already has 4 SP committed before 7.4 planning meeting (2026-05-15). Capacity reminder: Grace ~15 hr / 10 working days.

---

## PI7 Feature Refinement — Plan Block 3 / Block 5

| ID | Title | Pri | BV | State | Has Desc | Has AC | Has Stories |
|----|-------|----:|---:|-------|:--------:|:------:|:-----------:|
| #201708 | **Chippens Inventory** | 2 | **15** | New | ✗ | ✗ | ✗ |
| #200075 | Notice/Due Process Feature | 2 | 9 | New | ✗ | ✗ | child #200073 only |
| #178746 | Orfel TCT Transfer | 2 | 4 | Active | ✓ | ✗ | child #203864 in 7.6 |
| #192486 | Jairosoft/JIT Village Sign | 2 | 5 | Active | ✓ | ✗ | children #202912/#202913 |
| #197095 | PhilGeps Account Renewal | 2 | 7 | Active | ✓ | ✗ | none |
| #198979 | Japan Visa — Jove Moralde | 2 | 9 | Active | ✓ | ✗ | none |
| #200071 | Strategic Rightsizing & Lean Team | 2 | 10 | Active | ✓ | ✗ | none (1 SP set on Feature itself) |
| #203019 | Jairosoft SEC GIS Report 2026 | 1 | 10 | Active | ✓ | ✗ | none |
| #203025 | JIT Assessment Center Amended SEC | 2 | 10 | Active | ✓ | ✗ | none |
| #203346 | AI-QA Role Feature | 2 | 10 | Active | ✓ | ✗ | child #203588 (in 7.3) |

> **Block 3 (Chippens) still required.** No decomposition since plan was written.
> **Block 5 (#200075) still required.** No Desc, no AC, only 1 child story #200073 already in 7.4. Decide: merge or split per plan.
> **New refinement debt surfaced:** 6 PI7 Features have no stories at all (#197095, #198979, #200071, #203019, #203025, #203346). Plan didn't enumerate these. If session has slack, queue.

---

## PI8 Features — Plan Block 4 expanded

| ID | Title | Pri | BV | Stories | DoR Status |
|----|-------|----:|---:|:-------:|-----------|
| #199535 | Adam H1B / Green Card | 2 | 10 | ✗ | Plan Block 4 covers — split S1–S5; pull S1 forward to 7.4 |
| #198758 | Visa Readiness — Bomar/Earl/B… | 2 | 8 | ✗ | **Not in plan** — companion to #199535; group H1B/visa work |
| #201710 | Solar Panel — Davao Office | 2 | 7 | ✓ | Children #201815, #201820 in 8.1 — DoR ✓ |
| #194824 | Set-up 25 Computers for Bubble MCC | 2 | 7 | ✗ | **Not in plan** — no Desc, no AC |
| #203347 | AI-Developer Role | 2 | — | ✗ | **Not in plan** — Desc present, no AC, no BV |
| #203348 | AI-PM/PO Role | 2 | — | ✗ | **Not in plan** — Desc present, no AC, no BV |

**Suggested addition to Block 4:** Group #199535 + #198758 as the visa/H1B cluster. Pull S1 of #199535 to 7.4 (lawyer engagement) per existing plan; add #198758 discovery into same block — same employee-immigration domain, lawyer engagement is shared.

---

## Stale Epics — Plan Block 6 — UNCHANGED

All 3 still Active in PI3/PI4:

| Epic | Iter Path | Pri | Has Desc | Has AC | Recommended |
|------|-----------|----:|:--------:|:------:|-------------|
| #178743 Holy Trinity Back Lot | OTP\PI 3 | 2 | ✗ | ✗ | Close (one live child #178746→#203864 in 7.6) — lift child, archive epic |
| #191886 Mabolo Occupancy Permit | OTP\PI4 | 2 | ✓ | ✗ | Close — verify no open obligation |
| #191943 Employee 201 File Digitization | OTP\PI 4 | **1** | ✓ | ✗ | Decompose into PI7/PI8 OR downgrade Pri 1 → 3 |

> Iteration path inconsistency: `OTP\PI4` (no space) vs `OTP\PI 4` (with space). Either normalize or both will need separate ADO updates. Flag during session.

---

## NEW FINDING — Add to Plan Block 6

**AB#197093 CEBU Occupancy Permit** (Feature, New, Pri 2, no iteration — sits at root `OTP`)

- No Description
- No Acceptance Criteria
- No iteration assignment
- Sister concept to #191886 Mabolo Occupancy Permit (also government compliance)

**Decision needed:** assign to PI7/PI8 OR close as duplicate of Mabolo OR document why CEBU is separate scope.

---

## Updated Block 7 — Iter 7.4 Commit Refresh

Plan Block 7 candidate list still valid. Pre-loaded items confirmed:

- ✅ #200073 Notice & Due Process (2 SP, **already in 7.4**)
- ✅ #202913 Installation of Street Signage (2 SP, **already in 7.4**, AC patch needed)
- ➕ NEW Chippens S1 (2 SP) — pending Block 3 split
- ➕ NEW H1B S1 (1 SP) — pending Block 4 split (lawyer engagement)
- ➕ Carry-over from 7.3 if any unfinished

Pre-loaded SP: 4. Add 3 from splits: 7. Capacity 15 hr — comfortable. Could pull 1 more if Bomar visa scoping done.

---

## Refreshed Outputs Checklist

Yesterday's plan outputs section is largely intact. Add:

- [ ] **#197093 CEBU Occupancy Permit** — decide scope (assign iter / close / merge to Mabolo)
- [ ] Acknowledge new 7.3 stories #203588, #203792 are DoR-compliant (no action)
- [ ] AC patch on #202913 even though it's in 7.4 (not 7.3 as plan said)
- [ ] Optional: queue 4 PI8 stragglers (#194824, #203347, #203348, #198758) for stretch refinement if Chippens/H1B finish under timebox

---

## Audit Trail

- ADO project ID: `e7739905-28a3-4ae1-9173-7f6cd13b3494` (use ID, not name — see memory `reference_ado_otp_api.md`)
- ADO team ID: `64de61f0-1203-4b01-aee2-6b4415aec52b`
- Backlog categories queried: `Microsoft.RequirementCategory` (9 stories), `Microsoft.FeatureCategory` (17 features)
- 3 stale Epics fetched explicitly by ID (Epics not in either backlog category)
- No ADO mutations performed; refresh-only
