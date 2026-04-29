# Jodex QA Automation Skill

## Feature ID
003

## Feature Name
QA Automation Skill

## Description
Enable Jodex to autonomously generate, convert, execute, and report on functional and end-to-end tests using structured inputs such as PRDs, BRDs, and Excel test cases.

---

## User Story 1: Plugin Lifecycle & Extract Skill Verification

**As a** System Engineer  
**I want** to compile, package, and publish the qa-ai plugin to GitHub  
**So that** I can verify the full plugin lifecycle: install → run the extract skill (BRD → xlsx test cases) → uninstall  

### Acceptance Criteria (Jenkins format)

#### Install
- Given the qa-ai plugin is published to GitHub (`jairosoft-com/jodex-qa-ai`)  
  When I run `plugin marketplace add jairosoft-com/jodex-qa-ai`  
  Then the marketplace source should be registered successfully  

- Given the marketplace source is registered  
  When I run `plugin install qa-ai@jodex-qa-ai`  
  Then the plugin should install without errors  
  And `/qa-ai:extract`, `/qa-ai:generate`, `/qa-ai:browser` should appear in command completion  

#### Run (Extract Skill)
- Given a valid BRD/PRD markdown document  
  When I invoke `/qa-ai:extract <brd_path>`  
  Then it should parse the document and identify all testable requirements (ACs, FRs, NFRs)  

- Given extracted requirements  
  When the skill classifies them  
  Then it should distinguish E2E-testable criteria from non-E2E (lint, type-check, code inspection)  
  And present the classification for user confirmation before proceeding  

- Given confirmed E2E classifications  
  When the skill generates test cases  
  Then each test case should follow the header-row + step-rows Azure DevOps format  
  And be appended to an existing xlsx test plan (forked, original untouched) or a new xlsx  

- Given an existing xlsx test plan with prior test cases  
  When new test cases have matching titles  
  Then duplicates should be detected and skipped with a report  

- Given test case generation completes  
  When output is produced  
  Then a coverage report should list every requirement as covered, skipped, or deduped  

#### Uninstall
- Given the qa-ai plugin is installed  
  When I run `plugin uninstall qa-ai@jodex-qa-ai`  
  Then the plugin should be removed without errors  
  And `/qa-ai:extract`, `/qa-ai:generate`, `/qa-ai:browser` should no longer appear in command completion  

- Given the plugin is uninstalled  
  When I run `plugin marketplace remove jodex-qa-ai`  
  Then the marketplace source should be deregistered  
  And standalone skills (`brd-to-test-cases`, `write-playwright-test-from-test-cases`, `playwright-cli`) should remain functional  

---

## User Story 2: Plugin Generate Skill — Playwright Script Generation from Test Cases

**As a** QA Automation Engineer  
**I want** to invoke the qa-ai plugin's generate skill (`/qa-ai:generate`) against an xlsx test plan  
**So that** Playwright test scripts are automatically created from structured test cases  

### Acceptance Criteria (Jenkins format)

#### Parsing
- Given an xlsx test plan with header-row + step-rows structure  
  When I invoke `/qa-ai:generate [xlsx_path]`  
  Then it should parse test cases and their steps from the spreadsheet  

- Given no xlsx path is provided  
  When the skill searches `raw/data/`  
  Then it should auto-discover xlsx files and prompt the user if multiple exist  

#### Script Generation
- Given parsed test cases with UI action steps  
  When the skill generates scripts  
  Then it should open a live browser, explore the target site, and capture stable semantic locators  
  And produce valid Playwright TypeScript `.spec.ts` files  

- Given a generated spec file  
  When written to `tests/`  
  Then line 3 must be `// Test Case TBD - <Title>` exactly (TBD placeholder for ADO linking)  
  And the test description should be concise and lowercase  

#### Idempotency
- Given test cases that already have corresponding `.spec.ts` files in `tests/`  
  When the skill derives the target filename from the test case title  
  Then it should skip existing specs and report them as skipped  
  And not overwrite or duplicate existing test files  

#### Verification
- Given a newly generated spec file  
  When the skill runs `npx playwright test tests/<new-spec>.spec.ts`  
  Then the test should pass against the target site  
  And failures should be inspected, locators fixed, and re-run until passing  

---

## User Story 3: Generate Test Execution Report (`/qa-ai:report`)

**As a** QA Lead  
**I want** to invoke the qa-ai plugin's report skill to generate an HTML quality report from test results  
**So that** I have a shareable, embeddable summary of test execution outcomes  

### Acceptance Criteria (Jenkins format)

#### Report Generation
- Given completed test execution results  
  When I invoke `/qa-ai:report [results_path]`  
  Then it should produce an HTML file with pass/fail counts, error details, and test case summaries  
  And the HTML should be email-embeddable (inline styles, no external dependencies)  

- Given no results path provided  
  When the skill searches `test-results/`  
  Then it should auto-discover the latest execution results  

---

## User Story 4: Send Report via Outlook Email (`/qa-ai:email`)

**As a** QA Lead  
**I want** to invoke the qa-ai plugin's email skill to send an HTML report to stakeholders via Outlook  
**So that** test results reach recipients automatically without manual copy-paste  

### Acceptance Criteria (Jenkins format)

#### Email Composition
- Given a generated HTML report  
  When I invoke `/qa-ai:email <report_path> <recipient>`  
  Then the HTML report should be embedded in the Outlook email body (not as attachment)  
  And the email should render correctly in Outlook desktop and web clients  

#### Email Delivery
- Given a valid recipient email address  
  When the skill sends the email  
  Then it should deliver via the authenticated Outlook account  
  And confirm delivery status to the user  

#### Independence
- Given the email skill is invoked standalone  
  When no report skill has been run  
  Then it should accept any valid HTML file path — not coupled to `/qa-ai:report`  

---

## User Story 5: Scheduled QA Pipeline Orchestration

**As a** QA Lead  
**I want** to schedule qa-ai plugin skills to run automatically on a recurring basis using OS-native scheduling  
**So that** the full QA pipeline (extract → generate → report → email) executes unattended on a defined cadence  

### Acceptance Criteria (Jenkins format)

#### Pipeline Chaining
- Given a PRD or Excel input  
  When the pipeline starts  
  Then it should chain skills in order: extract → generate → report → email  
  And each stage output should feed the next stage input  

- Given pipeline execution  
  When running  
  Then each stage should log progress in `progress.txt`  

- Given failures in any stage  
  When encountered  
  Then the pipeline should stop and log the failure with stage name and error details  

#### macOS Scheduling (launchd)
- Given a macOS operator  
  When the pipeline is configured for scheduling  
  Then it should generate a launchd plist (`com.jairosoft.qa-ai-pipeline.plist`)  
  And the plist should be installable via `launchctl load`  
  And support configurable cron-like intervals (daily, weekly, custom)  

#### Windows Scheduling (Task Scheduler)
- Given a Windows operator  
  When the pipeline is configured for scheduling  
  Then it should generate a Task Scheduler XML or `schtasks` command  
  And support the same configurable intervals as the macOS variant  

#### Cross-Platform
- Given either OS scheduling mechanism  
  When the scheduled task fires  
  Then it should invoke the qa-ai pipeline with preconfigured arguments (BRD path, xlsx path, recipient)  
  And execution logs should be written to a persistent location for troubleshooting  
---

## Enabler Story: Skill Plugin Development Environment Setup

**As a** System Engineer  
**I want** to set up a standardized project structure and tooling for developing Jodex skill plugins compatible with Claude Code, Codex, and Gemini Marketplace  
**So that** skills can be consistently developed, tested, and deployed across multiple AI platforms  

### Acceptance Criteria (Jenkins format)
- Given a new skill plugin project  
  When initialized  
  Then it should follow a standardized directory structure  

- Given the development environment  
  When configured  
  Then it should support Claude Code, Codex, and Gemini Marketplace integrations  

- Given plugin development  
  When dependencies are installed  
  Then required SDKs and CLI tools should be available  

- Given a sample skill  
  When executed  
  Then it should run successfully across supported platforms  

- Given deployment requirements  
  When packaging is performed  
  Then the plugin should be compatible with each marketplace format  

- Given development lifecycle  
  When changes are made  
  Then testing and validation workflows should be available
