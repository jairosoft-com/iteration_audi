---
title: "Portfolio Meeting Agenda — 2026-04-25"
type: summary
tags: [portfolio, meeting-agenda, iteration-7-2, pi7]
sources: ["../portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260425.html"]
created: 2026-04-25
updated: 2026-04-25
---

# Portfolio Meeting Agenda — 2026-04-25

**Meeting:** Portfolio Review · PI7 · Iteration 7.2 Day 6  
**Duration:** 30 minutes  
**Generated:** Apr 25, 2026 · 09:50 PHT  
**Source dashboard:** PORTFOLIO_20260425_1533.html

**Attendees:**
- Ramon Aseniero — CEO / Project Owner
- Karl Caumban — Portfolio Delivery Manager

## Agenda structure (30 min)

| # | Topic | Time |
|---|-------|------|
| 1 | Portfolio Snapshot & Scorecard | 3 min |
| 2 | Critical & High Risk Teams | 8 min |
| 3 | Quick Wins & Escalations | 5 min |
| 4 | Structural Risks | 5 min |
| 5 | Decisions Needed | 4 min |
| 6 | Action Items & Owners | 3 min |
| 7 | Wrap-up & Next Steps | 2 min |

**Facilitator note:** Topics 2–3 carry the most value. If time runs short, skip Topic 4 and capture structural risks as async follow-ups.

---

## Topic 1 — Portfolio Snapshot (3 min)

**Talking points:**
- Mean 69.7, Median 69.4 · 1 High Risk · 0 Critical
- Mean dipped 0.2 vs Apr 24 — driven by Colina HCI rubric correction (82→72), not delivery regression
- Two improvers: JIT (+2.2), Flawless (+0.6); 7 teams flat
- Day 6 = early-sprint annotation threshold; stalled DP now a real signal
- Portfolio floor: Shared Services 56.1 · Ceiling: HR Recruitment 83.7

Full trend: [[summaries/portfolio-20260425-1533]] · [[synthesis/portfolio-trend]]

---

## Topic 2 — At-Risk Teams (8 min)

### [[entities/team-ado-shared|Shared Services]] — High Risk · 56.1 · flat (2nd consecutive day)
- Iteration Planning: 19.4 · DoR: 66.7 · DP: 0.0
- #202464 + #203231 at "Passed UAT Testing" — 3 SP uncredited; two-click transition to Closed
- #202687 title-only since Apr 17 (8 days) — no Description, AC, or SP
- #202551 + #203221 unsized — drives 33% untouched ratio and Estimation gap
- 11 PI7-parent User Stories without sub-iteration assignment (suppresses IP at 19.4)
- **P0 ceiling:** all five Day-6 actions → 73.8 (Moderate) in one session, no dev work required

### [[entities/team-ado-ls-dev|Life Style Help]] — Moderate · fragile · 61.1
- BR = 24.3 (Critical dimension) — 5 stale_90 items + #187240 at 251 days (15 audits)
- #195727 untouched 8 calendar days (Ike) — one item shy of BR escalation trigger (drop to ~55–58 High Risk)
- Sprint scope: 4 items / 6 SP — lowest in PI7 series; no sprint goal

### [[entities/team-git-aa-dev|Auto Allies]] — Moderate · HCI Critical · 65.7
- HCI = 59 — no branch protection; 10/11 PRs self-merged; Earl 4 direct commits to `dev` (no PR, no AB#)
- SGPI = 0.0% (0 of 27 SP closed, Day 6); only #203118 has a clear path this week
- Earl direct-commit pattern on lawyer/onboarding logic — **second consecutive sprint**
- raseniero GitHub token still 404 — HCI evidence frozen at Apr 21 baseline

### [[entities/team-git-cc-dev|Colina Health]] — Moderate · 66.9 (−4.0 today)
- HCI corrected 82 → 72 (rubric correction, not regression)
- 4 items at "Passed QA Testing" (8 SP) unclosed — primary near-term velocity unlock
- #202028 (PRN defect, 2 SP) stalled in Ready for Dev 11+ days — no GitHub branch or PR
- Kyaa-A holds 5 of 11 scored items but not on ADO capacity roster (capacity understated)

---

## Topic 3 — Quick Wins & Escalations (5 min)

Quick wins < 30 min each, pure ADO/GitHub hygiene:

| Team | Action | Owner | Impact | Effort |
|------|--------|-------|--------|--------|
| Shared Services | Close #202464 + #203231 (UAT → Closed) | Teofilo | +5.4 pts | ~2 min |
| Finance | Assign #203043 to Iteration 7.2 | Karl / Grace | +3.6 pts | ~1 min |
| Finance | Close #203040 (AA Escalation, 1 SP) | Grace | +2.0 pts | Today |
| Shared Services | Add Description + AC to #202687 | Jaszmeine | +4.7 pts | ~15 min |
| Shared Services | Set SP on #202687 + #203221 | Vicsante / Jaszmeine | +4.8 pts | ~5 min |
| Administration | Close #202939 (Professional Fee IC, 2 SP) | Mark | ~+5 pts (DP) | Today |
| Administration | Add Description + AC to #202909 | Mark | DoR pass | ~15 min |
| Colina Health | Close 4 "Passed QA Testing" items (8 SP) | Paul / Kyaa-A | SGPI unlock | ~5 min |

**Escalation candidates (multi-audit, unactioned):**
- **raseniero GitHub token** (Day 6 of outage) — highest-priority external blocker; Auto Allies + Colina HCI evidence frozen since Apr 21
- **Shared #202687** — title-only since Apr 17 (3 audits flagged, zero remediation); PDM sign-off needed on descope vs. fix
- **LS Dev #187240** — 251 days stale, 15th consecutive flag; disposition decision overdue
- **BIR eAFS portal (#201448, Finance)** — 10 days past Apr 15 deadline; unclear if item belongs in ADO
- **Admin's 9 PI7-root unscoped legacy items** — 6th consecutive audit flag; triage decision needed

---

## Topic 4 — Structural Risks (5 min)

| Risk | Scope | Details |
|------|-------|---------|
| Bus Factor = 1 | Admin, Finance, HR, OTP, LS Dev | Single contributor or extreme concentration per team; PI8 capacity planning needed |
| Backlog Debt / DoR stalls | Shared, OTP, HR, JIT (×5 teams) | DoR-failing items 3–7 audits unresolved; each < 15 min to fix |
| Iteration Planning drag | Flawless (7.4), Shared (19.4), LS Dev (28.6), OTP (53.8) | Oversized legacy backlogs, unscoped PI-parent items; structural, won't fix mid-sprint |
| GitHub engineering health | git_aa_dev, git_cc_dev | No branch protection on either repo; Earl repeating direct-commit on sensitive paths; token outage Day 6 |
| Delivery Predictability | 9/10 teams at 0 SP closed | Early-sprint annotation lifted; repeating PI7.1 burst-delivery anti-pattern |
| Capacity roster gaps | git_cc_dev | Kyaa-A not in ADO capacity config — one edit fix |

---

## Topic 5 — Decisions Needed (4 min)

| Decision | Owner | Priority |
|----------|-------|----------|
| Resolve raseniero GitHub token outage | Ramon | URGENT |
| Add Kyaa-A to Colina ADO capacity roster | Karl | Normal |
| Enforce review gate on Auto Allies sensitive backend (enable branch protection on `dev`) | Ramon / Karl | URGENT |
| Disposition Life Style #187240 (251 days stale) — Won't Do / Spike / Epic; EOD Apr 26 | Karl | Normal |
| PI8 capacity planning — address Bus Factor=1 across 5 teams (cross-training pairs, rebalance dates) | Ramon + Karl | PI8 Planning |
| BIR eAFS portal #201448 escalation — clarify ownership and current status | Ramon | URGENT |

---

## Topic 6 — Action Items (3 min)

### P0 — Do today (Apr 25–26)
- Shared Services: Close #202464 + #203231 · Add Description/AC to #202687 · Size #202687 + #203221 · Touch #202551
- Finance: Assign #203043 to 7.2 · Close #203040
- Administration: Close #202939 · Add DoR to #202909
- Ramon: Resolve raseniero GitHub token (404 scope)

### P1 — Before sprint close (May 3)
- Finance: Close #203034 + #203038 (6 SP) — would push Finance to ~95.7
- Colina: Close 4 "Passed QA Testing" items (8 SP)
- Colina: Resolve #202028 (PRN defect, stalled 11+ days)
- LS Dev: Touch #195727 (Ike) — prevents BR penalty trigger
- Karl: Add Kyaa-A to Colina ADO capacity roster
- Mark / Karl: Triage 9 PI7-root unscoped Admin items
- Ramon: Enable branch protection on Auto Allies `dev`

### P2 — PI8 planning (May 4+)
- Cross-training plan for 5 Bus-Factor=1 teams
- Disposition LS Dev #187240
- Introduce Spikes/Features into US-dominant teams (lifts Work Item Balance ceiling above 70.0)
- Empirical velocity ceiling baseline for ADO teams (curb chronic over-commitment)

---

## Topic 7 — Wrap-up (2 min)

**Impact if P0s actioned today:**
- Shared Services: 56.1 → 73.8 (+17.7 · High → Moderate)
- Finance: 77.9 → 83.5 (Moderate → Low Risk)
- Portfolio mean: 69.7 → ~71.9 (+2.2 in one day)
- 0 teams in High Risk; 2 teams in Low Risk

**Impact if deferred:**
- Shared Services stays High Risk for Day 7+
- Life Style risks BR trigger → ~55–58 (High Risk)
- PI7.1 burst-delivery anti-pattern repeats
- Auto Allies direct-commit pattern continues into PI8

**Next steps:**
- EOD Apr 26: Shared + Finance + Admin P0s closed in ADO; re-run portfolio dashboard
- Apr 27: Daily audit captures the lift; PI readiness check at Day 8 (57% elapsed)
- By May 3 (sprint close): Finance and JIT close as Low Risk; git teams close "Passed QA" backlog; raseniero token restored for clean PI7.3 baseline
- PI8 Planning: Bus-Factor=1, cross-training, branch protection, velocity ceilings

---

## Related
- [[summaries/portfolio-20260425-1533]] — source dashboard
- [[synthesis/portfolio-trend]] — full multi-sprint trend
- [[concepts/risk-bands]] — scoring thresholds
