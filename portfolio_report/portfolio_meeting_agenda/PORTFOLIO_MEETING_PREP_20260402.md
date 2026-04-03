# Portfolio Review — April 2, 2026

**Iteration 6.6 (IP) | Day 11 of 14 | 3 working days left**
Ramon Aseniero (CEO) + Karl Caumban (PDM) | 30 min

---

## Agenda

| # | Topic | Time | Purpose |
|---|-------|------|---------|
| 1 | Portfolio Snapshot + Scorecard | 3 min | Set context — where we stand today |
| 2 | Critical & High Risk Teams | 8 min | Deep dive on 5 at-risk teams |
| 3 | Quick Wins & Escalations | 5 min | OTP fix, HR PI7 assignment, Finance PO acceptance |
| 4 | Structural Risks | 5 min | Backlog debt, engineering gaps, bus factor |
| 5 | Decisions | 4 min | 5 items needing Karl's sign-off |
| 6 | Action Items & Owners | 3 min | Assign P0 actions, confirm owners |
| 7 | Wrap-up & Next Steps | 2 min | PI7 readiness, follow-up cadence |
| | **Total** | **30 min** | |

**Facilitator tip:** Topics 2-3 carry the most value. If time runs short, skip Topic 4 and capture structural risks as async follow-ups.

---

## Topic 1: Portfolio Snapshot + Scorecard (3 min)

| Metric | Value | vs Apr 1 |
|--------|-------|----------|
| Mean | 59.6 | -5.1 |
| Median | 59.2 | -13.1 |
| At Risk | 5 of 9 | 3 High + 2 Critical |

**Why the drop?** Holy Week freeze (5 boards inactive) + Administration sprint evacuation (-45.6). Seasonal, not systemic.

| Team | Score | Band | Trend | One-Line Status |
|------|-------|------|-------|-----------------|
| Finance | 84.6 | Low | = | Stable. Ramon: accept #200432, #200446 (11 days overdue) |
| JIT | 82.8 | Low | = | Stable. 3 items stale 8-9 days — verify armelita |
| Colina Health | 82.7 | Low | -1.1 | Sprint done (4/4 stories). 7 defects untriaged today |
| **OTP** | **77.1** | **Mod** | **= x5** | **2.9 pts from Low Risk. Fix: close 2 items (5 min). Unactioned 7 audits** |
| Life Style Help | 59.2 | High | = x3 | Frozen. Backlog Refinement 0.0 for 7 audits. 30 stale items |
| Auto Allies | 49.7 | High | +0.3 | Zero code reviews (41 PRs). No branch protection |
| Flawless Wedding | 46.8 | High | +0.1 | 9 items at Passed UAT/QA but zero closures. 51 stale items |
| Administration | 26.7 | Crit | -45.6 | Sprint evacuated to PI7. Intentional. Expect recovery |
| HR Recruitment | 26.7 | Crit | = | Scoring artifact. Actual: 14/14 items, 27/27 SP. **16 items unassigned to PI7** |

---

## Topic 2: Critical & High Risk Teams (8 min)

**Critical — acknowledge and move on (2 min):**

- **Administration (26.7):** Sprint evacuated to PI7. Intentional Holy Week action. Score will recover when PI7 populates. No corrective action needed — just PI7 backlog prep.
- **HR Recruitment (26.7):** Scoring artifact. Actual delivery is perfect (14/14 items, 27/27 SP, 2nd consecutive perfect sprint). **Real issue:** 16 items unassigned to any PI7 iteration. Must assign today.

**High Risk — where to focus (6 min):**

- **Life Style Help (59.2):** Frozen 3 audits. Backlog Refinement 0.0 for 7 audits. 30 items >180 days. No board activity. Single contributor (Samantha). This team needs the most intervention.
- **Auto Allies (49.7):** Zero code reviews across 41 PRs. No branch protection. SGPI at 42.9%. Highest engineering risk in portfolio.
- **Flawless Wedding (46.8):** 9 items substantively complete (Passed UAT/QA) but not formally closed. 51 stale items. Luke carries 67% of sprint.

---

## Topic 3: Quick Wins & Escalations (5 min)

| Win | Impact | Effort | Who |
|-----|--------|--------|-----|
| Close OTP #199522 + #200686 | 77.1 to ~80.9 (Low Risk) | 5 min | Grace — escalate? |
| Close 9 Flawless Wedding UAT/QA items | +13 SP delivery credit | 30 min | Luke |
| Accept Finance #200432, #200446 | Clears 11-day PO backlog | 10 min | Ramon (self) |
| Assign 16 HR items to PI7 | Unblocks PI7 planning | 30 min | Karl + Almera |

---

## Topic 4: Structural Risks (5 min)

*If running short on time, capture these as async follow-ups.*

1. **Backlog debt:** Life Style Help (30 items >180d), Flawless Wedding (51 items), Auto Allies. Schedule a portfolio grooming day Apr 3-5?
2. **Engineering gaps:** Neither Git team has branch protection. Auto Allies has 0% code review coverage. Mandate for PI7 DoD?
3. **Bus Factor = 1:** Admin (Mark), Finance (Grace), HR (Almera), OTP (Grace), Life Style Help (Samantha). Set cross-training targets for PI7?

---

## Topic 5: Decisions (4 min)

| # | Decision | Urgency | Yes/No |
|---|----------|---------|--------|
| 1 | Escalate OTP closures to Grace | Today | |
| 2 | Approve HR PI7 assignment (16 items) | Today | |
| 3 | Schedule sprint close blitz call Apr 3 | Today | |
| 4 | Approve backlog grooming day (3 teams) | This week | |
| 5 | Mandate branch protection for Git teams in PI7 | This week | |

---

## Topic 6: Action Items & Owners (3 min)

### Do Today

| Action | Owner | Est. |
|--------|-------|------|
| Assign 16 HR items to PI7 | Karl/Almera | 30 min |
| Close OTP #199522, #200686 | Grace | 5 min |
| Accept Finance #200432, #200446 | Ramon | 10 min |
| Close 9 Flawless Wedding UAT/QA items | Luke | 30 min |

### Do Before Sprint Close (Apr 5)

| Action | Owner | Est. |
|--------|-------|------|
| Purge stale items: LSH (30), FW (51) | Team leads | 2 hr |
| Enable branch protection (AA, Colina) | Dev leads | 15 min |
| Fix DoR on 4 Admin PI7 items | Mark | 30 min |
| Triage 7 Colina Health defects | Dev team | 1 hr |

---

## Topic 7: Wrap-up & Next Steps (2 min)

**PI7 readiness (Karl to own):**
- Define iteration goals for all 9 teams
- Set cross-training targets for single-contributor teams
- Configure Holy Week days-off in capacity settings

**Impact of acting today vs not:**

| Scenario | Mean | OTP | Outcome |
|----------|------|-----|---------|
| No action | ~59-60 | Stays Moderate | Flat through sprint close |
| P0 done today | ~62-64 | ~80.9 (Low Risk) | 4th team enters Low Risk |

**Follow-up:** Next portfolio review after PI7 Day 3 to re-baseline.

---

*Source: 9 team audits, 7 portfolio dashboards | `PORTFOLIO_20260402_0900.html`*
