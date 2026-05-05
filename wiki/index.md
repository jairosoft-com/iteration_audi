# Wiki Index

Catalog of every page in this wiki. Agent updates this file on every ingest.

> **Also see:** [[TODO]] — persistent cross-session to-do list for things we've identified but deferred.

**Page counts:** entities 30 · concepts 6 · summaries 408 active + 1 tombstone · synthesis 20

## Synthesis

| Page | Span / Scope | Notes |
|------|--------------|-------|
| [[synthesis/portfolio-trend]] | 2026-03-25 → 2026-04-19 | 20 portfolio snapshots; 3-arc narrative (PI6 close → PI boundary → PI7.1 climb); flags 3 scoring artifacts; recomposition shock at 10-team |
| [[synthesis/iteration-7.1-close]] | PI7.1 (2026-04-06 → 2026-04-19) | Cross-team retrospective; cleanest monotonic climb (62.0 → 81.0); themes + PI7.2 forward asks |
| [[synthesis/ups-masking-pattern]] | Auto Allies case study | UPS 68.6 hides HCI 49 + SGPI 21.2%; proposes Options A+C (component columns + min-component band pill) |
| [[synthesis/scoring-artifacts]] | 4 rubric false-negatives | Perfect-sprint hold · rubric-version baseline · Day-14 T-1 fallback · JIT DP visible-board reset — carve-outs; updated 2026-04-28 |
| [[synthesis/service-model-scoring]] | Shared Services tier-aware rubric | Add team_type attribute; drop User-Story penalty for services; add Cross-Team Delivery dim |
| [[synthesis/capacity-planning]] | Portfolio's weakest spot | 3 failure modes (not-configured · overbooked · wrong-mix); proposes capacity-discipline gate for PI7.2 |
| [[synthesis/dor-leakage]] | DoR-incomplete items at commitment | 3/10 teams leaked; proposes `provisional` tag + `closed-with-debt` tracking at planning gate |
| [[synthesis/pi6-close]] | PI6 close retrospective (2026-03-31) | Mean 72.4 / median 77.1; Admin +22.1 biggest mover (capacity config + bulk-add rollback) |
| [[synthesis/pi7-plan]] | PI7.2 planning checklist | Consolidates 6+ prior syntheses; top 3 changes: capacity gate · DoR gate · UPS component breakdown |
| [[synthesis/compliance-misalignment]] | Regulatory work decoupled from ADO | #201448 Active 9 days across BIR deadline; proposes `compliance` tag + `deadline` field + receipt-based scoring |
| [[synthesis/stale-work-items]] | Chronic backlog debt | LS Dev #187240 at 244 days stalest; proposes PI-close quarterly amnesty sweep |
| [[synthesis/top-compliance-issues]] | Portfolio-wide issue ranking | 16 issues ranked by frequency; DoR + WIB + stale + bus-factor + capacity account for ~60% |
| [[synthesis/team-rankings]] | Team-by-team current score + momentum + outlook | Reproducible ranking from 270 audits; OTP only genuine decline; Auto Allies masked decline; Flawless highest momentum |
| [[synthesis/shared-services-turnaround]] | Shared Services Critical→Low journey | 32.2→84.6 in 9 sprint days; 3 structural drivers documented; fastest Low-Risk promotion in 7.2 |
| [[synthesis/score-streaks]] | Longest runs of ≥80 Low Risk | JIT 13-streak (record) · Colina 7-streak broken · HR longest active streak; Day-9 refresh 2026-04-28 |
| [[synthesis/github-compliance-issues]] | GitHub compliance for Git-audited teams | 14 issues ranked across 48 Git audits; two distinct failure modes — AA engineering-health degradation · CC review-discipline + HIPAA exposure |
| [[synthesis/ci-health]] | Engineering-health baseline for Git teams | Pre-P0 HCI: AA 49, CC 74; top 3 post-P0 metrics: required-reviewer rate · PR review latency · HIPAA 2-reviewer compliance |
| [[synthesis/bus-factor]] | Portfolio SPOF catalog | 9 signals across 7 teams; 5 delivery-side (Mark/Admin, Armelita/JIT, etc.), 2 near-1, 2 review-side; proposes ≥40% SP-concentration flag |
| [[synthesis/ado-mcp-api-patterns]] | ADO MCP API work item creation | System.Parent silent failure, Task required fields, batch linking, Gherkin in `<pre>`, preflight search; derived from Feature #203435 creation |
| [[synthesis/audit-automation]] | Consolidated roadmap | 29 auto-check rules across 4 layers (planning gates · per-audit flags · repo enforcement · dashboard widgets); priority 1: UPS component surfacing |

## Summaries — Portfolio snapshots (chronological, newest first)

| Page | Date | Mean / Median | Dist (L·M·H·C) | Headline |
|------|------|--------------:|----------------|----------|
| [[summaries/portfolio-20260429-0300]] | Apr 29 03:00 | **~77.1** / — | **4·6·0·0** | First 0 High/Critical in 7.2 · Finance+OTP promoted Low · LS Dev exits High (+16.8) |
| [[summaries/portfolio-20260428-0930]] | Apr 28 09:30 | **72.5** / 73.7 | **2·7·1·0** | Shared first Low Risk · LS Dev Day 2 High · JIT DP reset |
| [[summaries/portfolio-20260427-1110]] | Apr 27 11:10 | **70.8** / 71.2 | **1·8·1·0** | First High Risk (LS Dev 50.7) · Shared upgrade +11.5 |
| [[summaries/portfolio-20260426-1400]] | 04-26 14:00 | **70.0** / — | **1·8·1·0** | Afternoon snapshot; predates Apr 26 evening batch (OTP +6.1 + Shared +8.1 not yet reflected); evening mean computes to ~71.3 |
| [[summaries/portfolio-20260426-0935]] | 04-26 09:35 | **69.9** / — | **1·8·1·0** | Morning snapshot; Shared 56.1 sole High Risk; predates all Apr 26 evening improvements |
| [[summaries/portfolio-20260425-1533]] | 04-25 15:33 | **69.7** / 69.4 | **1·8·1·0** | Day 6 DP inflection — annotation removed; JIT +2.2 (3 closures); Flawless 53.3% DP leads; Finance 2.1 pts from Low; LS Dev one BR trigger from High Risk |
| [[summaries/portfolio-20260424-0935]] | 04-24 09:35 | **69.9** / — | **1·8·1·0** | 🎯 **Critical band cleared** (first in 7.2); **+5.3 overnight** (largest 7.2 jump); 2 upward band crossings (fl_dev, ls_dev); 3 record gains (LS +21.4, Shared +15.0, Flawless +11.1) |
| [[summaries/portfolio-20260423-1535]] | 04-23 15:35 | 64.6 / 68.0 | 1·6·2·1 | Day-4 afternoon: **Shared exits Critical · LS-Dev falls in** (first inversion); AA ICS 100% |
| [[summaries/portfolio-20260422-1000]] | 04-22 10:00 | 63.9 / 66.6 | 1·6·2·1 | Day 3 flat; only HR moved (+2.0 from 3 closures) |
| [[summaries/portfolio-20260421-0130]] | 04-21 01:30 | 63.9 / 67.2 | 1·6·2·1 | 7.2 Day 2 sprint-open; −12.2 mean vs 7.1 close |
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

## Summaries — Meeting Agendas

| Page | Date | Iteration | Headline |
|------|------|-----------|----------|
| [[summaries/meeting-agenda-20260429]] | Apr 29 | PI7.2 Day 10 | Day 10 · 4L 6M 0H 0C · Finance/OTP Low · AA/CC QA push decisions |
| [[summaries/meeting-agenda-20260428]] | Apr 28 | PI7.2 Day 9 | Day 9 portfolio review meeting agenda |
| [[summaries/meeting-agenda-20260427]] | Apr 27 | PI7.2 Day 8 | 30-min · Ramon + Karl · LS Dev High Risk + BE#55 + credential rotation |
| [[summaries/meeting-agenda-20260426-2130]] | Apr 26 21:30 | PI7.2 Day 7 | Evening refresh · JIT Low Risk path + Teofilo DoR batch |
| [[summaries/meeting-agenda-20260426]] | Apr 26 14:00 | PI7.2 Day 7 | Afternoon snapshot · scorecard + trend |
| [[summaries/meeting-agenda-20260425]] | Apr 25 | PI7.2 Day 6 | Day 6 DP inflection review |
| [[summaries/meeting-agenda-20260424]] | Apr 24 | PI7.2 Day 5 | Day 5 decisions + action items |
| [[summaries/meeting-agenda-20260423-1600]] | Apr 23 16:00 | PI7.2 Day 4 | Day 4 decisions + action items |
| [[summaries/meeting-agenda-20260421]] | Apr 21 | PI7.2 Day 2 | Sprint-open review |

## Summaries — Raw Transcripts

| Page | Date | Source | Headline |
|------|------|--------|----------|
| [[summaries/transcript-jit-review-2026-04-23]] | Apr 23 | JIT Program Alignment & LPM Review | 46 min · Ramon + Karl · P&L report action, GitHub PAT fix, task management convention, story sizing |
| [[summaries/transcript-lpm-review-2026-04-23]] | Apr 23 | Lean Portfolio Leadership Review | LPM review transcript |

## Summaries — Per-team audits

**312 audit summaries + 25 portfolio snapshots + 9 meeting agendas + 2 raw transcripts = 348 total summary pages.** Full per-team lists live in each team entity page's "Audit history" section (click through).

### Latest audit per team (Iteration 7.2 Day 10 — 2026-04-29)

> **Data modes:** ADO teams all live. Git AA partial (GitHub 404 carry-forward). Git CC full (404 resolved). DP annotation removed as of Day 6 for all teams.

| Page | Team | Score | Band | Δ vs Day 9 |
|------|------|------:|------|:-------:|
| [[summaries/audit-ado-fin-20260429-0204]] | ADO Finance | **89.6** | 🟢 Low | **+11.7 (Moderate→Low)** |
| [[summaries/audit-ado-shared-20260429-0207]] | ADO Shared | 87.4 | 🟢 Low | +2.8 |
| [[summaries/audit-ado-otp-20260429-0206]] | ADO OTP | **82.5** | 🟢 Low | **+7.7 (Moderate→Low)** |
| [[summaries/audit-ado-hr-20260429-0204]] | ADO HR | 81.4 | 🟢 Low | 0.0 |
| [[summaries/audit-ado-admin-20260429-0204]] | ADO Admin | 78.3 | 🟡 Moderate | +4.9 |
| [[summaries/audit-git-cc-dev-20260429-0241]] | Git Colina | 75.3 | 🟡 Moderate | +5.9 |
| [[summaries/audit-ado-jit-20260429-0204]] | ADO JIT | 72.9 | 🟡 Moderate | +2.5 |
| [[summaries/audit-ado-fl-dev-20260429-0204]] | ADO Flawless | 72.5 | 🟡 Moderate | −1.5 |
| [[summaries/audit-git-aa-dev-20260429-0242]] | Git AA Dev | 66.5 | 🟡 Moderate | −4.5 (partial data) |
| [[summaries/audit-ado-ls-dev-20260429-0204]] | ADO LS Dev | **64.7** | **🟡 Moderate** | **+16.8 (exits High Risk)** |

### Full audit backlog per team (counts)

| Team | Audits ingested | Span | Entity page |
|------|-----------------|------|-------------|
| Administration | 42 | 2026-02-25 → 2026-04-29 | [[entities/team-ado-admin]] |
| Finance | 41 | 2026-02-25 → 2026-04-29 | [[entities/team-ado-fin]] |
| Flawless Wedding App | 33 | 2026-03-11 → 2026-04-29 | [[entities/team-ado-fl-dev]] |
| HR Recruitment | 41 | 2026-02-25 → 2026-04-29 | [[entities/team-ado-hr]] |
| JIT Operation | 46 | 2026-02-24 → 2026-04-29 | [[entities/team-ado-jit]] |
| Life Style Help App | 34 | 2026-03-11 → 2026-04-29 | [[entities/team-ado-ls-dev]] |
| Office of the President | 40 | 2026-02-24 → 2026-04-29 | [[entities/team-ado-otp]] |
| Shared Services | 9 | 2026-04-19 → 2026-04-29 | [[entities/team-ado-shared]] |
| Auto Allies (Git) | 35 | 2026-03-09 → 2026-04-29 | [[entities/team-git-aa-dev]] |
| Colina Health (Git) | 30 | 2026-03-11 → 2026-04-29 | [[entities/team-git-cc-dev]] |
| **Total** | **351** | **2026-02-24 → 2026-04-29** | — |
| (Plus 9 portfolio snapshots + 9 meeting agendas + 2 transcripts ingested 4/21–4/29) | | | |

## Entities (teams · people · systems)

### Teams — ADO (8)

| Page | Latest overall | Band | Latest summary |
|------|---------------:|------|----------------|
| [[entities/team-ado-admin]] | 78.3 | 🟡 Moderate | [[summaries/audit-ado-admin-20260429-0204]] |
| [[entities/team-ado-fin]] | **89.6** | 🟢 Low | [[summaries/audit-ado-fin-20260429-0204]] |
| [[entities/team-ado-fl-dev]] | 72.5 | 🟡 Moderate | [[summaries/audit-ado-fl-dev-20260429-0204]] |
| [[entities/team-ado-hr]] | **81.4** | 🟢 Low | [[summaries/audit-ado-hr-20260429-0204]] |
| [[entities/team-ado-jit]] | 72.9 | 🟡 Moderate | [[summaries/audit-ado-jit-20260429-0204]] |
| [[entities/team-ado-ls-dev]] | 64.7 | 🟡 Moderate | [[summaries/audit-ado-ls-dev-20260429-0204]] |
| [[entities/team-ado-otp]] | **82.5** | 🟢 Low | [[summaries/audit-ado-otp-20260429-0206]] |
| [[entities/team-ado-shared]] | **87.4** | 🟢 Low | [[summaries/audit-ado-shared-20260429-0207]] |

### Teams — Git (2)

| Page | Latest UPS | Band | Latest summary |
|------|-----------:|------|----------------|
| [[entities/team-git-aa-dev]] | UPS 66.5 | 🟡 Moderate | [[summaries/audit-git-aa-dev-20260429-0242]] |
| [[entities/team-git-cc-dev]] | UPS 75.3 | 🟡 Moderate | [[summaries/audit-git-cc-dev-20260429-0241]] |

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
| [[entities/person-almera]] | Sole HR operator (bus-factor-1) | [[entities/team-ado-hr]] |
| [[entities/person-teofilo]] | Instructor (JIT) + DevOps/IT (Shared Services) | [[entities/team-ado-jit]], [[entities/team-ado-shared]] |
| [[entities/person-jaszmeine]] | Design (Colina Health + Shared Services) — non-dev exception | [[entities/team-git-cc-dev]], [[entities/team-ado-shared]] |
| [[entities/person-vicsante]] | Developer (Shared Services) — Jodex owner | [[entities/team-ado-shared]] |
| [[entities/person-ike]] | Developer (LS Dev, Flawless) — 253-day stale item | [[entities/team-ado-ls-dev]], [[entities/team-ado-fl-dev]] |
| [[entities/person-luke]] | Primary developer (Flawless) | [[entities/team-ado-fl-dev]] |
| [[entities/person-cliff]] | Developer (Auto Allies) | [[entities/team-git-aa-dev]] |
| [[entities/person-samantha-babael]] | Developer/Documentation (LS Dev, JIT) — cross-team | [[entities/team-ado-ls-dev]], [[entities/team-ado-jit]] |
| [[entities/person-kyaa-a]] | Developer — Asnari Pacalna (Colina Health) | [[entities/team-git-cc-dev]] |
| [[entities/person-pcoronia]] | Lead Developer — Paul Coronia (Colina Health) | [[entities/team-git-cc-dev]] |

### Systems

| Page | Scope | Status |
|------|-------|--------|
| [[entities/system-macpilot]] | `scripts/agents/` — launchd-scheduled Claude CLI harness (MacPilot, MIT, © Raul Riera) | 5 production wrappers shipped 2026-04-23 (08:30/09:00/09:30/09:45/09:50 daily portfolio chain); vendored as git subtree (3 commits) |
| [[entities/system-jodex]] | Rust CLI + plugin marketplace (Claude Code, Codex, Gemini) — QA automation, product management skills | 3 Features in ADO (#200094 Closed, #203319 Active, #203435 New); owned by Vicsante; 21 SP queued in 7.2 |

## Concepts

| Page | Domain | Referenced by |
|------|--------|---------------|
| [[concepts/scoring-ado-rubric]] | ADO audits | 8 ADO entities, all ADO/portfolio summaries, 4 syntheses |
| [[concepts/scoring-git-ups]] | Git audits | Git entities + summaries, [[synthesis/ups-masking-pattern]], [[synthesis/portfolio-trend]] |
| [[concepts/risk-bands]] | Both | every entity, every summary, every synthesis |
| [[concepts/compliance-deadlines]] | Regulatory (BIR / eAFS) | [[entities/team-ado-fin]], [[entities/person-grace]], [[synthesis/iteration-7.1-close]], [[synthesis/compliance-misalignment]] |
| [[concepts/stakeholder-roles]] | Governance (PDM/PM/EM/PO/SM) | All person entities; [[synthesis/pi7-plan]] |
| [[concepts/headless-skill-mode]] | Skill design (scheduled / unattended invocation) | [[entities/system-macpilot]], `.claude/skills/portfolio-email/SKILL.md` §Step 6.5 |
| [[concepts/ado-mcp-call-patterns]] | ADO MCP tooling rules (always use IDs) | [[entities/team-ado-otp]], all ADO audit skills |

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
