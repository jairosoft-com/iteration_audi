# Wiki Log

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
