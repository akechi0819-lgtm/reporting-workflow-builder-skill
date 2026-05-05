# Reporting Workflow Builder Skill

Turn recurring reports and presentation work into reusable AI-assisted workflows.

`reporting-workflow-builder` is a Codex/Claude-style skill for building repeatable reporting workflows from messy real-world inputs: prior reports, slide decks, spreadsheets, dashboard exports, databases, logs, CRM exports, support tickets, manual notes, and other evidence sources.

It is not a one-off report-writing prompt. Its purpose is to help an agent guide a user from scattered materials to a durable workflow that can be reused for weekly reports, monthly business reviews, KPI reviews, operating reviews, executive updates, and recurring presentation decks.

## Why This Exists

Many recurring reports fail for the same reasons:

- The user has data, but does not know which source supports which claim.
- Prior reports and slide decks contain useful habits, but also stale structure.
- Aggregate KPI tables get stretched into unsupported causal explanations.
- The first setup conversation becomes too long before the user sees any output.
- A workflow works once in a coding agent, then fails when handed to a lighter cowork-style assistant.

This skill addresses those problems by separating workflow setup from repeat execution.

## Core Idea

The skill uses two main modes:

- **Build Mode**: used for first setup, major redesign, new data sources, or new reporting formats.
- **Run Mode**: used after the workflow exists, when the user only wants the current-period report or deck.

It also includes **Repair Mode** for schema drift, broken runs, missing fields, stale outputs, or evidence gaps.

The guiding rule is:

> Define resource boundaries before designing the report.

The available data, evidence depth, and automation environment determine what the workflow can responsibly produce.

## What It Helps Build

The skill can help an agent produce and maintain:

- Written reports
- Slide decks and presentation packs
- KPI review workflows
- Operating review workflows
- Spreadsheet-backed reporting templates
- Evidence maps
- Field dictionaries
- Data source maps
- Reusable runbooks
- Resurrection prompts for future sessions
- Cleanup policies for generated artifacts

Automatic slide-deck generation is treated as a normal deliverable when the local agent environment can create or edit presentation files.

## Workflow Modes

### Build Mode

Use Build Mode when the workflow is being created or redesigned.

The agent should:

1. Survey the reporting goal, audience, cadence, available data, and future run environment.
2. Audit prior reports, decks, templates, and screenshots without treating them as the ceiling.
3. Produce a low-fidelity outline or deck skeleton early.
4. Split data sources into structured performance data and detail evidence.
5. Build an evidence map from intended claims to actual fields and sources.
6. Prune or downgrade unsupported sections.
7. Choose an implementation path: direct agent delivery, template reuse, or engineered rerun.
8. Save workflow state, run instructions, style constraints, evidence rules, and a resurrection prompt.

### Run Mode

Use Run Mode when the workflow already exists and the user has new-period data.

The agent should:

1. Load the saved workflow state, runbook, or resurrection prompt.
2. Validate current-period inputs and required fields.
3. Run the established analysis path.
4. Generate the requested report, deck, spreadsheet, or dashboard artifact.
5. Check for stale dates, missing placeholders, unsupported claims, chart issues, and readability problems.
6. Return the final artifact plus a brief run summary and unresolved data gaps.

Run Mode should ask only blocking questions.

### Repair Mode

Use Repair Mode when a previously working workflow breaks.

Typical triggers:

- A source file changed columns.
- A database query stopped returning expected fields.
- A chart is empty.
- A report uses stale period data.
- A deck rendered with missing placeholders or unreadable text.
- A causal section lacks detail evidence.

Repair Mode should diagnose the failure, patch the workflow, validate the fix, and then rerun.

## Evidence Discipline

The skill separates data into two layers:

| Layer | Answers | Examples |
|---|---|---|
| Structured performance data | What happened? | KPI exports, dashboard tables, spreadsheet templates, database query results, period summaries |
| Detail evidence | Why did it happen? | Transaction rows, CRM activity, support tickets, follow-up notes, cancellation reasons, comments, incident records |

Aggregate data can support trends, rankings, mix shifts, and anomalies. It cannot by itself support detailed causal claims, user intent, process-quality judgments, or representative case examples.

If evidence is missing, the agent must downgrade the claim, mark it as a hypothesis, or remove the section.

## Installation

Copy the skill folder into your agent's skills directory.

For Codex:

```text
~/.codex/skills/reporting-workflow-builder
```

For Claude Code:

```text
~/.claude/skills/reporting-workflow-builder
```

On Windows, these are typically:

```text
C:\Users\<you>\.codex\skills\reporting-workflow-builder
C:\Users\<you>\.claude\skills\reporting-workflow-builder
```

Restart the agent or open a new session after installation.

## Repository Layout

```text
reporting-workflow-builder/
  SKILL.md
  agents/
    openai.yaml
  references/
    build-mode.md
    run-mode.md
    evidence-rules.md
  scripts/
    scaffold_reporting_workspace.py
```

## Example Prompts

Start a new workflow:

```text
Use the reporting-workflow-builder skill to help me build a reusable weekly reporting workflow.
I will upload prior reports, previous slide decks, and current data exports.
Start by checking my data boundaries and output needs before designing the report structure.
```

Generate a current-period output from an existing workflow:

```text
Use the saved reporting workflow in this folder.
The current-period data is attached.
Generate this period's report/deck with the existing structure and style.
Only ask if a required field is missing.
```

Repair a failed workflow:

```text
The report workflow used to run, but this week's output has missing charts and stale dates.
Use reporting-workflow-builder in Repair Mode to diagnose the issue, patch the workflow, and rerun it.
```

## Optional Workspace Scaffold

The skill includes a small helper script that creates a neutral reporting-workflow workspace:

```bash
python scripts/scaffold_reporting_workspace.py ./my-reporting-workflow
```

It creates files such as:

- `workflow_state.md`
- `data_sources.md`
- `field_dictionary.md`
- `evidence_map.md`
- `outline.md`
- `deck_plan.md`
- `runbook.md`
- `resurrection_prompt.md`
- `cleanup_policy.md`

These files are intentionally generic and should be adapted to the user's organization or project.

## Design Principles

- Start with resource boundaries, not ambitious report structure.
- Use prior materials as references, not as hard limits.
- Deliver a small skeleton early to avoid long conversation setup.
- Separate "what happened" data from "why it happened" evidence.
- Refuse unsupported causal claims.
- Keep setup and recurring execution separate.
- Make future runs simple enough for nontechnical users.
- Keep the skill layer industry-neutral.

## Open-Source Hygiene

This skill is intentionally industry-neutral. Do not add private organization names, client-specific terms, internal table names, proprietary metrics, or sector-specific business assumptions to the reusable skill layer.

Organization-specific rules should live in the user's local project workspace, not in this skill.

## Validation

If you have the Codex skill creator utilities available, validate the skill structure with:

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ./reporting-workflow-builder
```

You can also smoke-test the scaffold script:

```bash
python reporting-workflow-builder/scripts/scaffold_reporting_workspace.py ./tmp-reporting-workflow
```

## Status

Early reusable skill draft. It is intended for real-world testing across different reporting domains before being treated as stable.
