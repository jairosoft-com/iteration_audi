# Plan: Wiki Batch Ingest — Apr 28, 2026 (PI7.2 Day 9)

## Context

Daily audit batch for Apr 28 has run. Wiki last updated: Apr 27 batch (pending commit). 13 new sources need ingestion across 8 ADO teams, 2 Git teams (3 files), portfolio dashboard, and meeting agenda.

**Critical signals:**
- ADO Shared: +17.0 → first Low Risk audit ever for that team
- ADO LS Dev: 47.9 (still High Risk, −2.8 from yesterday — declining)
- ADO JIT: −5.6, DP reset to 0.0
- git_aa_dev: two runs today (0247 = overnight crossover, 0902 = Day 9 proper)

---

## Source Inventory

| # | Source file | Wiki slug | Priority |
|---|---|---|---|
| 1 | `ado_admin/audit/AUDIT_20260428_0902.md` | `audit-ado-admin-20260428-0902` | normal |
| 2 | `ado_fin/audit/AUDIT_20260428_0902.md` | `audit-ado-fin-20260428-0902` | normal |
| 3 | `ado_fl_dev/audit/AUDIT_20260428_0902.md` | `audit-ado-fl-dev-20260428-0902` | normal |
| 4 | `ado_hr/audit/AUDIT_20260428_0203.md` | `audit-ado-hr-20260428-0203` | normal |
| 5 | `ado_jit/audit/AUDIT_20260428_0203.md` | `audit-ado-jit-20260428-0203` | **HIGH** (DP reset) |
| 6 | `ado_ls_dev/audit/AUDIT_20260428_0203.md` | `audit-ado-ls-dev-20260428-0203` | **HIGH** (continued High Risk) |
| 7 | `ado_otp/audit/AUDIT_20260428_0204.md` | `audit-ado-otp-20260428-0204` | normal |
| 8 | `ado_shared/audit/AUDIT_20260428_0204.md` | `audit-ado-shared-20260428-0204` | **HIGH** (band upgrade +17.0) |
| 9 | `git_aa_dev/audit/AUDIT_20260428_0247.md` | `audit-git-aa-dev-20260428-0247` | normal (overnight crossover) |
| 10 | `git_aa_dev/audit/AUDIT_20260428_0902.md` | `audit-git-aa-dev-20260428-0902` | **canonical Day 9** |
| 11 | `git_cc_dev/audit/AUDIT_20260428_0241.md` | `audit-git-cc-dev-20260428-0241` | normal |
| 12 | `portfolio_report/PORTFOLIO_20260428_0930.html` | `portfolio-20260428-0930` | normal |
| 13 | `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260428.html` | `meeting-agenda-20260428` | normal |

### Note on git_aa_dev dual files

`AUDIT_20260428_0247.md` = overnight run (Day 8 crossover, PHT timezone). `AUDIT_20260428_0902.md` = Day 9 proper run. Ingest both; treat _0902 as canonical Day 9. Mark _0247 with `data_mode: CROSSOVER · SUPERSEDED by 20260428-0902` in its summary.

---

## Scores Preview (Day 9)

| Team | Score | Band | Δ | Key signal |
|------|------:|------|---|---|
| ADO Shared | **84.6** | 🟢 Low | **+17.0** | **First Low Risk ever for this team** |
| ADO HR | 81.4 | 🟢 Low | 0.0 | 5 consecutive days without closure |
| ADO Finance | 77.9 | 🟡 Moderate | 0.0 | 10-audit plateau at 77.9 |
| ADO Flawless | 74.0 | 🟡 Moderate | +3.8 | Two closures break velocity stall |
| ADO OTP | 74.8 | 🟡 Moderate | 0.0 | Zero SP closed at Day 9 |
| ADO Admin | 73.4 | 🟡 Moderate | +1.3 | Over-commitment remains structural |
| ADO JIT | 70.4 | 🟡 Moderate | **−5.6** | DP reset to 0.0 |
| ADO LS Dev | **47.9** | **🟠 High** | **−2.8** | Entire sprint reactive defects |
| Git AA Dev (0902) | UPS 71.0 | 🟡 Moderate | +0.3 | PR #131+#89 merged for #199818 |
| Git AA Dev (0247) | UPS 70.7 | 🟡 Moderate | +2.4 | Crossover run |
| Git Colina | UPS 69.39 | 🟡 Moderate | +0.90 | 28 SP queued at QA/UAT; ADO state lag |

---

## Execution Plan (4 phases, sequenced to avoid shared-file conflicts)

### Phase 1 — Parallel: ADO team summaries + entity updates (3 agents)

Do NOT write to `index.md`, `log.md`, or `synthesis/` in this phase. Summaries + entities only.

**ADO Agent A** (`ado_admin`, `ado_fin`, `ado_fl_dev`):
- Read each source audit fully
- Create 3 summary pages in `wiki/summaries/` (YAML frontmatter, 7-dim score table, key signals, open questions)
- Update 3 entity pages in `wiki/entities/` (score, band, `updated` date, latest audit link)

**ADO Agent B** (`ado_hr`, `ado_jit`, `ado_ls_dev`):
- Same as Agent A
- For JIT: flag DP reset to 0.0 with `> ⚠️` callout
- For LS Dev: extend band-drop callout from Day 8; note 2nd consecutive High Risk day and reactive-only sprint composition

**ADO Agent C** (`ado_otp`, `ado_shared`):
- Same as Agent A
- For Shared: add `> ✅ BAND UPGRADE` callout — first Low Risk; note the +17.0 jump driver

### Phase 2 — Parallel: Git team summaries + entity updates (2 agents, after Phase 1)

**Git Agent D** (`git_aa_dev` — both files):
- Create `audit-git-aa-dev-20260428-0247` with `data_mode: CROSSOVER · SUPERSEDED by 20260428-0902`
- Create `audit-git-aa-dev-20260428-0902` as canonical Day 9 (UPS 71.0, PR merges noted)
- Update `entities/team-git-aa-dev.md` with _0902 as authoritative Day 9

**Git Agent E** (`git_cc_dev`):
- Create `audit-git-cc-dev-20260428-0241` (UPS 69.39, 28 SP at QA/UAT, ADO state lag)
- Update `entities/team-git-cc-dev.md`

### Phase 3 — Parallel: Portfolio + meeting agenda (2 agents, after Phase 1+2)

**Agent F** (portfolio):
- Parse `PORTFOLIO_20260428_0930.html` for team scores, mean, median, band distribution
- Create `wiki/summaries/portfolio-20260428-0930.md`

**Agent G** (meeting agenda):
- Parse `PORTFOLIO_MEETING_AGENDA_20260428.html`
- Create `wiki/summaries/meeting-agenda-20260428.md`
- Extract: agenda items, team highlights, risks surfaced, decisions/actions

### Phase 4 — Sequential: Synthesis updates (1 agent, after Phase 1+2+3 complete)

**Synthesis Agent**:
1. Update `synthesis/portfolio-trend.md` — append Apr 28 data point (mean, band dist, Shared upgrade + LS Dev continued decline)
2. Update `synthesis/team-rankings.md` — refresh scores + ranks + trend arrows for all 10 teams
3. Update `wiki/TODO.md` — add Shared Services upgrade milestone; update LS Dev item (Day 2 of High Risk); add JIT DP regression note

### Phase 5 — Sequential: Index + Log (1 agent, after all phases complete)

**Consolidation Agent**:
1. Update `wiki/index.md`:
   - Prepend `portfolio-20260428-0930` row to Portfolio Snapshots table
   - Replace "Latest audit per team" rows with Apr 28 scores + bands + deltas
   - Bump page counts (summaries: +13, entities: unchanged count but updated)
2. Append to `wiki/log.md`:
   - Header: `## [2026-04-28 HH:MM] ingest | Day-9 batch — 10 audits + portfolio + meeting agenda`
   - Key signals: Shared first Low Risk, LS Dev Day-2 High Risk, JIT DP reset
   - Full source list, writes section, escalations

---

## Files Modified

| File | Action | Phase |
|---|---|---|
| `wiki/summaries/audit-ado-admin-20260428-0902.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-fin-20260428-0902.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-fl-dev-20260428-0902.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-hr-20260428-0203.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-jit-20260428-0203.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-ls-dev-20260428-0203.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-otp-20260428-0204.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-shared-20260428-0204.md` | CREATE | 1 |
| `wiki/entities/team-ado-admin.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-fin.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-fl-dev.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-hr.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-jit.md` | UPDATE score+band+DP-reset flag | 1 |
| `wiki/entities/team-ado-ls-dev.md` | UPDATE score+band+Day2-High callout | 1 |
| `wiki/entities/team-ado-otp.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-shared.md` | UPDATE score+band+upgrade callout | 1 |
| `wiki/summaries/audit-git-aa-dev-20260428-0247.md` | CREATE (crossover/superseded) | 2 |
| `wiki/summaries/audit-git-aa-dev-20260428-0902.md` | CREATE (canonical Day 9) | 2 |
| `wiki/summaries/audit-git-cc-dev-20260428-0241.md` | CREATE | 2 |
| `wiki/entities/team-git-aa-dev.md` | UPDATE with _0902 canonical | 2 |
| `wiki/entities/team-git-cc-dev.md` | UPDATE score+band | 2 |
| `wiki/summaries/portfolio-20260428-0930.md` | CREATE | 3 |
| `wiki/summaries/meeting-agenda-20260428.md` | CREATE | 3 |
| `wiki/synthesis/portfolio-trend.md` | UPDATE Apr 28 data point | 4 |
| `wiki/synthesis/team-rankings.md` | UPDATE all scores | 4 |
| `wiki/TODO.md` | UPDATE (Shared upgrade + LS Dev Day 2 + JIT) | 4 |
| `wiki/index.md` | UPDATE (counts, rows) | 5 |
| `wiki/log.md` | APPEND batch entry | 5 |

Total: 13 new pages · 10 entity updates · 2 synthesis updates · 1 TODO update · 1 index update · 1 log append

---

## Verification

1. After Phase 1: 8 ADO summary files exist; 8 entity `updated` dates = 2026-04-28
2. After Phase 2: 3 Git summary files exist; 2 entity `updated` dates = 2026-04-28; AA _0247 marked SUPERSEDED
3. After Phase 3: portfolio + meeting agenda summaries exist
4. After Phase 4: `synthesis/portfolio-trend.md` has Apr 28 row; `TODO.md` has Shared upgrade + LS Dev Day-2 items
5. After Phase 5: `wiki/index.md` page count +13; `wiki/log.md` tail shows new entry
6. Spot-checks:
   - `audit-ado-shared-20260428-0204.md` contains band-upgrade callout
   - `audit-ado-ls-dev-20260428-0203.md` contains Day-2 High Risk callout
   - `audit-ado-jit-20260428-0203.md` contains DP-reset callout
   - `audit-git-aa-dev-20260428-0247.md` contains SUPERSEDED marker
