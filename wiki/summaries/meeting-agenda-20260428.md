---
title: "Portfolio Meeting Agenda — April 28, 2026"
type: summary
tags: [meeting, agenda, portfolio, iteration-7-2]
sources: ["../../portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260428.html"]
created: 2026-04-28
updated: 2026-04-28
---

# Portfolio Meeting Agenda — April 28, 2026

**Generated:** April 28, 2026 PHT · Source: PORTFOLIO_20260428_0930.html + 10 team audits (Apr 28) · 30-minute agenda · Attendees: Ramon Aseniero (CEO), Karl Caumban (PDM) · PI7 · Iteration 7.2 · **Day 9 of 14**

> **Headline:** Portfolio mean hits 7-day high at 72.5 (+1.7 vs Apr 27). Two teams now Low Risk — Shared Services jumps +17.0 to 84.6 (first Low Risk audit ever) and HR holds at 81.4. FW App posts strongest single-day gain (+3.8). Risk concentrated in LS Dev (47.9, declining) and a delivery-throughput crisis: 7 of 10 teams at zero or near-zero SP formally closed at Day 9 (64% sprint elapsed).

---

## Meeting metadata

| Field | Value |
|-------|-------|
| PI / Iteration | PI7 · Iteration 7.2 |
| Sprint window | Apr 20 – May 3, 2026 |
| Sprint day | Day 9 of 14 |
| Duration | 30 minutes |
| Attendees | Ramon Aseniero (CEO), Karl Caumban (PDM) |
| Portfolio mean | 72.5 (+1.7 vs Apr 27) |
| Portfolio median | 73.7 (+2.5 vs Apr 27) |
| Teams at risk | 1 High Risk · 0 Critical |

---

## Agenda items

- **Topic 1 — Portfolio Snapshot & Scorecard** (3 min) — Mean 72.5 (7-day high); 2 Low Risk, 7 Moderate, 1 High Risk
- **Topic 2 — At-Risk Teams & Day-9 Watch List** (8 min) — LS Dev High Risk (47.9 declining); 5 Moderate teams with structural fragility; HR throughput watch
- **Topic 3 — Quick Wins & Escalations** (5 min) — 8 actions under 30 min; escalation table for multi-audit unactioned items
- **Topic 4 — Structural Risks** (5 min) — Delivery predictability crisis; bus factor; WIB/engineering gaps
- **Topic 5 — Decisions Needed** (4 min) — 9 decisions from DO TODAY to PI Planning
- **Topic 6 — Action Items & Owners** (3 min) — P0/P1/P2 tables with owners and score impact
- **Topic 7 — Wrap-up & Next Steps** (2 min) — PI7.2 milestones; next audit Day 10 (~Apr 29)

**Facilitator tip:** Topics 2–3 carry the most value. If time runs short, skip Topic 4 and capture structural risks as async follow-ups.

---

## Team scores — Day 9 (descending)

| Team | Score | Band | Type |
|------|-------|------|------|
| [[team-ado-shared\|Shared Services]] | 84.6 | Low Risk | ADO |
| [[team-ado-hr\|HR Recruitment]] | 81.4 | Low Risk | ADO |
| [[team-ado-fin\|Finance]] | 77.9 | Moderate | ADO |
| [[team-ado-otp\|Office of President]] | 74.8 | Moderate | ADO |
| [[team-ado-fl-dev\|Flawless Wedding App]] | 74.0 | Moderate | ADO |
| [[team-ado-admin\|Administration]] | 73.4 | Moderate | ADO |
| [[team-git-aa-dev\|Auto Allies]] | 71.0 | Moderate | Git |
| [[team-ado-jit\|JIT Operation]] | 70.4 | Moderate | ADO |
| [[team-git-cc-dev\|Colina Health]] | 69.4 | Moderate | Git |
| [[team-ado-ls-dev\|Life Style Help App]] | 47.9 | High Risk | ADO |

---

## Team highlights flagged in the agenda

- **[[team-ado-shared\|Shared Services]] (84.6, +17.0)** — First Low Risk audit ever; sprint scope expanded 8→26 items with 6 new User Stories; 20/33 SP closed. 8 of 26 items unestimated (Estimation at 69.2); DoR fix on #202464 + #203393 needed to lock Low Risk solidly at ~89.
- **[[team-ado-hr\|HR Recruitment]] (81.4)** — Stable Low Risk but zero throughput at Day 9 (last ADO activity Apr 23 19:30 UTC, 5 consecutive sprint days silent). 5 Active items, 12 Ready, 0 Closed visible. Body-text defects #203057 and #203063 persist for 11 consecutive audits. Bus factor = 1 (Almera).
- **[[team-ado-fin\|Finance]] (77.9)** — 10th consecutive audit at 77.9; 2.1 pts below Low Risk. Single fix: assign #203043 to Iter 7.2 + close #203040 (1 SP) + close #203038 (3 SP) = 87.0 Low Risk. Grace's last ADO activity Apr 27 06:52 UTC.
- **[[team-ado-otp\|OTP]] (74.8)** — Sprint scope reshuffled mid-sprint (4 items removed, 5 new US added). 0 SP closed at Day 9; two items in Resolved (#175360, #201811 = 4 SP) — closing both lifts DP to 25.0.
- **[[team-ado-fl-dev\|FW App]] (74.0, +3.8)** — 2 closures (#200791, #202723), 12/15 SP done. Path to Low Risk: #191079 + #194538 pass QA → DP 80→100 → ~81.2 Low Risk. WIB locked at 30.0 for 8+ consecutive sprints (zero User Stories).
- **[[team-ado-admin\|Administration]] (73.4, +1.3)** — DoR fix on #202909 drove today's gain. Still 0/39 SP closed (only 3 SP closed all sprint at 0.33 SP/day). Mark solo on 39 SP — over-committed; realistic ceiling 75-76 this sprint.
- **[[team-git-aa-dev\|Auto Allies]] (71.0)** — 0/29 SP closed at Day 9. FE#131 + BE#89 merged Apr 28; AB#199818 ready for QA (Jerlyn). Joseph: 3 Active items no GitHub branch (#203281, #203287, #203289). Code review bypassed on most PRs; Spike #202169 closed but enforcement not institutionalized.
- **[[team-ado-jit\|JIT Operation]] (70.4, −5.6)** — Score collapse is a rubric paradox: 17 SP / 9 items closed exit visible backlog, leaving DP=0/31. Real velocity strong. Two new unestimated items (#203241, #203410) added today drag Estimation 100→85.7.
- **[[team-git-cc-dev\|Colina Health]] (69.4)** — Strongest momentum: BE#55 (HIPAA logging, 8 SP) and FE#145 (Husky hooks, 1 SP) both merged Apr 28. 28 of 30 SP at Passed QA / Ready for UAT. Headline SGPI 6.7% vs proxy 93.3% — ADO-closing 4 Passed-QA items today lifts UPS to ~78. 3 DoD failures persist (#200093, #200828, #202028).
- **[[team-ado-ls-dev\|Life Style Help App]] (47.9, −2.8)** — High Risk and declining. New Defect #203390 added Apr 28 pushes Defect dominance to 66.7% (second WIB penalty, 40→30). Estimation collapsed 50.0→33.3. Ike Yana idle 9 consecutive sprint days; 4 stale_90 items unchanged since Dec 2025. #187240 still 253 days stale (17 audits).

---

## Risks surfaced

- **LS Dev Critical band threat** — Declining from 47.9 toward mid-40s; without reassignment of Ike and item estimates, next audit could breach Critical (<40).
- **Delivery throughput crisis** — 7 of 10 teams at zero or near-zero SP formally closed at Day 9 (64% sprint elapsed). Root causes split between rubric artifact (JIT/HR closed items exit visible backlog) and genuine execution gaps (Admin/Finance/OTP/LS Dev).
- **Bus factor = 1 in 5 teams** — Admin (Mark), Finance (Grace), HR (Almera), OTP (Grace), LS Dev (Samantha). Grace carries both Finance AND OTP (~23 SP across two teams).
- **JIT scoring paradox** — 17 SP delivered but DP=0.0; same shape masks HR real Days 2-3 throughput. Affects fairness for 3+ teams; escalated as skill rubric review item.
- **FW App WIB structural cap** — WIB locked at 30.0 for 8 consecutive sprints (zero User Stories); caps overall ceiling regardless of throughput.
- **Auto Allies code review enforcement gap** — Only ~3 of 13 in-window PRs have confirmed reviewer; Spike #202169 closed but branch protection not yet institutionalized.
- **OTP mid-sprint scope churn** — 5 new User Stories replaced 4 prior at Day 9. No formal PDM policy for Day-7+ scope changes.
- **No published Iteration 7.2 sprint goal** — Still flagged across all 10 audits.

---

## Decisions / actions noted

### DO TODAY (Apr 28)

| Decision | Owner | Impact |
|----------|-------|--------|
| LS Dev: Reassign Ike → #203247/#203390 + estimate both | Samantha + Karl PDM | Est 33→100; ~+10 pts → 58; exits High Risk |
| Finance: Assign #203043 → Iter 7.2 + Close #203040 + #203038 | Grace (Finance) | +9.1 pts → 87.0 Low Risk |
| Colina: ADO-close 4 Passed-QA items (#202594, #202595, #202690, #202696) | per-item assignee | SGPI 6.7→80+; UPS 69.4→~78 |
| OTP: Close #175360 + #201811 (both Resolved 24h) | Grace (OTP) | DP 0→25; ~+3 pts |
| Shared Services: Estimate 8 unestimated + DoR fix #202464 + #203393 | Vicsante / Jaszmeine | Est 69→100; locks Low Risk +5 |
| JIT: Set SP on #203241 + #203410 | Armelita / Samantha | Est 85.7→100; +2 pts |
| HR: Fix body defects #203057 + #203063; close 1 Active item | Almera Tayao | Defends Low Risk; breaks 5-day silence |

### Before Sprint Close (by May 3)

| Decision | Owner |
|----------|-------|
| FW App: Pass #191079 + #194538 through QA | Ressa (QA) |
| LS Dev: Close #187240 as Won't Fix (BR +20; ~+3 pts) | Ike / Samantha |
| Admin: Drive 2-3 closures from Active backlog | Mark Colina |
| Auto Allies: Jerlyn picks up AB#199818 (Ready for QA); Joseph open PRs for #203281/#203287/#203289 | Jerlyn / Joseph |
| Colina: Backfill DoD on #200093, #200828, #202028 | per-item assignee |
| Ramon: Publish Iteration 7.2 sprint goal | Ramon Aseniero |

### PI Planning

| Decision | Owner |
|----------|-------|
| FW App PI8: Mandate ≥1 User Story per sprint OR formalize Project Exception | Karl PDM + Luke/Ressa |
| Admin + LS Dev PI8: Cap commitment at empirical velocity | Karl PDM |
| Bus factor mitigation: Cross-train second contributor on Admin, Finance, HR | Karl PDM |
| Skill rubric review: Include closed items in DP denominator (JIT/HR paradox) | Ramon + skill maintainer |
| Both Git teams: Configure branch protection + CODEOWNERS on main/develop | Ramon / team leads |
| Colina Health: Add Asnari Pacalna (Kyaa-A) to ADO capacity roster | Karl PDM |

---

## Open questions

- Is the Day 9 zero-throughput pattern across 5 ADO teams a midpoint cadence artifact or a structural scope-vs-velocity gap? Day 10–11 closures are diagnostic — if Admin/Finance/OTP/HR all clear at least one Resolved item, the gap is cadence; if not, it is structural for PI8.
- Should the DP scoring rubric include closed items in the denominator to eliminate the JIT/HR visibility paradox? (Escalated to skill maintainer)
- Will LS Dev recover to Moderate band by Day 11 with reassignment, or does it require de-scoping to exit High Risk?
- Can Finance cross Low Risk before Day 10 if Grace's dual OTP load is formally prioritized by PDM?
- Is Shared Services' first-ever Low Risk reading stable, or will the 8 unestimated items drag it back to Moderate on next audit?

---

## 7-day trend (PI7.2)

Apr 22: 63.9 → Apr 23: 64.6 → Apr 24: 69.9 → Apr 25: 69.7 → Apr 26: 70.0 → Apr 27: 70.8 → **Apr 28: 72.5** (PI7.2 high)

**Next audit cycle:** Day 10 (~Apr 29). Run `/portfolio-health` after P0 actions to confirm score lifts.

---

*See also:* [[meeting-agenda-20260427]] · [[team-ado-ls-dev]] · [[team-ado-shared]] · [[team-git-cc-dev]]
