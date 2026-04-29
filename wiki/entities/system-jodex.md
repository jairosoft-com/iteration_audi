---
title: "System — Jodex"
type: entity
tags: [system, jodex, cli, rust, plugin, ai]
sources:
  - "../../jodex-qa-ai.md"
  - "../../working/qa_automation_creation_log.md"
created: 2026-04-29
updated: 2026-04-29
---

# Jodex

Rust-based CLI tool with a plugin marketplace architecture, designed to work across **Claude Code**, **Codex**, and **Gemini Marketplace**. Owned and developed by [[entities/person-vicsante|Vicsante Aseniero]]. Lives on the [[entities/team-ado-shared]] board under Area Path `Enabler Artificial Intelligence`.

## ADO Features

| ID | Title | State | Iteration |
|----|-------|-------|-----------|
| 200094 | Refactor Jodex CLI | Closed | — |
| 203319 | Jodex Product Manager Skills | Requirements Gathering | 7.2 |
| **203435** | **Jodex QA Automation Skill** | **New** | **7.2** |

## Feature 003: QA Automation Skill (active)

Created 2026-04-29. Enables Jodex to autonomously generate, convert, execute, and report on functional and E2E tests using structured inputs (PRDs, BRDs, Excel test cases).

**Plugin commands:** `/qa-ai:extract`, `/qa-ai:generate`, `/qa-ai:browser`, `/qa-ai:report`, `/qa-ai:email`

| Story ID | Title | SP | Tasks |
|----------|-------|----|-------|
| 203436 | Plugin Lifecycle & Extract Skill Verification | 5 | 6 |
| 203437 | Playwright Script Generation from Test Cases | 5 | 6 |
| 203438 | Generate Test Execution Report | 2 | 3 |
| 203439 | Send Report via Outlook Email (with guardrails) | 3 | 7 |
| 203440 | Scheduled QA Pipeline Orchestration | 3 | 5 |
| 203441 | Skill Plugin Dev Environment Setup (Enabler) | 3 | 6 |

**Totals:** 21 SP, 33 tasks, 130h estimated, 39 Gherkin scenarios.

Email guardrails added after Codex adversarial review: recipient allowlist, dry-run preview, HTML sanitization, send audit logging.

## Architecture

- **Language:** Rust (Cargo workspace)
- **Distribution:** GitHub (`jairosoft-com/jodex-qa-ai`)
- **Plugin model:** Marketplace install/uninstall via CLI commands
- **Multi-platform:** Claude Code + Codex + Gemini Marketplace
- **Test framework:** Playwright (TypeScript `.spec.ts` generation)
- **Scheduling:** macOS launchd + Windows Task Scheduler

## GitHub repos

- `jairosoft-com/jodex-qa-ai` — QA Automation plugin (planned)
- Other Jodex repos TBD — capture from ADO work items on next audit

## Linked pages

- [[entities/team-ado-shared]] — hosting team board
- [[synthesis/ado-mcp-api-patterns]] — creation workflow used for Feature 003
