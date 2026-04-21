# Wiki Schema (LLM Wiki Agent)

This folder is an **LLM-maintained knowledge wiki**. The agent (Claude) owns every file here. The human curates sources and asks questions; the agent does the reading, summarizing, cross-referencing, and bookkeeping.

## Three-layer architecture

1. **Raw sources** (immutable — read, never write):
   - `../ado_*/` — Azure DevOps audit workspaces (each contains `audit/AUDIT_*.md`, `CLAUDE.md`, sometimes `todo/`, `memory/`, `report/`)
   - `../git_*/` — GitHub audit workspaces (same shape as ADO)
   - `../portfolio_report/` — generated portfolio dashboards (`PORTFOLIO_*.html`, `PORTFOLIO_TREND_*.html`)
   - `../raw/` — arbitrary external sources dropped in by the user (articles, PDFs, images, web clips)
2. **Wiki** (this folder — agent writes, human reads):
   - `entities/` — one page per team, person, system, or stable thing
   - `concepts/` — one page per recurring idea (scoring rubric, risk band, SAFe ceremony, etc.)
   - `summaries/` — one page per ingested source (audit, portfolio report, article)
   - `synthesis/` — cross-cutting analyses, comparisons, theses, trend pieces
   - `index.md` — content catalog (update every ingest)
   - `log.md` — chronological append-only activity log
3. **Schema** — this file. Co-evolves with the wiki as conventions settle.

## Folder conventions

```
wiki/
├── CLAUDE.md         # this schema
├── index.md          # catalog of all pages (grouped by type)
├── log.md            # chronological ingests, queries, lint passes
├── entities/         # one .md per team / person / system
├── concepts/         # one .md per recurring idea
├── summaries/        # one .md per source document
└── synthesis/        # comparisons, theses, trends
```

Filenames use `kebab-case.md`. Source summaries mirror the source name: `AUDIT_20260419_1345.md` → `summaries/audit-ado-shared-20260419-1345.md`.

## Page format (YAML frontmatter required)

```markdown
---
title: "Human-readable title"
type: entity | concept | summary | synthesis
tags: [safe, portfolio, audit]
sources: ["../portfolio_report/PORTFOLIO_20260419_1953.html"]   # relative paths, optional
created: 2026-04-19
updated: 2026-04-19
---

# Title

Body in concise markdown. Use `[[wiki-links]]` between wiki pages; use relative paths for raw sources.
```

Cross-link liberally. If a page mentions a team that has (or should have) an entity page, link it. Orphans are lint findings.

## Operations

### INGEST — "process this source"

1. **Read** the source end-to-end (for HTML portfolio reports, extract the structured team/score data; don't paste raw markup).
2. **Discuss** 3–5 key takeaways with the user before writing, unless the user says "ingest silently."
3. **Write** a `summaries/` page: one-paragraph TL;DR, key claims (bulleted with citations), extracted entities, open questions.
4. **Update or create** every affected `entities/` and `concepts/` page. A single ingest typically touches 5–15 wiki pages.
5. **Flag contradictions** explicitly on the affected page: `> ⚠️ Contradicts [[older-page]] (source: ...)`. Do not silently overwrite.
6. **Update `index.md`**: add the new summary, any new entities/concepts.
7. **Append to `log.md`**: `## [YYYY-MM-DD HH:MM] ingest | <source title>` + 1–3 lines on what changed.

Default to **one source at a time** with the user in the loop. Batch ingest only when the user explicitly says so.

### QUERY — "what does the wiki say about X?"

1. Read `index.md` first to find candidate pages.
2. Drill into relevant pages (and their linked pages as needed).
3. Answer with citations: `[[page-name]]` for wiki pages, relative paths for raw sources.
4. If the answer is a meaningful synthesis (comparison, analysis, trend), **offer to file it back as a `synthesis/` page** so it compounds. Append to `log.md` with `## [timestamp] query | <question>` once filed.

### LINT — "health-check the wiki"

Run on request. Report:

- Contradictions between pages (same claim, different answers)
- Stale claims superseded by newer sources (check `updated` dates vs source dates)
- Orphan pages (no inbound `[[links]]`)
- Missing pages (concept referenced 3+ times but no dedicated page)
- Hub pages (many inbound links — good candidates for refactor)
- Suggested new questions / sources to close data gaps

Append `## [timestamp] lint` to `log.md` with the findings summary.

## Domain-specific rules (SAFe audit portfolio)

- **Entity pages for all 10 teams** are first-class: `entities/team-ado-admin.md`, `entities/team-git-aa-dev.md`, etc. Each team page carries the latest score, risk band, trend arrow, key blockers, and links to its most recent summaries.
- **People pages** only for stakeholders with recurring decision authority (Ramon, Karl, Bomar, Grace, team PDMs). Personal detail stays minimal; focus on role, ownership, and decision history.
- **Scoring concept pages** are canonical definitions: `concepts/scoring-ado-rubric.md`, `concepts/scoring-git-ups.md`, `concepts/risk-bands.md`. Link to them from every audit summary.
- **Portfolio trend synthesis** lives at `synthesis/portfolio-trend.md` and updates whenever a new portfolio report is ingested.
- **Never modify raw sources.** If an audit report in `ado_*/audit/` is wrong, note it in the wiki summary as a `> ⚠️ Discrepancy` — don't edit the original.

## Output discipline

- Keep wiki pages **terse and scannable**: short paragraphs, bullets, tables when comparing.
- Cite every non-trivial claim with `[source](relative/path)` or `[[wiki-page]]`.
- No chat-style language in wiki pages ("Let me know if...", "I hope this helps"). This is reference material.
- Code fences only for actual code, commands, or data.
- Match the user's root-level [YAML output style](../CLAUDE.md) in chat, but wiki pages are plain markdown.

## Conventions the agent may evolve

Anything in this file is editable as patterns settle. When the agent notices a convention drifting (e.g. file naming inconsistency, cross-reference gaps), it should propose a schema amendment rather than silently deviating.
