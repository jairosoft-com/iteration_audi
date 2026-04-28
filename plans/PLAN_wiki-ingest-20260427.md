# Plan: Wiki Batch Ingest — Apr 27, 2026 (PI7.2 Day 8)

## Context

Daily audit batch for Apr 27 has run. Wiki last updated: Apr 26 evening. 13 new sources need ingestion:
- 8 ADO team audits (all `AUDIT_20260427_1110.md`, same scheduled run)
- 2 Git team audits from the 09:02 run (`git_aa_dev` + `git_cc_dev`)
- 1 additional AA audit (`AUDIT_20260428_0247.md`) — overnight re-run with restored token, supersedes the partial 09:02 run
- 1 portfolio dashboard (`PORTFOLIO_20260427_1110.html`)
- 1 meeting agenda (`PORTFOLIO_MEETING_AGENDA_20260427.html`)

**Critical signal**: LS Dev dropped to High Risk (50.7, −10.4) — first High Risk of PI7.2. All other teams flat or minor moves.

---

## Source Inventory

| Source file | Wiki slug | Priority |
|---|---|---|
| `ado_admin/audit/AUDIT_20260427_1110.md` | `audit-ado-admin-20260427-1110` | normal |
| `ado_fin/audit/AUDIT_20260427_1110.md` | `audit-ado-fin-20260427-1110` | normal |
| `ado_fl_dev/audit/AUDIT_20260427_1110.md` | `audit-ado-fl-dev-20260427-1110` | normal |
| `ado_hr/audit/AUDIT_20260427_1110.md` | `audit-ado-hr-20260427-1110` | normal |
| `ado_jit/audit/AUDIT_20260427_1110.md` | `audit-ado-jit-20260427-1110` | normal |
| `ado_ls_dev/audit/AUDIT_20260427_1110.md` | `audit-ado-ls-dev-20260427-1110` | **HIGH** (band drop) |
| `ado_otp/audit/AUDIT_20260427_1110.md` | `audit-ado-otp-20260427-1110` | normal |
| `ado_shared/audit/AUDIT_20260427_1110.md` | `audit-ado-shared-20260427-1110` | normal |
| `git_aa_dev/audit/AUDIT_20260427_0902.md` | `audit-git-aa-dev-20260427-0902` | partial/superseded |
| `git_aa_dev/audit/AUDIT_20260428_0247.md` | `audit-git-aa-dev-20260428-0247` | **canonical Day 9** |
| `git_cc_dev/audit/AUDIT_20260427_0902.md` | `audit-git-cc-dev-20260427-0902` | normal |
| `portfolio_report/PORTFOLIO_20260427_1110.html` | `portfolio-20260427-1110` | normal |
| `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260427.html` | `meeting-agenda-20260427` | normal |

### Note on git_aa_dev dual files

`AUDIT_20260427_0902.md` = partial run (GitHub token issue). `AUDIT_20260428_0247.md` = full audit after token restoration (Day 9 early morning PHT crossing midnight = Apr 28 timestamp). Ingest both: mark _0902 as `data_mode: PARTIAL · SUPERSEDED` in its summary, treat _0247 as canonical.

---

## Scores Preview (Day 8)

| Team | Score | Band | Δ | Key signal |
|------|------:|------|---|---|
| ADO HR | 81.4 | 🟢 Low | flat | DP drop; Almera bus factor |
| ADO Shared | 67.6 | 🟡 Moderate | +3.4 | #202687 DoR fixed (11-day gap) |
| ADO JIT | 76.0 | 🟡 Moderate | +2.1 | First real delivery (34% DP) |
| ADO Finance | 77.9 | 🟡 Moderate | flat | 9-day plateau |
| ADO OTP | 74.8 | 🟡 Moderate | flat | DP 0.0; items at Resolved state |
| ADO Admin | 72.1 | 🟡 Moderate | small ↑ | First DP move; #202898 closed with DoR gap |
| ADO Flawless | 70.2 | 🟡 Moderate | flat | WIB capped (all Defects); QA pipeline moving |
| ADO LS Dev | **50.7** | **🟠 High** | **−10.4** | **Band drop; WIB collapse; 0 SP closed** |
| Git AA Dev | UPS 70.7 | 🟡 Moderate | TBD | SGPI 0.0 Critical; ICS 100 |
| Git Colina | UPS 68.49 | 🟡 Moderate | flat | SGPI 6.7 Critical; BE#55 still blocked |

---

## Execution Plan (4 phases, sequenced to avoid shared-file conflicts)

### Phase 1 — Parallel: Write team audit summaries + entity updates (5 agents)

Do NOT write to `index.md`, `log.md`, or `synthesis/` in this phase. Summaries + entities only.

**ADO Agent A** (`ado_admin`, `ado_fin`, `ado_fl_dev`):
- Read each source audit fully
- Create 3 summary pages in `wiki/summaries/` using ADO format (YAML frontmatter, 7-dim score table, key signals, open questions)
- Update 3 entity pages in `wiki/entities/` (score, band, `updated` date, latest audit link)

**ADO Agent B** (`ado_hr`, `ado_jit`, `ado_ls_dev`):
- Same as Agent A; flag LS Dev High Risk drop prominently in summary
- For LS Dev: add a `> ⚠️ BAND DROP` callout in its summary noting this is first High Risk of PI7.2

**ADO Agent C** (`ado_otp`, `ado_shared`):
- Same as Agent A

**Git Agent D** (`git_aa_dev` — both files):
- Create `audit-git-aa-dev-20260427-0902` with `data_mode: PARTIAL · SUPERSEDED by 20260428-0247`; include brief partial scores
- Create `audit-git-aa-dev-20260428-0247` as canonical Day 9 full audit (UPS 70.7, full scoring)
- Update `entities/team-git-aa-dev.md` with _0247 scores as the authoritative Day 9 read

**Git Agent E** (`git_cc_dev`):
- Create `audit-git-cc-dev-20260427-0902` (UPS 68.49, SGPI 6.7 Critical, BE#55 still blocked)
- Update `entities/team-git-cc-dev.md`

### Phase 2 — Parallel: Portfolio + meeting agenda (2 agents, after Phase 1)

**Agent F** (portfolio):
- Parse `PORTFOLIO_20260427_1110.html` for team scores, mean, median, band distribution
- Create `wiki/summaries/portfolio-20260427-1110.md`
- Note: this snapshot reflects the 11:10 ADO audit batch; Git teams may reflect prior evening run

**Agent G** (meeting agenda):
- Parse `PORTFOLIO_MEETING_AGENDA_20260427.html`
- Create `wiki/summaries/meeting-agenda-20260427.md`
- Extract: agenda items, team highlights flagged, risks surfaced, decisions/actions noted

### Phase 3 — Sequential: Synthesis updates (1 agent, after Phase 1+2 complete)

**Synthesis Agent**:
1. Update `synthesis/portfolio-trend.md` — append Apr 27 data point (mean, band distribution, LS Dev drop note)
2. Update `synthesis/team-rankings.md` — refresh scores + ranks + trend arrows for all 10 teams
3. Check `wiki/TODO.md` — add new item for LS Dev High Risk drop; close or update any items resolved by today's audits (e.g., LS Dev Ike #195727 trigger condition)

### Phase 4 — Sequential: Index + Log (1 agent, after all phases complete)

**Consolidation Agent**:
1. Update `wiki/index.md`:
   - Prepend `portfolio-20260427-1110` row to Portfolio Snapshots table
   - Replace "Latest audit per team" rows with Apr 27 scores + bands + deltas
   - Bump page counts (summaries: +13, entities: unchanged count but updated)
2. Append to `wiki/log.md`:
   - Header: `## [2026-04-27 HH:MM] ingest | Day-8 batch — 10 audits + portfolio + meeting agenda`
   - Narrative: key signals (LS Dev drop, Shared recovery, JIT delivery)
   - Full source list
   - Writes section (page counts)
   - Escalations: LS Dev High Risk, AA SGPI 0.0 Critical, Colina BE#55 Day 11+

---

## Files Modified

| File | Action | Phase |
|---|---|---|
| `wiki/summaries/audit-ado-admin-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-fin-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-fl-dev-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-hr-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-jit-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-ls-dev-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-otp-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-ado-shared-20260427-1110.md` | CREATE | 1 |
| `wiki/summaries/audit-git-aa-dev-20260427-0902.md` | CREATE (partial/superseded) | 1 |
| `wiki/summaries/audit-git-aa-dev-20260428-0247.md` | CREATE (canonical Day 9) | 1 |
| `wiki/summaries/audit-git-cc-dev-20260427-0902.md` | CREATE | 1 |
| `wiki/entities/team-ado-admin.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-fin.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-fl-dev.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-hr.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-jit.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-ls-dev.md` | UPDATE score+band+band-drop flag | 1 |
| `wiki/entities/team-ado-otp.md` | UPDATE score+band | 1 |
| `wiki/entities/team-ado-shared.md` | UPDATE score+band | 1 |
| `wiki/entities/team-git-aa-dev.md` | UPDATE with _0247 as canonical | 1 |
| `wiki/entities/team-git-cc-dev.md` | UPDATE score+band | 1 |
| `wiki/summaries/portfolio-20260427-1110.md` | CREATE | 2 |
| `wiki/summaries/meeting-agenda-20260427.md` | CREATE | 2 |
| `wiki/synthesis/portfolio-trend.md` | UPDATE Apr 27 data point | 3 |
| `wiki/synthesis/team-rankings.md` | UPDATE all scores | 3 |
| `wiki/TODO.md` | UPDATE (new LS Dev escalation) | 3 |
| `wiki/index.md` | UPDATE (counts, rows) | 4 |
| `wiki/log.md` | APPEND batch entry | 4 |

Total writes: 13 new pages · 10 entity updates · 2 synthesis updates · 1 TODO update · 1 index update · 1 log append

---

## Verification

1. After Phase 1: confirm 11 summary files exist + 10 entity `updated` dates = 2026-04-27
2. After Phase 2: confirm portfolio and meeting agenda summaries exist
3. After Phase 3: confirm `synthesis/portfolio-trend.md` contains Apr 27 row; `TODO.md` has LS Dev item
4. After Phase 4: `wiki/index.md` page count incremented by 13; `wiki/log.md` tail shows new entry
5. Spot-check: `audit-ado-ls-dev-20260427-1110.md` contains band-drop callout; `audit-git-aa-dev-20260427-0902.md` contains SUPERSEDED marker
