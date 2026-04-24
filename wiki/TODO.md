# Wiki TODO

Persistent cross-session to-do list for items surfaced in conversations — things we identified but deferred, decisions captured but not yet executed, wiki bookkeeping that's worth doing but not urgent. Agent appends items as they're identified; closes them (moving to the archive) when completed.

**Format per item:** status checkbox · date-added · category tag · one-line description · (links to source context if applicable).

**Conventions:**
- `[ ]` open · `[x]` closed · `[~]` in progress / partially done
- `⏳` waiting on external action (not the agent's to execute)
- When closing an item, move to the Archive at the bottom and add a `closed: YYYY-MM-DD` note with the outcome.
- Re-open only if the original item was closed prematurely.
- This file is wiki-maintained. Source of truth. Agent updates it; human curates priorities.

---

## Open — external / waiting on others (⏳)

- [ ] ⏳ **2026-04-23 · ramon-action** · Fix `raseniero` GitHub token access-scope so AA + Colina repos stop returning 404. Committed in LPM meeting; no ETA. Until done, HCI dims 1–6 on AA + Colina carry `data_mode: partial` and use 2026-04-21 baseline. Source: [[summaries/transcript-lpm-review-2026-04-23]]
- [ ] ⏳ **2026-04-23 · karl-action** · Share hiring-risk register with Grace + capture mitigation meeting minutes. Source: transcript.
- [ ] ⏳ **2026-04-23 · karl-action** · Execute Admin 12 SP de-scope in ADO (Ramon authorized in meeting — move 3–4 items to 7.3 backlog, e.g., #202937 Solar quotation, #202945 Grass cutting, #202939 Professional fee). Source: transcript + [[summaries/audit-ado-admin-20260423-0113]]
- [ ] ⏳ **2026-04-23 · program-action** · Claude partner workflow → epic migration (structural ADO change, owner TBD). Source: transcript.
- [ ] ⏳ **2026-04-23 · grace-action** · DoR remediation on #175360, #202911, #202913 — P0 overdue 2 post-return workdays. Source: [[summaries/audit-ado-otp-20260423-0900]]
- [ ] ⏳ **2026-04-23 · mark-action** · DoR remediation on #202898 + #202909 — deadline missed Day 3. Source: [[summaries/audit-ado-admin-20260423-0113]]
- [ ] ⏳ **2026-04-23 · pcoronia-action** · BE#55 HIPAA rework — 10 CHANGES_REQUESTED findings (5 Critical HIPAA). Day 6. If not resubmitted by Day 5 (Apr 24), 8 SP threatens sprint close. Source: [[summaries/audit-git-cc-dev-20260423-0856]]
- [ ] ⏳ **2026-04-23 · ike-action** · Dispose #187240 (248 days stale, 12 audits). Source: [[summaries/audit-ado-ls-dev-20260423-0900]]
- [ ] ⏳ **2026-04-23 · team-action** · LS-Dev configure capacity for 7.2 — 4 days unactioned. Source: same.
- [ ] ⏳ **2026-04-23 · cliff-earl-action** · Configure branch protection on develop/dev/main both AA repos — single action from HCI Moderate (+3 to +4). Source: [[summaries/audit-git-aa-dev-20260423-0855]]
- [ ] ⏳ **2026-04-23 · carol-ramon-action** · Configure Shared Services capacity for 7.2 — 4 consecutive audits unactioned. Source: [[summaries/audit-ado-shared-20260423-0900]]
- [ ] ⏳ **2026-04-23 · almera-action** · De-scope HR 7.2 to ≤22 SP (currently 38 SP, 73% overbook). P0 unactioned 4 audits. Source: [[summaries/audit-ado-hr-20260423-0914]]
- [ ] ⏳ **2026-04-23 · luke-action** · Add ≥1 User Story to Flawless 7.2 sprint (structural WIB 30 ceiling — 4 audits). Source: [[summaries/audit-ado-fl-dev-20260423-0910]]

## Open — wiki bookkeeping (agent-executable)

- [ ] **2026-04-23 · synthesis** · Create `synthesis/dor-form-vs-content.md` — "DoR passes but content is wrong" pattern now surfaced in 3 workspaces (Shared #202687 empty, Flawless #202827 1-char-short, HR #203057+#203063 wrong-candidate copy-paste). Rubric measures character counts, not accuracy. Worth a dedicated synthesis page. Trigger: wait until a 4th instance or when pattern directly affects a scoring dispute.
- [ ] **2026-04-23 · synthesis** · Annotate `synthesis/team-rankings.md` that AA's HCI 58 and Colina's HCI 78 are capped by token-side evidence access during the 4/21+ blackout, not team performance. Recompute expectations once `raseniero` token is fixed.
- [ ] **2026-04-23 · synthesis** · Update `synthesis/portfolio-trend.md` — last snapshot covered through 4/19; should extend to 4/23 Day 4 now that 3 new portfolio dashboards are ingested (4/21, 4/22, 4/23).
- [ ] **2026-04-23 · convention** · Formalize in `wiki/CLAUDE.md` schema: *"Wiki may propagate meeting-documented decisions to source CLAUDE.md Project Exceptions, additively, with source citation and log entry."* First precedent set this session (AA + Colina non-dev exceptions). Not in schema yet.
- [ ] **2026-04-23 · bookkeeping** · Spot-check the ~25 4/22 same-day re-run audits for distinct signal (most expected flat holds or degraded-mode; skip if no change). Low priority.
- [ ] **2026-04-23 · bookkeeping** · Spot-check the ~7 4/23 afternoon re-run audits (_1100, _1254, _1505, _1510, _1515) for distinct signal. The 4/23 1535 portfolio dashboard indicates some of these moved (LS-Dev 41.0 → 39.7, Shared 35.3 → 41.1, OTP 63.3 → 65.2, JIT 75.5 → 73.2); ingesting these would surface the real Day-4 closing state.
- [ ] **2026-04-23 · bookkeeping** · Verify whether `PORTFOLIO_MEETING_AGENDA_20260423.html` (non-timestamped) is distinct from the ingested `_1600` version. Skip if duplicate; ingest if distinct.
- [ ] **2026-04-23 · bookkeeping** · JIT transcript cut off at 46:24 with Ramon pivoting to "let me just jump to the JIT program" — the JIT program discussion content was not captured. If a continuation transcript exists or if a follow-up meeting transcript arrives, ingest and link.

## Open — scripts/agents/ tooling (from earlier wiki log)

- [ ] **earlier · P0** · Localize `CLAUDE.md` in `scripts/agents/` (upstream Raul Riera doc still in place — superficial cleanup).
- [ ] ⏳ **earlier · P0** · Verify `config/.env` — Ramon's manual check, hook-blocked from tool reads.
- [ ] **earlier · P2** · Lint consolidation: add parsing rule in lint.py — "if prompt contains 'Use the X skill', allowlist must contain `Skill`." Would have caught the 2026-04-23 launchd Skill-tool-missing defect earlier.
- [ ] **earlier · P3** · `daily-portfolio.sh`, `rotate-logs`, `pmset` ergonomics (3 items).
- [ ] **earlier · P2** · MacPilot: P1 + portfolio-email + portfolio-meeting-prep TODO checkboxes (most items shipped this session but boxes still open).

---

## Archive — closed items

*(Move items here with `[x]` + `closed: YYYY-MM-DD` + one-line outcome. Keep chronological, newest first.)*

- *(None yet — this file was created 2026-04-23.)*
