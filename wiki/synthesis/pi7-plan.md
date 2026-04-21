---
title: "PI7.2 Planning — Consolidated Checklist"
type: synthesis
tags: [pi7, planning, forward-look, checklist]
sources:
  - "../synthesis/iteration-7.1-close.md"
  - "../synthesis/capacity-planning.md"
  - "../synthesis/dor-leakage.md"
  - "../synthesis/ups-masking-pattern.md"
  - "../synthesis/scoring-artifacts.md"
  - "../synthesis/service-model-scoring.md"
  - "../synthesis/portfolio-trend.md"
created: 2026-04-20
updated: 2026-04-20
---

# PI7.2 Planning — Consolidated Checklist

## Headline

Consolidates seven syntheses into one playbook [[entities/person-ramon]] and [[entities/person-karl]] can run against during PI7.2 planning. Core theme: **PI7.1 closed at peak portfolio health (median 80.9, zero High) but the four systemic gaps — capacity discipline, DoR leakage at sprint edges, UPS composite masking, rubric artifacts on service teams — all carry forward into 7.2 unchanged unless planning ceremony absorbs them** ([[synthesis/iteration-7.1-close]], [[synthesis/portfolio-trend]]).

## Team-by-team forward asks

- **[[entities/team-ado-hr]] HR (87.0 Low):** rebalance 7.2 commitment from 30 SP to ≤22 SP empirical capacity ([[synthesis/iteration-7.1-close]]); triage #202888 "APE — Caumban — Copy" as duplicate-risk before kickoff ([[synthesis/iteration-7.1-close]]); verify Almera bus-factor-1 — name a second committer for the 22 SP pipeline ([[synthesis/capacity-planning]]).
- **[[entities/team-ado-admin]] Admin (87.0 Low):** prune 7.2 pipeline from 32 SP to ≤24 SP ([[synthesis/iteration-7.1-close]]); groom #202894 (title/SP/Desc/AC) before sprint start ([[synthesis/dor-leakage]]); document PI7-root legacy home for the 8 unassigned items; split [[entities/person-mark-colina]]'s 18 SP single-day burst pattern across at least two committers ([[synthesis/capacity-planning]]).
- **[[entities/team-ado-fin]] Finance (93.7 Low):** reconcile #201448 (BIR eAFS Apr 15 filing) status in ADO before 7.2 planning — record Transaction Number or re-path ([[synthesis/iteration-7.1-close]]); right-size 7.2 commitment to 12 SP empirical with 1 SP Spike buffer ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-ado-jit]] JIT (68.8 Moderate):** unblock [[entities/person-grace]]'s #201504 / #201514 or reassign — 1h/day allocation cannot carry a 2-item commitment ([[synthesis/capacity-planning]]); re-path PI6 leakage (#200766, #202514–202517) out of the 7.2 denominator ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-ado-otp]] OTP (71.2 Moderate):** close #198587 before retrospective (moves band Moderate → near-Low) ([[synthesis/iteration-7.1-close]]); formally re-path #202229 to 7.2 with status comment on the Akira dependency; add an Enabler to the solar-install chain to lift Work Item Balance 70 → 100 ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-ado-fl-dev]] Flawless (79.3 Moderate):** add [[entities/person-carol]] Cuison to ADO capacity config before 7.2 kickoff — exits the 66.7 Team Capacity stuck across 8+ audits ([[synthesis/capacity-planning]]); close #201569 Netlify/GitHub Transfer Spike today for ~+4.8 Overall lift ([[synthesis/iteration-7.1-close]]); hide PI8 items from default backlog view ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-ado-ls-dev]] Life Style (82.4 Low):** archive #187240 Enabler (244d stale) plus 3 of 4 PI5 stragglers — lifts Backlog Refinement 18.3 → ~98 (+~11 Overall) ([[synthesis/iteration-7.1-close]]); right-size 7.2 commitment to 8–10 SP ([[synthesis/iteration-7.1-close]]); schedule Luzmibel Paculanang onto a testing assignment to break Samantha bus-factor-1 ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-ado-shared]] Shared Services (32.2 Critical baseline):** wire team capacity config before 7.2 Day 1 ([[synthesis/capacity-planning]]); groom the 3 committed items out of Grooming before kickoff ([[synthesis/dor-leakage]]); move stories to User Story type where possible to exit −70 Work Item Balance penalty; adopt tier-aware rubric per [[synthesis/service-model-scoring]] before next audit ([[synthesis/iteration-7.1-close]]).
- **[[entities/team-git-cc-dev]] Colina (90.6 Low):** review HIPAA PR BE#55 (#202696, 42 files) before 7.2 code freeze ([[synthesis/iteration-7.1-close]]); enable branch-protection on `main` ([[synthesis/iteration-7.1-close]]); triage 11 new project-level defects (#202269 … #202483) against 7.2 capacity.
- **[[entities/team-git-aa-dev]] Auto Allies (UPS 68.6, component Critical):** surface component Criticals in dashboards per [[synthesis/ups-masking-pattern]]; break the QA-gate bottleneck (14 SP parked, third Red-SGPI sprint) ([[synthesis/iteration-7.1-close]]); activate retro spikes #202168 / #202169; reinstate [[entities/person-jerlyn]] Ates and Mary Secusana after two consecutive zero-contribution sprints ([[synthesis/iteration-7.1-close]]).

## Systemic changes

1. **Capacity-discipline pre-planning gate.** Before any team opens 7.2 planning, verify ADO team capacity is populated and `committed_SP ≤ team_capacity_hours × historical SP/hour` ([[synthesis/capacity-planning]]). Targets: [[entities/team-ado-shared]], [[entities/team-ado-fl-dev]], [[entities/team-ado-hr]], [[entities/team-ado-admin]].
2. **DoR gate at planning close.** Items lacking Description ≥30 nws, AC ≥20 nws, or SP (for point-eligible types) flagged `provisional` and auto-ejected from iteration path if not groomed within kickoff +2 days ([[synthesis/dor-leakage]]). Closes the Shared Services Grooming-commitment / Admin #202894 / Flawless closed-with-debt pattern.
3. **UPS component-breakdown in every dashboard row.** Ship options (A) + (C) from [[synthesis/ups-masking-pattern]] — render min-component band beside UPS, require ICS/HCI/SGPI columns on every portfolio dashboard. Kills the Auto Allies 9-audit masking streak.
4. **Rubric carve-outs codified.** Adopt the 5 detection rules from [[synthesis/scoring-artifacts]]: rubric-version baseline, zero-denominator collapse, close-window board state, one-day ≥40-point delta, composite-masks-component. Stop flagging the same artifacts every cycle.
5. **Service-model tier in rubric.** Add `team_type: product | service | hybrid` to workspace CLAUDE.md; apply service reweighting and Critical-floor rule from [[synthesis/service-model-scoring]]. Reclassifies Shared Services baseline from 32.2 Critical-on-artifact to ~55–60 High on real issues only.

## Pre-planning checklist — week of PI7.2 planning

- [ ] Confirm capacity config populated for all 10 teams — flag [[entities/team-ado-shared]], [[entities/team-ado-fl-dev]] explicitly ([[synthesis/capacity-planning]]).
- [ ] Verify every 7.2 candidate backlog item meets DoR (Description ≥30 nws, AC ≥20 nws, SP present). Flag [[entities/team-ado-admin]] #202894, [[entities/team-ado-shared]] #202928/#202929/#202932 ([[synthesis/dor-leakage]]).
- [ ] Identify bus-factor-1 risks: Almera (HR 22 SP), [[entities/person-mark-colina]] (Admin 27 SP), [[entities/person-grace]] (OTP sole, JIT 1h/day), Samantha (Life Style 9/10 SP) ([[synthesis/capacity-planning]]).
- [ ] Identify compliance deadlines landing in 7.2: Finance BIR filings (post-eAFS cadence), Colina HIPAA review gate BE#55, OTP Akira dependency ([[synthesis/iteration-7.1-close]]).
- [ ] Confirm team_type assignment per [[synthesis/service-model-scoring]]; lock [[entities/team-ado-shared]] as `service` before next audit.
- [ ] Resolve portfolio data gap: 2026-04-18 snapshot missing ([[synthesis/portfolio-trend]] Open Q#4).

## During-planning checklist — at planning session

- [ ] Capacity-vs-commitment check per team: `committed_SP / empirical_capacity_SP`. Red > 1.10, Yellow 1.00–1.10. Would have flagged HR 1.36 and Admin 1.19 at 7.1 close ([[synthesis/capacity-planning]]).
- [ ] DoR gate enforcement: reject `Grooming`-state items from iteration commitment; flag any thin-Description closures from 7.1 carried forward ([[synthesis/dor-leakage]]).
- [ ] Flag provisional items explicitly on the iteration board with a tag or comment so audits can carve them out rather than scoring against them.
- [ ] Confirm no team opens 7.2 without resolving its 7.1 forward-ask (team-by-team list above).
- [ ] Record capacity override decisions in writing for any commitment > empirical ceiling.

## Post-planning checklist — immediately after

- [ ] Publish capacity + commitment ratio per team to the portfolio dashboard with the new overbook column ([[synthesis/capacity-planning]]).
- [ ] Run a baseline audit of 7.2 backlog state — DoR compliance %, stale-item count, capacity config Y/N, bus-factor share — before Day 1 execution begins. Sets the T-0 floor for trend comparisons.
- [ ] Confirm [[entities/team-ado-shared]] is scored against the service-tier rubric on its first 7.2 audit ([[synthesis/service-model-scoring]]).
- [ ] Update [[concepts/scoring-ado-rubric]] and [[concepts/scoring-git-ups]] with the adopted carve-outs before the first 7.2 audit batch runs.
- [ ] Log planning decisions to `log.md` so next retrospective can compare plan-to-actual.

## Success criteria for PI7.2

- **Zero Critical at close** under the revised rubric (Shared Services scored via [[synthesis/service-model-scoring]] tier-aware rubric, not product-team rubric).
- **Zero High at close** — sustains the PI7.1 breakthrough ([[synthesis/portfolio-trend]]).
- **Median ≥ 80** at Day 14 close (PI7.1 closed 80.9 at 10-team; hold or improve).
- **[[entities/team-git-aa-dev]] HCI recovers above 60** — breaks the 9-audit Critical-HCI streak ([[synthesis/ups-masking-pattern]]); SGPI above 40 (out of Critical band).
- **[[entities/team-ado-jit]] [[entities/person-grace]] blocker resolved** — #201504 / #201514 either closed, reassigned off JIT, or Grace reassigned to stakeholder-only on JIT ([[synthesis/capacity-planning]]).
- **Zero DoR-failing commitments at planning close** — gate enforced, `provisional` items tracked separately ([[synthesis/dor-leakage]]).
- **Capacity config Y for all 10 teams** on Day 1 — ends Mode 1 failures ([[synthesis/capacity-planning]]).
- **No manual band overrides** in the portfolio dashboard — component-breakdown reporting makes overrides unnecessary ([[synthesis/ups-masking-pattern]]).
- **Zero one-day ≥40-point deltas** attributable to scoring artifacts — carve-outs in place ([[synthesis/scoring-artifacts]]).

## Open questions

1. **Hybrid team classification.** Do [[entities/team-ado-fl-dev]] and [[entities/team-ado-ls-dev]] qualify as `hybrid` given platform work? Default 70/30 product/service until data says otherwise ([[synthesis/service-model-scoring]] Open Q#1).
2. **Cross-Team Delivery automation.** Can the new service-rubric dimension be pulled from ADO queries, or does it need a manual spike each iteration ([[synthesis/service-model-scoring]] Open Q#2)?
3. **Burst-closure cadence.** Four teams showed Day-12–18 heroics at 7.1 close. Rubric rewards outcome; the pattern may hide over-commitment. Do we add a "sustainable pace" flag to the dashboard ([[synthesis/iteration-7.1-close]] Theme 6)?
4. **[[entities/person-grace]] role.** Reassign to stakeholder (non-committer) on JIT, or keep at 1h/day with a hard 1-item cap? Decision blocks JIT Delivery Predictability recovery ([[synthesis/capacity-planning]] Mode 3).
5. **Compliance-item tracking.** Finance BIR and Colina HIPAA both live outside ADO. Do we require a mirror work-item for every regulatory deadline landing in 7.2, or accept external-tracker status reports ([[synthesis/iteration-7.1-close]] Theme 4)?
6. **Perfect-sprint carry-forward.** Adopt the [[synthesis/capacity-planning]] proposal (hold overall static after 100% close) in time for 7.2 first audit, or defer to PI8?
7. **Dashboard redesign scope.** Three syntheses independently request new columns (capacity ratio, DoR %, UPS components, bus-factor). Batch in one dashboard revision or ship incrementally?

## Related

- [[synthesis/iteration-7.1-close]] — retrospective feeding the team-by-team forward asks
- [[synthesis/capacity-planning]] — capacity-discipline proposal (systemic change #1)
- [[synthesis/dor-leakage]] — DoR gate proposal (systemic change #2)
- [[synthesis/ups-masking-pattern]] — dashboard component-breakdown (systemic change #3)
- [[synthesis/scoring-artifacts]] — 5 rubric carve-outs (systemic change #4)
- [[synthesis/service-model-scoring]] — tier-aware rubric (systemic change #5)
- [[synthesis/portfolio-trend]] — PI6 close → PI7.1 close context
- [[concepts/scoring-ado-rubric]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]
- [[entities/person-ramon]] · [[entities/person-karl]] · [[entities/person-grace]] · [[entities/person-mark-colina]] · [[entities/person-carol]] · [[entities/person-jerlyn]]
