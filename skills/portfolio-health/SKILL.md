---
name: portfolio-health
description: Generate an interactive HTML portfolio health dashboard that aggregates scores from all `ado_*` and `git_*` workspace audits into a unified scorecard with visualizations.
argument-hint: [dashboard] or [summary]
allowed-tools: Read, Glob, Grep, Bash, Write
---

# Portfolio Health Dashboard Skill

Generate an interactive, self-contained HTML dashboard that aggregates the latest audit scores from every `ado_*` and `git_*` workspace into a unified portfolio view.

Do not use this skill for:

- Running individual project audits (use `ado-safe-audit` or `git_iteration_audit`)
- Re-computing individual audit scores
- PDF generation

## Authority and precedence

This skill is the authoritative source for:

- portfolio scoring methodology (UPS formula, normalization)
- portfolio report structure and output policy
- cross-project analysis methodology
- risk band definitions for portfolio-level comparison

This skill defers to:

- `ado-safe-audit` SKILL.md for how ADO scores are computed
- `git_iteration_audit` SKILL.md for how Git scores (ICS, SGPI, HCI) are computed
- individual workspace `CLAUDE.md` files for team metadata

**Critical rule:** Never re-compute individual audit scores. Read scores from existing audit reports only.

## Accepted inputs

- `portfolio-health` or `portfolio-health dashboard` — full interactive HTML dashboard
- `portfolio-health summary` — lightweight HTML with scorecard table and charts only (no narratives)

## Required workflow

1. **Discover teams:** Scan all top-level directories matching `ado_*` and `git_*` that contain `CLAUDE.md`. Process in alphabetical order.
2. **Read team metadata:** From each workspace's `CLAUDE.md`, extract:
   - Team name
   - ADO project and team identifiers
   - Workspace type (`ado` or `git`)
3. **Find latest audit:** In each workspace's `audit/` directory, find the most recent `AUDIT_*.md` file by filename sort (descending).
4. **Extract scores:** Parse the latest audit report using the extraction patterns below.
5. **Compute UPS:** Normalize scores into Unified Portfolio Scores using the formula below.
6. **Read prior portfolio report:** Find the most recent `PORTFOLIO_*.html` in `portfolio_report/` for trend delta. If none exists, this is the baseline run.
7. **Analyze cross-cutting themes:** Identify systemic patterns across teams from the audit reports.
8. **Generate HTML:** Produce a self-contained HTML dashboard following the template specification below.
9. **Write output:** Save to `portfolio_report/PORTFOLIO_<date>_<time>.html`.

## Score extraction patterns

### ADO audit reports (`ado_*`)

Look for the Overall Score in the Audit Metadata table:

```
| **Overall Score** | **90.8 / 100 (Low Risk)** |
```

Pattern: `Overall\s+Score.*?(\d+\.?\d*)\s*/\s*100`

Also extract the risk band text from the same match: `(Low Risk|Moderate Risk|High Risk|Critical)`

### Git audit reports (`git_*`)

Look for the three scores in the Scores at a Glance table or KPI table:

```
| Iteration Compliance Score | **54.7% (Red)** |
| SGPI (Committed Scope)     | **0.0%**        |
| HCI                        | **20/100**      |
```

Patterns:

- ICS: `Iteration Compliance.*?(\d+\.?\d*)%`
- SGPI: `SGPI.*?(\d+\.?\d*)%`
- HCI: `HCI.*?(\d+\.?\d*)\s*/\s*100`

If any score cannot be extracted, mark that team as "Extraction failed" in the dashboard and continue.

## Unified Portfolio Score (UPS)

### ADO workspaces

```
UPS = ADO Overall Score (used as-is, already 0–100)
```

### Git workspaces

```
UPS = (ICS × 0.50) + (HCI × 0.30) + (SGPI × 0.20)
```

| Component | Weight | Rationale |
|-----------|--------|-----------|
| **ICS** (Iteration Compliance) | 50% | Most comparable to the ADO 7-dimension score |
| **HCI** (Engineering Health) | 30% | Engineering quality signals unique to Git teams |
| **SGPI** (Sprint Goal Predictability) | 20% | Delivery outcome; lower weight prevents early-sprint distortion |

Round UPS to 1 decimal place.

**Early-sprint guard:** When SGPI = 0% and the audit report indicates early sprint (Day 1–5 of 14), note in the dashboard that SGPI is "expected early-sprint" and show UPS both with and without SGPI for context.

### Risk bands (universal)

| Band | Range | Color | Hex |
|------|-------|-------|-----|
| Low Risk | >= 80 | Green | `#22c55e` |
| Moderate | 60 – 79.9 | Yellow | `#eab308` |
| High Risk | 40 – 59.9 | Orange | `#f97316` |
| Critical | < 40 | Red | `#ef4444` |

## Portfolio-level metrics

### Tier 1 — Aggregate

- **Portfolio Mean** — average UPS across all teams with data, rounded to 1 decimal
- **Portfolio Median** — median UPS, rounded to 1 decimal
- **Tier Distribution** — count of teams per risk band

### Tier 2 — Cross-cutting indicators

Identify from individual audit reports:

- **Bus Factor Index** — count of teams where a single person carries all work
- **Stagnation Count** — teams with no iteration activity or empty iterations
- **Recommendation Adoption** — qualitative patterns of unfixed issues repeated across audits

### Tier 3 — Trend (vs. prior portfolio snapshot)

- **Score Movement** — per-team UPS delta from prior portfolio report
- **Risk Band Transitions** — teams that moved up or down a band
- **Portfolio Mean Trend** — direction of the overall average

## HTML output specification

### Design reference

Use Stitch mockup `6ca7618e` as the visual reference. The design is saved at `portfolio_report/stitch_reference_6ca7618e.html`.

### Architecture

- **Self-contained single HTML file** — all CSS and JS inline
- **Tailwind CSS via CDN** (`https://cdn.tailwindcss.com`) for styling
- **Google Fonts** — Manrope for headings, Inter for body text
- **Material Symbols Outlined** for icons
- **No other external dependencies**
- **Responsive** — works on desktop and tablet
- **Print stylesheet** — `@media print` for clean browser-to-PDF export

### Required HTML sections (in order)

#### 1. Header

- Full-width, no sidebar
- Left: Title "Portfolio Health Dashboard" (large, bold, Manrope), subtitle with iteration name and date
- Right: Three metric cards in a row:
  - "Portfolio Mean" with value and colored left-border accent
  - "Portfolio Median" with value and colored left-border accent
  - "Teams at Risk" with count, dark/red background

#### 2. Portfolio Scorecard Table

- Section title "Portfolio Scorecard" with "Export PDF" button (print trigger)
- Full-width styled table with columns:
  - Rank (zero-padded, e.g., 01)
  - Team name (bold)
  - Type — pill badge: "ADO" (blue `bg-sky-100 text-sky-700`) or "Git" (purple `bg-purple-100 text-purple-700`)
  - UPS Score — number + horizontal progress bar colored by risk band
  - Risk Band — colored pill badge (green/yellow/orange/red)
  - Trend — Material icon arrow (arrow_upward green, arrow_downward red/orange, trending_flat gray, add for new baseline)
  - Latest Audit — date of the audit file used
- Sorted by UPS descending
- Hover highlight on rows

#### 3. Charts Row (two-column grid)

- **Left — Risk Distribution:** SVG donut chart showing team counts per band. Center text: total team count. Legend beside the chart with colored dots and labels.
- **Right — Score Comparison:** Horizontal bar chart with one bar per team, sorted descending. Bar color matches risk band. Score value at end of each bar.

#### 4. Tier Analysis and Cross-Cutting Themes (two-column grid, 2/3 + 1/3)

- **Left — Tier Analysis:** Four collapsible cards with colored left borders:
  - "Top Performers" (green border, expanded by default)
  - "Moderate" (yellow border, collapsed)
  - "Needs Attention" (orange border, collapsed)
  - "Critical" (red border, collapsed)
  - Each card contains a brief narrative about the teams in that tier
- **Right — Cross-Cutting Themes:** Numbered items with colored circle badges and brief descriptions

#### 5. Trend Analysis (if prior portfolio report exists)

- Table: Team, Prior UPS, Current UPS, Delta, Direction arrow
- Highlight risk band transitions

#### 6. Evidence Gaps

- Teams with no audit data, stale audits, or extraction failures

#### 7. Footer

- Methodology: "UPS = ADO Overall Score (ADO teams) | UPS = ICS×0.50 + HCI×0.30 + SGPI×0.20 (Git teams)"
- Generation timestamp
- Risk band legend

### Color scheme

Use these colors consistently throughout:

- Low Risk / Green: `#22c55e`
- Moderate / Yellow: `#eab308`
- High Risk / Orange: `#f97316`
- Critical / Red: `#ef4444`
- ADO badge: `bg-sky-100 text-sky-700`
- Git badge: `bg-purple-100 text-purple-700`
- Background: `#faf8ff`
- Text: `#113069`

### Interactive features

- **Export PDF button:** Triggers `window.print()` for browser print/PDF export
- **Collapsible tier sections:** Use `<details><summary>` HTML elements
- **Hover effects:** Row highlights on the scorecard table

## Output policy

- **Location:** `portfolio_report/` at the repo root
- **Naming:** `PORTFOLIO_<date>_<time>.html` (dashboard) or `PORTFOLIO_<date>_<time>_SUMMARY.html` (summary)
- **Timestamps:** Every report gets a unique timestamp — files are never overwritten
- **Format:** Self-contained HTML
- **Not written to:** `report/`, `temp/`, or any workspace's `audit/`

## Trend persistence

No separate data store. The most recent `portfolio_report/PORTFOLIO_*.html` file is the trend baseline. Extract scores from its scorecard table for delta computation. First run shows "Baseline" in trend columns.

## Failure behavior

- **Empty audit directory:** Show team row with "No audit data" badge. Continue.
- **Score extraction fails:** Show "Extraction failed" badge with filename. Continue.
- **No prior portfolio report (first run):** Trend columns show "Baseline."
- **ALL workspaces fail:** Do not produce report. Report failure explicitly.

## Completion checklist

Before finishing, verify:

- All `ado_*` and `git_*` directories with `CLAUDE.md` were scanned
- Scores were extracted from existing audit reports only (no re-computation)
- UPS formula applied correctly for Git teams (ICS×0.50 + HCI×0.30 + SGPI×0.20)
- ADO scores passed through unchanged
- Risk bands assigned using the universal scale
- Portfolio mean and median computed correctly
- HTML is self-contained and opens correctly in a browser
- Donut chart and bar chart data match the scorecard table
- Collapsible tier sections function
- Prior portfolio report read for trend (or "Baseline" on first run)
- Output saved to `portfolio_report/PORTFOLIO_<date>_<time>.html`
- No files written to `report/`, `temp/`, or workspace `audit/` directories
