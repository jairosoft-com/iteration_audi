---
title: "Portfolio Meeting Agenda — April 27, 2026"
type: summary
tags: [portfolio, meeting-agenda, iteration-7-2]
sources: ["../../portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260427.html"]
created: 2026-04-27
updated: 2026-04-27
---

# Portfolio Meeting Agenda — April 27, 2026

**Generated:** April 27, 2026 PHT · Source: 10 team audits (Apr 26 EOD ADO · AA `AUDIT_20260428_0247.md` · CC `AUDIT_20260427_0902.md`) · 30-minute agenda · Attendees: Ramon Aseniero (CEO), Karl Caumban (PDM)

> **Notable milestone:** First meeting agenda in PI7.2 with **0 High Risk and 0 Critical teams**. Portfolio mean reached 71.6 after GitHub token restoration enabled full re-audits of both Git teams. Shared Services broke out of High Risk overnight (56.1 → 64.2).

---

## Meeting metadata

| Field | Value |
|-------|-------|
| PI / Iteration | PI7 · Iteration 7.2 |
| Sprint window | Apr 20 – May 3, 2026 |
| Sprint day | Day 8 of 14 |
| Duration | 30 minutes |
| Attendees | Ramon Aseniero (CEO), Karl Caumban (PDM) |
| Portfolio mean | 71.6 (+1.6 vs Apr 26 14:00) |
| Portfolio median | 70.9 (+1.4 vs prior) |
| Teams at risk | 0 High Risk · 0 Critical |

---

## Agenda timeline

| # | Topic | Time |
|---|-------|------|
| 1 | Portfolio Snapshot & Scorecard | 3 min |
| 2 | At-Risk Teams & Day-8 Watch List | 8 min |
| 3 | Quick Wins & Escalations | 5 min |
| 4 | Structural Risks | 5 min |
| 5 | Decisions Needed | 4 min |
| 6 | Action Items & Owners | 3 min |
| 7 | Wrap-up & Next Steps | 2 min |

**Facilitator tip:** Topics 2–3 carry the most value. If time runs short, skip Topic 4 and capture structural risks as async follow-ups.

---

## Topic 1 — Portfolio Snapshot

**7-day trend (PI7.2):** Apr 22: 63.9 → Apr 23a: 64.1 → Apr 23p: 64.6 → Apr 24: 69.9 → Apr 25: 69.7 → Apr 26a: 69.9 → Apr 26p: 70.0 → **Apr 27: 71.6**

**Headline:** Portfolio cleared High Risk band; GitHub token restored. Shared Services (56.1 → 64.2, +8.1), OTP (68.7 → 74.8, +6.1), AA token re-audit reveals +2.4 pts (68.3 → 70.7, full HCI evidence). First 0-at-risk reading in PI7.2; 100% of teams in Moderate or Low.

### Team scores — Day 8 (descending)

| Team | Score | Band | Type |
|------|-------|------|------|
| HR Recruitment | 83.7 | Low Risk | ADO |
| Finance | 77.9 | Moderate | ADO |
| Office of President | 74.8 | Moderate | ADO |
| JIT Operation | 73.9 | Moderate | ADO |
| Administration | 71.0 | Moderate | ADO |
| Auto Allies | 70.7 | Moderate | Git |
| Flawless Wedding App | 70.2 | Moderate | ADO |
| Colina Health | 68.5 | Moderate | Git |
| Shared Services | 64.2 | Moderate | ADO |
| Life Style Help App | 61.1 | Moderate | ADO |

---

## Topic 2 — At-Risk Teams & Watch List

### No High Risk / No Critical (first in PI7.2)

Shared Services exited High Risk overnight (56.1 → 64.2 via 5 SP closed in 8h: #202464, #203231, #203266). LS Dev recovered to Moderate Apr 24 and held.

### Day-8 Watch List — 3 Moderate teams with structural fragility

1. **Life Style Help App (61.1)** — Lowest score; 4 audits flat; 69+ hr ADO silence; 0/6 SP closed at midpoint. Backlog Refinement 24.3 (Critical, dual-penalty). Critical ordering risk: if #203239 closes before Ike activates #195727, untouched ratio rises to 33% and BR collapses 24.3 → 4.3 (Overall ~57, drops to High Risk). Item #187240 now 253 days stale (17 audits).

2. **Shared Services (64.2)** — Just broke out of High Risk but Estimation regressed 66.7 → 42.9 after 3 unestimated items (#203296, #203309, #203221) added mid-sprint. #203296 AC = "Account renewed" (14 chars, fails 20-char rule). #202687 hits 10 days title-only (sprint record). P0 ceiling: ~80.3 Low Risk if 4 admin tasks complete today.

3. **Auto Allies (70.7)** — Day 9 with 0/27 SP closed; SGPI = 0.0. Token-restored re-audit (Apr 28 02:47): 11/12 PRs merged, median cycle ~2h (HCI +8 to 69). Critical gap: code review bypassed on 10/11 PRs — Spike #202169 unresolved. Joseph: 3 Active items no branch/PR (#203281, #203287, #203289). #203118 (Earl, 2 SP) aging Day 7+ in QA Testing — fastest path to first closure.

**Bright spots:** OTP (+6.1 overnight, full DoR + full Estimation), Colina Health (Kyaa-A delivered #202028 fix; pcoronia merged credential rotation PRs FE#157 + BE#64 — code-level security P0 resolved), FW App (8/15 SP = 53.3% delivery, sole non-zero in ADO portfolio).

### Process Violations — Activated WITHOUT DoR (3 teams)

- **JIT (#203155 + #203156)** — moved Ready → Active overnight without Description or AC. Teofilo executing without verifiable done-criteria.
- **Admin (#202898)** — moved Ready → Active overnight without Description or AC. 8th consecutive day no DoR; #202909 also Active without DoR (8 days).
- **HR (#203057, #203063)** — wrong candidate names in body for 9th consecutive audit. Items Ready and approaching Active; recruiter confusion risk if activated as-is.

---

## Topic 3 — Quick Wins & Escalations

### Quick wins (each under 30 minutes)

| Priority | Time | Action | Owner | Score Impact |
|----------|------|--------|-------|-------------|
| Highest ROI | 3 min | Finance → Low Risk: Assign #203043 to 7.2 + Close #203040 | Grace (Finance) | +5.6 pts → 83.5 Low Risk |
| P0 Day 8 | 5 min | OTP → Low Risk: Close #203026 (2 SP) + #203029 (4 SP) | Grace (OTP) | DP 0 → 42.9% · +5.9 pts → 80.7 Low Risk |
| Prevent regression | 2 min | LS Dev: Ike activates #195727 (Ready → Active) | Ike Yana | Prevents BR 24.3 → 4.3 collapse |
| DoR fix | 30 sec | Shared: Fix AC on #203296 + set SP on #203221, #203296, #203309 | Vicsante / Jaszmeine | Est 42.9 → 100; ~80.3 Low Risk |
| DoR fix | 25 min | JIT: Add Desc+AC to #203155 + #203156 | Teofilo | Restores DoR compliance |
| Operational quality | 5 min | HR: Fix body defects #203057 (Ramos) + #203063 (Abina) | Almera Tayao | Prevents recruiter error |
| Git gain | 10 min | Colina: ADO-close 5 Ready-for-UAT / Passed-QA items | per-item assignee | SGPI 6.7 → 43.3 · UPS +5+ pts |
| Break zero plateau | 2 min | Admin: Close #202939 (2 SP, Ready, full DoR) | Mark Colina | DP 0 → 5.1%; breaks 8-day zero plateau |

### Escalations — Unactioned across multiple audits

| Item | Team | Age | Action Required |
|------|------|-----|-----------------|
| #187240 — Evaluate Deployment Options · 253 days stale | LS Help | 17 audits | Close as Won't Fix → removes -20 BR penalty (BR 24.3 → 44.3) |
| #202687 — Onboarding Design · title-only 10 days (record) | Shared Services | 10 days | Add Desc + AC + SP today, OR de-scope to 7.3 |
| #203057 + #203063 — wrong candidate names in body | HR Recruitment | 9 audits | 2-min text swap — do before items go Active |
| #202909, #202898 — Active without DoR | Administration | 8 days | Add Desc+AC before any closure can be verified |
| BE#55 (#202696) — HIPAA · CHANGES_REQUESTED | Colina Health | Day 11+ | pcoronia rework + raseniero second review · dominant sprint risk |
| FE#145 (Day 16, 202594) — Husky pre-commit hooks awaiting raseniero review; FE#146 merged Apr 28 01:50 | Colina Health | 1 PR open | raseniero review · 1 SP enabler |

---

## Topic 4 — Structural Risks

1. **Activation Gap (Day 8)** — 5 of 10 teams at 0 SP closed at Day 8: Admin (39 SP committed), Finance (7), OTP (14), LS Dev (6), Auto Allies (27). ADO silence windows: Admin 25h+, Finance 72h+, LS Dev 69+. Root cause: CEO check-in cadence gap, not velocity limitation — sprint scopes are achievable.

2. **GitHub Token — Resolved** — raseniero token restored Apr 27 ~11:10 PHT. Re-audits complete: AA (Day 9 early, UPS 70.7, data_mode: full) and CC (Day 8 late, UPS 68.49). Remaining structural gap: code review bypassed on 10/11 AA PRs (Spike #202169 unresolved); CC CI/CD regression (BE removed lint + unit tests). Branch protection still unconfigured on main/develop for both Git teams; CODEOWNERS missing. External credential rotation still pending: AWS IAM key, JWT secret, DB password, Outlook password (code-level merge complete, external rotation outstanding).

3. **Bus Factor & Composition** — 4 teams single-contributor: Admin (Mark), Finance (Grace), OTP (Grace, accepted), HR (Almera) = 40% of ADO portfolio. FW App Work Item Balance at 30.0 (Critical) — zero User Stories for 8 sprints. JIT WIB regressed 100 → 70 after 7.2 → 7.3 Training re-paths (positive scope decision, structural side effect). Shared Services: 11 PI7-parent User Stories never sub-iterated (IP at 19.4%). Colina Health: Kyaa-A delivers most PRs but absent from ADO capacity roster.

---

## Topic 5 — Decisions

| Decision | Urgency | Status |
|----------|---------|--------|
| Resolve raseniero GitHub token scope | RESOLVED | Done — token restored Apr 27 11:10 PHT; AA/CC re-audits complete |
| External credential rotation post FE#157 + BE#64 merge (AWS IAM, JWT, DB, Outlook) | DO TODAY | Open — pcoronia + Ramon execute manual rotation |
| BE#55 HIPAA rework (#202696, 8 SP) — dominant Colina sprint risk | DO TODAY | Open — pcoronia rework; raseniero second review needed |
| HR Recruitment: Authorize sprint de-scope to ~22 SP | THIS WEEK | Open — PDM sign-off; move 4+ items to 7.3; realistic DP 63-73% |
| LS Dev: Close #187240 as Won't Fix | BEFORE SPRINT CLOSE | Open — removes -20 BR penalty (BR 24.3 → 44.3, Overall 61.1 → ~64.3) |
| FW App PI8: Mandate ≥1 User Story per sprint, OR formal Project Exception | PI PLANNING | Open — WIB locked at 30.0 for 8 consecutive sprints |
| Admin + HR PI8: Cap commitment at 110% of empirical velocity | PI PLANNING | Open — Admin ≤30 SP, HR ≤18 SP; PDM enforces at PI8 planning |
| Iteration 7.2 Sprint Goal — define and publish | THIS WEEK | Open — flagged across all 10 audits; Ramon publishes |

---

## Topic 6 — Action Items

### P0 — Do Today (Apr 27)

| Action | Owner | Time | Score Impact |
|--------|-------|------|-------------|
| Ramon PAT restored Apr 27 11:10 PHT — AA + CC re-audited | Ramon Aseniero | DONE | Both Git teams on full data |
| Manual external credential rotation (AWS IAM, JWT, DB, Outlook) post BE#64+FE#157 | Ramon / pcoronia | 30 min | Closes security P0 end-to-end |
| OTP: Close #203026 (2 SP) + #203029 (4 SP) — both Active 5 days | Grace (OTP) | 5 min | DP 0→42.9% · 74.8 → 80.7 Low Risk |
| Finance: Assign #203043 → Iter 7.2 + Close #203040 (1 SP) | Grace (Finance) | 3 min | +5.6 pts → 83.5 Low Risk |
| LS Dev: Ike activates #195727 (Ready → Active) — BR protection | Ike Yana | 2 min | Prevents BR 24.3 → 4.3 collapse |
| Shared Services: Fix #203296 AC + set SP on #203221, #203296, #203309 | Vicsante / Jaszmeine | 5 min | Est 42.9 → 100; ~80.3 Low Risk |
| JIT: Add Desc+AC to #203155 + #203156 (Active without DoR) | Teofilo (JIT) | 10 min | Restores DoR compliance |
| HR: Fix body defects #203057 (Ramos) + #203063 (Abina) | Almera Tayao (HR) | 5 min | Prevents recruiter confusion |
| Colina: ADO-close 5 Ready-for-UAT / Passed-QA items | per-item assignee | 10 min | SGPI 6.7 → 43.3 · UPS +5+ pts |
| pcoronia: BE#55 HIPAA rework status confirm; raseniero second review | pcoronia / Ramon | 30+ min | Unblocks 8 SP HIPAA sprint risk |

### P1 — Before Sprint Close (by May 3)

| Action | Owner | Time | Score Impact |
|--------|-------|------|-------------|
| Admin: Close #202939 (2 SP, Ready, full DoR) | Mark Colina | ADO update | DP 0 → 5.1% · breaks plateau |
| Admin: Add Desc+AC to #202898 + #202909 (Active without DoR) | Mark Colina | 10 min | Prevents unverifiable closure |
| Shared Services: Resolve #202687 (10 days title-only) — content or de-scope to 7.3 | Jaszmeine | 10 min | DoR ceiling lift |
| HR: De-scope 4+ items to 7.3 (align to ~22 SP per PDM decision) | Almera + Karl PDM | Planning | Realistic DP target |
| Auto Allies: Joseph open PRs for 4 Active items | Joseph Gerona | per item | SGPI evidence trail |
| JIT: Close #203268 (Bubble Presentation, 1 SP, UAT 4 days) | Teofilo (JIT) | 5 min | +1 SP DP credit |

### P2 — Next PI Planning

| Action | Owner | Target |
|--------|-------|--------|
| Ike (LS Dev): Dispose #187240 — close as Won't Fix | Ike Yana | Before PI7 close |
| FW App PI8: Mandate ≥1 User Story per sprint OR formalize Project Exception | Karl PDM + Luke / Ressa | PI8 Sprint Planning |
| Admin + HR PI8: Cap commitment at 110% of empirical velocity (Admin ≤30 SP, HR ≤18 SP) | Karl PDM | PI8 Sprint Planning |
| Shared Services: Sub-iterate 11 PI7-parent User Stories; +1 US to 7.3 | Karl PDM + Vicsante | 7.3 Planning |
| Colina Health: Add Asnari Pacalna (Kyaa-A) to ADO capacity roster | Karl PDM | 7.3 Setup |
| Both Git teams: Configure branch protection + CODEOWNERS on main/develop | Ramon / team leads | Before PI8 |

---

## Topic 7 — Wrap-up & Next Steps

**PI7.2 remaining milestones:**
- Day 8 (Apr 27): Activate Ready items; close Active items; restore Git token
- Day 10 (Apr 29): Mid-late check — DP should reach 40%+ portfolio-wide
- May 1: Labor Day holiday — reduced capacity
- Days 13–14 (May 2–3): Final closure; carry-forward decisions
- May 3: Sprint close — open items close or move to 7.3
- May 4: PI7.3 starts — capacity entries renewed in ADO

**Next audit cycle:** Day 9 (~Apr 28). Run `/portfolio-health` after P0 actions to confirm score lifts.

**Key PI8 diagnostic question:** Is the Day 7-8 zero-delivery pattern across 5 ADO teams a midpoint artifact or a structural execution gap? Day 9-10 data is diagnostic. Pre-write a velocity-cap policy for PI8 either way.

---

## Act-vs-no-act impact

| Act Today (P0 complete) | No Action |
|-------------------------|-----------|
| Finance + OTP cross Low Risk → 3 Low Risk teams by Day 9 | Finance misses Low Risk for 9th consecutive day |
| Shared Services pushes from 64.2 to ~80.3 Low Risk | 5 ADO teams + Auto Allies enter Day 9 still at 0 SP closed |
| LS Dev BR protected at 24.3 (prevents High Risk regression) | LS Dev at risk of BR collapse 24.3 → 4.3 if Samantha closes #203239 first |
| Colina SGPI 6.7 → 43.3; UPS into low-70s | HR #203057 + #203063 go Active with wrong candidate names |
| Portfolio Mean: 71.6 → ~74-76 by Day 9 | JIT + Admin newly-Active items remain DoR-non-compliant |
| GitHub token already restored — AA +2.4 pts (full HCI data) | BE#55 HIPAA (8 SP) slips PI7.2; Colina sprint risk dominant |
| External credential rotation closes security P0 end-to-end | Git teams: token resolved; remaining risk is code review enforcement (AA) and BE#55 rework (CC) |

---

## Differences from Apr 26 21:30 agenda

Compared to [[meeting-agenda-20260426-2130]], this agenda reflects overnight and morning activity on Apr 27:

- **GitHub token restored** (Apr 27 11:10 PHT) — AA and CC re-audited on full data; AA UPS 68.3 → 70.7, CC UPS confirmed 68.49.
- **Shared Services graduated from High Risk** (56.1 → 64.2) — 5 SP closed overnight including UAT items.
- **OTP surged +6.1** (68.7 → 74.8) via full DoR + full Estimation; OTP now 1 closure pair from Low Risk (80.7).
- **0 High Risk / 0 Critical** for first time in PI7.2 (prior agenda still showed 2 High Risk).
- **Credential rotation P0 added** — code-level FE#157 + BE#64 merged; external systems rotation still required.
- **BE#55 HIPAA rework elevated** to DO TODAY decision — Day 11+ CHANGES_REQUESTED now dominant Colina risk.
- **Sprint Goal decision added** — no published goal for 7.2 flagged across all 10 audits.
- **Bus factor count updated** — 4 single-contributor teams (Admin, Finance, OTP, HR) vs 3 in prior agenda.
- **Colina FE#146 merged** (Apr 28 01:50) — FE#145 remains last open non-HIPAA PR.
