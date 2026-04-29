---
title: "ADO MCP API Patterns — Work Item Creation & Linking"
type: synthesis
tags: [ado, mcp, api, automation, work-items]
sources:
  - "../../working/qa_automation_creation_log.md"
  - "../../plans/PLAN_jodex_qa_automation_board.md"
created: 2026-04-29
updated: 2026-04-29
---

# ADO MCP API Patterns — Work Item Creation & Linking

Lessons from batch-creating Feature #203435 (Jodex QA Automation Skill): 1 Feature + 6 stories + 33 tasks with parent-child hierarchy, Gherkin ACs, and hour estimates. These patterns apply to any future ADO work item creation via MCP tools.

## Pattern 1: `System.Parent` silently ignored on `wit_create_work_item`

Setting `System.Parent` as a field during creation does **not** establish the parent-child link. The field value appears in the response body but no `Hierarchy-Forward`/`Hierarchy-Reverse` relation is created. ADO accepts the field without error — silent failure.

**Fix:** Use `wit_work_items_link` with `type: "child"` as a second pass after all items are created. Batch-link in one call per parent (API deduplicates updates per work item).

## Pattern 2: Tasks require `OriginalEstimate` + `RemainingWork`

Jairosoft Portfolio process rules enforce both `Microsoft.VSTS.Scheduling.OriginalEstimate` and `Microsoft.VSTS.Scheduling.RemainingWork` as **required fields** on Tasks. `wit_add_child_work_items` cannot set these fields (only supports `title`, `description`, `areaPath`, `iterationPath`, `format`). All 12 attempts returned `TF401320: Rule Error for field Remaining Work. Error code: Required, InvalidEmpty`.

**Fix:** Create tasks via `wit_create_work_item` (supports arbitrary fields), then link via `wit_work_items_link`. Set `RemainingWork` = `OriginalEstimate` on creation (same value initially).

## Pattern 3: Gherkin ACs render in `<pre>` blocks

Acceptance criteria in Gherkin format render cleanly in ADO when wrapped in `<pre>...</pre>` tags with `format: "Html"`. HTML-escape `<`, `>`, `&`, `"` inside the Gherkin text. ADO preserves whitespace and indentation inside `<pre>`.

## Pattern 4: Batch linking via `wit_work_items_link`

The API accepts an `updates` array with multiple `{id, linkToId, type}` entries. It deduplicates by parent — if you send 6 child links for parent A and 6 for parent B, the response returns 2 items (one per parent), each with all children attached. All 200s = success. Use `type: "child"` (not "parent") from the parent's perspective.

## Pattern 5: Preflight search prevents duplicates

Before creating a Feature, search via `search_workitem` filtered by project + work item type + title. If found, abort. Persist all created IDs to a log file (`working/qa_automation_creation_log.md`) for recovery if session interrupts mid-creation.

## Pattern 6: Story fields that work on create

These fields are confirmed working on `wit_create_work_item` for User Story / Enabler types:

| Field | Notes |
|-------|-------|
| `System.Title` | Required |
| `System.Description` | Use `format: "Html"` |
| `Microsoft.VSTS.Common.AcceptanceCriteria` | Use `format: "Html"`, `<pre>` for Gherkin |
| `Microsoft.VSTS.Scheduling.StoryPoints` | String value ("5") |
| `System.AssignedTo` | Full format: `"Name <email>"` |
| `System.IterationPath` | Use `\\` escaped backslashes |
| `System.AreaPath` | Use `\\` escaped backslashes |

## Recommended creation workflow

1. **Preflight** — search for existing Feature by title
2. **Create Feature** via `wit_create_work_item`
3. **Create stories/enablers** via `wit_create_work_item` (parallel batches of 2–3)
4. **Link stories → Feature** via `wit_work_items_link` with `type: "child"`
5. **Create tasks** via `wit_create_work_item` (include `OriginalEstimate` + `RemainingWork`)
6. **Link tasks → stories** via `wit_work_items_link` with `type: "child"`
7. **Persist creation log** to `working/` for recovery

## Linked pages

- [[entities/team-ado-shared]] — first use case for this workflow
- [[entities/system-jodex]] — Feature #203435 created using these patterns
- [[synthesis/audit-automation]] — broader automation roadmap
