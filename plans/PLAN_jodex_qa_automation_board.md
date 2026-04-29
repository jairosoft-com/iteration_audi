# Plan: Add Jodex QA Automation Skill to Shared Services Board

## Context

Ramon has a new feature spec (`jodex-qa-ai.md`) with 5 User Stories + 1 Enabler Story for the Jodex QA Automation Skill (Feature 003). These need to be added to the **Shared Services Team** board in ADO project **Jairosoft Portfolio**, assigned to **Vicsante Aseniero** (`vaseniero@jairosoft.com`), with story point estimates and child tasks.

No existing "QA Automation Skill" Feature exists in ADO. Related Jodex features: #200094 (Refactor Jodex CLI, Closed), #203319 (Jodex Product Manager Skills, active).

## Iteration Assignment

**Decision:** All items assigned to **Iteration 7.2** (Apr 20 – May 3, current) per Ramon's direction.

## Work Items to Create

### 1. Feature (Parent)

| Field | Value |
|-------|-------|
| Type | Feature |
| Title | Jodex QA Automation Skill |
| Assigned To | Vicsante Aseniero |
| Iteration | Jairosoft Portfolio\2026-PI7\Iteration 7.2 |
| Area Path | Jairosoft Portfolio\Shared Services - Jairosoft\Enabler Artificial Intelligence |
| Description | Enable Jodex to autonomously generate, convert, execute, and report on functional and E2E tests using structured inputs (PRDs, BRDs, Excel test cases). |

---

### 2. User Stories & Enabler (6 items, all children of Feature above)

#### US1: Plugin Lifecycle & Extract Skill Verification — **5 SP**

| Field | Value |
|-------|-------|
| Type | User Story |
| Title | Plugin Lifecycle & Extract Skill Verification |
| SP | 5 |
| Description | As a System Engineer, I want to compile, package, and publish the qa-ai plugin to GitHub so that I can verify the full plugin lifecycle: install → run the extract skill (BRD → xlsx test cases) → uninstall |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Plugin Lifecycle & Extract Skill Verification

  Scenario: Install qa-ai plugin from GitHub marketplace
    Given the qa-ai plugin is published to GitHub (jairosoft-com/jodex-qa-ai)
    When I run "plugin marketplace add jairosoft-com/jodex-qa-ai"
    Then the marketplace source should be registered successfully

  Scenario: Install qa-ai plugin locally
    Given the marketplace source is registered
    When I run "plugin install qa-ai@jodex-qa-ai"
    Then the plugin should install without errors
    And "/qa-ai:extract", "/qa-ai:generate", "/qa-ai:browser", "/qa-ai:report", "/qa-ai:email" should appear in command completion

  Scenario: Extract testable requirements from BRD/PRD
    Given a valid BRD/PRD markdown document
    When I invoke "/qa-ai:extract <brd_path>"
    Then it should parse the document and identify all testable requirements (ACs, FRs, NFRs)

  Scenario: Classify requirements as E2E or non-E2E
    Given extracted requirements
    When the skill classifies them
    Then it should distinguish E2E-testable criteria from non-E2E (lint, type-check, code inspection)
    And present the classification for user confirmation before proceeding

  Scenario: Generate xlsx test cases from confirmed classifications
    Given confirmed E2E classifications
    When the skill generates test cases
    Then each test case should follow the header-row + step-rows Azure DevOps format
    And be appended to an existing xlsx test plan (forked, original untouched) or a new xlsx

  Scenario: Detect and skip duplicate test cases
    Given an existing xlsx test plan with prior test cases
    When new test cases have matching titles
    Then duplicates should be detected and skipped with a report

  Scenario: Produce coverage report after generation
    Given test case generation completes
    When output is produced
    Then a coverage report should list every requirement as covered, skipped, or deduped

  Scenario: Uninstall qa-ai plugin
    Given the qa-ai plugin is installed
    When I run "plugin uninstall qa-ai@jodex-qa-ai"
    Then the plugin should be removed without errors
    And "/qa-ai:extract", "/qa-ai:generate", "/qa-ai:browser", "/qa-ai:report", "/qa-ai:email" should no longer appear in command completion

  Scenario: Deregister marketplace source
    Given the plugin is uninstalled
    When I run "plugin marketplace remove jodex-qa-ai"
    Then the marketplace source should be deregistered
    And standalone skills (brd-to-test-cases, write-playwright-test-from-test-cases, playwright-cli) should remain functional
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Compile and publish qa-ai plugin to GitHub (jairosoft-com/jodex-qa-ai) | 4 |
| 2 | Implement plugin install/uninstall CLI commands | 4 |
| 3 | Build BRD/PRD document parser for testable requirements | 8 |
| 4 | Implement E2E vs non-E2E classification with user confirmation | 4 |
| 5 | Build xlsx test case generator (ADO header-row + step-rows format) | 8 |
| 6 | Implement duplicate detection and coverage report | 4 |

---

#### US2: Playwright Script Generation from Test Cases — **5 SP**

| Field | Value |
|-------|-------|
| Type | User Story |
| Title | Plugin Generate Skill — Playwright Script Generation from Test Cases |
| SP | 5 |
| Description | As a QA Automation Engineer, I want to invoke the qa-ai plugin's generate skill (/qa-ai:generate) against an xlsx test plan so that Playwright test scripts are automatically created from structured test cases |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Playwright Script Generation from Test Cases

  Scenario: Parse test cases from xlsx test plan
    Given an xlsx test plan with header-row + step-rows structure
    When I invoke "/qa-ai:generate [xlsx_path]"
    Then it should parse test cases and their steps from the spreadsheet

  Scenario: Auto-discover xlsx files when no path provided
    Given no xlsx path is provided
    When the skill searches "raw/data/"
    Then it should auto-discover xlsx files and prompt the user if multiple exist

  Scenario: Generate Playwright specs with live browser exploration
    Given parsed test cases with UI action steps
    When the skill generates scripts
    Then it should open a live browser, explore the target site, and capture stable semantic locators
    And produce valid Playwright TypeScript .spec.ts files

  Scenario: Spec file format compliance
    Given a generated spec file
    When written to "tests/"
    Then line 3 must be "// Test Case TBD - <Title>" exactly (TBD placeholder for ADO linking)
    And the test description should be concise and lowercase

  Scenario: Skip existing spec files (idempotency)
    Given test cases that already have corresponding .spec.ts files in "tests/"
    When the skill derives the target filename from the test case title
    Then it should skip existing specs and report them as skipped
    And not overwrite or duplicate existing test files

  Scenario: Verify generated specs pass
    Given a newly generated spec file
    When the skill runs "npx playwright test tests/<new-spec>.spec.ts"
    Then the test should pass against the target site
    And failures should be inspected, locators fixed, and re-run until passing
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Implement xlsx test plan parser | 4 |
| 2 | Build auto-discovery for xlsx files in raw/data/ | 2 |
| 3 | Implement browser-based semantic locator capture | 8 |
| 4 | Build Playwright TypeScript spec file generator | 8 |
| 5 | Implement idempotency check for existing specs | 2 |
| 6 | Implement auto-verification runner (run + fix locators) | 4 |

---

#### US3: Generate Test Execution Report — **2 SP**

| Field | Value |
|-------|-------|
| Type | User Story |
| Title | Generate Test Execution Report (/qa-ai:report) |
| SP | 2 |
| Description | As a QA Lead, I want to invoke the qa-ai plugin's report skill to generate an HTML quality report from test results so that I have a shareable, embeddable summary of test execution outcomes |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Test Execution Report Generation

  Scenario: Generate HTML report from test results
    Given completed test execution results
    When I invoke "/qa-ai:report [results_path]"
    Then it should produce an HTML file with pass/fail counts, error details, and test case summaries
    And the HTML should be email-embeddable (inline styles, no external dependencies)

  Scenario: Auto-discover latest test results
    Given no results path is provided
    When the skill searches "test-results/"
    Then it should auto-discover the latest execution results
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Implement test result parser | 4 |
| 2 | Build email-embeddable HTML report generator (inline styles, no external deps) | 4 |
| 3 | Implement auto-discovery of latest test results in test-results/ | 2 |

---

#### US4: Send Report via Outlook Email — **2 SP**

| Field | Value |
|-------|-------|
| Type | User Story |
| Title | Send Report via Outlook Email (/qa-ai:email) |
| SP | 3 |
| Description | As a QA Lead, I want to invoke the qa-ai plugin's email skill to send an HTML report to stakeholders via Outlook so that test results reach recipients automatically without manual copy-paste |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Send Report via Outlook Email

  Scenario: Compose email with embedded HTML report
    Given a generated HTML report
    When I invoke "/qa-ai:email <report_path> <recipient>"
    Then the HTML report should be embedded in the Outlook email body (not as attachment)
    And the email should render correctly in Outlook desktop and web clients

  Scenario: Deliver email via authenticated Outlook account
    Given a valid recipient email address
    When the skill sends the email
    Then it should deliver via the authenticated Outlook account
    And confirm delivery status to the user

  Scenario: Accept any HTML file standalone
    Given the email skill is invoked standalone
    When no report skill has been run
    Then it should accept any valid HTML file path — not coupled to /qa-ai:report

  Scenario: Enforce recipient allowlist
    Given a recipient email address
    When the skill validates the recipient
    Then it should check against a configured recipient allowlist
    And reject recipients not on the allowlist with a clear error message

  Scenario: Dry-run preview before sending
    Given the --dry-run flag is passed
    When the skill prepares the email
    Then it should render a preview of the email content and recipient
    And not send the email until the user explicitly confirms

  Scenario: Sanitize HTML content before embedding
    Given an HTML report file
    When the skill processes the content for email embedding
    Then it should sanitize the HTML to remove scripts, iframes, and external resource links
    And preserve safe formatting (inline styles, tables, images as data URIs)

  Scenario: Log all email send events for audit
    Given an email is sent or attempted
    When the delivery completes or fails
    Then a send audit log entry should be written with timestamp, recipient, subject, status, and file path
    And the audit log should be stored in a persistent location
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Implement email composition with embedded HTML body (not attachment) | 4 |
| 2 | Integrate Outlook authenticated delivery with status confirmation | 4 |
| 3 | Support standalone mode — accept any valid HTML file path | 2 |
| 4 | Implement recipient allowlist configuration and validation | 4 |
| 5 | Implement dry-run preview mode with user confirmation | 2 |
| 6 | Implement HTML sanitization for email content | 4 |
| 7 | Implement send audit logging | 2 |

---

#### US5: Scheduled QA Pipeline Orchestration — **3 SP**

| Field | Value |
|-------|-------|
| Type | User Story |
| Title | Scheduled QA Pipeline Orchestration |
| SP | 3 |
| Description | As a QA Lead, I want to schedule qa-ai plugin skills to run automatically on a recurring basis using OS-native scheduling so that the full QA pipeline (extract → generate → report → email) executes unattended on a defined cadence |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Scheduled QA Pipeline Orchestration

  Scenario: Chain pipeline stages in order
    Given a PRD or Excel input
    When the pipeline starts
    Then it should chain skills in order: extract → generate → report → email
    And each stage output should feed the next stage input

  Scenario: Log progress during pipeline execution
    Given pipeline execution
    When running
    Then each stage should log progress in "progress.txt"

  Scenario: Stop pipeline on stage failure
    Given failures in any stage
    When encountered
    Then the pipeline should stop and log the failure with stage name and error details

  Scenario: Schedule pipeline on macOS via launchd
    Given a macOS operator
    When the pipeline is configured for scheduling
    Then it should generate a launchd plist (com.jairosoft.qa-ai-pipeline.plist)
    And the plist should be installable via "launchctl load"
    And support configurable cron-like intervals (daily, weekly, custom)

  Scenario: Schedule pipeline on Windows via Task Scheduler
    Given a Windows operator
    When the pipeline is configured for scheduling
    Then it should generate a Task Scheduler XML or schtasks command
    And support the same configurable intervals as the macOS variant

  Scenario: Cross-platform scheduled execution
    Given either OS scheduling mechanism
    When the scheduled task fires
    Then it should invoke the qa-ai pipeline with preconfigured arguments (BRD path, xlsx path, recipient)
    And execution logs should be written to a persistent location for troubleshooting
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Implement pipeline chaining (extract → generate → report → email) | 8 |
| 2 | Implement progress logging to progress.txt | 2 |
| 3 | Implement stage failure handling and error reporting | 4 |
| 4 | Generate macOS launchd plist (com.jairosoft.qa-ai-pipeline.plist) | 4 |
| 5 | Generate Windows Task Scheduler XML/schtasks command | 4 |

---

#### Enabler: Skill Plugin Dev Environment Setup — **3 SP**

| Field | Value |
|-------|-------|
| Type | Enabler |
| Title | Skill Plugin Development Environment Setup |
| SP | 3 |
| Description | As a System Engineer, I want to set up a standardized project structure and tooling for developing Jodex skill plugins compatible with Claude Code, Codex, and Gemini Marketplace so that skills can be consistently developed, tested, and deployed across multiple AI platforms |

**Acceptance Criteria (Gherkin):**

```gherkin
Feature: Skill Plugin Development Environment Setup

  Scenario: Initialize standardized project structure
    Given a new skill plugin project
    When initialized
    Then it should follow a standardized directory structure

  Scenario: Configure multi-platform AI integrations
    Given the development environment
    When configured
    Then it should support Claude Code, Codex, and Gemini Marketplace integrations

  Scenario: Install required dependencies
    Given plugin development
    When dependencies are installed
    Then required SDKs and CLI tools should be available

  Scenario: Execute sample skill across platforms
    Given a sample skill
    When executed
    Then it should run successfully across supported platforms

  Scenario: Package plugin for marketplace deployment
    Given deployment requirements
    When packaging is performed
    Then the plugin should be compatible with each marketplace format

  Scenario: Validate development lifecycle workflows
    Given development lifecycle
    When changes are made
    Then testing and validation workflows should be available
```

**Child Tasks:**

| # | Task Title | Est (h) |
|---|-----------|---------|
| 1 | Define standardized plugin directory structure | 2 |
| 2 | Configure Claude Code, Codex, and Gemini Marketplace integrations | 4 |
| 3 | Set up required SDKs and CLI tools | 4 |
| 4 | Create sample skill execution test across supported platforms | 2 |
| 5 | Configure packaging for each marketplace format | 4 |
| 6 | Set up testing and validation workflows | 2 |

---

## Totals

| Metric | Value |
|--------|-------|
| Feature | 1 |
| User Stories | 5 |
| Enablers | 1 |
| Child Tasks | 36 |
| Total Story Points | 21 SP |
| Total Task Hours | 130 h |
| Gherkin Scenarios | 39 |

## Execution Steps

### Step 0: Preflight (idempotency guard)
- `search_workitem` for "Jodex QA Automation Skill" in Jairosoft Portfolio
- If Feature already exists → abort, report existing ID
- Log all created IDs to `working/qa_automation_creation_log.md` for recovery

### Step 1: Create Feature
`wit_create_work_item` (type: Feature) with fields:
- `System.Title` = "Jodex QA Automation Skill"
- `System.Description` (format: Html) = feature description
- `System.AssignedTo` = "Vicsante Aseniero <vaseniero@jairosoft.com>"
- `System.IterationPath` = "Jairosoft Portfolio\2026-PI7\Iteration 7.2"
- `System.AreaPath` = "Jairosoft Portfolio\Shared Services - Jairosoft\Enabler Artificial Intelligence"

### Step 2: Create 6 stories/enablers
`wit_create_work_item` for each, with fields:
- `System.Title`
- `System.Description` (format: Html) — user story format
- `Microsoft.VSTS.Common.AcceptanceCriteria` (format: Html) — Gherkin in `<pre>` block
- `Microsoft.VSTS.Scheduling.StoryPoints`
- `System.AssignedTo` = "Vicsante Aseniero <vaseniero@jairosoft.com>"
- `System.IterationPath` = "Jairosoft Portfolio\2026-PI7\Iteration 7.2"
- `System.AreaPath` = "Jairosoft Portfolio\Shared Services - Jairosoft\Enabler Artificial Intelligence"
- `System.Parent` = Feature ID from Step 1

### Step 3: Create 32 child tasks
`wit_add_child_work_items` per story (6 batches), with:
- `title` = task title
- `description` = task description
- `iterationPath` = "Jairosoft Portfolio\2026-PI7\Iteration 7.2"
- `areaPath` = "Jairosoft Portfolio\Shared Services - Jairosoft\Enabler Artificial Intelligence"
Then `wit_update_work_item` each task to set:
- `System.AssignedTo` = "Vicsante Aseniero <vaseniero@jairosoft.com>"
- `Microsoft.VSTS.Scheduling.OriginalEstimate` = hours

### Step 4: Persist creation log
Write all created work item IDs → `working/qa_automation_creation_log.md`

## Verification

- Run `wit_get_work_items_for_iteration` for Iteration 7.2 to confirm all items appear
- Verify parent-child links via `wit_get_work_item` on Feature and each story
- Check board at `https://dev.azure.com/jairo/Jairosoft%20Portfolio/_boards/board/t/Shared%20Services%20Team/Stories`
