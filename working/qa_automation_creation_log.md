# Jodex QA Automation Skill — ADO Creation Log

**Created:** 2026-04-29
**Iteration:** 7.2 (Apr 20 – May 3, 2026)
**Assigned To:** Vicsante Aseniero (vaseniero@jairosoft.com)
**Area Path:** Jairosoft Portfolio\Shared Services - Jairosoft\Enabler Artificial Intelligence

## Feature

| ID | Type | Title |
|----|------|-------|
| 203435 | Feature | Jodex QA Automation Skill |

## Stories & Enablers (children of Feature #203435)

| ID | Type | Title | SP |
|----|------|-------|----|
| 203436 | User Story | Plugin Lifecycle & Extract Skill Verification | 5 |
| 203437 | User Story | Plugin Generate Skill — Playwright Script Generation from Test Cases | 5 |
| 203438 | User Story | Generate Test Execution Report (/qa-ai:report) | 2 |
| 203439 | User Story | Send Report via Outlook Email (/qa-ai:email) | 3 |
| 203440 | User Story | Scheduled QA Pipeline Orchestration | 3 |
| 203441 | Enabler | Skill Plugin Development Environment Setup | 3 |

**Total Story Points:** 21 SP

## Child Tasks

### US1 (#203436) — Plugin Lifecycle & Extract Skill

| ID | Title | Est (h) |
|----|-------|---------|
| 203443 | Compile and publish qa-ai plugin to GitHub | 4 |
| 203444 | Implement plugin install/uninstall CLI commands | 4 |
| 203445 | Build BRD/PRD document parser for testable requirements | 8 |
| 203446 | Implement E2E vs non-E2E classification with user confirmation | 4 |
| 203447 | Build xlsx test case generator (ADO header-row + step-rows format) | 8 |
| 203448 | Implement duplicate detection and coverage report | 4 |

### US2 (#203437) — Playwright Script Generation

| ID | Title | Est (h) |
|----|-------|---------|
| 203449 | Implement xlsx test plan parser | 4 |
| 203450 | Build auto-discovery for xlsx files in raw/data/ | 2 |
| 203451 | Implement browser-based semantic locator capture | 8 |
| 203452 | Build Playwright TypeScript spec file generator | 8 |
| 203453 | Implement idempotency check for existing specs | 2 |
| 203454 | Implement auto-verification runner (run + fix locators) | 4 |

### US3 (#203438) — Test Execution Report

| ID | Title | Est (h) |
|----|-------|---------|
| 203455 | Implement test result parser | 4 |
| 203456 | Build email-embeddable HTML report generator | 4 |
| 203457 | Implement auto-discovery of latest test results | 2 |

### US4 (#203439) — Outlook Email (with guardrails)

| ID | Title | Est (h) |
|----|-------|---------|
| 203458 | Implement email composition with embedded HTML body | 4 |
| 203459 | Integrate Outlook authenticated delivery | 4 |
| 203460 | Support standalone mode — accept any valid HTML file path | 2 |
| 203461 | Implement recipient allowlist configuration and validation | 4 |
| 203462 | Implement dry-run preview mode with user confirmation | 2 |
| 203463 | Implement HTML sanitization for email content | 4 |
| 203464 | Implement send audit logging | 2 |

### US5 (#203440) — Pipeline Orchestration

| ID | Title | Est (h) |
|----|-------|---------|
| 203465 | Implement pipeline chaining (extract → generate → report → email) | 8 |
| 203466 | Implement progress logging to progress.txt | 2 |
| 203467 | Implement stage failure handling and error reporting | 4 |
| 203468 | Generate macOS launchd plist | 4 |
| 203469 | Generate Windows Task Scheduler XML/schtasks command | 4 |

### Enabler (#203441) — Dev Environment Setup

| ID | Title | Est (h) |
|----|-------|---------|
| 203470 | Define standardized plugin directory structure | 2 |
| 203471 | Configure Claude Code, Codex, and Gemini Marketplace integrations | 4 |
| 203472 | Set up required SDKs and CLI tools | 4 |
| 203473 | Create sample skill execution test across supported platforms | 2 |
| 203474 | Configure packaging for each marketplace format | 4 |
| 203475 | Set up testing and validation workflows | 2 |

## Totals

| Metric | Value |
|--------|-------|
| Feature | 1 (#203435) |
| User Stories | 5 (#203436–203440) |
| Enablers | 1 (#203441) |
| Tasks | 33 (#203443–203475) |
| Total Story Points | 21 SP |
| Total Task Hours | 130 h |
| ID Range | 203435–203475 |
