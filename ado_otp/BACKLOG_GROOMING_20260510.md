# OTP Backlog Grooming & Refinement — Meeting Prep

**Date:** 2026-05-10 | **Facilitator:** Ramon Aseniero  
**Iteration:** 7.3 (May 4–17, Day 7/14) | **PI:** PI7 (Apr 6 – Jun 28)  
**Planning Horizon:** 7.4 → 7.5 → 7.6 (3 sprints, 7 weeks)  
**Attendees:** ART / Program Team + Grace (sole assignee)

---

## Meeting Agenda

| # | Topic | Time | Purpose |
|---|-------|------|---------|
| 1 | Sprint 7.3 Status Check | 10 min | Where are we? What carries over? |
| 2 | Backlog Walkthrough — All Open Items | 20 min | Review every item, confirm priority |
| 3 | AC Refinement — 3 Weak Items | 15 min | Refine acceptance criteria to meet DoR |
| 4 | Feature Decomposition — New Stories | 20 min | Break features into sprint-ready stories |
| 5 | Sprint Planning — 7.4, 7.5, 7.6 | 20 min | Assign stories to iterations |
| 6 | Structural Fixes & Actions | 10 min | ADO housekeeping, links, subscriptions |
| 7 | Decision Log & Parking Lot | 5 min | Capture decisions, defer items |

**Total: ~100 min (1h 40m)**

---

## 1. Sprint 7.3 Status Check (Day 7 of 14)

### Board Snapshot

| ID | Title | SP | State | Risk |
|----|-------|----|-------|------|
| #203016 | Generate & Validate GIS 2026 Report | 3 | **Closed** | — |
| #203797 | Submission of GIS Report | 2 | **Closed** | — |
| #203588 | Implementation of QA AI Roles | 4 | Active | 5.5h remaining, 4 tasks open |
| #203792 | Release of Memorandum (QAA AI) | 2 | Active | 1.5h remaining, 2 tasks open |
| #202913 | Installation of Street Signage | 2 | Active | IterationPath = 7.4, showing on 7.3 board |
| #202912 | Fabrication of Signage | 2 | **New** | **Day 7 stall — not started** |
| #203589 | Akira signed Letter of Invitation | 2 | **New** | **Day 7 stall — not started** |

```
Credited:      5 SP (29%)
In-progress:   8 SP (3 stories Active)
Not started:   4 SP (2 stories New at midpoint — RISK)
Remaining:    10h across 9 open tasks, 7 days left
```

### Discussion Points
- **DECIDE:** #202912 and #203589 still New — activate this week or defer to 7.4?
- **DECIDE:** #202913 — officially in 7.3 or 7.4? IterationPath mismatch.
- **CHECK:** #203588 (QA AI, 4 SP) — 4 tasks still New. Can all close by May 17?

---

## 2. Backlog Walkthrough — All Open Items by Priority

### Tier 1: HIGH Priority (Deadline-Driven or Compliance)

| ID | Type | Title | Iter | SP | State | Deadline/Urgency |
|----|------|-------|------|----|-------|-----------------|
| #203019 | Feature | Jairosoft SEC GIS Report 2026 | PI7 | — | Active | **P1** — statutory SEC deadline, child #203016 closed, #203978 next |
| #203978 | Story | FTC Approval from SEC of GIS 2026 | 7.4 | 1 | New | SEC acknowledgement pending |
| #198979 | Feature | Japan Business Visa — Jove Moralde | PI7 | — | Active | Travel deadline imminent, **no stories created** |
| #200071 | Feature | Strategic Rightsizing & Lean Team | PI7 | 2 | Active | DOLE labor compliance |
| #200073 | Story | Notification & Due Process (Legal) | 7.4 | 2 | New | Legal phase of LeanSizing — DOLE 30-day notice |
| #199535 | Feature | Adam H1B / Green Card Renewal | PI8 | — | Active | **Immigration deadline — verify PI8 covers it** |
| #198758 | Feature | Visa Readiness (Bomar, Earl, Bon) | PI8 | — | Active | **Immigration deadline — verify PI8 covers it** |

### Tier 2: MEDIUM Priority (Active Initiatives)

| ID | Type | Title | Iter | SP | State | Notes |
|----|------|-------|------|----|-------|-------|
| #203588 | Story | Implementation of QA AI Roles | 7.3 | 4 | Active | In-flight, 5.5h left |
| #203792 | Story | Release of Memorandum (QAA AI) | 7.3 | 2 | Active | In-flight, 1.5h left |
| #203346 | Feature | AI-QA Role | PI7 | — | Active | Parent initiative, stories in 7.3 |
| #192486 | Feature | Jairosoft/JIT Village Sign | PI7 | — | Active | Physical work, children #202912/#202913 |
| #202912 | Story | Fabrication of Signage | 7.3 | 2 | New | Weak ACs — needs refinement |
| #202913 | Story | Installation of Street Signage | 7.3/7.4 | 2 | Active | Weak ACs — needs refinement, depends on #202912 |
| #203589 | Story | Akira signed Letter of Invitation | 7.3 | 2 | New | Weak ACs — needs refinement |
| #197095 | Feature | 2026 PhilGeps Account Renewal | PI7 | — | Active | Has embedded story/task descriptions, **no ADO stories created** |
| #203864 | Story | Release of TCT | 7.6 | 2 | New | Cabantian backlot title transfer |

### Tier 3: LOW Priority / Future (PI8+)

| ID | Type | Title | Iter | SP | State | Notes |
|----|------|-------|------|----|-------|-------|
| #178746 | Feature | Orfel Gonzaga Transfer of Title | PI7 | — | Active | 14 months old, no SP, no AC, **DoR incomplete** |
| #203347 | Feature | AI-Developer Role | PI8 | — | New | No AC, no SP, no stories — needs full grooming |
| #203348 | Feature | AI-PM/PO Role | PI8 | — | New | No AC, no SP, no stories — needs full grooming |
| #201815 | Story | Physical Installation & Grid Integration | 8.1 | 2 | New | Solar project — not starting until PI8 |
| #201820 | Story | Monitoring & Handover | 8.1 | 2 | New | Solar project — not starting until PI8 |

### Closed / Resolved (No Action Needed)

| ID | Title | Closed |
|----|-------|--------|
| #203025 | JIT Assessment Center Amended SEC | May 7 |
| #203016 | Generate & Validate GIS 2026 Report | May 5 |
| #203797 | Submission of GIS Report | May 10 |

### Discussion Points
- **DECIDE:** Priority ranking — does team agree with Tier 1/2/3 split?
- **DECIDE:** #198979 (Japan Visa Jove) — when is travel? Needs stories NOW if within 3 weeks.
- **VERIFY:** #199535 and #198758 (immigration) — do PI8 dates (Jun 29+) align with actual deadlines?
- **DECIDE:** #178746 (Orfel Transfer) — 14 months active with no progress. Close or groom?

---

## 3. AC Refinement — 3 Items Below DoR

### Item A: #202912 — Fabrication of Signage (2 SP)

**Current ACs (WEAK — too vague):**
1. Safety measures should be implemented
2. Local community/brgy compliant

**Proposed Refined ACs:**
1. Safety equipment (hard hats, gloves, harnesses) procured and documented with receipts
2. Barangay clearance/permit obtained before fabrication starts — copy on file
3. Materials procurement completed per approved BOM (bill of materials)
4. Fabrication completed per approved design specs and dimensions
5. Photo documentation of completed signage before delivery to installation site

> **DECIDE:** Accept refined ACs? Any additions?

---

### Item B: #203589 — Akira Signed Letter of Invitation (2 SP)

**Current AC (WEAK — single line):**
1. Accomplished invitation letter for Japan Embassy

**Proposed Refined ACs:**
1. Company details package (registration, address, contact person, business nature) sent to Akira within 3 business days
2. Signed invitation letter received on Akira company letterhead with authorized signatory
3. Letter contains all Japan Embassy required fields: purpose of visit, duration of stay, financial guarantee statement
4. Scanned PDF copy uploaded to SharePoint project folder
5. Original hard copy received via courier (if required by embassy)

> **DECIDE:** Accept refined ACs? Is there an embassy submission deadline?

---

### Item C: #202913 — Installation of Street Signage (2 SP)

**Current AC (WEAK — single line):**
1. Installed Street signage

**Proposed Refined ACs:**
1. Predecessor #202912 (Fabrication) must be Closed before installation begins
2. Installation date coordinated with barangay and local traffic management
3. Signage installed at approved location per site plan
4. Post-installation safety inspection completed — signed checklist on file
5. Photo documentation (before/during/after) uploaded to project folder

> **DECIDE:** Accept refined ACs? Add predecessor link in ADO?

---

## 4. Feature Decomposition — Stories Needed

These features are Active in PI7 but have **no user stories** in ADO. Team needs to decompose them into sprint-ready stories.

### Feature #198979 — Japan Business Visa (Jove Moralde) — HIGH

**Existing description includes 3 document categories + 4 processing steps. Suggested stories:**

| Proposed Story | SP Est. | Target Iter | Description |
|---------------|---------|-------------|-------------|
| Gather Employee Documents (Category A) | 2 | 7.4 | Passport, visa form, photo, COE, bank cert |
| Prepare Company Documents (Category B) | 1 | 7.4 | Travel order, dispatch letter, ITR |
| Coordinate Japanese Inviter Documents (Category C) | 2 | 7.4 | Letter of invitation, guarantee, itinerary — **links to #203589** |
| Book JVAC Appointment & Submit | 2 | 7.5 | Online booking, payment, in-person submission |
| Track & Receive Visa | 1 | 7.5 | Monitor 8-digit reference, collect passport |

> **DECIDE:** Accept decomposition? Adjust SP? Confirm travel date to set urgency.

---

### Feature #197095 — PhilGeps Account Renewal — MEDIUM

**Feature description already contains embedded story structure. Suggested stories:**

| Proposed Story | SP Est. | Target Iter | Description |
|---------------|---------|-------------|-------------|
| Document Consolidation & Audit | 2 | 7.5 | Tax clearance, Mayor's permit, AFS verification |
| Online Submission & Payment | 2 | 7.5 | Portal update, Platinum membership payment, status monitoring |

> **DECIDE:** Accept? Is there a PhilGeps renewal deadline?

---

### Feature #200071 — Strategic Rightsizing (LeanSizing) — HIGH

**Has #200073 (Notification & Due Process) already in 7.4. Additional stories from description:**

| Proposed Story | SP Est. | Target Iter | Description |
|---------------|---------|-------------|-------------|
| Board Resolution / Management Affidavit | 2 | 7.5 | Business justification document for DOLE |
| Selection Criteria Definition | 2 | 7.5 | Performance ratings, seniority, skill sets framework |
| Comparative Job Analysis | 2 | 7.6 | Prove removed roles are absorbed by lean structure |

> **DECIDE:** Accept? Check DOLE timeline constraints.

---

### Feature #178746 — Orfel Gonzaga Transfer of Title — LOW

**14 months old, Active, no stories. Description lists 5 document requirements.**

| Proposed Story | SP Est. | Target Iter | Description |
|---------------|---------|-------------|-------------|
| Collect Transfer Documents Package | 2 | 7.6 | Original title, tax clearance, deed of sale, BIR, ROD |
| Submit to Registry of Deeds | 2 | PI8 | File documents, pay fees, track processing |

> **DECIDE:** Still relevant? Groom or close?

---

## 5. Sprint Planning — Proposed Allocation

### Iteration 7.4 (May 18–31) — Target: 10-12 SP

| ID | Title | SP | Source | Priority |
|----|-------|----|--------|----------|
| #202913 | Installation of Street Signage | 2 | Existing | MEDIUM |
| #200073 | Notification & Due Process (Legal) | 2 | Existing | HIGH |
| #203978 | FTC Approval from SEC of GIS 2026 | 1 | Existing | HIGH |
| NEW | Gather Employee Docs — Jove Visa (Cat A) | 2 | From #198979 | HIGH |
| NEW | Prepare Company Docs — Jove Visa (Cat B) | 1 | From #198979 | HIGH |
| NEW | Coordinate Inviter Docs — Jove Visa (Cat C) | 2 | From #198979 | HIGH |
| | **Proposed Total** | **10** | | |

**Carryover candidates from 7.3** (if not completed by May 17):
- #202912 Fabrication of Signage (2 SP)
- #203589 Akira Letter of Invitation (2 SP)

---

### Iteration 7.5 (Jun 1–14) — Target: 10-12 SP

| ID | Title | SP | Source | Priority |
|----|-------|----|--------|----------|
| NEW | Book JVAC Appointment & Submit — Jove | 2 | From #198979 | HIGH |
| NEW | Track & Receive Visa — Jove | 1 | From #198979 | HIGH |
| NEW | Board Resolution / Affidavit — LeanSizing | 2 | From #200071 | HIGH |
| NEW | Selection Criteria Definition — LeanSizing | 2 | From #200071 | HIGH |
| NEW | Document Consolidation — PhilGeps | 2 | From #197095 | MEDIUM |
| NEW | Online Submission — PhilGeps | 2 | From #197095 | MEDIUM |
| | **Proposed Total** | **11** | | |

---

### Iteration 7.6 (Jun 15–28) — Target: 8-10 SP (PI7 close, lighter load)

| ID | Title | SP | Source | Priority |
|----|-------|----|--------|----------|
| #203864 | Release of TCT | 2 | Existing | MEDIUM |
| NEW | Comparative Job Analysis — LeanSizing | 2 | From #200071 | HIGH |
| NEW | Collect Transfer Docs — Orfel Title | 2 | From #178746 | LOW |
| | **Proposed Total** | **6** | | |
| | **Buffer for carryover** | **4** | | |

---

### Planning Summary

| Sprint | Current SP | Proposed SP | Status |
|--------|-----------|-------------|--------|
| 7.3 | 17 | — | In-flight (Day 7) |
| 7.4 | 5 | **10** (+5 new) | Needs 3 new stories from #198979 |
| 7.5 | 0 | **11** (+11 new) | Needs 6 new stories |
| 7.6 | 2 | **6** (+4 new) | Light load, buffer for carryover |
| **Total PI7 remaining** | **7** | **27** | | |

---

## 6. Structural Fixes — ADO Housekeeping

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Subscribe Iteration 7.4 as team iteration | Ramon | HIGH |
| 2 | Subscribe Iteration 7.5 as team iteration | Ramon | HIGH |
| 3 | Subscribe Iteration 7.6 as team iteration | Ramon | HIGH |
| 4 | Add predecessor link: #202912 → #202913 | Grace | MEDIUM |
| 5 | Resolve #202913 IterationPath (7.3 vs 7.4) | Team | HIGH |
| 6 | Update ACs for #202912, #203589, #202913 | Grace | HIGH |
| 7 | Create new stories from Section 4 decomposition | Grace | HIGH |

---

## 7. Decision Log (Capture During Meeting)

| # | Decision | Agreed | Owner | Date |
|---|----------|--------|-------|------|
| D1 | #202912 / #203589 — activate or defer to 7.4? | | | |
| D2 | #202913 — stays in 7.3 or officially 7.4? | | | |
| D3 | Refined ACs for #202912 — accepted? | | | |
| D4 | Refined ACs for #203589 — accepted? | | | |
| D5 | Refined ACs for #202913 — accepted? | | | |
| D6 | Japan Visa (#198979) — travel date confirmed? Stories approved? | | | |
| D7 | PhilGeps (#197095) — renewal deadline? Stories approved? | | | |
| D8 | LeanSizing (#200071) — DOLE timeline? Stories approved? | | | |
| D9 | Orfel Transfer (#178746) — still relevant or close? | | | |
| D10 | Sprint 7.4 plan — approved? | | | |
| D11 | Sprint 7.5 plan — approved? | | | |
| D12 | Sprint 7.6 plan — approved? | | | |
| D13 | Immigration items (#199535, #198758) — PI8 dates OK? | | | |
| D14 | Priority tiers — agreed? | | | |

### Parking Lot

| Item | Reason Deferred | Revisit When |
|------|----------------|--------------|
| #203347 AI-Developer Role | No desc/AC/SP — needs full grooming | PI8 planning |
| #203348 AI-PM/PO Role | No desc/AC/SP — needs full grooming | PI8 planning |
| #201815 Physical Installation (Solar) | PI8 committed | PI8 planning |
| #201820 Monitoring & Handover (Solar) | PI8 committed | PI8 planning |

---

## Quick Reference — DoR Compliance

| Iteration | Stories | Pass | Weak | Compliance |
|-----------|---------|------|------|------------|
| 7.3 | 7 | 4 | 3 | 57% |
| 7.4 (current) | 3 | 2 | 1 | 67% |
| 7.6 | 1 | 1 | 0 | 100% |
| **All** | **11** | **7** | **4** | **64%** |

**Target after this meeting: 100% DoR on all items planned for 7.4–7.6.**

---

## Quick Reference — Velocity & Capacity

| Metric | Value |
|--------|-------|
| Historical velocity | 10–16 SP/sprint |
| Grace capacity/sprint | ~28h (6h/day effective) |
| SP-to-hours ratio | ~2-3h per SP |
| PI7 sprints remaining | 3 (7.4, 7.5, 7.6) |
| Total PI7 capacity | ~30-48 SP |
| Currently planned | 7 SP |
| **Gap** | **23-41 SP** |

---

*Generated 2026-05-10 by Claude Code — live ADO data pull*  
*Meeting prep for ART/Program Team backlog grooming session*
