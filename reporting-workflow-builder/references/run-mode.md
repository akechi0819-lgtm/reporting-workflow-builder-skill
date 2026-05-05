# Run Mode

Use Run Mode when the workflow already exists and the user wants the current-period output.

## Entry Conditions

Before running, locate at least one of:

- `workflow_state.md`
- `workflow_state.json`
- `runbook.md`
- `resurrection_prompt.md`
- Prior output plus stable input templates
- Existing scripts or registered query definitions

If none exist, switch to Build Mode.

## Run Steps

1. **Load state**
   Read the workflow state and style/output constraints. Do not redesign the report unless the user asks or the current data makes the old structure invalid.

2. **Validate inputs**
   Check file presence, date period, required fields, sheet names, schema drift, duplicate records, empty values, and stale files.

3. **Execute analysis**
   Use fixed scripts, templates, queries, or established calculations. Prefer registered/known queries over ad hoc data digging.

4. **Generate output**
   Produce the report, slide deck, spreadsheet, or dashboard artifact requested by the user. Keep visual style consistent with the stored constraints.

5. **Quality assurance**
   Check date ranges, chart emptiness, placeholder text, unsupported claims, text overflow, font size, table legibility, and output file validity.

6. **Return concise run summary**
   Include output path, data period, major generated sections, warnings, and unresolved evidence gaps.

## Blocking Conditions

Stop or downgrade when:

- A required metric field is missing.
- The current period cannot be determined.
- The data source is from the wrong period.
- The requested causal claim lacks detail evidence.
- A chart would be empty or misleading.
- A template changed enough that mappings cannot be trusted.

Do not ask non-blocking preference questions in Run Mode.

## Cowork-Style Handoff

Run Mode should feel like this to the user:

```text
Use the saved workflow. Current-period data is attached. Generate this period's report/deck, keep the existing structure and style, and only ask if a required field is missing.
```

The assistant should call established scripts and templates where available, then return the artifact and a short summary.

## Resurrection Prompt Pattern

Create prompts that a nontechnical user can save and reuse:

```text
[Reusable reporting workflow start prompt]
I need to generate the current-period operating review using the saved workflow in this folder.
Load the workflow state, data source map, evidence rules, visual constraints, and runbook.
Use the new files I attach for this period.
Do not redesign the structure unless required fields are missing or I explicitly ask for a redesign.
Generate the requested output and list any evidence gaps.
```
