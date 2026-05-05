---
name: reporting-workflow-builder
description: Use when a user wants to turn recurring weekly, monthly, business review, KPI report, operating review, or presentation work into a reusable workflow from prior reports, slide decks, spreadsheets, dashboards, databases, logs, CRM exports, support tickets, notes, or other evidence sources.
---

# Reporting Workflow Builder

## Overview

Build reusable reporting workflows, not just one-off reports. Use this skill to help a user move from scattered data and prior materials to a repeatable process that can generate written reports, slide decks, dashboards, or operating review packs.

The core rule is: define resource boundaries before designing the report. The available data, evidence depth, and automation environment determine what the workflow can responsibly produce.

## Mode Selection

Start by choosing the mode.

| Mode | Use when | Goal |
|---|---|---|
| Build Mode | First setup, major redesign, new data sources, new audience, new output format | Create reusable workflow assets and validate one sample run |
| Run Mode | Workflow already exists and the user has new-period data | Generate the current report/deck with minimal questions |
| Repair Mode | A run failed, outputs drifted, fields changed, or evidence is missing | Diagnose the failure, patch the workflow, then rerun |

If the user is not sure, start in Build Mode and produce a small early skeleton before deep implementation.

## Build Mode

Follow this sequence.

1. **Boundary survey first**
   Identify output type, audience, cadence, available files/systems, user technical comfort, and where future runs should happen. Do not design advanced analysis before knowing whether the evidence exists.

2. **Prior-material audit**
   Use previous reports, slide decks, dashboard screenshots, templates, and notes to infer structure, visual constraints, recurring metrics, and stakeholder expectations. Treat them as references, not as the ceiling.

3. **Low-fidelity skeleton**
   Deliver an early outline or deck wireframe constrained by available resources. Show the user what the final output could become before asking for many more details.

4. **Data and evidence mapping**
   Split inputs into structured performance data and ledger/detail evidence. Build a map from each intended claim to its source, fields, evidence strength, and missing pieces.

5. **Prune or downgrade unsupported modules**
   Keep strong-evidence sections, mark weak-evidence sections carefully, and remove or downgrade sections that require unavailable data. Never invent root causes, user reasons, process failures, or detailed examples without evidence.

6. **Choose the implementation path**
   Pick the simplest viable path:
   - Direct agent delivery: Codex/Claude Code generates the report or deck now.
   - Template reuse: a nontechnical user updates fixed inputs and prompts.
   - Engineered rerun: scripts, registered queries, field mappings, validations, and runbooks support future cowork-style runs.

7. **Solidify workflow assets**
   Save the output structure, data map, field dictionary, evidence rules, style constraints, run instructions, cleanup policy, and a resurrection prompt for future sessions.

For detailed Build Mode steps, load `references/build-mode.md`.

## Run Mode

Run Mode should be short and operational.

1. Load the existing workflow configuration, prompt, runbook, or prior state block.
2. Check that current-period files and required fields exist.
3. Run the established analysis path; avoid redesign unless blocked.
4. Generate the requested output: written report, slide deck, spreadsheet summary, or dashboard artifact.
5. Perform quality checks: missing placeholders, stale dates, unsupported claims, chart/text overlap, font/readability issues, empty visuals, and wrong data period.
6. Return the final artifact plus a brief run summary and unresolved data gaps.

Ask only blocking questions. If a field is missing, state which output section is affected and either downgrade that section or stop if the report would be misleading.

For detailed Run Mode and handoff patterns, load `references/run-mode.md`.

## Evidence Rules

Use structured performance data to answer "what happened" and detail evidence to answer "why it happened."

Examples of structured performance data: KPI exports, BI/dashboard tables, spreadsheet templates, database query results, product/service metrics, revenue or conversion tables, campaign summaries, operational logs aggregated by period.

Examples of detail evidence: transaction rows, account/customer records, CRM activity, support tickets, call notes, follow-up logs, cancellation reasons, failure reasons, survey comments, issue threads, incident records, manual annotations.

Do not turn aggregate movements into causal explanations unless detail evidence supports the claim. If only aggregate data exists, write observations and hypotheses, not definitive causes.

For evidence mapping and anti-hallucination rules, load `references/evidence-rules.md`.

## Output Rules

The skill may produce reports, slide decks, scripts, templates, and runbooks. Automatic slide-deck generation is a normal deliverable, including for nontechnical users, when the local agent environment can create or edit presentation files.

Prefer intermediate artifacts for repeatability:

- `workflow_state.md` or `workflow_state.json`
- `data_sources.md`
- `evidence_map.md`
- `field_dictionary.md`
- `outline.md`
- `deck_plan.md`
- `runbook.md`
- `resurrection_prompt.md`
- `cleanup_policy.md`

For presentation generation, keep design reusable: separate content outline, chart specifications, and visual style constraints before rendering the deck.

## Workspace Scaffolding

If the user asks to create a local workflow folder, run or adapt:

```bash
python scripts/scaffold_reporting_workspace.py <target-folder>
```

The scaffold creates a neutral reporting-workflow workspace without industry-specific assumptions.

## Open-Source Hygiene

Keep the skill industry-neutral. Avoid embedding client names, internal table names, private metrics, proprietary channel names, or sector-specific examples in the skill layer. Put organization-specific rules in the user's project workspace, not in this reusable skill.
