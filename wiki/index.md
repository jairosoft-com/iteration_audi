# Wiki Index

Catalog of every page in this wiki. Agent updates this file on every ingest.

**Page counts:** entities 19 · concepts 5 · summaries 299 active + 1 tombstone · synthesis 18

## Synthesis

| Page | Span / Scope | Notes |
|------|--------------|-------|
| [[synthesis/portfolio-trend]] | 2026-03-25 → 2026-04-19 | 20 portfolio snapshots; 3-arc narrative (PI6 close → PI boundary → PI7.1 climb); flags 3 scoring artifacts; recomposition shock at 10-team |
| [[synthesis/iteration-7.1-close]] | PI7.1 (2026-04-06 → 2026-04-19) | Cross-team retrospective; cleanest monotonic climb (62.0 → 81.0); themes + PI7.2 forward asks |
| [[synthesis/ups-masking-pattern]] | Auto Allies case study | UPS 68.6 hides HCI 49 + SGPI 21.2%; proposes Options A+C (component columns + min-component band pill) |
| [[synthesis/scoring-artifacts]] | 3 rubric false-negatives | Perfect-sprint hold · rubric-version baseline · Day-14 T-1 fallback — carve-outs |
| [[synthesis/service-model-scoring]] | Shared Services tier-aware rubric | Add team_type attribute; drop User-Story penalty for services; add Cross-Team Delivery dim |
| [[synthesis/capacity-planning]] | Portfolio's weakest spot | 3 failure modes (not-configured · overbooked · wrong-mix); proposes capacity-discipline gate for PI7.2 |
| [[synthesis/dor-leakage]] | DoR-incomplete items at commitment | 3/10 teams leaked; proposes `provisional` tag + `closed-with-debt` tracking at planning gate |
| [[synthesis/pi6-close]] | PI6 close retrospective (2026-03-31) | Mean 72.4 / median 77.1; Admin +22.1 biggest mover (capacity config + bulk-add rollback) |
| [[synthesis/pi7-plan]] | PI7.2 planning checklist | Consolidates 6+ prior syntheses; top 3 changes: capacity gate · DoR gate · UPS component breakdown |
| [[synthesis/compliance-misalignment]] | Regulatory work decoupled from ADO | #201448 Active 9 days across BIR deadline; proposes `compliance` tag + `deadline` field + receipt-based scoring |
| [[synthesis/stale-work-items]] | Chronic backlog debt | LS Dev #187240 at 244 days stalest; proposes PI-close quarterly amnesty sweep |
| [[synthesis/top-compliance-issues]] | Portfolio-wide issue ranking | 16 issues ranked by frequency; DoR + WIB + stale + bus-factor + capacity account for ~60% |
| [[synthesis/team-rankings]] | Team-by-team current score + momentum + outlook | Reproducible ranking from 270 audits; OTP only genuine decline; Auto Allies masked decline; Flawless highest momentum |
| [[synthesis/score-streaks]] | Longest runs of ≥80 Low Risk | JIT 13-streak (record) · Colina 7-streak (active) · Finance 48% cumulative; 4 of top 5 streaks broken by rubric-transition artifact |
| [[synthesis/github-compliance-issues]] | GitHub compliance for Git-audited teams | 14 issues ranked across 48 Git audits; two distinct failure modes — AA engineering-health degradation · CC review-discipline + HIPAA exposure |
| [[synthesis/ci-health]] | Engineering-health baseline for Git teams | Pre-P0 HCI: AA 49, CC 74; top 3 post-P0 metrics: required-reviewer rate · PR review latency · HIPAA 2-reviewer compliance |
| [[synthesis/bus-factor]] | Portfolio SPOF catalog | 9 signals across 7 teams; 5 delivery-side (Mark/Admin, Armelita/JIT, etc.), 2 near-1, 2 review-side; proposes ≥40% SP-concentration flag |
| [[synthesis/audit-automation]] | Consolidated roadmap | 29 auto-check rules across 4 layers (planning gates · per-audit flags · repo enforcement · dashboard widgets); priority 1: UPS component surfacing |

## Summaries — Portfolio snapshots (chronological, newest first)

| Page | Date | Mean / Median | Dist (L·M·H·C) | Headline |
|------|------|--------------:|----------------|----------|
| [[summaries/portfolio-20260419-1953]] | 04-19 19:53 | 76.1 / 80.9 | 5·4·0·1 | 10-team recomposition; Shared Services baseline |
| [[summaries/portfolio-20260419-1345]] | 04-19 13:45 | 81.0 / 82.4 | 5·4·0·0 | 🎯 peak portfolio health; first full-cycle zero-Critical |
| [[summaries/portfolio-20260417-0900]] | 04-17 09:00 | 72.1 / 78.4 | 3·4·1·1 | 🚧 Life Style formula artifact (77.1→11.2) |
| [[summaries/portfolio-20260416-0900]] | 04-16 09:00 | 77.6 / 78.4 | 4·5·0·0 | first zero-High-and-Critical; Auto Allies QA Crisis |
| [[summaries/portfolio-20260413-1800]] | 04-13 18:00 | 75.6 / 77.6 | 2·7·0·0 | High band emptied; Flawless +18.6 |
| [[summaries/portfolio-20260412-1800]] | 04-12 18:00 | 70.0 / 71.1 | 2·5·2·0 | JIT -10.5 regression |
| [[summaries/portfolio-20260409-1800]] | 04-09 18:00 | 70.4 / 75.6 | 2·5·2·0 | JIT promoted Low 81.6 |
| [[summaries/portfolio-20260408-1800]] | 04-08 18:00 | 68.5 / 74.9 | 1·6·2·0 | Colina +28.3 High→Low |
| [[summaries/portfolio-20260407-1800]] | 04-07 18:00 | 64.4 / 66.3 | 1·4·4·0 | HR 91.1 sole Low; Colina ICS drop |
| [[summaries/portfolio-20260406-0900]] | 04-06 09:00 | 62.0 / 66.9 | 0·5·4·0 | PI7 Day 1; HR +53.2, Admin +45.4 |
| [[summaries/portfolio-20260405-0900]] | 04-05 09:00 | 56.9 / 63.1 | 1·4·2·2 | 🚧 rubric transition 6-dim→7-dim |
| [[summaries/portfolio-20260404-0155]] | 04-04 01:55 | 60.4 / 61.4 | 4·1·2·2 | JIT leads 86.8 |
| [[summaries/portfolio-20260402-0900]] | 04-02 09:00 | 59.6 / 59.2 | 3·1·3·2 | Admin Holy Week / IP evacuation (-45.6) |
| [[summaries/portfolio-20260401-0900]] | 04-01 09:00 | 64.7 / 72.3 | 3·2·3·1 | 🚧 HR perfect-sprint artifact (-63.4) |
| [[summaries/portfolio-20260331-0900]] | 03-31 09:00 | 72.4 / 77.1 | 3·3·3·0 | Admin +22.1, Colina +19.5 |
| [[summaries/portfolio-20260330-0900]] | 03-30 09:00 | 67.6 / 60.3 | 3·2·4·0 | first zero-Critical; Auto Allies promoted |
| [[summaries/portfolio-20260328-0900]] | 03-28 09:00 | 66.1 / 60.3 | 3·2·3·1 | LS Dev crosses into Moderate |
| [[summaries/portfolio-20260326-1651]] | 03-26 16:51 | 65.7 / 58.5 | 3·1·4·1 | OTP enters at 78.2 |
| [[summaries/portfolio-20260325-1900]] | 03-25 19:00 | 64.3 / 57.8 | 3·0·4·1 | baseline; AA Dev Critical |

## Summaries — Per-team audits

**280 audit summaries** across 10 workspaces. Full per-team lists live in each team entity page's "Audit history" section (click through).

### Latest audit per team (Iteration 7.2 Day 2 sprint-open, 2026-04-21)

| Page | Team | Score | Band | Δ vs 7.1 close |
|------|------|------:|------|:--------------:|
| [[summaries/audit-ado-admin-20260421-0800]] | Administration | 69.5 | 🟡 Moderate | −17.5 |
| [[summaries/audit-ado-fin-20260421-0800]] | Finance | 77.9 | 🟡 Moderate | −15.8 |
| [[summaries/audit-ado-fl-dev-20260421-0800]] | Flawless | 59.6 | 🟠 High | −19.7 |
| [[summaries/audit-ado-hr-20260421-1400]] | HR | 81.4 | 🟢 Low | −5.6 |
| [[summaries/audit-ado-jit-20260421-1400]] | JIT | 72.9 | 🟡 Moderate | **+4.1** (Grace blocker removed) |
| [[summaries/audit-ado-ls-dev-20260421-1400]] | Life Style | 41.0 | 🟠 High | −41.4 (2-item sprint) |
| [[summaries/audit-ado-otp-20260421-0930]] | OTP | 64.8 | 🟡 Moderate | −6.4 (#198587 CLOSED ✓) |
| [[summaries/audit-ado-shared-20260421-0930]] | Shared Services | 37.7 | 🔴 Critical | +5.5 (capacity STILL missing) |
| [[summaries/audit-git-aa-dev-20260421-0900]] | Auto Allies | ICS 95.3 · HCI 53 · SGPI 0.0% | HCI 🔴 Critical | HCI +4 · 1st human PR review in team |
| [[summaries/audit-git-cc-dev-20260421-0055]] | Colina | ICS 93.6 · HCI 79 · SGPI 0.0% | HCI 🟡 Moderate+ | HCI +5 · reviewer bottleneck broke |

> **Day 2 early-sprint context:** Delivery Predictability = 0.0 across all ADO teams; SGPI 0.0% on both Git teams. Many "drops" are denominator effects from un-started iteration items, not regressions. See each summary's TL;DR for the distinction.

### Full audit backlog per team (counts)

| Team | Audits ingested | Span | Entity page |
|------|-----------------|------|-------------|
| Administration | 35 | 2026-02-25 → 2026-04-21 | [[entities/team-ado-admin]] |
| Finance | 34 | 2026-02-25 → 2026-04-21 | [[entities/team-ado-fin]] |
| Flawless Wedding App | 26 | 2026-03-11 → 2026-04-21 | [[entities/team-ado-fl-dev]] |
| HR Recruitment | 34 | 2026-02-25 → 2026-04-21 | [[entities/team-ado-hr]] |
| JIT Operation | 39 | 2026-02-24 → 2026-04-21 | [[entities/team-ado-jit]] |
| Life Style Help App | 27 | 2026-03-11 → 2026-04-21 | [[entities/team-ado-ls-dev]] |
| Office of the President | 33 | 2026-02-24 → 2026-04-21 | [[entities/team-ado-otp]] |
| Shared Services | 2 | 2026-04-19 → 2026-04-21 | [[entities/team-ado-shared]] |
| Auto Allies (Git) | 27 | 2026-03-09 → 2026-04-21 | [[entities/team-git-aa-dev]] |
| Colina Health (Git) | 23 | 2026-03-11 → 2026-04-21 | [[entities/team-git-cc-dev]] |
| **Total** | **280** | **2026-02-24 → 2026-04-21** | — |

## Entities (teams · people · systems)

### Teams — ADO (8)

| Page | Latest overall | Band | Latest summary |
|------|---------------:|------|----------------|
| [[entities/team-ado-admin]] | 87.0 | 🟢 Low | [[summaries/audit-ado-admin-20260419-1345]] |
| [[entities/team-ado-fin]] | 93.7 | 🟢 Low | [[summaries/audit-ado-fin-20260419-1345]] |
| [[entities/team-ado-fl-dev]] | 79.3 | 🟡 Moderate | [[summaries/audit-ado-fl-dev-20260419-1345]] |
| [[entities/team-ado-hr]] | 87.0 | 🟢 Low | [[summaries/audit-ado-hr-20260419-1345]] |
| [[entities/team-ado-jit]] | 68.8 | 🟡 Moderate | [[summaries/audit-ado-jit-20260419-1345]] |
| [[entities/team-ado-ls-dev]] | 82.4 | 🟢 Low | [[summaries/audit-ado-ls-dev-20260419-1345]] |
| [[entities/team-ado-otp]] | 71.2 | 🟡 Moderate | [[summaries/audit-ado-otp-20260419-1345]] |
| [[entities/team-ado-shared]] | 32.2 | 🔴 Critical | [[summaries/portfolio-20260419-1953]] |

### Teams — Git (2)

| Page | Latest UPS | Band | Latest summary |
|------|-----------:|------|----------------|
| [[entities/team-git-aa-dev]] | 68.6 | 🟡 Moderate (masking Critical) | [[summaries/audit-git-aa-dev-20260419-1345]] |
| [[entities/team-git-cc-dev]] | 90.6 | 🟢 Low | [[summaries/audit-git-cc-dev-20260419-1345]] |

### People

| Page | Role | Teams |
|------|------|-------|
| [[entities/person-ramon]] | CEO & audit owner | All 10 workspaces |
| [[entities/person-grace]] | Finance/Admin · JIT Documentation (1h/day) | [[entities/team-ado-fin]], [[entities/team-ado-jit]] |
| [[entities/person-carol]] | PM (Shared Services rostered) · IC on Flawless spikes | [[entities/team-ado-shared]], [[entities/team-ado-fl-dev]] |
| [[entities/person-mark-colina]] | Sole Administration team member (bus-factor-1) | [[entities/team-ado-admin]] |
| [[entities/person-jerlyn]] | Auto Allies QA/Requirements · zero-contribution 3+ sprints | [[entities/team-git-aa-dev]] |
| [[entities/person-karl]] | Portfolio Delivery Manager | All 10 workspaces (portfolio-wide) |
| [[entities/person-bomar]] | Engineering Manager | Portfolio-wide; primarily Git + ADO dev teams |
| [[entities/person-armelita]] | PM + PO + IC for JIT (triple-hat) | [[entities/team-ado-jit]] — routinely 70–80%+ SP concentration |

### Systems

| Page | Scope | Status |
|------|-------|--------|
| [[entities/system-macpilot]] | `scripts/agents/` — launchd-scheduled Claude CLI harness (MacPilot, MIT, © Raul Riera) | Scaffolding vendored, untracked in git; no custom agents written yet (only `example.sh`) |

## Concepts

| Page | Domain | Referenced by |
|------|--------|---------------|
| [[concepts/scoring-ado-rubric]] | ADO audits | 8 ADO entities, all ADO/portfolio summaries, 4 syntheses |
| [[concepts/scoring-git-ups]] | Git audits | Git entities + summaries, [[synthesis/ups-masking-pattern]], [[synthesis/portfolio-trend]] |
| [[concepts/risk-bands]] | Both | every entity, every summary, every synthesis |
| [[concepts/compliance-deadlines]] | Regulatory (BIR / eAFS) | [[entities/team-ado-fin]], [[entities/person-grace]], [[synthesis/iteration-7.1-close]], [[synthesis/compliance-misalignment]] |
| [[concepts/stakeholder-roles]] | Governance (PDM/PM/EM/PO/SM) | All person entities; [[synthesis/pi7-plan]] |

## Next content candidates

All prior backlogs drafted. Natural next additions as new audit data or reviews arrive:

- **synthesis/pi7-close** — write after PI7 PI-close (end of 7.2)
- **synthesis/ci-health** — engineering-practice deep-dive using Git team HCI data (feed to [[entities/person-bomar]])
- **synthesis/bus-factor** — portfolio-wide single-point-of-failure catalog ([[entities/person-mark-colina]] is the seed case)
- **concepts/iteration-cadence** — define PI vs iteration vs IP week boundaries so audit comparisons are unambiguous
- **concepts/dor-definition** — canonical checklist version (what Description/AC/SP thresholds constitute DoR)
- **synthesis/audit-automation** — proposals from the last several syntheses that rely on skill-level automation (capacity pre-check, DoR gate, UPS component surfacing, stale-item sweep)

## Conventions

- `[[wiki-page]]` for internal links; relative paths (`../ado_shared/audit/AUDIT_*.md`) for raw sources
- Filenames: `kebab-case.md`
- See [CLAUDE.md](CLAUDE.md) for full schema
