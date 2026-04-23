# Wiki Log

<!-- markdownlint-disable MD013 MD022 MD032 MD058 MD060 -->

Append-only chronological record. Newest at the bottom. Each entry header prefix `## [YYYY-MM-DD HH:MM]` so `grep '^## \[' log.md | tail` works.

---

## [2026-04-19 22:40] init | wiki bootstrap

- Created wiki schema ([CLAUDE.md](CLAUDE.md))
- Created folder layout: `entities/`, `concepts/`, `summaries/`, `synthesis/`
- Created [index.md](index.md) and this log
- Raw source roots registered: `../ado_*/`, `../git_*/`, `../portfolio_report/`, `../raw/`

## [2026-04-19 22:45] ingest | Portfolio Health Dashboard — Iteration 7.1 (April 19, 2026 19:53 PDT)

- Source: `../portfolio_report/PORTFOLIO_20260419_1953.html`
- Created [[summaries/portfolio-20260419-1953]]
- Created [[entities/team-ado-shared]] (score 32.2, Critical — first appearance)
- Created concept pages: [[concepts/scoring-ado-rubric]], [[concepts/scoring-git-ups]], [[concepts/risk-bands]]
- Open questions: Shared Services 32.2 baseline vs. normalized scoring; Auto Allies UPS 68.6 masking Critical HCI (49) and Red SGPI (21.2%) — flagged for synthesis page on next ingest

## [2026-04-19 23:10] batch-ingest | all ado_*and git_* workspaces (9 teams)

- Coordinated via 5 parallel agents (ADO batch A/B/C + 2 Git agents), each wrote its own entity + summary pages.
- Newest audit per workspace ingested (all dated 2026-04-19 13:45, except ado_shared which was 19:47 and already loaded).
- **Entities created (9):** [[entities/team-ado-admin]] 87.0 🟢, [[entities/team-ado-fin]] 93.7 🟢, [[entities/team-ado-fl-dev]] 79.3 🟡, [[entities/team-ado-hr]] 87.0 🟢, [[entities/team-ado-jit]] 68.8 🟡, [[entities/team-ado-ls-dev]] 82.4 🟢, [[entities/team-ado-otp]] 71.2 🟡, [[entities/team-git-aa-dev]] UPS 68.6 🟡, [[entities/team-git-cc-dev]] UPS 90.6 🟢.
- **Summaries created (9):** one per workspace, `audit-<slug>-20260419-1345.md`.
- **Portfolio consistency check:** 5 Low (Admin·Finance·HR·Life Style·Colina) + 4 Moderate (Flawless·OTP·JIT·Auto Allies) + 1 Critical (Shared Services) matches [[summaries/portfolio-20260419-1953]] ✓.
- **Signals surfaced:**
  - 🔴 UPS-masking pattern confirmed: Auto Allies UPS 68.6 (Moderate) hides Critical HCI (49) and Red SGPI (21.2%) — worth a [[synthesis/ups-masking-pattern]] page.
  - 🔴 JIT Delivery Predictability 0.0 — Grace's #201504/#201514 untouched 16d.
  - 🔴 Finance 93.7 but eAFS BIR Apr 15 deadline passed without ADO confirmation on #201448 (quality-vs-compliance tension).
  - 🟡 Flawless climbing (+10.5): closing #201569 Netlify Spike today promotes them to ~84.1 (Low).
  - 🔴 Colina Health has an unreviewed HIPAA PR (BE#55, 42 files) carrying into 7.2 under no-branch-protection — compliance hotspot.
  - 🔴 HR 7.2 overbooked (30 SP committed vs. 22 SP capacity) — capacity planning miss.
- **Index updated:** [[index.md]] now lists all 10 teams, 10 summaries, 3 concepts.
- **Next suggested syntheses:** ups-masking-pattern, iteration-7.1-close retrospective, service-model-scoring proposal for Shared Services.

## [2026-04-19 23:55] batch-ingest | portfolio_report/ — 19 snapshots + 1 trend rollup

- Coordinated via 4 parallel agents (March+trend / early April / mid April / late April).
- Every `portfolio_report/PORTFOLIO_*.html` ingested as a compact summary except `PORTFOLIO_20260419_1953.html` which was already in the wiki.
- **Summaries created (19):** `portfolio-20260325-1900` → `portfolio-20260419-1345` plus `portfolio-trend-20260331` (rollup).
- **New synthesis page:** [[synthesis/portfolio-trend]] — full 2026-03-25 → 2026-04-19 trend analysis; 3-arc narrative (PI6 close → PI boundary → PI7.1 climb); timeline table; theme breakdowns; open questions feed.
- **Key signals surfaced:**
  - 🎯 Portfolio peak: 2026-04-19 13:45 (mean 81.0 / median 82.4, zero-Critical, zero-High) — best reading in the captured window.
  - 🔴 Recomposition shock: adding Shared Services (baseline 32.2) as 10th team dropped mean 81.0 → 76.1. **Median held (82.4 → 80.9)** — median is a more robust metric across team-count changes.
  - 🚧 Three **scoring artifacts** masquerading as regressions (must be excluded from slope calcs):
    1. 2026-04-01: HR -63.4 (perfect-sprint artifact after 14/14 close)
    2. 2026-04-05: rubric transition 6-dim → 7-dim (JIT -22.1, Finance -12.1, many)
    3. 2026-04-17: Life Style 77.1 → 11.2 (sprint-close formula), Auto Allies color-override
  - 🔴 Auto Allies UPS masking confirmed across 03-26 → 04-19: headline Moderate consistently hides Critical HCI/SGPI components.
  - 📉 First zero-Critical day: 2026-03-30. First zero-High day: 2026-04-13. First zero-both: 2026-04-16. Maintained until Shared Services joined.
  - 📅 Timeline gap: no snapshot on 2026-04-18 — confirm with Ramon whether skipped or missing.
- **Index updated:** [[index.md]] now catalogs 10 entities · 3 concepts · 29 summaries · 1 synthesis.
- **Next suggested syntheses:** ups-masking-pattern (Auto Allies case), scoring-artifacts (formal carve-out proposal), iteration-7.1-close retrospective, service-model-scoring (Shared Services tier-aware rubric).

## [2026-04-20 00:30] full-backfill | all historical audits across 10 workspaces

- **Scope:** 261 historical AUDIT_*.md files (every non-latest audit in every ado_*/git_* workspace). Coordinated via 9 parallel agents (one per workspace with audits to backfill; ado_shared handled inline after the fact).
- **Result: 261 new compact summary pages + 1 ado_shared summary (`audit-ado-shared-20260419-1947.md`)** = 262 new. Total audit summaries in wiki now **270** (nine already existed from the per-team ingest); portfolio summaries remain 20; grand total summaries = **290**.
- **Pattern:** each audit summary is ~30–50 lines with YAML frontmatter, compact 7-dim (ADO) or UPS (Git) scores table, 3–5 top issues, and a `Δ vs prior` line linking to the prior audit summary in sequence — so every workspace's audit lineage is navigable as a linked chain.
- **Rubric-era transitions flagged across workspaces:**
  - **Legacy 10-pt / 5-cat / 8-dim qualitative** (Feb 24 → ~Mar 22) — older ADO audits use pre-SAFe-v1 scorecards; most dim slots marked "—" in the table.
  - **6-dim ADO SAFe v1** (~Mar 23 → Apr 4) — Delivery Predictability not yet present.
  - **7-dim** (Apr 5 onward) — current rubric; the Apr 5 cutover itself caused widespread negative deltas (JIT −22.1, Finance −12.1, etc.) that are artifacts of the methodology change, not performance regressions.
- **Scoring-artifact confirmations** (corroborate [[synthesis/portfolio-trend]]):
  - HR Apr 1 perfect-sprint artifact (header 91.1 vs computed 76.1 on Apr 7 also noted).
  - LS Dev Apr 17 formula dip (77.1 → 11.2 close-day artifact).
  - Multiple Apr 1–5 sprint-complete artifacts (Administration 22.9–26.7 Critical stretch).
- **Entity pages updated:** every `entities/team-*.md` Audit history section rewritten from a 10-row preview table to a **full bullet list** linking every audit's wiki summary and raw file. Dates now present per-row using pretty `YYYY-MM-DD HH:MM` format.
- **Index updated:** [[index.md]] now shows per-team counts (34, 33, 25, 33, 38, 26, 32, 1, 26, 22 = 270) with span coverage. Full summary listing intentionally omitted from index (would be unwieldy) — team entity pages are the canonical per-team catalog.
- **Process note:** 5 of 9 backfill agents hit their token-rate limit at the end but had already completed all Write operations before the cap; the limit only blocked their final reply text. No data loss.
- **Next:** candidate synthesis pages (ups-masking-pattern, scoring-artifacts, iteration-7.1-close, service-model-scoring) are all now fully sourceable from the backfilled summaries — can be drafted without re-reading any raw audit.

## [2026-04-20 01:10] lint | first wiki-wide health check

**Overall verdict:** ✅ wiki is structurally healthy — 1 known broken link, 0 orphans, 0 frontmatter gaps, 0 stale summaries, 100% team-score consistency between entity pages and latest audit summaries.

Counts

- Total pages: **307** (10 entities · 3 concepts · 290 summaries · 1 synthesis · 3 meta: index/log/CLAUDE)
- Resolved outbound [[wiki-links]]: **1,573**
- Broken links: **1** ([[synthesis/ups-masking-pattern]] referenced in this log as a known future page — not yet created)

Hub distribution (top 5, inbound-link count)

- [[concepts/risk-bands]] — 305 (every entity + every summary)
- [[concepts/scoring-ado-rubric]] — 255
- [[concepts/scoring-git-ups]] — 74
- [[entities/team-ado-jit]] — 45
- [[entities/team-ado-admin]] — 44

Team entities have 33–45 inbound each; [[entities/team-ado-shared]] has 7 (correct — only 1 audit so far).

Contradictions: **none found**. Entity-page "Current state" scores match expected latest values for all 10 teams.

Staleness: **none** — every summary's `updated: 2026-04-19` is ≥ its source date.

Missing-page candidates (proper nouns referenced 3+ times without dedicated entity/concept page):

- **Grace — 88 mentions.** Recurring blocker in JIT audits; warrants an `entities/person-grace.md`.
- **Carol — 33 mentions.** Project Manager across Shared Services / Flawless; warrants `entities/person-carol.md`.
- **Ramon — 30 mentions.** Already heavily referenced but no dedicated page (he's the primary stakeholder).
- **Jerlyn — 10 mentions.** Auto Allies zero-contribution pattern; dedicated page optional.
- **eAFS (24) + BIR (19).** Finance compliance deadlines; combine into `concepts/compliance-deadlines.md`.
- **Holy Week (14).** PI-boundary artifact driver; fold into future `synthesis/scoring-artifacts` page.
- **#201569, #187240, #202894.** Stale work items referenced repeatedly — low priority, but a `concepts/stale-work-items.md` could collate them.

Known future pages (referenced but not created — intentional): [[synthesis/ups-masking-pattern]] · [[synthesis/scoring-artifacts]] · [[synthesis/iteration-7.1-close]] · [[synthesis/service-model-scoring]].

No changes made during this pass — findings only.

## [2026-04-20 01:45] content-wave | Grace + compliance concept + 4 synthesis pages

Drafted the 6 follow-ups identified by the lint pass:

1. [[entities/person-grace]] — first person entity; resolves 88-mention gap; documents JIT blocker pattern (#201504/#201514 untouched 16 days) and the Finance/Admin + 1h-JIT-Documentation dual role.
2. [[concepts/compliance-deadlines]] — defines eAFS / BIR / AFS terms (43 combined mentions previously undefined); notes the 2026-04-15 BIR deadline that Finance audit can't confirm in ADO.
3. [[synthesis/ups-masking-pattern]] — Auto Allies case (UPS 68.6 Moderate hides HCI 49 + SGPI 21.2%); recommendation: **Options A+C combined** (show all 3 components per row + surface min-component band as a second pill).
4. [[synthesis/scoring-artifacts]] — three carve-outs proposed: **(1) perfect-sprint hold** (freeze Overall at close-day value for remainder of iteration), **(2) rubric-version baseline** (first post-change audit is baseline, no cross-boundary deltas), **(3) Day-14 T-1 fallback** (if Day-12→14 score ≥30 pts below T-1 due to zero-denominators, substitute T-1 with close-window flag).
5. [[synthesis/iteration-7.1-close]] — cross-team retrospective; top theme: **cleanest monotonic climb in the dataset (62.0 → 81.0), zero High Risk from 04-13**, powered by Day-12–18 burst closures that exposed capacity planning + DoR-at-edges as portfolio's weakest links heading into 7.2.
6. [[synthesis/service-model-scoring]] — Shared Services tier-aware rubric: add `team_type` attribute (product|service|hybrid); for `service` teams, drop User-Story WIB penalty, swap Iteration Planning denominator to active-in-progress, add **Cross-Team Delivery** dimension, floor service composites at 40 unless both Team Capacity and Delivery Predictability are 0.

Index updated: entities 11, concepts 4, synthesis 5; "Next content candidates" list refreshed with person-ramon, person-carol, person-jerlyn, person-mark-colina, synthesis/capacity-planning, synthesis/dor-leakage.

Process note: 4 synthesis pages written in parallel by background agents; person-grace + compliance-deadlines written inline. No rate-limit errors this pass.

## [2026-04-20 02:05] lint-fix | reconcile broken links

Re-ran lint after content wave. Initial scan reported 10 broken links. Resolved all:

- 8 x escaped-pipe wiki-link aliases in [[synthesis/ups-masking-pattern]] — the agent wrote `double-bracket target backslash pipe alias double-bracket` instead of the plain pipe form. Stripped the backslashes; aliases now render correctly.
- 2 x `[[summaries/portfolio-trend-20260331]]` — target file was missing (never written by an earlier agent despite being claimed in its report). Created the summary as a rollup stub citing the trend-rollup HTML source; it links into [[synthesis/portfolio-trend]] as the canonical multi-PI view.

Final state: **313 pages · 1,667 resolved links · 0 broken · 0 orphans · 100% team-score consistency preserved**.

## [2026-04-20 02:40] content-wave 2 | 4 people + 2 synthesis

Next content candidates from prior lint addressed:

1. [[entities/person-ramon]] — CEO & audit owner; documents conventions + decision authority + stakeholder graph. Written inline.
2. [[entities/person-mark-colina]] — Sole Administration assignee; bus-factor-1 risk flagged; 67% burst-delivery pattern documented. Written inline.
3. [[entities/person-carol]] — Carol Cuison: rostered Shared Services PM who operates as IC spike-assignee on Flawless (#201569 Netlify Spike, #199682, #202087); persistent capacity-config gap. Drafted via agent.
4. [[entities/person-jerlyn]] — Jerlyn Ates: Auto Allies QA/Requirements; **zero GitHub artifacts across all 14 days of Iter 7.1**, the 3rd consecutive sprint (traceable back to March). Drafted via agent.
5. [[synthesis/capacity-planning]] — **Killer stat:** Shared Services posted Team Capacity 0.0 because the config step was never wired. Three failure modes:
   - **Not configured** (Shared Services 0.0)
   - **Overbooked** (HR 30 vs 22 SP · Admin 32 vs 27 SP for 7.2)
   - **Wrong mix** (JIT Grace 1h/day for 2 items · Admin 5h/day fiction masking 18-SP Apr-17 burst · Flawless 66.7 stuck because Carol absent from config)
6. [[synthesis/dor-leakage]] — **Killer stat:** 3 of 10 teams carried DoR-incomplete items into Iter 7.1 (Shared Services 3/5 Grooming · Flawless 2 closed without remediation · Admin spawned #202894 on Day 14). Flawless sat at **DoR 28.6 Critical** as late as 04-12. Proposed gate: `provisional` tag auto-ejects at kickoff+2d; closures with thin DoR tagged `closed-with-debt`.

Index updated: entities 15, concepts 4, synthesis 7. "Next content candidates" refreshed with Karl, Bomar, per-PI syntheses, compliance-misalignment, stale-work-items, stakeholder-roles concept.

Process note: 4 background agents (2 people + 2 synthesis) + 2 inline writes (Ramon + Mark). No rate-limit issues.

## [2026-04-20 03:15] content-wave 3 | 2 people + 1 concept + 4 synthesis

Continuing through the candidate backlog:

1. [[entities/person-karl]] — Portfolio Delivery Manager; bridges portfolio outcomes and team delivery; co-reviewer with Ramon in recurring portfolio meetings. Written inline.
2. [[entities/person-bomar]] — Engineering Manager; least-profiled stakeholder (stub page with room to grow as audit record accumulates). Written inline.
3. [[concepts/stakeholder-roles]] — canonical definitions of PDM, PM, EM, PO, SM, Auditor; codifies the practitioner-vs-role distinction that shows up in Carol + Grace dual-hat patterns. Written inline.
4. [[synthesis/pi6-close]] — PI6 close retrospective at 2026-03-31 (mean 72.4 / median 77.1, 3L/3M/3H/0C, 9 teams pre-Shared-Services); biggest single-day mover was **Admin +22.1** (51.0 → 73.1) driven by capacity config being wired + a bulk-add rollback — not actual delivery. Drafted via agent.
5. [[synthesis/pi7-plan]] — PI7.2 planning checklist consolidating 6 prior syntheses. Theme: **"PI7.1 closed at peak health but four systemic gaps (capacity, DoR, UPS masking, service-rubric misfit) carry into 7.2 unless planning absorbs them."** Top 3 systemic changes: capacity-discipline pre-planning gate, DoR gate at planning close with provisional auto-eject, UPS component-breakdown in every dashboard row. Drafted via agent.
6. [[synthesis/compliance-misalignment]] — **Killer fact:** Finance #201448 (eAFS Portal Submission) sat Active for 9 days across the Apr 15 BIR deadline — last ChangedDate Apr 10 — so Finance scored 93.7 Low while the regulator likely already had the filing. Policy proposal: `compliance` tag + mandatory `deadline` field + scoring on attached regulatory receipt rather than `System.State`; compliance misses surface as a standalone dashboard widget. Drafted via agent.
7. [[synthesis/stale-work-items]] — Stalest: **LS Dev #187240 "Evaluate Deployment and Distribution Options"** (Enabler, **244 days stale**, 9-audit `stale_180` penalty streak). Proposed cadence: **PI-close amnesty sweep** every quarter — items >90d `ChangedDate` default to close-as-obsolete unless an owner defends it in a 10-minute triage window; carve-outs for capacity-blocked reassignment and 30-day AC deadlines on stuck Spikes. Drafted via agent.

Index updated: entities 17, concepts 5, synthesis 11. "Next content candidates" refreshed with: pi7-close (future), ci-health, bus-factor, iteration-cadence, dor-definition, audit-automation.

Process note: 4 background synthesis agents + 3 inline writes. No rate-limit issues; all agents returned clean replies.

## [2026-04-20 03:30] lint | post-wave-3 health check

**Verdict: ✅ clean on every measurable axis.**

| Check | Result |
|-------|-------:|
| Pages | 326 |
| Types | 17 entity · 5 concept · 11 synthesis · 290 summary · 3 meta |
| Resolved [[links]] | **1,906** |
| Broken links | **0** |
| Orphans | **0** |
| Frontmatter issues | **0** |
| Stale summaries (updated < source) | **0** |
| Score consistency (entity ↔ expected) | **10 / 10 ✓** |

Hub growth since 2026-04-20 01:10 lint (first pass):

| Hub | Before | Now | Δ |
|-----|------:|----:|--:|
| [[concepts/risk-bands]] | 305 | 313 | +8 |
| [[concepts/scoring-ado-rubric]] | 255 | 264 | +9 |
| [[concepts/scoring-git-ups]] | 74 | 80 | +6 |
| [[entities/team-ado-jit]] | 45 | 53 | +8 |
| [[entities/team-ado-admin]] | 44 | 53 | +9 |
| [[summaries/portfolio-20260419-1953]] | 15 | 20 | +5 |
| [[synthesis/iteration-7.1-close]] | 3 | **16** | +13 |
| [[synthesis/portfolio-trend]] | 3 | 12 | +9 |
| [[entities/team-ado-shared]] | 7 | 15 | +8 |

Synthesis cross-linking (indicator of a well-connected analytic layer):

- **High** (≥7 inbound): [[synthesis/iteration-7.1-close]] (16) · [[synthesis/portfolio-trend]] (12) · [[synthesis/scoring-artifacts]] (12) · [[synthesis/ups-masking-pattern]] (9) · [[synthesis/capacity-planning]] (8) · [[synthesis/service-model-scoring]] (8)
- **Thin** (2–4 inbound): [[synthesis/dor-leakage]] (4) · [[synthesis/pi7-plan]] (3) · [[synthesis/compliance-misalignment]] (2) · [[synthesis/pi6-close]] (2) · [[synthesis/stale-work-items]] (2) — recently added; will accumulate inbound links naturally as future syntheses cite them

Missing-page candidates that warrant attention (proper nouns referenced many times without a dedicated page):

| Term | Mentions | Recommendation |
|------|---------:|----------------|
| Iteration 6.6 | 109 | Seed a `concepts/iteration-cadence.md` (PI boundaries + iteration naming) |
| Iteration 6.5 | 71 | ↑ same |
| eAFS · BIR | 57 · 48 | Already in [[concepts/compliance-deadlines]] — detector is keyword-matching, not page-matching; false positive |
| #201448 | 46 | Core to [[synthesis/compliance-misalignment]]; optional `entities/item-201448.md` |
| Branch protection | 41 | Seed for `synthesis/ci-health` (already queued) |
| #201569 Netlify Spike | 37 / 15 | Part of [[entities/person-carol]]'s IC pattern + [[synthesis/stale-work-items]] |
| HIPAA · BE#55 | 18 · 15 | Seed for `synthesis/ci-health` (engineering-practice angle) |
| Holy Week | 23 | Already cited in [[synthesis/scoring-artifacts]] as PI-boundary driver |

No changes made during this pass — findings only.

## [2026-04-20 03:50] verify | summary ↔ source consistency sweep

Scanned all 290 summaries against their frontmatter `sources:` paths; then for 270 audit summaries, extracted the cited Overall score and checked it appears in the raw audit.

**Source-path integrity:**

- 291 / 291 source paths resolved on disk ✓ — **except** [[summaries/portfolio-trend-20260331]], which cites `portfolio_report/PORTFOLIO_TREND_20260331.html`. **That file has been removed from disk since original ingest.** Added a ⚠️ note to the summary noting the raw source is no longer available; page retained for its preserved analytical content.

**Audit-summary score consistency (270 audit summaries):**

| Result | Count |
|--------|------:|
| ✓ Score cited in summary is present in raw (any variant: `42.0` ↔ `42` ↔ `42/100`) | **216** |
| — No score cited ("—" in table; pre-rubric legacy format) | **46** |
| ✗ Apparent mismatch — investigated and explained | **8** |
| Source missing on disk | 0 |

**The 8 apparent mismatches are all correct transformations, not errors:**

- 7 × `ado_hr` legacy audits (2026-03-04 → 2026-03-22) — raw uses **10-point scale** (e.g., `4 / 10 (High Risk)`); summary normalized to 100-pt scale (`40.0`). Transformation is faithful.
- 1 × [[summaries/audit-git-aa-dev-20260419-1345]] — summary cites UPS 68.6 but raw audit only shows component scores (ICS 99.4%, HCI 49, SGPI 21.2%). The **68.6 composite comes from the portfolio dashboard**, not the team audit itself. Consistent with [[concepts/scoring-git-ups]] formula (ICS·0.50 + HCI·0.30 + SGPI·0.20).

**Structural finding:** wiki summaries that normalize scale representations (10-pt → 100-pt) or compose composites (UPS from components) are faithful but not character-verifiable. Future verifiers should accept variant matching and composite derivation as valid. The verifier now uses variant matching (`42.0` / `42` / `42/10`) to avoid false positives.

Minor wiki change: added a ⚠️ archived-source note to [[summaries/portfolio-trend-20260331]]. Wiki otherwise remains **trustworthy against its sources.**

## [2026-04-20 04:05] cleanup | user-confirmed deletion of PORTFOLIO_TREND_20260331.html

User confirmed they deleted the raw HTML. Actions:

- Converted `wiki/summaries/portfolio-trend-20260331.md` into a **tombstone** (archived: 2026-04-20 in frontmatter; body points to [[synthesis/portfolio-trend]] as the live analytical successor).
- Removed `portfolio-trend-20260331` entries from: [[index.md]] summary table · [[synthesis/portfolio-trend]] sources frontmatter + body · [[synthesis/pi6-close]] sources frontmatter + body (body now describes the analysis inline and links to [[synthesis/portfolio-trend]]).
- Kept the tombstone file intact so future link visits don't 404; its only remaining inbound link is this log (historical record).

Post-cleanup lint: **326 pages · 1,897 links resolved · 0 broken · 0 orphans**. No other references to the deleted file remain. Tombstone has 1 inbound (this log) — intentional.

## [2026-04-20 04:20] query-to-synthesis | top-compliance-issues filed

User asked "what are the most common compliance issues?" — answered via frequency scan across all 326 wiki pages + triangulation with existing synthesis layer. Filed the categorized ranking as [[synthesis/top-compliance-issues]] so future queries return a canonical answer.

**Top 5 issues by mention frequency:**

1. DoR leakage (257 mentions) — [[synthesis/dor-leakage]]
2. Work Item Balance penalty (238) — [[synthesis/service-model-scoring]]
3. Stale chronic items (57) — [[synthesis/stale-work-items]]
4. Bus factor 1 (49) — [[entities/person-mark-colina]]
5. Branch protection / CI hygiene (43) — Colina HIPAA PR BE#55

All 16 issues map to one of the 4 systemic changes in [[synthesis/pi7-plan]] or to residual fixes queued elsewhere (ci-health, compliance-tag, service-tier, stale-amnesty, iteration-goal-gate).

Index updated: synthesis count 11 → 12.

## [2026-04-20 04:40] query-to-synthesis | team-rankings filed
User asked for a ranking of projects by score + trend direction. Computed programmatically from 270 audit summaries: extracted Overall/UPS scores chronologically per team, derived latest + 7d slope + volatility σ + min/max range + historical mean. Filed as [[synthesis/team-rankings]] with methodology note so future runs are reproducible.

**Key findings:**
- 🏆 **Portfolio leader:** [[entities/team-ado-fin]] at 93.7 (+1.71/d).
- 🌊 **Highest momentum:** [[entities/team-ado-fl-dev]] at +4.72/d (from rubric-era floor of 6.1; genuine climb).
- 📉 **Only genuine negative slope + high confidence:** [[entities/team-ado-otp]] at −0.88/d, σ 4.01.
- ⚠️ **Hidden decline:** [[entities/team-git-aa-dev]] UPS stable +1.14/d while HCI 49 (Critical) + SGPI 21.2% (Red) — masking remains.
- 🔄 **Fresh drop:** [[entities/team-ado-jit]] Δ −9.6 last audit (DP collapse to 0.0); 7d slope still flat because earlier rise cancels it.
- 📏 **Below own historical mean:** only [[entities/team-ado-otp]] (−4.5 below mean of 75.7).
- 🚩 **Volatility leaders (σ):** HR 22.56, Flawless 20.85, JIT 20.03 — artifact-prone.

PI7.2 forward-look buckets: **Strong bets** (Finance · Colina · Admin · HR with caveats). **Watch closely** (JIT · OTP · Life Style). **Structural intervention** (Auto Allies UPS fix · Shared Services tier-aware rubric).

Index updated: synthesis count 12 → 13.

## [2026-04-20 04:55] query-to-synthesis | score-streaks filed
User asked "which project has the most streak maintaining 80% score?" Computed consecutive ≥80 runs across all 270 audit summaries per team. Filed as [[synthesis/score-streaks]] with three different leaderboards (longest single streak · currently-active streak · cumulative frequency) plus artifact-break analysis.

**Three crowns, three teams:**
- 🏆 **Longest single streak ever:** [[entities/team-ado-jit]] JIT Operation — **13 consecutive audits** (2026-03-18 → 2026-04-04), broken by 2026-04-05 rubric transition.
- 🔥 **Longest active streak:** [[entities/team-git-cc-dev]] Colina Health — **7 consecutive audits** and still running (2026-04-08 → 2026-04-19). Immune to the 04-05 ADO rubric change because Git teams use UPS.
- 📊 **Highest cumulative ≥80 share:** [[entities/team-ado-fin]] Finance — **16 of 33 audits (48%)**.

**Pattern:** 4 of the top 5 streaks were broken by **scoring artifacts** (rubric transition + perfect-sprint), not real performance regressions. Reinforces the case for the rubric-version-baseline carve-out in [[synthesis/scoring-artifacts]].

**Three teams have never hit 80+:** Flawless (max 79.3, close), Auto Allies (max UPS 68.9, masked), Shared Services (1 audit baseline).

Index updated: synthesis count 13 → 14.

## [2026-04-20 05:05] correction | team member full names on JIT
User provided full-name corrections for three [[entities/team-ado-jit]] members:

- **Grace → Grace Garcia** (already in [[entities/person-grace]]; no change needed)
- **Teofilo → Teofilo Limpag** (was incorrectly listed as "Teofilo Manosa" in [[entities/team-ado-jit]]; fixed)
- **Armelita → Armelita Pulido** (no last name was on record; added)

Changes:
- [[entities/team-ado-jit]] — description paragraph + Stakeholders table updated with corrected full names; now links to [[entities/person-armelita]] and [[entities/person-grace]]
- New: [[entities/person-armelita]] — PM + PO + IC triple-hat on JIT; routinely carries 70–80%+ of sprint SP. Bus-factor risk parallel to [[entities/person-mark-colina]] on Admin (cited in [[synthesis/top-compliance-issues]] rank #4)

**Open question raised:** the earliest JIT audit ([[summaries/audit-ado-jit-20260224-2100]]) logs the third member as "Samantha Babael" but subsequent summaries consistently call her "Samantha Manosa". One of the two is a transcription error — flagged in the entity page as pending confirmation.

No changes to summary files (historical record; short-form names acceptable in context). Raw workspace `ado_jit/CLAUDE.md` not modified per wiki schema ("never modify raw sources") — the corrections live in the wiki layer.

## [2026-04-20 05:25] correction + query-to-synthesis | Teofilo's role + GitHub compliance
User corrected Teofilo Limpag's role: **Instructor** (CSS NC II / TESDA training delivery), not generic "Team member (Training)". Updated in [[entities/team-ado-jit]] and [[entities/person-armelita]].

Then answered: "what are the common GitHub compliance issues?" Scanned 48 Git audit summaries across [[entities/team-git-aa-dev]] (26) and [[entities/team-git-cc-dev]] (22). Ranked 14 issues by frequency + per-team split. Filed as [[synthesis/github-compliance-issues]].

**Key finding: two distinct failure modes on the two Git teams:**
- 🔴 **Auto Allies — engineering-health degradation:** traceability gaps (20/26), HCI Critical (12/26), zero-contribution (Jerlyn 3), branch protection (16/26). UPS composite math hides it.
- 🔴 **Colina Health — review-discipline + HIPAA exposure:** review latency (4/22), unreviewed merges (3/22), HIPAA-adjacent PRs unreviewed (2/22, includes BE#55 42-file PR). Strong UPS headline hides the review-discipline gap.

**4-tier remediation proposal:**
- **P0** — branch protection on all 5 repos (addresses 3 ranks at once)
- **P1** — Colina HIPAA review gate (≥2 reviewers for `hipaa`-labeled PRs)
- **P2** — AA AB# traceability enforcement (pre-commit hook)
- **P3/P4** — SGPI linking + silent-contributor weekly alert

Index updated: synthesis 14 → 15.

## [2026-04-20 05:55] content-wave 4 | 3 synthesis pages: ci-health · bus-factor · audit-automation
Drafted the three next-candidate syntheses in parallel:

1. [[synthesis/ci-health]] — **Engineering-health baseline for Git teams.** Pre-P0 HCI: Auto Allies **49** (High; Section-9 sub-score 48 Critical), Colina Health **74** (Moderate). Top 3 post-P0 metrics to track: % of PRs with required-reviewer approval at merge · mean PR review latency · `hipaa`-labeled PR 2-reviewer compliance. Establishes the "before" reading for measuring the branch-protection remediation in [[synthesis/github-compliance-issues]].

2. [[synthesis/bus-factor]] — **Portfolio single-point-of-failure catalog.** 9 bus-factor signals across 7 of 10 teams. Five delivery-side: Admin/Mark · HR/Almera · Finance/Grace · OTP/Grace · JIT/Armelita (70–80%+ SP). Two near-1: LS Dev/Samantha (~90%), Flawless/Carol (100% of open). Two review-side: CC Dev (`raseniero` sole approver), AA Dev (Jerlyn inverse case — zero-contribution hidden). Proposed guardrail: ≥40% SP-concentration flag at planning with mandatory backup-plan sentence + <2-distinct-reviewer `review-bus-factor` flag per repo.

3. [[synthesis/audit-automation]] — **Consolidated engineering roadmap.** 29 automation rules across 4 execution layers (L1 planning gates ×5, L2 per-audit flags ×11, L3 repo enforcement ×5, L4 dashboard widgets ×8), drawn from 9 prior synthesis pages + both SKILL.md sources. Top-3 priorities:
   - **L2.1** UPS component-breakdown surfacing (kills Auto Allies's 9-audit masking streak at lowest cost)
   - **L1.1** capacity-configured gate (eliminates Shared Services' deterministic 0.0)
   - **L2.7** tier-aware scoring (reclassifies Shared Services 32.2 Critical → ~55–60 on real issues only)

Dependency highlights:
- L2.7 blocks on `team_type` convention being added to workspace `CLAUDE.md` files first
- L2.6 blocks on ADO `compliance` tag + `deadline` custom field
- L3.2–L3.5 block on L3.1 branch protection
- All L4 widgets depend on their source L2 rule being live

Index updated: synthesis 15 → 18.

## [2026-04-21 14:30] batch-audit | /ado-safe-audit all-projects + /git_iteration_audit all-git-projects
Full-portfolio iteration audit on Day 2 of Iteration 7.2 (early-sprint). 5 parallel agent teams (3 ADO + 2 Git) per batch conventions. **10 new audits written; 10 summaries ingested; all 10 entity audit-history sections refreshed.**

### ADO scoreboard (Iteration 7.2 Day 2)
| Team | 7.1 close | 7.2 Day 2 | Δ | Note |
|------|----------:|----------:|--:|------|
| [[entities/team-ado-admin]] | 87.0 🟢 | 69.5 🟡 | −17.5 | 39 SP vs 27 SP ceiling · #202894 DoR gap · 9 PI7-root legacy un-iterated |
| [[entities/team-ado-fin]] | 93.7 🟢 | 77.9 🟡 | −15.8 | #201448 eAFS DROPPED from backlog (trail broken) · WIB −30 (no Spike) |
| [[entities/team-ado-fl-dev]] | 79.3 🟡 | 59.6 🟠 | −19.7 | zero User Stories in 7.2 → −40 WIB; 8/11 items untouched since iter start |
| [[entities/team-ado-hr]] | 87.0 🟢 | 81.4 🟢 | −5.6 | 37 SP vs 22 SP cap (68% overbook) · bus-factor-1 Almera |
| [[entities/team-ado-jit]] | 68.8 🟡 | 72.9 🟡 | **+4.1** | ⭐ Grace's #201504/#201514 chronic blocker REMOVED from backlog |
| [[entities/team-ado-ls-dev]] | 82.4 🟢 | 41.0 🟠 | **−41.4** | 2-item sprint · capacity 0.0 · #187240 246d stale (10th consecutive audit) |
| [[entities/team-ado-otp]] | 71.2 🟡 | 64.8 🟡 | −6.4 | ⭐ #198587 (negative-slope driver) CLOSED 04-20 · new DoR gaps on 3 items |
| [[entities/team-ado-shared]] | 32.2 🔴 | 37.7 🔴 | +5.5 | Team Capacity **STILL NOT CONFIGURED** for 7.2 (baseline P1 unresolved) · DoR +43.3 |

### Git scoreboard (Iteration 7.2 Day 2)
| Team | Prior | 7.2 Day 2 | Δ | Notable |
|------|-------|-----------|---|---------|
| [[entities/team-git-aa-dev]] | ICS 99.4 · HCI 49 · SGPI 21.2% | ICS 95.3 · HCI 53 · SGPI 0.0% | HCI +4 | ⭐ **First human PR review in team history** (Earl→Cliff, TS compile errors) · retro #202168 CLOSED by Jerlyn · Jerlyn ADO-active first time in 4 sprints |
| [[entities/team-git-cc-dev]] | ICS 96.8 · HCI 74 · SGPI 100% | ICS 93.6 · HCI 79 · SGPI 0.0% | HCI +5 | ⭐ **Reviewer bottleneck BROKE** — raseniero 10-finding HIPAA review on BE#55; pcoronia first peer-approval · HCI 1 pt from Low band |

### Headline wins
- **[[entities/team-ado-otp]] recovery signal:** the only team with genuine negative slope at 7.1 close is now post-blocker — #198587 signage closed 04-20. [[synthesis/team-rankings]] forecast likely to turn.
- **[[entities/team-ado-jit]] Grace blocker resolved:** the chronic pair of items cited across every recent JIT summary + [[entities/person-grace]] is gone from the visible backlog. Wait for confirmation of close vs re-path.
- **[[entities/team-git-aa-dev]] UPS masking crack:** Jerlyn's return to ADO-activity + retro #202168 closure + the first-ever human PR review broke a 3-sprint pattern of engineering-health stagnation.
- **[[entities/team-git-cc-dev]] reviewer concentration addressed:** `raseniero`'s adversarial review on the HIPAA PR BE#55 + `pcoronia` providing a peer approval suggests the review-bus-factor pattern flagged in [[synthesis/bus-factor]] is actively remediating.

### New concerns
- **[[entities/team-ado-ls-dev]] sharp drop to 41.0** — no capacity configured AND sprint under-planned AND #187240 now 246d stale. The [[synthesis/capacity-planning]] "not configured" failure mode is biting harder.
- **[[entities/team-ado-shared]] capacity still missing** after explicit P1 recommendation at baseline. Most-repeated recommendation in the workspace history remains unactioned.
- **[[entities/team-ado-fin]] #201448 eAFS disappeared** from backlog without explicit disposition trail — [[synthesis/compliance-misalignment]] concern worsened.
- **[[entities/team-ado-fl-dev]] zero User Stories** in 7.2 commitment (−40 WIB penalty is structural for this cycle).
- **[[entities/team-git-aa-dev]] branch protection still 0/4** — biggest single HCI move available, still unactioned despite retro spike #202169.

### Wiki updates
- 10 new summary pages: `wiki/summaries/audit-*-20260421-*.md`
- All 10 entity pages' **Audit history** sections refreshed (prepended 2026-04-21 entry, newest first)
- `wiki/index.md` — totals: summaries 289 → 299; per-team counts bumped by 1 each; Latest-audit table now shows Iteration 7.2 Day 2 scores with Δ vs 7.1 close
- Entity page "Current state" sections NOT rewritten (still show 7.1 close numbers; 7.2 data lives in summaries + audit-history). This is intentional — the entity pages capture the most recently **completed** iteration as canonical state; mid-sprint is too early.

### Next suggested follow-ups
- Refresh [[synthesis/team-rankings]] with 7.2 Day 2 deltas (the OTP outlook has shifted; JIT's direction flipped positive)
- Refresh [[synthesis/score-streaks]] (Colina's 7-streak extended to 8; only audits ≥80 carry streaks)
- Watch [[synthesis/ups-masking-pattern]] — if AA's HCI breaks 60 this sprint, the masking pattern breaks with it
- Update [[synthesis/compliance-misalignment]] with the #201448 eAFS disappearance

## [2026-04-20 06:05] chart-embed | portfolio-trend Mermaid timelines
User asked for a portfolio UPS trend chart with Mermaid. Clarified that UPS is Git-specific (only 2 teams); produced portfolio-MEAN timeline + dedicated Git-UPS timeline. Honored the "no xychart-beta" rule from root CLAUDE.md by using Mermaid `timeline` diagram type.

Embedded three visualizations into [[synthesis/portfolio-trend]] between the Timeline table and the Themes section:
1. **Mermaid `timeline`** — portfolio mean 3-arc narrative (PI6 close → IP/nadir → PI7.1 climb → peak → recomposition)
2. **Mermaid `timeline`** — Git-team UPS trajectories (AA 53→68.6 masked · CC 51.9→90.6 clean)
3. **Text sparkline** — 20-snapshot compact view with arc labels

Also added a headline-numbers summary: start 64.3 · nadir 56.9 · peak 81.0 · current 76.1 · window delta +11.8 mean / +23.1 median (median growing faster signals bottom-band teams pulled up).

File updated: `synthesis/portfolio-trend.md` — frontmatter `updated: 2026-04-20`.

## [2026-04-22 22:30] ingest | scripts/ automation scaffolding

- Source: `../scripts/` (untracked in git as of ingest)
- `scripts/agents/` = unmodified vendoring of [MacPilot](https://github.com/raulriera/MacPilot) (MIT, © Raul Riera). Only `example.sh` + `com.macpilot.example.plist` ship — no project-specific agents yet.
- `scripts/lint/` = 6 ad-hoc Python files (~580 LoC total) for markdown linting. **Scope gap:** hardcoded to 4 ADO workspaces only (`ado_fin`, `ado_fl_dev`, `ado_ls_dev`, `ado_otp`); misses `ado_admin`, `ado_hr`, `ado_jit`, `ado_shared`, both Git workspaces, and `wiki/`. Two `*_lint(ing).py` file pairs look like iteration duplicates — candidates for consolidation.
- **Created:** [[entities/system-macpilot]] — documents origin, harness shape, operational defaults (sonnet · max-turns 10 · timeout 300s · JSON→jq), Ramon's 4 target agents (ado-audit-all, git-audit-all, portfolio-health, portfolio-email), and caveats (launchd wake behavior, `.env` hook-blocked, upstream doc drift, MIT attribution).
- **Index updated:** entity count 18 → 19; new Systems subsection added under Entities.
- **Next seeded at `scripts/TODO.md`:** P0 git-tracking decision → P1 ado-audit-all agent → P1 git-audit-all → P1 portfolio-health → P2 portfolio-email (gated on authorized recipient list) → P2 lint consolidation.
