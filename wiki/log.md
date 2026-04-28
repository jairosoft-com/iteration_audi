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

## [2026-04-23 00:55] ship | 3 MacPilot agents + portfolio-email headless mode

Wrote three new MacPilot agent wrappers + plists, completing the daily portfolio chain (08:30 ado → 09:00 git → 09:30 health → 09:45 email):

- `agents/git-audit-all.sh` + plist (09:00 daily, sonnet, max-turns 40, timeout 1200s) — wraps `/git_iteration_audit all-git-projects`
- `agents/portfolio-health.sh` + plist (09:30 daily, sonnet, max-turns 15, timeout 600s) — wraps `/portfolio-health`
- `agents/portfolio-email.sh` + plist (09:45 daily, sonnet, max-turns 20, timeout 300s) — wraps `/portfolio-email <allowlist>` in headless mode

Patched `.claude/skills/portfolio-email/SKILL.md` to add **Step 6.5 — Headless mode (scheduled invocation)**: an env-var-gated bypass of the previously "non-negotiable" Step 7 confirmation. Three-var handshake (`AUTO_SEND` trigger + `AUTHORIZED_RECIPIENTS` allowlist + `DRY_RUN` escape hatch); fail-closed on every partial-config or off-list-recipient case. Interactive behavior unchanged when all three vars are unset.

Initial recipient allowlist: `ramon, kcaumban, grace, bsinday @jairosoft.com` (4 internal addresses, mirrors the past send pattern). Edits to the plist's recipient list should be reviewed before re-install — this is the only wrapper whose misuse is not local-only.

`portfolio-email.sh` adds a defensive **freshness guard**: skip cleanly (exit 0) if today's `PORTFOLIO_*.html` doesn't exist, instead of emailing a stale dashboard. Catches the case where portfolio-health failed silently.

**Created:** [[concepts/headless-skill-mode]] — generalized pattern for taking interactive-only skills unattended; cites portfolio-email as reference implementation.

**Updated:** [[entities/system-macpilot]] — replaced "Intended agents (not yet written)" section with "Production agents" table (4 agents · schedule · env vars). Added "Conventions encoded across the 4 wrappers" section. Bumped `updated: 2026-04-23`.

**Index updated:** concepts count 5 → 6; Systems status changed from "no custom agents written yet" to "4 production wrappers shipped".

**Still open:** P0 git-tracking decision for `scripts/agents/` (vendor subtree vs submodule vs local-only) — independent of this work; tracked in `../scripts/TODO.md`. Lint consolidation (P2) also still open.

## [2026-04-23 01:13] ship | portfolio-meeting-prep MacPilot agent (5th)

Added the last portfolio-cycle wrapper, completing the daily 08:30→09:50 chain:

- `agents/portfolio-meeting-prep.sh` + plist (09:50 daily, sonnet, max-turns 20, timeout 600s) — wraps `/portfolio-meeting-prep <duration>`
- `MEETING_DURATION` env var defaults to `"30m"` (also accepts `"45m"`, `"60m"`)
- **No freshness guard.** Skill degrades gracefully on stale/missing inputs and the output is local-only HTML — a stale agenda is harmless to leave on disk. Contrast with `portfolio-email`, which DOES need a guard (shared-state action).
- Slot at 09:50 = 5 min after `portfolio-email`. Meeting-prep is independent of email's success: even if email fails or skips (per its freshness guard), the agenda still has all the inputs it needs from earlier in the chain (latest portfolio HTML + audits + workspace todos + memory/user_*.md).
- Same-day re-runs auto-suffix with `_HHMM` per the skill's documented behavior — no clobbering when Ramon manually invokes before a meeting.

Discovered orthogonal **09:00 plist collision**: `com.macpilot.example.plist` (Raul Riera's template, haiku · max-turns 1 · prints today's date) fires at the same minute as `git-audit-all`. Harmless — example finishes in <1s and touches no project files — but flagged in [[entities/system-macpilot]] §Caveats so it's uninstalled once the production chain is settled.

**Updated:** [[entities/system-macpilot]] — Production agents table 4 → 5 rows; schedule diagram extended to 09:50; "Conventions" heading bumped 4 → 5 wrappers; new caveat for the 09:00 collision and the freshness-guard rationale.

**No new concept page** — meeting-prep is a straight application of the read-render-write shape pioneered by portfolio-health; introduces no novel pattern.

**Index unchanged** — no new entities/concepts/summaries/syntheses; the Systems-row status text "4 production wrappers" is close enough to be left as is until the next batch.

**Still open:** P0 git-tracking decision (`scripts/agents/`); lint consolidation (P2); first install + first scheduled run (Ramon's call).

## [2026-04-23 01:40] update | system-macpilot conventions + caveats refresh

Two corrections to [[entities/system-macpilot]] (no new pages, no concept-page candidate):

- **OneDrive no longer load-bearing.** Project moved to `/Users/jairo/Projects/iteration_audit` (off `~/Library/CloudStorage/OneDrive-…/`). The "skip `sync_repo`" rationale was rewritten to lead with "in-progress work + untracked `scripts/`" and demoted OneDrive to a historical note. Resolves a stale claim that has been in the entity page since the original ingest (2026-04-22).
- **Env-leakage caveat.** Discovered during today's `portfolio-meeting-prep` dry-run (exit 1 in 99 s, no stderr): `lib/macpilot.sh:225` unsets only 2 of the 5 `CLAUDE*` env vars present in a Claude Code session. Production launchd is unaffected (clean env). Documented the workaround (`env -u …` prefix) and the 1-line lib hardening opportunity. Filing the caveat without the lib fix because (a) the fix is Ramon's call and (b) the dry-run was killed before the env-scrubbed re-run could confirm the hypothesis end-to-end.

No log line for the failed dry-run itself — too speculative until either the lib is hardened or a confirmed reproduction is captured.

## [2026-04-23 02:00] resolve | scripts/ git-tracking (P0) → Option A subtree

Ramon resolved the P0 blocker that had been open since the original [[entities/system-macpilot]] ingest (2026-04-22): `scripts/agents/` is now vendored as a git subtree, not a submodule and not local-only. 28 files tracked across 3 commits:

- `60f4dce` "Add MacPilot agent scripts and comprehensive linting tools" — initial bulk add (covered 4 of 5 production agents + lib + harness + lint)
- `a4708d6` "Add portfolio-email agent script and plist for automated email sending"
- `b156c15` "Add portfolio-meeting-prep agent script and plist for automated meeting agenda generation"

`scripts/agents/.claude/data/sessions/*.json` (5 files) correctly excluded by root `.gitignore`'s `**/.claude/data/sessions/` rule. `scripts/agents/.gitignore` preserved inside the subtree to keep MacPilot's own `logs/` `reports/` `tmp/` `.env` exclusions in scope.

**Stale wiki claims cleaned up this turn:**

- [[entities/system-macpilot]] paragraph 1 — "untracked in git" → "vendored as a git subtree (3 commits)" with the commit SHAs cited.
- [[entities/system-macpilot]] Conventions §"Skip `sync_repo`" — dropped the "untracked `scripts/` folder" half of the dirty-tree rationale (only "in-progress audit work" stands now). Demoted the OneDrive churn to a historical-notes parenthetical.
- [[wiki/index]] Systems row — "still untracked in git" → "vendored as git subtree (3 commits)"; also bumped 4 → 5 production wrappers (caught up the meeting-prep count that was deferred earlier).
- `../scripts/TODO.md` — both copies of the P0 git-tracking checkbox marked `[x]` with commit refs and Option-A label.

**Still open in `scripts/TODO.md`:** P0 "Localize `CLAUDE.md`" (upstream Raul Riera doc still in place — superficial cleanup, not load-bearing); P0 "Verify `config/.env`" (Ramon's manual check, hook-blocked from tool reads); P2 lint consolidation; P3 ergonomics. Most of P1 + portfolio-email + portfolio-meeting-prep checkboxes are also stale (the agents shipped this session) — left unchanged this turn since the user only asked for the git-tracking cleanup; flag as a separate ~5-min sweep if you want it.

## [2026-04-23 11:55] fix | Skill tool missing from all 5 wrapper allowlists (P0 launchd defect)

First scheduled launchd run (`portfolio-health` at 09:30) failed with exit 1; manual `launchctl kickstart` at 11:29 reproduced. After patching `lib/macpilot.sh` to preserve the claude CLI JSON on failure (3-line diagnostic patch), the next failure exposed the actual issue:

```
.permission_denials = [{"tool_name":"Skill","tool_input":{"skill":"portfolio-health"}}]
.subtype             = "error_max_turns"
.errors              = ["Reached maximum number of turns (15)"]
.num_turns           = 16
```

**Root cause:** wrapper prompts all say "Use the X skill" but none of the 5 wrappers had the `Skill` tool in `--allowedTools`. The agent's first move (call the Skill tool) was denied; it fell back to executing the skill's workflow manually (Glob audits → Read 10 files → extract scores → render HTML → Write), which exhausted the 15-turn budget.

**Fix applied:** `Skill` added to `--allowedTools` in all 5 wrapper scripts:

- `ado-audit-all.sh`
- `git-audit-all.sh`
- `portfolio-health.sh` (also bumped default `AUDIT_MAX_TURNS` 15 → 25 + matching plist value, as defense-in-depth)
- `portfolio-email.sh`
- `portfolio-meeting-prep.sh`

**Why this slipped past lint:** `sh -n` and `plutil -lint` validate syntax, not semantics. The `--allowedTools` value is a free-form string; nothing in the verification pipeline asserts that the tools the prompt invokes are present in the allowlist. A future `lint.py` consolidation (TODO P2) could add a parsing rule: "if prompt contains 'Use the X skill', allowlist must contain `Skill`."

**Why earlier `ado-audit-all` runs (yesterday 23:59) appeared to succeed:** still uncertain. Possibilities: the earlier successful runs may have been done in interactive Claude Code mode where the Skill tool isn't gated the same way; or the agent fan-out path (3 parallel sub-agents via `Agent` tool, which IS in the allowlist) sidestepped the parent's need to invoke `Skill` at all. Worth confirming on the next 08:30 launchd fire.

**Generalizable lesson filed to [[entities/system-macpilot]] §Conventions:** new bullet — *"`Skill` tool MUST be in `--allowedTools`"* with the failure-mode signature (`error_max_turns` + Skill in `.permission_denials`) so future debugging is faster.

**Diagnostic infrastructure also kept:** the 3-line patch to `lib/macpilot.sh:257` that preserves the JSON response in the agent log on failure. Without it, this diagnosis would have required several more blind kickstart cycles to triangulate.

## [2026-04-23 13:50] fix | lib/macpilot.sh stream-json + WATCHDOG_KILL labeling

`portfolio-meeting-prep` failure cascade today exposed two diagnostic gaps:

1. **Sonnet 4.6 (200k context) blew the context window** during the rich agenda render — `result: "Prompt is too long"`, `terminal_reason: "blocking_limit"`, $1.50/run. Switched MEETING_MODEL to **opus** (claude-opus-4-7, 1M context) to give 5x headroom.
2. **The next Opus run hit the 1200s watchdog** with empty preserved stdout — because `--output-format json` buffers the full response and SIGTERM flushes nothing. The earlier "preserve JSON on failure" patch couldn't help here.

**Lib fix shipped this turn:**

- `--output-format json` → `--output-format stream-json --verbose` (line 236). JSONL one-event-per-line emission means partial progress is on disk at every moment, even when killed.
- Result/subtype/turn parsers updated to JSONL idiom: `jq 'select(.type == "result") | .X' | tail -n 1` instead of the prior single-object branching (lines 271, 286, 297).
- Failure branch now explicitly labels exit 143 as `WATCHDOG_KILL after ${timeout}s` (line 261). Eliminates the "is this a timeout or a real exit 1?" ambiguity that cost us a couple of cycles today.
- 5 small edits, no behavioral change on success path; failure path is strictly more informative.

`scripts/agents/test.sh` 55/55 still passing. End-to-end validation pending the next launchctl kickstart of `portfolio-meeting-prep`.

**Generalizable wins:**

- All 5 agents inherit this immediately (shared lib).
- Future watchdog kills now leave a partial transcript in the agent's `.log` between `--- claude CLI stream-json events` delimiters — enough to see which file the agent was reading or which tool call was in flight at the moment of kill.
- [[entities/system-macpilot]] §"Operational defaults" table refreshed with the new format flag and reason.

**Still open:** validate the next kickstart actually completes (or fails informatively). If Opus + 20-min timeout + stream-json preserves enough detail to show progress, that's the production-ready configuration. If Opus also runs >20 min, we have evidence-based grounds to either bump again or slim the skill inputs.

## [2026-04-23 16:00] iterate | meeting-prep cascade resolved + plist-caching caveat + 1 ingest

**The cascade that started at 13:09 reached its diagnostic conclusion this turn:**

1. **First Opus-attempt run** (13:55) timed out at 20 min watchdog → stream-json patch surfaced full event stream → confirmed claude was making progress (not stuck); the 200k Sonnet context window had been the actual ceiling all along.
2. **Switched MEETING_MODEL=opus + timeout 1200s + plist edited** — but the next run STILL exhausted Sonnet's 200k window, returned `terminal_reason: "blocking_limit"`, and was reported as exit 1.
3. **Two new findings from that JSON:**
    - The model swap **did not take effect** — launchd caches plist `EnvironmentVariables` at first load; editing the file alone is not enough. Requires `launchctl bootout` + `bootstrap` to refresh. Filed as new caveat in [[entities/system-macpilot]] §Caveats.
    - The harness reports **false negatives when output is written before context exhausts** — `PORTFOLIO_MEETING_AGENDA_20260423_1600.html` IS on disk (Write tool fired in the preserved stream events), but the lib treated `is_error: true` as a clean failure. Filed as second new caveat — "always check the expected output path before assuming a failure means no work was done."

**Lib state today (commit `e5a4b29`):** `--output-format stream-json --verbose` is now the default; `WATCHDOG_KILL after <timeout>s` labels exit 143 explicitly; partial events preserved on every failure mode.

**Created [[summaries/meeting-agenda-20260423-1600]]** — first ingest of a portfolio meeting agenda artifact (new convention; meeting agendas are synthesis-of-audits rather than primary source data, but this one captures the full Day-4 picture across 10 teams in one place and is worth indexing).

**Index updated:** summaries 299 → 300.

**Still open in TODO:** P0 Localize CLAUDE.md, Verify .env. P2 lint consolidation. P3 daily-portfolio.sh / rotate-logs / pmset.

## [2026-04-23 16:30] ingest | OTP audit 2026-04-22 06:44 UTC (A35, 7.2 Day 3)

Started resumption of the post-4/21 ingest backlog. User direction: "ingest oldest unprocessed first." Picked `ado_otp/AUDIT_20260422_0644.md` — earliest 4/22 filename across all 10 workspaces (tied with `ado_shared/AUDIT_20260422_0644.md`; alphabetical tiebreak).

**Score:** 65.2 (Moderate). Δ +1.9 vs same-iteration A34 (Apr 22 18:00 PHT, 63.3). Δ +0.4 vs last wiki ingest (4/21 0930, 64.8).

**Driver:** single commit — `#203249 "AI Integration & Competency Mapping"` added to strict Iter 7.2 path (Grace, US, SP=2, Desc ≥30 ✓, AC ≥20 ✓). Shifts denominators on three dims: Iteration Planning 50.0 → 53.8, Estimation 83.3 → 85.7, DoR Compliance 50.0 → 57.1.

**Persistent debt unchanged:** #175360 (no AC), #202911 (title-only), #202913 (title-only + no SP) fail DoR for 3rd consecutive audit. #201811 untouched since Apr 8 → −10 Backlog Refinement. #203020 still at parent `OTP\2026 - PI7` path (not 7.2), and still likely duplicate of #203016.

**Pages touched:**

- Created [[summaries/audit-ado-otp-20260422-0644]]
- Updated [[entities/team-ado-otp]] — Current state reframed to 7.2 Day 3 (was frozen 7.1 close); added 4/22 entry to audit-history list; bumped `updated` to 2026-04-22; 7.1 close state moved to "Historical" section.
- Updated [[index]] — summary count 300 → 301; total ingested 280 → 281; OTP audits 33 → 34; Latest-audit row swapped to new summary; entity-table Latest swapped to new summary + 71.2 → 65.2; section heading clarified that OTP is Day 3 while rest of portfolio still shows Day 2 (to prevent stale-band misreads until the other 9 teams are ingested).

**Audit-numbering note filed to the summary:** report body uses `A35` (cites A34 at 18:00 PHT / 10:00 UTC). Filename timestamps appear to be UTC — strict 4/22 chrono order for OTP is 0644 → 0900 → 1450 → 1800 → 1930 → 2343. Ingest order follows filename UTC, not A-number.

**Backlog remaining for 4/22:** 9 more team audits (admin/fin/fl_dev/hr/jit/ls_dev/shared/aa/cc earliest timestamps); same-day OTP re-runs at 0900, 1450, 1800, 1930, 2343 can be folded into a single combined-day summary later or skipped if superseded — flag for user decision before proceeding past today's first wave.

## [2026-04-23 16:45] ingest | Shared Services audit 2026-04-22 06:44 UTC (A5, 7.2 Day 3)

Continuing oldest-first. Picked `ado_shared/AUDIT_20260422_0644.md` — tied earliest 4/22 timestamp with the OTP audit just ingested.

**Score:** 53.1 (🟠 High). **Δ +15.4 vs last wiki ingest** (A3, 4/21 0930, 37.7 Critical). **Band promotion Critical → High** — first exit from Critical since workspace creation at 4/19 baseline.

**Primary driver — DevOps IT sub-team delivery:** Teofilo Limpag closed 4 Enablers (#202393 Branch Protection, #202396 GitHub Automation, #203114 DevOps Users, #203115 Cebu Network Monitoring) = 8 SP, plus #202459 Spike closed and #202464 Auto Allies Blocker Passed UAT. Delivery Predictability jumps **0.0 → 57.1** (first non-zero in series).

**Secondary driver — denominator effects:**

- Iteration Planning 20.7 → 41.9: live iteration read now surfaces 13 items (was 6) because Enablers that closed became visible-in-iteration as they moved through the DevOps IT sub-team's flow.
- Work Item Balance 30 → 60: Enabler share dropped from >60% (triggering dominant-type penalty) to 53.8% as Design and Training items entered scope.
- Backlog Refinement 80 → 90: fewer untouched items.

**What did NOT improve:**

- **Team Capacity STILL 0.0** — `work_get_team_capacity` returned `No team capacity assigned to the team` for the 5th consecutive audit. Karl / Carol P0 recommendation unactioned across entire series. Configuring even 1 h/day per contributor lifts Overall to ~67.4.
- **#202687 still title-only** (no Desc, no AC) — flagged every audit A1 → A5.
- **12 PI7-parent User Stories orphan** (#202059–#202071) — no sub-iteration.
- **DoR regressed** 83.3 → 69.2 as new items (#202396, #202464, #203229) entered without refinement.

**Pages touched:**

- Created [[summaries/audit-ado-shared-20260422-0644]]
- Updated [[entities/team-ado-shared]] — Current state reframed from 7.1-close baseline (32.2 Critical) to 7.2 Day 3 A5 (53.1 High); history list prepended; updated: 2026-04-22; baseline state moved to "Historical" section.
- Updated [[index]] — summary count 301 → 302; total ingested 281 → 282; Shared Services audits 2 → 3; Latest-audit row swapped (37.7 → 53.1 with band change + bold Δ); entity-table Latest swapped (32.2 Critical → 53.1 High, now citing the actual Shared Services summary instead of the portfolio snapshot); Day-3 heading clarifier extended to "OTP + Shared".

**Audit-numbering note:** report body labels this **A5** and cites `AUDIT_20260422_0900.md` (A3, 37.7) and A4 (35.3) as intermediate priors. Per §10 the A4 date annotation mentions `Apr 23` which appears to be a PHT/UTC crossover. Filename-UTC ordering for 4/22 Shared is 0644 → 0900 → 1450 → 1930; ingest follows filename, not A-number.

**Synthesis implications to track:**

- [[synthesis/capacity-planning]] — Shared Services is now the canonical "capacity-unconfigured persists past positive delivery" case. A deliverable team without capacity config is a new wrinkle (prior capacity-planning doc framed it as "capacity signals vacation/holiday"). Worth a follow-up edit when we have 4/23 data.
- [[synthesis/service-model-scoring]] — this audit is the **first empirical data point** showing the rubric can register a service-team delivery signal. The −40 no-User-Story penalty remains, but Delivery Predictability works correctly when closures happen. Adjusts the service-model thesis.
- [[synthesis/dor-leakage]] — DoR REGRESSED this audit (83.3 → 69.2) as new items entered mid-sprint without refinement. This is a new failure mode — not "planning-time leakage" but "mid-sprint injection without DoR."

(Not editing those synthesis pages yet — flag for a later cross-cutting update once more 4/22 and 4/23 audits are ingested.)

## [2026-04-23 17:00] ingest | Administration audit 2026-04-22 06:46 UTC (7.2 Day 3, live-data)

Third ingest in the oldest-first sweep. `ado_admin/AUDIT_20260422_0646.md` — earliest of three tied `_0646` files (alphabetical before ado_fin, ado_fl_dev).

**Score:** 71.0 (🟡 Moderate). Δ **+1.5** vs prior ingest (4/21 0800, 69.5). Δ +1.5 vs held #34 at 09:00 (degraded mode, 69.5).

**Single driver — Backlog Refinement 80 → 90:** live data confirmed 9 of 11 sprint items touched on/after Apr 20 iter start; untouched-current dropped 45.5% → 18.2% (falls into −10 band rather than −20). All other dimensions unchanged.

**Notable:** this is the **first live-data audit after a degraded-mode hold.** The 0900 audit (#34) ran without ADO connectivity and held prior scores; this 0646 UTC run is the next live confirmation. For wiki ingest purposes, degraded-mode audits don't warrant separate summary pages — they add no live signal. Skipping such holds if/when we see them in the remaining 4/22 backlog.

**Unchanged risk posture:**

- Over-commit 39 SP vs 27 SP PI7.1 ceiling = +44%.
- Bus-factor-1 — Mark Colina sole owner of all 11 items.
- **DoR remediation deadline missed.** #202898 (Condo dues, 3 SP) moved New → Ready with no Desc/AC. #202909 (Davao Admin Adhoc, 4 SP) moved New → Active with no Desc/AC. 7 SP in flight without done-criteria.
- 9 PI7-root legacy items (192221, 193412, 197023, 197028, 197029, 197111, 197113, 197115, 202894) unchanged for 4th consecutive audit. Caps Iteration Planning at 55.0 indefinitely.
- #202357 (Rooftop Davao, 5 SP, Active, last touched Apr 17) and #202366 (PhilGeps, 3 SP, Active, last touched Apr 17) still pre-sprint dates — a 1-click state update removes the remaining −10 Backlog Refinement penalty → 100.0.

**Pages touched:**

- Created [[summaries/audit-ado-admin-20260422-0646]]
- Updated [[entities/team-ado-admin]] — Current state reframed 7.1-close (87.0 Low) → 7.2 Day 3 (71.0 Moderate); history list prepended; updated: 2026-04-22; 7.1 close state kept in "Historical" section.
- Updated [[index]] — summaries 302 → 303; total ingested 282 → 283; Admin audits 35 → 36; Latest-audit row swapped; entity-table row swapped (87.0 Low → 71.0 Moderate); Day-3 heading clarifier extended to "Admin + OTP + Shared".

**Convention note for degraded-mode runs:** not ingesting as standalone summaries. When a live-data successor exists for the same audit number / sprint day, skip the degraded run and let the live run supersede. If a degraded run is the only available data for a day, ingest it with a `data_mode: degraded` tag in frontmatter and flag the score as "held" rather than "measured" — no audit encountered this case yet.

**Remaining 4/22 earliest cohort:** ado_fin/_0646, ado_fl_dev/_0646 (tied with the one just ingested). Then the _0900 batch (hr, jit, ls_dev, aa, cc).

## [2026-04-23 17:15] ingest | Finance audit 2026-04-22 06:46 UTC (7.2 Day 3, live-data)

Fourth ingest in the oldest-first sweep. `ado_fin/AUDIT_20260422_0646.md` — second of three tied `_0646` files (after ado_admin).

**Score:** 77.9 (🟡 Moderate). Δ **0.0** vs prior ingest (4/21 0800, 77.9). Δ 0.0 vs audit #35 at 0900 (also 77.9). **Flat score but leading indicators positive.**

**First work activity of the sprint confirmed:** Grace returned from configured off-days (4/21–22 elapsed per her 4h/day capacity config) and moved two items to Active — #203038 (Career Mapping market rates, 3 SP) and #203040 (AA Escalation, 1 SP). ChangedDates Apr 23 03:30 UTC map to Apr 22 PHT evening. No closures yet, so Delivery Predictability holds at 0.0.

**Short path to Low band:**

- Move #203043 (FTC HR for signed APEF, 2 SP) from `Jairosoft FINOPS\2026-PI7` root → `...\Iteration 7.2`. 60-second edit. Iter Planning 75.0 → 100.0, Overall 77.9 → 81.5 (Low).
- Close #203040 (1 SP Issue, already Active). Delivery Pred 0.0 → 14.3, Overall → 80.1 (Low).
- Combined: 83.9. All three closures by Day 7 gets 86.1.

**Compliance risk escalating:** #201448 eAFS Portal Submission still absent from backlog across 4 consecutive audits (dropped at 4/19 close). BIR deadline Apr 15 is now 7 days elapsed. Report recommends Grace surface disposition today — either create a closure record in ADO or escalate to Ramon as a compliance breach. [[synthesis/compliance-misalignment]] thesis continues to hold.

**Pages touched:**

- Created [[summaries/audit-ado-fin-20260422-0646]]
- Updated [[entities/team-ado-fin]] — Current state reframed 7.1-close (93.7 Low) → 7.2 Day 3 (77.9 Moderate); history list prepended; updated: 2026-04-22.
- Updated [[index]] — summaries 303 → 304; total 283 → 284; Finance count 34 → 35; Latest-audit row swapped; entity-table row swapped (93.7 Low → 77.9 Moderate); Day-3 heading clarifier extended to "Admin + Finance + OTP + Shared".

**Audit-numbering note:** report labels itself unnamed but cites audit #35 at 0900 as prior. Filename-UTC ordering for 4/22 Finance: 0646 → 0900 → 1000 → 2341 → 2350. All 5 are Day-3/Day-4 samples of the same iteration state; likely many will be degraded-mode or near-duplicate — will assess each when reached.

**Progress toward 4/22 catch-up:** 4 of 10 teams now have 4/22 summaries (OTP, Shared, Admin, Finance). Remaining: Flawless Wedding (`_0646` tied), HR (`_0900`), JIT (`_0900`), Life Style (`_0900`), Auto Allies (`_0900`), Colina (`_0900`). Plus optional same-day re-runs if they show distinct state (most expected to be flat holds).

## [2026-04-23 17:30] ingest | Flawless Wedding App audit 2026-04-22 06:46 UTC (7.2 Day 3, live-data)

Fifth ingest. `ado_fl_dev/AUDIT_20260422_0646.md` — last of three tied `_0646` files; completes the earliest-timestamp 4/22 cohort. All `_0646` runs ingested (OTP, Shared, Admin, Fin were in reality `_0644` each; only Admin, Fin, Fl Dev share the exact `_0646` timestamp — OTP and Shared were `_0644`. Corrected cohort tally reflected in this entry).

**Score:** 62.5 (🟡 Moderate). Δ **+2.9** vs prior ingest (4/21 0800, 59.6 High). **Band promotion High → Moderate.** Δ +2.9 vs held audit #34 at 0900 (degraded, 59.6).

**Primary driver — Luke's Day-3 closures:** #202072 (Vendor Login Error, 2 SP) + #202119 (Blank Dashboard, 2 SP) = 4 SP closed, first non-zero Delivery Predictability of sprint (0 → 28.6 — above "early-sprint low-delivery" rubric baseline). #202569 (Bride notification, 1 SP) advanced to QA Testing. QA pipeline now loaded with 5 SP awaiting Ressa.

**Secondary driver — Backlog Refinement 80 → 90:** untouched-current dropped 72.7% → 25.0% as 9 of 12 items refreshed post-iter-start (only Apr-15 trio #190892, #191079, #201326 remain pre-sprint).

**Small regressions:**

- Estimation 100 → 90: new Defect #203230 ("Vendor users unable to login — deleted flag") added mid-sprint with 0 SP. Doesn't count toward Delivery Pred when closed; assign ≥1 SP fixes.
- DoR Compliance 100 → 91.7: #202827 Spike Description is **29 non-whitespace chars** ("Reports and Iteration Team Events") — 1 char short of 30-char threshold. **Easiest DoR fix in the entire portfolio** — one more descriptive word restores 100.0.

**Structural ceiling unchanged:**

- Work Item Balance stuck at **30.0** — 10 Defects (83.3%) + 2 Spikes (16.7%) + **0 User Stories**. −40 no-US penalty stacked with −30 dominant-type. Adding one US from 7.3 pipeline is the single highest-leverage action anywhere in the 4/22 audit set (+5.7 to Overall, lifts to 68.2).
- Iteration Planning 7.4 — 12/162 visible items in 7.2. Ressa's BacklogCleanUp Spike (#202873) targets this directly.

**Pages touched:**

- Created [[summaries/audit-ado-fl-dev-20260422-0646]]
- Updated [[entities/team-ado-fl-dev]] — Current state reframed 7.1-close (79.3 Moderate "0.7 from Low") → 7.2 Day 3 (62.5 Moderate with −16.8 regression); history list prepended; updated: 2026-04-22. Note: the team moved from "almost Low" to "risk band promoted from High" in three days — captures both the 7.1→7.2 reset and the Day-3 delivery recovery.
- Updated [[index]] — summaries 304 → 305; total 284 → 285; Flawless count 26 → 27; Latest-audit row swapped with **bold Δ** and band-promotion callout; entity-table row swapped (79.3 → 62.5); Day-3 heading clarifier extended to "Admin + Finance + Flawless + OTP + Shared".

**Audit report edge case:** section 1's metadata table printed `Risk Band: High Risk (40–59.9 → boundary; actual 62.5 = Moderate Risk)` with an inline correction. The report's self-check caught its own template default. Recorded the live score 62.5 in the wiki — band label is Moderate per rubric.

**Progress toward 4/22 catch-up:** 5 of 10 teams now have 4/22 summaries. All `_0644`/`_0646` cohort done (5 teams). Remaining 5 are all `_0900`: HR, JIT, Life Style, Auto Allies, Colina. Next ingest would be `ado_hr/AUDIT_20260422_0900.md` (alphabetical first in the `_0900` cohort).

## [2026-04-23 17:45] ingest | HR Recruitment audit 2026-04-22 09:00 PHT (A35, 7.2 Day 3)

Sixth ingest. `ado_hr/AUDIT_20260422_0900.md` — first of the `_0900` cohort (alphabetical).

**Score:** 83.4 (🟢 Low). Δ **+2.0** vs prior ingest (4/21 1400, 81.4 Low). **Low band held for 3 consecutive audits — first sustained Low streak in workspace history.**

**Driver — first non-zero Delivery Predictability in PI7 series:** 0 → 13.5. Three User Stories closed on Day 2 at a single UTC timestamp (Apr 21 19:01:32) — #202017 Verano + #202022 Pabatao (Sr. Tech Lead client interviews, 2 SP each) + #202039 Fernandez (Sales & Mktg decision, 1 SP) = 5 SP. Likely a batch decision-recording session rather than 3 independent same-day completions; report flags this as Almera recording decisions already made during the day.

**Six of seven dimensions at or above ceiling** (5 × 100.0, WIB 70.0 structural 100% US penalty, DP 13.5 early-sprint low-expected).

**Unresolved P0 for 3rd consecutive audit:**

- Overbook **37 SP vs 22 SP PI7.1 velocity = +68%**. Required burn rate 3.2 SP/day vs historical 1.57 SP/day (roughly 2× pace needed). P0 de-scope recommendation from #33 + #34 + #35 unactioned. Report suggests moving #203053 Fajardo, #203057 Ramos (also has body defect), #203067 Tayao APE self-eval, and one LinkedIn/Comm item to 7.3.

**New findings this audit (content-accuracy flags):**

- **#203057 (Sr. Tech Lead — Rodelio Ramos)** — description body references "Reban Cliff Fajardo" (candidate in #203053). Cloned-from-source; title updated, body not. DoR char thresholds still pass (score unchanged 100.0), but content is wrong.
- **#203063 (Sales & Mktg — Angel Dorothy Abina)** — description body references "Shamyll Gelbolingo". Same cloned-body pattern.

These are flagged as quality issues outside the rubric; both should be corrected before the items transition to Active. Notably, the rubric's DoR dimension measures **Description + AC char counts**, not **content accuracy** — a gap worth noting for future rubric evolution (candidate for a synthesis page: "DoR content-accuracy vs character-count").

**Persistent flags unchanged:**

- Bus factor = 1 (Almera; Grace 0 capacity 35 audits).
- No iteration goal documented (35th consecutive audit — rubric doesn't penalize).
- #200671 LinkedIn Tech Sales untouched since Apr 18 (3 audits) — 4.8% below 10% penalty threshold but suggestive of a blocker/waiting-on-LinkedIn situation.

**Pages touched:**

- Created [[summaries/audit-ado-hr-20260422-0900]]
- Updated [[entities/team-ado-hr]] — Current state: 7.1-close (87.0 Low) → 7.2 Day 3 (83.4 Low, +2.0); historical section preserved.
- Updated [[index]] — summaries 305 → 306; total 285 → 286; HR count 34 → 35; Latest-audit row swapped; entity-table row swapped (87.0 → 83.4 both Low); Day-3 heading clarifier extended.

**Lightweight convention filed:** for future rubric discussion — **DoR rubric measures form, not content.** Today's #203057 and #203063 are content-inaccurate but score 100 because Description and AC meet character thresholds. This is the second workspace this week to surface a "DoR-passes-but-is-wrong" pattern (Shared Services #202687 was empty; Flawless #202827 was 1 char short). A synthesis page tracking this could be valuable later.

**Progress toward 4/22 catch-up:** 6 of 10 teams done. Remaining `_0900` cohort: JIT, Life Style, Auto Allies, Colina. Next ingest: `ado_jit/AUDIT_20260422_0900.md`.

## [2026-04-23 18:00] ingest (batch) | remaining 4/22 _0900 cohort — JIT, Life Style, Auto Allies, Colina

User directed a batch ingest to complete the 4/22 sweep. All four `_0900` audits ingested in one pass.

**Infrastructure pattern today (2026-04-22):** something broke at the tooling layer during the 4/22 09:00 PHT scheduled audit window — **2 of 4 audits ran in degraded mode** (ADO MCP tools permission-denied) and **2 of 4 ran in partial mode** (ADO live, GitHub private-org 404 under current `raseniero` token). Pattern worth investigating — may indicate token rotation, org permission change, or MCP config issue across both ADO and GitHub integrations on the same morning.

### Per-team

**JIT Operation (A35 degraded):** 72.9 Moderate, **Δ 0.0 vs A34**. No live signal. Grace returns today from Apr 21–22 PTO; Summer Camp Training #203047 now 3 days out. P1 (armelita touch #199092, #198615) unverified. Audit explicitly acknowledges degraded mode and carries A34 scores. Later 4/22 JIT files (`_1400`, `_2344`, `_2351`) on disk may supersede.

**Life Style Help App (A27 degraded):** 41.0 High, **Δ 0.0 vs A26**. Second consecutive audit at 41.0. Audit agent explicitly names "score plateau risk" — locked at 41.0 until capacity or delivery breaks stalemate. **#187240 Enabler now 247 days stale — 11th consecutive audit flag.** Unchanged backlog failure mode.

**Auto Allies (7.2 Day 3 partial):** ICS 95.3 / SGPI 0.0 / HCI 53 — **all flat vs Day 2**. ADO fresh; GitHub API 404 on both repos. Key worsening: 5 Estimation items (10 SP) missed the Day-3 sprint-lock deadline. Path to Moderate HCI unchanged (+7 via branch protection + 2nd review + AB# on direct commits).

**Colina Health (7.2 Day 3 partial):** ICS 90.3 **(−3.3, fragile Green)** / SGPI 0.0 headline + 20.0% Delivered-Proxy (+16.7) / HCI 77 (−2). ADO fresh; 3 GitHub repos 404. **New DoD failure**: #202028 (PRN defect) missing AC field in live batch — joins persistent #200093 + #200828 null Descriptions. Third failure brings Quality/DoD to 72.7% — ICS now 0.3 pts above Yellow. **BE#55 HIPAA PR** rework still pending; **#202690 Secrets Mgmt** (HIPAA-adjacent, 3 SP) has zero GitHub activity by Day 3. Jaszmeine returns today; 4 new defects need triage.

### Pages touched (batch)

- Created: 4 summaries — `audit-ado-jit-20260422-0900`, `audit-ado-ls-dev-20260422-0900`, `audit-git-aa-dev-20260422-0900` (partial), `audit-git-cc-dev-20260422-0900` (partial). JIT + LS-Dev carry `data_mode: degraded` frontmatter; AA + Colina carry `data_mode: partial`.
- Updated: 4 entity pages — `team-ado-jit`, `team-ado-ls-dev`, `team-git-aa-dev`, `team-git-cc-dev`. Current state reframed from 7.1-close → 7.2 Day 3; historical sections preserved; audit-history lists prepended.
- Updated: `index.md` — summary count 306 → 310; total 286 → 290; counts bumped for all 4 teams; Latest-audit table fully updated; **entity-latest table now shows 7.2 Day 3 scores for all 10 teams**; Day-3 heading clarified with data-mode legend (6 live / 2 degraded / 2 partial).

### Milestone

**4/22 Day 3 portfolio snapshot is now complete in the wiki** — all 10 teams have 4/22 summaries. This is the first full-portfolio day ingested since 4/21. The 10-team Iter 7.2 Day-3 picture now reads (headline score or lead metric): Admin 71.0 · Fin 77.9 · Flawless 62.5 (band-promoted ↑) · HR 83.4 · JIT 72.9* · LS-Dev 41.0* · OTP 65.2 · Shared 53.1 (band-promoted ↑) · AA ICS 95.3/HCI 53^ · Colina ICS 90.3/HCI 77^. (* = degraded; ^ = partial GitHub.)

**Day-3 themes observable across the portfolio:**

1. **Two band-promotions since 4/21**: Shared Services Critical → High (+15.4, DevOps IT delivery); Flawless Wedding High → Moderate (+2.9, Luke Day-3 closures).
2. **Three "DoR passes but content wrong" cases**: Shared #202687 empty, Flawless #202827 29 chars (1 short), HR #203057 + #203063 wrong-candidate copy-paste. Pattern deserves a future synthesis page.
3. **Persistent capacity gaps**: Shared Services still 0.0 (5 audits), LS-Dev still 0.0 (3 audits into 7.2). Capacity-config is the cheapest single-action lever across the portfolio.
4. **GitHub access degradation**: `raseniero` token returned 404 on all 5 jairosoft-com repos today (2 AA + 3 Colina). Critical evidence gap for 2 Git-audited teams. **Fresh token was installed at the start of this session** — so the 4/22 09:00 failure was pre-token-rotation. The token rotation pattern in `.mcp.json` today (confirmed working at conversation start) should restore Git access for 4/23 audits.

### Remaining backlog

Same-day re-runs on disk for every team (`_0900` base audit plus 1–5 later timestamps per team — primarily afternoon/evening runs). Per established convention: skip degraded-mode same-day re-runs that hold identical scores; ingest later runs only if they carry distinct live-data signal. Listed by team (latest timestamps already on disk):

- ado_otp: `_0900`, `_1450`, `_1800`, `_1930`, `_2343`
- ado_shared: `_0900`, `_1450`, `_1930`
- ado_admin / ado_fin / ado_fl_dev: `_1000`, `_2341`, `_2350`
- ado_hr / ado_jit / ado_ls_dev: `_1400`, `_2340`, `_2344`, `_2350`–`_2352`
- git_aa_dev / git_cc_dev: no additional 4/22 files (single-audit day)

**Per-team plan:** spot-check each team's latest `_2300`-ish run for distinct score movement. If flat, skip with a single-line log note. If distinct, ingest. This can be a quick pass separate from full-day ingestions.

**Broader ingest backlog (not yet touched):** all 4/23 team audits (every team has at least one on disk) + 4/23 portfolio_report HTMLs (`_1020`, `_1530`, `_1535`).

## [2026-04-23 18:30] ingest (batch) | Full 4/23 Day-4 portfolio cohort — 10 teams

Second batch ingest in sequence. User directive: "go" (continue oldest-first 4/23 sweep under the prior "ingest all remaining" mandate). One canonical 4/23 audit per team (earliest timestamp per team), all 10 written as 4/23 Day-4 snapshots.

### Data-mode improvement across portfolio

**8 live, 2 partial** — significant infrastructure recovery from 4/22 (which was 6 live / 2 degraded / 2 partial). ADO MCP tools restored for all 8 ADO teams. GitHub private-org access still denied for AA + Colina (4th consecutive day). Fresh PAT installed at conversation start has not resolved GitHub access — likely an org-level access grant or SSO scope issue.

### Portfolio snapshot (Day 4, 2026-04-23 morning)

| Team | Score | Band | Δ vs 4/22 | Notable |
|------|------:|------|----------:|---------|
| Administration | 71.0 | 🟡 Moderate | 0.0 | DoR deadline missed 2nd day |
| Finance | 77.9 | 🟡 Moderate | 0.0 | 5 flat audits; Day 5 = last DP annotation |
| Flawless | 63.5 | 🟡 Moderate | **+1.0** | **5 SP delivered** (Ressa closed 3 Defects) |
| HR | 83.3 | 🟢 Low | −0.1 | **Low streak 4 audits** (first sustained) |
| JIT | **75.5** | 🟡 Moderate | **+2.6** | **Sprint expanded 26→50 SP**; 4 contributors active |
| LS-Dev | 41.0 | 🟠 High | 0.0 | **Plateau confirmed — 4 consecutive audits at 41.0**; #187240 = 248d |
| OTP | 63.3 | 🟡 Moderate | −1.5 | Live-data correction (#201811 untouched BR penalty) |
| Shared Services | **35.3** | 🔴 Critical | **−17.8 (scope)** | **Scoping correction** — A5 broader scope (53.1) vs A4 team-owned (35.3); not a real regression |
| Auto Allies | ICS **100** · HCI 58 | HCI 🟠 (+2 to Moderate) | ICS +4.7 · HCI +5 | **3 material Day-4 wins** (DoR perfect, sprint-lock done, #202530 in QA Testing) |
| Colina Health | ICS 90.3 · HCI 78 | ICS 🟢 fragile · HCI 🟡 | ICS 0 · HCI +1 | Movement Day: #202690 + #200828 advanced; #202033 regressed |

### Portfolio themes at Day 4

1. **Delivery activating** — Flawless +5 SP, Colina proxy 20%, AA #202530 in QA. **First non-zero delivery across multiple teams** in 7.2.
2. **Data-mode heterogeneity at the audit pipeline layer** — 4/22 morning had 2 ADO outages + 2 GitHub 404s; 4/23 has 0 ADO outages + 2 GitHub 404s still. ADO reliability restored; GitHub blackout persistent.
3. **Shared Services scoring boundary question surfaced** — A5 (4/22 PHT afternoon) counted DevOps IT cross-team deliverables that appear on the Shared Services iteration path; A4 (4/23 morning) tightens to team-owned items. Numeric drop 53.1 → 35.3 is **scoping correction, not regression**. Notable rubric question for future synthesis: how should cross-team items be scored?
4. **JIT breakthrough** — sprint expansion (11→20 items, 26→50 SP) activated Teofilo (21 SP Training) and Samantha (1 SP Facebook post) for first time. Concentration risk on armelita eased from 92% → 46%. BUT 6 of 7 new Teofilo items added without Desc/AC (DoR 100→70).
5. **LS-Dev plateau risk now named by audit agent** — 4 consecutive audits at 41.0 with zero ADO activity. **#187240 at 248 days** (12th flag); #195727 untouched 6 sprint days.
6. **OTP "first live 7.2 audit" surfaces two data corrections** — #201811 untouched penalty (BR −10) and #202913 assignee correction (retract A33 "first unassigned" finding).
7. **AA's 3-win Day-4 wave** — ICS perfect, sprint-lock done, PR#123 TS2304/TS2307 inferred merged via #202530 QA Testing transition. HCI +2 away from Moderate (branch protection fix alone crosses threshold).
8. **"DoR passes but content wrong" pattern** observed in HR this week: #203057 body names Fajardo, #203063 names Gelbolingo. Now 3 workspaces with this pattern (Shared, Flawless, HR) — rubric measures form not content.

### Pages touched (batch)

- **Created: 10 summaries** — one per team, 4/23 canonical:
  - audit-ado-admin-20260423-0113
  - audit-git-aa-dev-20260423-0855
  - audit-git-cc-dev-20260423-0856
  - audit-ado-ls-dev-20260423-0900
  - audit-ado-otp-20260423-0900
  - audit-ado-shared-20260423-0900
  - audit-ado-fin-20260423-0905
  - audit-ado-fl-dev-20260423-0910
  - audit-ado-hr-20260423-0914
  - audit-ado-jit-20260423-0916
- **Updated: 10 entity pages** — audit-history prepended, Current-state reframed to Day-4 score + prose.
- **Updated: index.md** — 310 → 320 summaries, 290 → 300 total. All Latest-audit rows swapped. Entity-table latest-summary links repointed to 4/23 summaries. Day-4 heading + data-mode legend updated (8 live / 2 partial).

### Milestone

**300 total audit summaries.** First 4-day portfolio continuity window established (4/20 close + 4/21 open + 4/22 Day 3 + 4/23 Day 4). Ready for mid-sprint synthesis once Day 5–7 delivery data arrives.

### Remaining ingest backlog

- **4/22 same-day re-runs** (~25 files) — mostly flat holds or superseded by 4/23 live data; skip by convention unless distinct signal.
- **Same-day 4/23 re-runs** (~7 files: ado_hr/_1500, ado_jit/_1254+_1505, ado_ls_dev/_1510, ado_otp/_1100, ado_shared/_1105, git_aa/_1515, git_cc/_1515) — afternoon follow-ups; likely Δ ≤ 1 point unless delivery happened.
- **Portfolio dashboards** — `_0130` (4/21), `_0900 + _1000` (4/22), `_1020 + _1530 + _1535` (4/23). Recommendation: ingest latest per day (3 files).
- **Meeting agendas** — `PORTFOLIO_MEETING_AGENDA_20260421.html` (historical) and `PORTFOLIO_MEETING_AGENDA_20260423.html` (likely superseded by already-ingested _1600).
- **raw/jit/meeting_transcript/Apr_23rd_2026.docx** — novel source type, discuss pattern before ingesting. *(path retired 2026-04-23 after folder reorg to `raw/meeting_transcripts/{jit,lean_portfolio_leadership}/Apr_23rd_26.docx`.)*

## [2026-04-23 19:00] ingest (batch) | Portfolio dashboards + meeting agenda + first raw transcript

Third and final batch of the day — closes the priority backlog per the user's "ingest remaining" direction. 5 summaries created covering different source types than per-team audits.

### Ingested

- **[[summaries/portfolio-20260421-0130]]** — 7.2 Day-2 sprint-open (mean 63.9 / median 67.2 / 1·6·2·1 distribution). First dashboard after 4/19 Low-Risk peak; −12.2 mean is expected Day-2 denominator reset.
- **[[summaries/portfolio-20260422-1000]]** — Day-3 morning snapshot (mean 63.9 / median 66.6, flat). Aggregates degraded-mode morning runs; only HR moved (+2.0). Distribution unchanged from 4/21.
- **[[summaries/portfolio-20260423-1535]]** — **Day-4 afternoon** (mean 64.6 / median 68.0 — first upward tick since sprint open). **Two notable band changes:** Shared Services exits Critical (37.7 → 41.1); LS-Dev falls INTO Critical (41.0 → 39.7, dropping below Shared — **first #9/#10 inversion in workspace history**). AA ICS 100% first perfect.
- **[[summaries/meeting-agenda-20260421]]** — 30-min sprint-open review. 9 P0 Quick Wins mapped to owners; 3 PDM Sign-Off decisions. Added follow-up-outcome tracking section noting which actions landed by 4/23 (HR closures ✓, AA DoR fix ✓, sprint-lock ✓, PR#123 merge ✓; Shared/LS-Dev capacity ✗, Admin DoR ✗, Flawless add US ✗).
- **[[summaries/transcript-lpm-review-2026-04-23]]** — **NEW SOURCE TYPE** (transcript-*). 46-min LPM Review meeting captured Ramon + Karl discussion at 11:40 PM PHT on 4/23. Two significant confirmations:
  1. **GitHub 404 root-caused** — `raseniero` token access-scope issue, Ramon committed to fix ("I just need to fix the API access"). Not a team compliance gap.
  2. **Jerlyn + Ressa are not developers** — Ramon explicitly said to document them as "not developers so they don't need GitHub." Resolves the 4-iteration "Jerlyn GitHub-silent" finding as a **documented project exception**, not a gap.

### Convention established

**New summary type filename pattern: `transcript-<workspace>-<date>.md`** for raw meeting transcripts. Policy: extract confirmations/decisions/action-items; do not paste raw transcript; note voice-to-text quality caveat. Filed in the transcript summary itself.

### Index updates

- Portfolio snapshots table — 3 new rows (4/21 0130, 4/22 1000, 4/23 1535) prepended; 4/19 1953 row retained.
- Summary count 320 → 325 (300 audits + 24 portfolio + 2 meeting agendas including 4/21 and 4/23_1600 + 1 transcript — 24 portfolio count includes new 3 plus prior 21).
- Header text updated to list the new counts breakdown.

### Unresolved-as-declined (skip-by-convention)

- **4/22 same-day re-runs** (~25 files) — mostly flat holds or degraded-mode; superseded by 4/23 live data.
- **4/23 afternoon re-runs** (~7 files) — 4/23 1535 portfolio already captures the afternoon state at the aggregate level.
- **PORTFOLIO_MEETING_AGENDA_20260423.html** (non-timestamped variant) — likely superseded by the already-ingested `_1600` version; left unless distinct.
- **Portfolio dashboards 4/22 0900 and 4/23 1020/1530** — not ingested (superseded by 4/22 1000 and 4/23 1535 same-day).

### Content gaps logged

From the transcript confirmations, two **project-exception edits** should propagate to source CLAUDE.md files (not done this session, flagged for followup):

1. `git_aa_dev/CLAUDE.md` — add to Project Exceptions: *"Jerlyn Ates and Mary Secusana are not developers; GitHub absence is expected. HCI 'GitHub-silent' findings for them are documented exceptions, not gaps."*
2. `git_cc_dev/CLAUDE.md` — add similar exception for any non-dev team members. (Not mentioned in transcript but same pattern applies.)
3. Temporary: HCI scoring on AA + Colina should carry `data_mode: partial` with a note that persistent GitHub 404 is a known token/scope issue pending Ramon's fix, not team failure. Update when GitHub access is restored.

**These are edits to immutable raw sources (source CLAUDE.md files), which the wiki is normally not supposed to touch.** Flagged for user approval before executing.

### Milestone

**325 total wiki pages** across summaries + entities + concepts + synthesis. **First complete portfolio week** (4/19 close + 4/21 open + 4/22 Day 3 + 4/23 Day 4) with all layers (per-team audits, portfolio dashboards, meeting agenda, transcript) ingested. First `transcript-*` source type established. Priority backlog complete.

## [2026-04-23 19:20] propagate | Project exceptions from LPM transcript → source CLAUDE.md files

User approved propagation of the two exception decisions captured in [[summaries/transcript-lpm-review-2026-04-23]]. **This is an unusual direction** — the wiki normally never writes to raw sources. User approval was explicit ("yes lets propagate the exceptions"), so proceeding.

### Raw-source edits (source-of-truth CLAUDE.md files)

**`git_aa_dev/CLAUDE.md` — Project Exceptions section:**

- Added exception: **Jerlyn Ates (QA/Requirements) and Mary Secusana (Documentation) are not developers.** GitHub absence for these roles is expected and must not be scored as HCI penalty or team compliance gap. Cites Ramon's direct quote from the 2026-04-23 LPM Review.
- Added exception: **GitHub API 404 on `raseniero` token (Apr 21 onward)** is a known access-scope issue. Audits during this window carry `data_mode: partial` frontmatter; HCI dims 1–6 scored as 4/21 carry-forward rather than fresh evidence. No team penalty while token issue unresolved.

**`git_cc_dev/CLAUDE.md` — Project Exceptions section:**

- Extended exception: **Non-developer team members** (Luzmibel Paculanang QA, Jaszmeine Villanueva Design) follow same principle — GitHub absence expected, no HCI penalty. Transcript didn't explicitly name Colina members but the principle was articulated cross-team.
- Same GitHub 404 exception as AA.

### Wiki entity updates

**`wiki/entities/team-git-aa-dev.md`:**
- Resolved the long-standing Open Question ("Jerlyn escalation path — HR review?") with strikethrough + resolution note pointing to transcript summary and the CLAUDE.md exception.
- Annotated the "Zero formal PR reviews" Real Fixable Issue with the Day-4 recovery (Earl's first human PR review on PR#123).

**`wiki/entities/team-git-cc-dev.md`:**
- Added new "Notes on project exceptions" section documenting both the non-dev exception and the GitHub 404 carry-forward policy.

### Scoring implication going forward

For AA and Colina audits through the token-fix window:

1. **Jerlyn (AA) and Mary (AA)** — HCI dim 10 "Capacity Balance & Ownership Distribution" should not flag their zero GitHub output as concentration imbalance.
2. **Luzmibel (Colina) and Jaszmeine (Colina)** — same principle. Jaszmeine's design/triage work (new defect triage, Apr 22 return) is legitimate contribution.
3. **HCI dims 1–6** on AA + Colina should be scored as Day-2 (2026-04-21) carry-forward until token fix. **Do not lower HCI** based on "stale" carry-forwards — the staleness is token-side, not team-side.
4. **Team-rankings synthesis** ([[synthesis/team-rankings]]) may need a note that AA's HCI 58 and Colina's HCI 78 are capped by evidence access, not necessarily team performance.

### Not done (deferred to user)

- **Follow-up with Ramon on token fix** — transcript captured the commitment; no ETA was discussed.
- **Karl hiring-risk register follow-up** with Grace — also captured in transcript; requires Karl to act, not a wiki edit.
- **Admin 12 SP de-scope** — authorized in meeting but execution is Karl's to do in ADO.
- **Claude partner → epic migration** — program direction; requires ADO structural change not a wiki edit.

These items are captured in the transcript summary's Action Items section for future audit reference but do not require wiki or source-file edits.

### Convention implication for future wiki edits

This is the **first precedent of the wiki writing to a source CLAUDE.md file.** Normally the wiki is strictly read-only on raw sources. The justification here:

1. User explicitly approved.
2. The edit is adding a **decision captured in a meeting** — classic source-of-truth content that belongs in the team's local CLAUDE.md.
3. Without this edit, every future audit would re-flag the same compliance-gap findings that have now been resolved by project exception.

**Future policy suggestion (not filed):** wiki can propagate **decisions** (documented with meeting source) to source CLAUDE.md Project Exceptions sections, but must:
- Cite the meeting/source in the exception text.
- Preserve the prior content (additive only).
- Log the propagation in `wiki/log.md` with the transcript/decision summary linked.

If the user wants this formalized, consider adding it to `wiki/CLAUDE.md` (the wiki schema). Not done this turn.

## [2026-04-23 19:30] bookkeeping | Created wiki/TODO.md for persistent cross-session to-do tracking

User asked: *"Is there a to-do list that we can maintain so that we can add the things that we need to do or that we have identified in the session that we can do later on?"* Created `wiki/TODO.md` as the canonical cross-session to-do surface.

### Structure

Three open-item sections:

1. **External / waiting on others (⏳)** — items that need Ramon, Karl, or a specific team member to act. Agent cannot execute these; just tracks them for visibility and reminds when relevant audits surface them again.
2. **Wiki bookkeeping (agent-executable)** — synthesis pages to write, cross-references to add, re-ingests to verify. These are the agent's to complete when cycles allow.
3. **Scripts/tooling** — carried over from earlier wiki log entries (the `scripts/agents/TODO.md` items worth visibility at wiki level).

Plus an **Archive** section at the bottom for closed items.

### Seeded items (12 external · 7 wiki · 5 tooling)

External items all trace back to meeting transcripts or Day-4 audit findings. The highest-leverage ones: Ramon's `raseniero` token fix (unblocks AA + Colina HCI scoring), Karl's Admin 12-SP de-scope (authorized but not executed), and the 4 per-team actions that have been carried across multiple audits without completion (Grace DoR, Mark DoR, Ike #187240, Carol/Ramon Shared capacity).

Wiki items include: the `synthesis/dor-form-vs-content` candidate (3 workspaces now show the "DoR passes but wrong" pattern); updating `synthesis/team-rankings` with HCI-evidence-cap annotations; extending `synthesis/portfolio-trend` past 4/19. The bookkeeping items (spot-check 4/22 + 4/23 afternoon re-runs, verify meeting-agenda variants) are low-priority if the afternoon data actually matters.

### Schema updates in `wiki/CLAUDE.md`

1. Added **"Cross-session TODO tracking"** section explaining `wiki/TODO.md` — categories, when to append, how to close items.
2. Added **"Wiki-to-source edits"** section formalizing the first-precedent from the 19:20 entry — wiki may write to source CLAUDE.md for meeting-documented decisions, with the four safeguards (user approval · source citation · additive only · log entry).

### Index update

Added to `wiki/index.md`: top-of-file pointer "*Also see: [[TODO]] — persistent cross-session to-do list for things we've identified but deferred.*"

### Memory

Saving a user memory entry so future sessions know `wiki/TODO.md` exists and the format conventions. Without this, the agent might recreate or duplicate the file in a future session.

## [2026-04-23 19:45] ingest / rename | LPL transcript surfaced — content-identical to JIT ingest

User asked to ingest "the new meeting transcript for lean portfolio leadership." Investigation found:

- **Raw folder reorganized since 4/23 19:00 batch.** Was: `raw/jit/meeting_transcript/Apr_23rd_2026.docx`. Now: `raw/meeting_transcripts/{jit,lean_portfolio_leadership}/Apr_23rd_26.docx` (plural parent, split by scope, filename shortened).
- **The "new" LPL file is content-identical to the JIT file.** Extracted-text md5 matches exactly across the two DOCX files; binary wrappers differ by 38 bytes (metadata timestamps only). Same 46-minute "Jairo Program Alignment and LPM Review" meeting from 2026-04-23 11:40 PM PHT, filed in both folders because the meeting spans both scopes.

### Action taken

Rather than create a duplicate summary, consolidated to a single canonical summary reflecting the meeting's true scope (LPM Review with a JIT pivot at the end), not just one workspace's framing:

- **Renamed** `summaries/transcript-jit-2026-04-23.md` → `summaries/transcript-lpm-review-2026-04-23.md`.
- **Updated frontmatter** `sources:` list to both DOCX paths (LPL folder + JIT folder, in that order — LPL first because it's the more authoritative scope).
- **Expanded body** with:
  - A clear "same meeting, two folder placements" note.
  - Corrected the "Ressa" reference to note it's most likely a voice-to-text mishearing of "Mary" given AA context.
  - Marked the Jerlyn/Mary non-dev exception as ✅ done (propagated 19:20).
  - Linked to `[[TODO]]`.
  - Retained all the original findings (GitHub 404 root cause, Flawless US requirement, Admin de-scope auth, etc.).

### Reference updates (6 files)

All active links to the old slug updated to new slug:

- `wiki/CLAUDE.md` (schema first-precedent example)
- `wiki/TODO.md` (Ramon token-fix entry)
- `wiki/log.md` (2 prior entries)
- `wiki/entities/team-git-aa-dev.md` (resolved Open Question)
- `wiki/entities/team-git-cc-dev.md` (new Notes section)
- `git_aa_dev/CLAUDE.md` (Project Exception source citation)
- `git_cc_dev/CLAUDE.md` (Project Exception source citation)

Deleted the old `transcript-jit-2026-04-23.md` file. Only remaining mentions of the old slug are historical notes inside the new summary itself (explaining the rename).

### Convention implication

The `transcript-<scope>-<date>.md` filename pattern established earlier still holds. Previous proposed scope (workspace slug) is now refined: **use the meeting's actual title/scope as the slug, not a workspace-of-convenience slug**. So `transcript-lpm-review-2026-04-23.md` rather than `transcript-jit-*.md` because the meeting was titled "LPM Review" with JIT as a side pivot at 46:24.

### Note on dual-filing

The raw-source taxonomy (filing the same DOCX in both `jit/` and `lean_portfolio_leadership/`) is presumably intentional — LPL leadership wants to find it in their folder; JIT program stakeholders want to find it in theirs. The wiki summary abstracts this via `sources: [...]` listing both paths, so search/navigation from either direction reaches the same summary.

If future meetings continue this pattern (dual-filed by scope), the same approach works: one summary, multi-path frontmatter.

## [2026-04-24 10:05] bookkeeping | Filed 2026-04-24 cron observations — 3 TODO items + 1 entity caveat

Reviewed today's MacPilot cron logs at `scripts/agents/logs/` (ado/git/portfolio-health/portfolio-email/portfolio-meeting-prep). 4 of 5 agents succeeded; `portfolio-email` was watchdog-killed at 300s (exit 143). Two other agents (`portfolio-health`, `portfolio-meeting-prep`) exceeded `--max-turns` caps but completed.

### Filings

1. **`wiki/TODO.md` — 3 new tooling items** (under "Open — scripts/agents/ tooling"):
   - P0: `portfolio-email` watchdog-kill — today's dashboard undistributed, diagnose and re-send.
   - P2: budget drift across `portfolio-health` (32/15) and `portfolio-meeting-prep` (33/20) — raise caps or tighten prompts.
   - P3: `.claude/hooks/session_start.py` ENOENT on every agent run (+ related `SessionEnd` ENOENT since ≥2026-04-22).
2. **`wiki/TODO.md` — 1 new bookkeeping item**: investigate silent-stdout regression on batch-audit agents — the 2026-04-24 runs wrote AUDIT files but dropped the customary YAML summary from stdout, and `turns: 1/60` is implausible for an 8-workspace batch. Diagnose before the 2026-04-25 08:30 run.
3. **`entities/system-macpilot.md` — new caveat** under Caveats list: *"Budget drift: skill complexity outpacing configured caps."* Cites two-day, two-agent evidence and notes the 2026-04-23 `--max-turns 15→25` bump on `portfolio-health` either didn't propagate or was already outgrown. Links back to the TODO P2.

### Why filed here vs a new synthesis page

Considered `synthesis/macpilot-budget-drift.md` but the evidence is 2 days × 2 agents — too thin for a standalone synthesis page (existing synthesis pages aggregate 9+ sources). Extending the existing `entities/system-macpilot.md` Caveats list — which already follows an `observed 2026-04-XX` format for operational patterns — keeps the observation close to the other MacPilot ops content.

### Not filed

- ~~Yesterday's 3× `portfolio-health` FAILED exit-1 → today's first-try OK. Clean explanation (the 2026-04-23 fix bumped max-turns and added `Skill` to allowlist) already captured in the system-macpilot entity and 2026-04-23 log entries — nothing new to file.~~ Revisited in the 10:30 entry below — two sub-observations were in fact worth filing.

## [2026-04-24 10:30] bookkeeping | Filed yesterday's recovery observation — 2026-04-23 fix revisited with 2026-04-24 evidence

Reopened the "not filed" item from the 10:05 entry. Today's logs actually contain two corrections/resolutions to the 2026-04-23 fix narrative that are worth the wiki's memory:

### 1. Failure count correction (2 → 3)

The 2026-04-23 11:55 fix entry (log.md line 494) and the then-new entity caveat both described `portfolio-health` as having "failed twice" from launchd. Actual count from `scripts/agents/logs/portfolio-health.log` is three: 09:35, 11:31, 11:45 (all exit 1 with `subtype=error_max_turns` and `Skill` in `.permission_denials`) — then success at 12:20. **Corrected in place** on [[entities/system-macpilot]] §Conventions (the `Skill` tool caveat).

### 2. `--max-turns 15 → 25` bump never reached the running service

The 2026-04-23 fix claimed `portfolio-health` got `--max-turns 15 → 25` as defense-in-depth. Today's 09:38 run logs `turns: 32/15` — the cap is still 15. Possibilities: (a) plist edited but `launchctl bootout` / `bootstrap` never executed (there's a caveat on that exact class of bug — plist env-var changes are cached at first load); (b) the `AUDIT_MAX_TURNS` default in `portfolio-health.sh` was bumped but the plist's `EnvironmentVariables` override still carries 15; (c) edit was reverted. **Flagged on [[entities/system-macpilot]] §Conventions** with a `⚠️ Contradicted 2026-04-24` blockquote next to the original claim, per wiki schema (flag contradictions, don't silently overwrite).

Verification command committed to the flag: `launchctl print gui/$(id -u)/com.macpilot.portfolio-health | grep -i max`.

### 3. Resolution of the 2026-04-23 "still uncertain" open question

The 2026-04-23 11:55 fix entry left this open: *"Why earlier `ado-audit-all` runs (yesterday 23:59) appeared to succeed: still uncertain. Possibilities: the earlier successful runs may have been done in interactive Claude Code mode where the Skill tool isn't gated the same way; or the agent fan-out path (3 parallel sub-agents via `Agent` tool, which IS in the allowlist) sidestepped the parent's need to invoke `Skill` at all."*

Two additional data points now resolve it:

- `ado-audit-all.log` **2026-04-22 23:59 run: `turns: 8/60`** — agent took 8 turns. Consistent with the parent manually orchestrating the workflow (glob → fan-out via `Agent` → aggregate) without calling `Skill`.
- `ado-audit-all.log` **2026-04-23 08:46 + 2026-04-24 08:46 runs: `turns: 1/60`** — agent took only 1 turn. Consistent with a single `Skill` call delegating the entire workflow.

**Conclusion:** the 2026-04-22 run succeeded not because it was in interactive mode, but because (a) `ado-audit-all`'s `--max-turns 60` gave plenty of headroom for the manual workflow, *and* (b) the `Agent` tool was already in its allowlist so the 3-parallel sub-agent fan-out worked independently of `Skill`. `portfolio-health` had neither protection — only 15 turns and no `Agent` fan-out — so its manual-fallback path hit the cap.

This confirms the fan-out-path hypothesis from the original entry. No edit to the 2026-04-23 entry itself (keeping it append-only); resolution lives here and is linked from the updated caveat.

### Not updated

- [[entities/system-macpilot]] §Conventions also claims the 2026-04-23 fix patched *"all 5 production wrappers"* — this remains accurate; the Skill tool is present in all 5 allowlists, only the max-turns bump is what didn't propagate.

## [2026-04-24 10:45] diagnosis | portfolio-health max-turns contradiction — root cause confirmed

Ramon ran the verification command proposed in the 10:30 entry. Result from `launchctl print gui/$(id -u)/com.macpilot.portfolio-health | grep -i max`: **`15`**.

### Three-location audit

| Location | `AUDIT_MAX_TURNS` value |
|---|---|
| `scripts/agents/agents/portfolio-health.sh` (script default) | `25` ✅ (matches 2026-04-23 fix) |
| `scripts/agents/plists/com.macpilot.portfolio-health.plist` (repo source) | `25` ✅ (matches 2026-04-23 fix) |
| `~/Library/LaunchAgents/com.macpilot.portfolio-health.plist` (loaded by launchd) | `15` ❌ (stale — pre-fix) |

Root cause is (a) from the 10:30 entry: the 2026-04-23 repo plist edit was made and committed, but `scripts/agents/install.sh` was never re-run to copy the new plist into `~/Library/LaunchAgents/` and `launchctl bootstrap` it. This is exactly the failure mode documented in the existing *"Plist env-var changes require `launchctl bootout` + `bootstrap`"* caveat — the fix entry itself hit it.

### Wiki updates

- **[[entities/system-macpilot]] §Caveats — Skill-tool ⚠️ blockquote**: rewritten from three-possibility hedge to confirmed root cause + concrete fix command.
- **[[entities/system-macpilot]] §Caveats — "Budget drift"**: softened from "agents exceed their caps" to "agents log `num_turns` above their caps *and still return OK*, pending a 3-turn diagnostic kickstart to distinguish aggregate-turn-rollup from advisory-cap." The original claim was too strong — with cap actually enforced at 15, a real 16th turn would have triggered `error_max_turns`; either the display counts sub-agent turns or the cap is advisory on success paths. TBD.
- **`wiki/TODO.md`**: upgraded P2 to P1 with specific remediation (`./install.sh` or `bootout`+`bootstrap`); added a new P2 for the 3-turn diagnostic experiment that decides whether the other agents have real drift or a display artifact.

### Open

- Running `./install.sh` picks up **all** repo plist edits, not just `portfolio-health`. Worth a quick `diff ~/Library/LaunchAgents/com.macpilot.*.plist scripts/agents/plists/com.macpilot.*.plist` (or reading install.sh's copy logic) before re-running, in case other agents have intentional local plist overrides that a re-install would clobber. Adding to this check to the P1 remediation step is conservative; skipping it and just running `./install.sh` is the normal MacPilot workflow.

## [2026-04-24 11:15] ingest | Day-5 batch — 10 audits + portfolio + meeting agenda

Full batch ingest of today's cron output. First ingest of a PI7.2 day where the audit-to-action feedback loop is visible.

### Sources ingested (12)

- 8 ADO audits: `ado_{admin,fin,fl_dev,hr,jit,ls_dev,otp,shared}/audit/AUDIT_20260424_08{33,33,33,34,34,34,35,35}.md`
- 2 Git audits: `git_{aa_dev,cc_dev}/audit/AUDIT_20260424_0902.md`
- 1 portfolio dashboard: `portfolio_report/PORTFOLIO_20260424_0935.html`
- 1 meeting agenda: `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260424.html`

### Headline — record overnight recovery

**Portfolio mean 69.9 (+5.3) · Critical band cleared (0 teams) · 2 upward band crossings.** Three record-gainer teams: **Life Style +21.4 (largest single-session gain in PI7.2 series; exits Critical), Shared Services +15.0 (ends 6-audit capacity-zero streak), Flawless +11.1 (High→Moderate).** Portfolio recovered to within 6.2 points of the 7.1-close baseline (76.1) after the 7.2-reset dip. First PI7.2 cycle with no Critical teams.

### Writes

- **12 new summaries** under `wiki/summaries/`: 10 per-team audit summaries + [[summaries/portfolio-20260424-0935]] + [[summaries/meeting-agenda-20260424]]. All follow the existing `-YYYYMMDD-HHMM` naming convention.
- **10 entity updates** (team-ado-×8, team-git-×2). Each gets a new "## Latest (Iteration 7.2 Day 5 — 2026-04-24 HH:MM PHT)" section prepended before the existing "Current state" block (which becomes historical context). Frontmatter `sources:` lists prepended with today's audit; `updated: 2026-04-24`.
- **3 synthesis updates**:
  - [[synthesis/capacity-planning]] — "two of four capacity issues resolved" update section; 2026-04-20's Mode-1 findings on Shared + LS (new issue surfaced in 7.2) both closed this cycle. HR + Admin Mode-2 overbooks remain.
  - [[synthesis/team-rankings]] — prepended "2026-04-24 snapshot" table superseding the 2026-04-19-close table (kept below as historical context). Band distribution 1·8·1·0.
  - [[synthesis/portfolio-trend]] — timeline extended through 2026-04-24; added "PI7.2 window" analysis section covering the reset dip + Day-5 breakthrough; flagged the audit-to-action feedback-loop candidate pattern.
- **`wiki/TODO.md` — 3 external-action closures** moved to Archive with outcomes:
  - `ramon-action` raseniero GitHub token → CLOSED (GitHub API live on both Git teams)
  - `team-action` LS-Dev configure capacity → CLOSED (3 contributors configured overnight)
  - `carol-ramon-action` Shared Services capacity → CLOSED (3 contributors configured overnight)
  Plus 2 synthesis-bookkeeping items closed (team-rankings HCI-cap annotation → superseded by token fix; portfolio-trend extend → done). `grace-action` partially updated (#175360 remediated; #202911 + #202913 still open).
- **[[index]]** — portfolio snapshot table prepended with 4/24 row; "Latest audit per team" block replaced 4/23 → 4/24 with updated scores/bands/deltas; entity tables (ADO 8 / Git 2) refreshed with today's summaries; audit-backlog counts bumped +1 per team (total 300 → 310).

### Patterns worth noting for future work

- **Audit-to-action feedback loop (candidate pattern).** The 3 record-gainer teams all moved on issues explicitly P0 in the 2026-04-23 meeting agenda. First observed one-day cycle between "audit surfaces a problem" and "team fixes it." Recorded in [[synthesis/portfolio-trend]] as candidate; track over next 3 sprints before promoting to standalone synthesis.
- **Mode-1 capacity fix is fast when a team chooses it.** Both Shared + LS fixed capacity in a single overnight window; the delay was decisional, not technical. Mode-2 overbook (HR, Admin) stays open because Karl must tell teams to drop work — a different class of problem.
- **AA masking pattern persists.** UPS 65.7 Moderate continues to hide HCI 59 Critical (1 point from Moderate). Branch protection remains the single highest-ROI fix.
- **GitHub API restoration = +4 HCI on Colina from evidence quality alone.** Meaningful data point for the `synthesis/ci-health` / `synthesis/ups-masking-pattern` pages: score can move on evidence access changes independently of team behavior.

### Not ingested this cycle

- No wiki page created for the "audit-to-action feedback loop" candidate pattern (2 days of data is too thin for standalone synthesis; captured as note in portfolio-trend).
- No update to `synthesis/dor-leakage` despite LS + Flawless DoR remediation events — existing synthesis already has strong evidence; no new pattern variant surfaced.
- 2 TODO bookkeeping items still open (spot-check 4/22 re-runs, spot-check 4/23 PM re-runs) — low priority, deferred.

## [2026-04-25 15:33] ingest | Day-6 batch — 10 audits + portfolio + meeting agenda

Full batch ingest of Iteration 7.2 Day 6 cron output. Day 6 is the DP inflection point — early-sprint annotation removed for all teams; 0 SP closed now carries full penalty.

### Sources ingested (12)

- 6 ADO audits (1533): `ado_{admin,fin,fl_dev,hr,jit,ls_dev}/audit/AUDIT_20260425_1533.md`
- 2 ADO audits (0833): `ado_{otp,shared}/audit/AUDIT_20260425_0833.md`
- 2 Git audits: `git_{aa_dev,cc_dev}/audit/AUDIT_20260425_1533.md`
- 1 portfolio dashboard: `portfolio_report/PORTFOLIO_20260425_1533.html`
- 1 meeting agenda: `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260425.html`

### Headline

**Portfolio mean 69.7 (−0.2 from Day 5) · 1 Low · 8 Moderate · 1 High · 0 Critical.** Day 6 = DP annotation removed; 7 of 10 teams at 0 SP closed entering real-penalty territory. Only movers: **JIT +2.2** (3 closures = 7 SP; first real delivery in PI7.2 ADO portfolio), **Flawless +0.6** (53.3% DP — portfolio-highest), **Colina −1.0** (rounding correction, not a behavioral regression).

### Writes

- **12 new summaries:** 10 per-team audit summaries + [[summaries/portfolio-20260425-1533]] + [[summaries/meeting-agenda-20260425]]
- **10 entity updates** (team-ado-×8, team-git-×2): `updated: 2026-04-25`; "Latest (Day 6)" section prepended to each
- **1 synthesis update:** [[synthesis/portfolio-trend]] — Day 6 row appended to timeline table; Day-6 DP-inflection narrative bullet added
- **[[index]]:** portfolio snapshot row prepended; "Latest audit per team" replaced Day 5 → Day 6; entity table scores/links updated; audit-backlog counts bumped (total 310 → 322)

### Escalations surfaced (carried forward to TODO)

- **HR #203057 / #203063 body defects — 7th consecutive audit.** Wrong candidate names in Active/Ready items. Operational quality risk requiring immediate team fix (<5 min).
- **Earl Carino direct commit to `dev` (AA, Apr 24)** — no PR, no reviewer, no AB# link — sensitive lawyer onboarding CLI logic. Second consecutive sprint pattern.
- **Shared Services #202464 + #203231 at Passed UAT** — 3 SP uncredited requiring only 2 state-transition clicks.
- **LS Dev #187240** — 251 days stale (15th consecutive audit); no disposal action taken.

### Not ingested this cycle

- [[synthesis/team-rankings]] not updated — scores unchanged for 7 of 10 teams; update deferred until a meaningful band crossing or score shift warrants a new snapshot.
- No new synthesis pages written — no novel cross-cutting patterns surfaced beyond those already in existing synthesis pages.

## [2026-04-26 22:15] ingest | Day-7/8 batch — 10 audits + 2 portfolio snapshots + 2 meeting agendas

Full batch ingest of Iteration 7.2 Day 7 EOD / Day 8 cron output. Continued in a new session after context compaction; entity page updates resumed from where prior session left off (5 of 10 entities updated in prior session; 5 remaining completed this session).

### Sources ingested (14)

- 8 ADO audits (22:00–22:10 PHT): `ado_{admin,fin,fl_dev}/AUDIT_20260426_2200.md` + `ado_{hr,jit,ls_dev}/AUDIT_20260426_2205.md` + `ado_{otp,shared}/AUDIT_20260426_2210.md`
- 2 Git audits (22:15 PHT): `git_{aa_dev,cc_dev}/AUDIT_20260426_2215.md`
- 2 portfolio dashboards: `PORTFOLIO_20260426_0935.html` (morning) + `PORTFOLIO_20260426_1400.html` (afternoon) — both predate evening audit batch
- 2 meeting agendas: `PORTFOLIO_MEETING_AGENDA_20260426.html` (14:00 PHT) + `PORTFOLIO_MEETING_AGENDA_20260426_2130.html` (21:30 PHT) — sourced from 1400 portfolio; 21:30 version has more structured P0/P1/P2 action tables

### Headline

**Portfolio mean ~71.3 (estimated, evening batch only) · 1 Low · 9 Moderate · 0 High · 0 Critical.** Two headline band crossings: **Shared Services +8.1 High→Moderate** (first delivery 5 SP; Est regression 66.7→42.9). **OTP +6.1 (+Largest single-session gain in 7.2 series)** — Grace completed all P0s in one 14-minute window ~23:15–23:29 PHT. Counter-signals: **JIT −2.3** (WIB regression; 2 new items activated without DoR), **LS Dev** unchanged with live BR trap race condition (#195727 vs #203239), **HR** 9th consecutive body-content defect streak.

### Writes

- **14 new summaries:** 10 per-team audit summaries + [[summaries/portfolio-20260426-0935]] + [[summaries/portfolio-20260426-1400]] + [[summaries/meeting-agenda-20260426]] + [[summaries/meeting-agenda-20260426-2130]]
- **10 entity updates** (team-ado-×8, team-git-×2): `updated: 2026-04-26`; "Latest (Day 7/8)" section prepended to each; audit history rows prepended
- **[[index]]:** 2 portfolio snapshot rows prepended; "Latest audit per team" table replaced Day 6 → Day 7/8 with new scores/bands/deltas; entity table scores and summary links updated; audit-backlog counts bumped (total 322 → 332); page count 337 → 351
- **`wiki/TODO.md`:** `grace-action` (#202911/#202913 DoR remediation) closed and moved to Archive — confirmed resolved by OTP A39. New `ike-action` item added for BR trap race condition (#195727 activation urgency).

### Key findings per team

| Team | Δ | Key signal |
|------|---|-----------|
| Admin A40 | 0.0 | #202898 moved Active with zero DoR/AC — CRITICAL; DP 0.0 at Day 8 |
| Finance A40 | 0.0 | 72+ hr ADO silence; two-edit Low path (83.5) still open |
| Flawless A39 | +0.1 | Only ADO team with non-zero DP (53.3%); WIB 30.0 8th audit |
| HR A41 | 0.0 | **9th body defect streak** #203057/#203063; 79+ hr zero-closure |
| JIT A42 | **−2.3** | #203157–159 re-pathed (−9 SP); WIB 100→70; 2 New→Active without DoR |
| LS Dev A33 | 0.0 | BR trap: #195727 must activate before #203239 closes; #187240 now 253 days |
| OTP A39 | **+6.1** 🏆 | Grace all P0s done; DoR/Est both 100.0; DP still 0.0 |
| Shared A9 | **+8.1** ✅ | **High→Moderate band change**; Est regression 66.7→42.9 (3 unestimated items) |
| AA (partial) | +0.3 | ICS 100.0 first perfect; HCI 61 (+1); SGPI 0.0 |
| CC (partial) | +1.64 | **First sprint closure #202810 (2 SP)**; 5 PRs await raseniero = 18 SP blocked |

### Not ingested this cycle

- [[synthesis/team-rankings]] not updated — Shared band crossing noted but net portfolio distribution unchanged (9M vs 8M: Shared moved from High to Moderate, net same row count).
- No new synthesis pages — existing synthesis pages cover all patterns surfaced (BR trap → [[synthesis/stale-work-items]]; body-content defects → [[synthesis/dor-leakage]]; AA masking → [[synthesis/ups-masking-pattern]]).

## [2026-04-26 22:45] lint | Full wiki health check post Apr-26 ingest

### Clean

- **No orphan summary pages.** All 14 new summaries have ≥2 inbound links. No zero-inbound pages across the entire summaries/ directory.
- **No broken wikilinks.** 9 unique `[[links]]` in the new summary pages (entities + concepts) all resolve to existing `.md` files. Initial grep false-positives from greedy `.*` regex — re-tested with non-greedy `[^]]*` and all clean.
- **All 10 entity pages updated.** `updated: 2026-04-26` confirmed across all ADO and Git team entities. All have a 2026-04-26 audit history entry.
- **All concept pages referenced exist.** `concepts/risk-bands`, `concepts/scoring-ado-rubric`, `concepts/scoring-git-ups`, `concepts/compliance-deadlines` all resolve.

### Corrected during lint

- **Index audit counts corrected.** HR over-counted (40→39 actual files), Shared over-counted (8→7 actual files) — both had pre-existing +1 index bias going into this session. Total 332→330. Span dates remain 2026-04-26 for both.
- **Index header count corrected.** Actual file count in `summaries/`: 364 files. Index said 363 active + 1 tombstone (363+1=364). Pre-existing under-count resolved: index was tracking ~14 fewer pages than actually exist, likely from summaries created in early sessions before the wiki count was established. Updated from 351→363 active.

### Stale / flag (not auto-fixed)

- **`synthesis/team-rankings.md`** — Day-5 (2026-04-25) snapshot table contains stale values: OTP 68.7 (now 74.8), Shared 56.1 🟠 High (now 64.2 🟡 Moderate — band change), AA UPS 65.7 (now 68.3), CC UPS 70.9 (now 68.19). Band distribution "1L · 8M · 1H · 0C" is stale (should be "1L · 9M · 0H · 0C"). **Recommend adding Day-7/8 snapshot to this synthesis before next portfolio review.**
- **`index.md` per-team detail line** — "300 audit summaries + 24 portfolio snapshots + 2 meeting agendas + 1 raw transcript = 325 total summary pages." Stale pre-existing inconsistency; authoritative counts are the header (363 active) and per-team table (330 audit summaries + 34 non-audit). Fixing this line requires a recount of each type; deferred as low-priority.

## [2026-04-27 13:00] ingest | Day-8 batch — 11 audits + portfolio + meeting agenda

PI7.2 Day 8 complete. LS Dev entered High Risk for the first time this PI (50.7, −10.4); all other 9 teams Moderate or better. Shared Services continued recovery (+3.4); JIT posted first meaningful delivery day (34% DP).

### Sources ingested (13)

- 8 ADO audits: `ado_{admin,fin,fl_dev,hr,jit,ls_dev,otp,shared}/audit/AUDIT_20260427_1110.md`
- 2 Git audits: `git_aa_dev/audit/AUDIT_20260427_0902.md` (partial/superseded) + `git_aa_dev/audit/AUDIT_20260428_0247.md` (canonical Day 9)
- 1 Git audit: `git_cc_dev/audit/AUDIT_20260427_0902.md`
- 1 portfolio: `portfolio_report/PORTFOLIO_20260427_1110.html`
- 1 meeting agenda: `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_20260427.html`

### Headline

**Portfolio mean 70.8 (+0.8) · Median 71.2 (+1.7) · Distribution: 1 Low · 8 Moderate · 1 High · 0 Critical**

First High Risk team of PI7.2: LS Dev 50.7 (−10.4). Shared Services simultaneous upgrade (56.1→67.6, +11.5) offset headcount — at-risk count stays at 1.

### Writes

- **13 new summaries:** 8 ADO Day-8 audits + 2 AA Dev (partial + canonical) + 1 CC Dev + 1 portfolio + 1 meeting agenda
- **10 entity updates** (`updated: 2026-04-27`): all 8 ADO entities + both git entities
- **2 synthesis updates:** [[synthesis/portfolio-trend]] (Apr 27 data point appended) · [[synthesis/team-rankings]] (all 10 teams refreshed, Day 8 section added)
- **[[wiki/TODO]]:** 2 new escalation items added; pcoronia BE#55 item updated to Day 11+; ike #195727 item confirmed still open
- **[[index]]:** portfolio row prepended; team table replaced with Day 8 scores; page counts bumped +13; meeting agenda row added

### Escalations surfaced

- 🔴 **LS Dev 50.7 High Risk** — WIB collapse (no User Stories, only 1 Defect + 1 Spike); 0 SP closed; Spike unestimated (4th audit). Recovery: add ≥1 US + estimate Spike + close #203239. Prereq: #195727 activation (BR trap still live). Owners: Ike, Samantha.
- 🔴 **Git AA Dev SGPI 0.0 Critical** — 27 SP committed, 0 closed across sprint. Code review gap: 10/11 PRs without reviewer. Earl direct push to `dev` flagged.
- 🔴 **Colina BE#55 Day 11+** — HIPAA rework still CHANGES_REQUESTED, 8 SP blocked. 5 sprint days remain. Owner: pcoronia.
- 🟡 **Finance 9-day plateau (77.9)** — #203038 in Review state; clear path to Low Risk if scoped + closed.
- 🟡 **OTP DP 0.0** — #175360 + #201811 at Resolved (one transition from closure); could resolve by Day 9.

### Not ingested this cycle

- No new synthesis pages created (existing pages updated; no novel cross-cutting patterns identified beyond LS Dev drop already tracked in TODO)
- `AUDIT_20260427_0902` for AA Dev ingested as partial/superseded record; canonical read is `AUDIT_20260428_0247`

## [2026-04-28 09:30] ingest | Day-9 batch — 10 audits + portfolio + meeting agenda

- Sources: 8 ADO team audits (0203/0204/0902 runs) + 2 Git team audits (AA Dev ×2, Colina ×1) + PORTFOLIO_20260428_0930.html + PORTFOLIO_MEETING_AGENDA_20260428.html
- Created: [[summaries/audit-ado-admin-20260428-0902]], [[summaries/audit-ado-fin-20260428-0902]], [[summaries/audit-ado-fl-dev-20260428-0902]], [[summaries/audit-ado-hr-20260428-0203]], [[summaries/audit-ado-jit-20260428-0203]], [[summaries/audit-ado-ls-dev-20260428-0203]], [[summaries/audit-ado-otp-20260428-0204]], [[summaries/audit-ado-shared-20260428-0204]], [[summaries/audit-git-aa-dev-20260428-0247]] (crossover/superseded), [[summaries/audit-git-aa-dev-20260428-0902]] (canonical), [[summaries/audit-git-cc-dev-20260428-0241]], [[summaries/portfolio-20260428-0930]], [[summaries/meeting-agenda-20260428]]
- Updated: 10 entity pages (all teams), [[synthesis/portfolio-trend]], [[synthesis/team-rankings]], [[wiki/TODO]]
- Key signals: ADO Shared first Low Risk (84.6, +17.0) · LS Dev Day 2 High Risk (47.9, −2.8) · JIT DP structural reset (0.0, −5.6) · Portfolio mean 72.5 new 7-day high
- Escalations: LS Dev reactive-only sprint sustained · JIT DP watch Day 10 · Colina ADO state lag (28 SP) · OTP mid-sprint scope violation
