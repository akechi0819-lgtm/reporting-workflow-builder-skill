# Build Mode

Use Build Mode when creating or redesigning a recurring reporting workflow.

## 0. Boundary Survey

Collect only enough information to constrain the first skeleton.

Ask about:

- Output: written report, slide deck, spreadsheet summary, dashboard, or multiple outputs.
- Cadence: weekly, monthly, quarterly, campaign-based, incident-based.
- Audience: executive, department lead, operating manager, frontline team, client, investor, internal project team.
- Decision purpose: review performance, explain changes, allocate resources, inspect execution quality, identify risks, plan next actions.
- Data access: manual files, dashboard exports, raw logs, database, API, existing scripts, RPA/low-code tool.
- Future run location: Codex/Claude Code, cowork-style assistant, spreadsheet template, BI tool, automation platform, or manual process.
- Technical comfort: upload-only, spreadsheet user, script runner, SQL-capable, engineer/analyst.

Use choices before open-ended questions. Example:

```text
Which best describes your data access?
A. I only have files/screenshots I can upload.
B. I can export cleaned tables from dashboards.
C. I have raw detail tables or logs.
D. I have read-only database/API access.
E. I already have scripts or queries.
```

## 1. Prior-Material Audit

Ask the user to upload a few previous reports, slide decks, templates, or screenshots if available. Extract:

- Required recurring sections.
- Stakeholder reading order.
- Metrics and naming conventions.
- Visual style constraints.
- Known weak spots in prior outputs.
- Repeated manual work that should be automated.

Do not blindly copy the prior structure. Review whether it has:

- Too many charts without interpretation.
- Too much text without a decision point.
- Claims without evidence.
- Small fonts or crowded slides.
- Stale sections kept only by habit.
- Missing action ownership.

## 2. Low-Fidelity Skeleton

Produce an early skeleton as soon as the boundary survey is complete.

For a written report, include section titles and 1-line purpose statements.

For a slide deck, include page order, page title, intended chart/table, and expected evidence.

Constrain the skeleton by data reality:

- If only aggregate tables exist, focus on trends, ranking, mix shift, and variance.
- If detail evidence exists, include root-cause, quality, and example sections.
- If no reliable time series exists, avoid trend claims.
- If no ownership field exists, avoid owner/team performance sections.

## 3. Data Source Layering

Separate data into two layers.

**Structured performance data** supports "what happened":

- KPI exports
- Dashboard tables
- Period summaries
- Database query results
- Spreadsheet templates
- Aggregated operational logs

**Ledger/detail evidence** supports "why it happened":

- Transaction rows
- Customer/account records
- CRM activities
- Support tickets
- Follow-up notes
- Cancellation/failure reasons
- Free-text comments
- Manual annotations

## 4. Evidence Map

Create an evidence map for each planned claim.

| Analysis question | Primary source | Backup source | Required fields | Evidence strength | Gap/action |
|---|---|---|---|---|---|
| Which segments changed most? | KPI export | Dashboard table | date, segment, metric | Strong | None |
| Why did conversion decline? | Detail rows | CRM notes | status, reason, owner, timestamp | Medium/Strong | Need reason text |
| Is follow-up quality weak? | Activity logs | Manual review | activity_count, content, timestamp | Medium | Need content for quality claims |

## 5. Hard Pruning

Apply architecture veto when the evidence is missing.

- Strong evidence: keep and write confidently.
- Partial evidence: keep with scoped wording.
- Missing evidence: downgrade to observation, hypothesis, or data gap.
- Misleading evidence: remove.

Never fill a missing cause with a plausible business story.

## 6. Implementation Path

Choose one path.

**Direct agent delivery**

Use when the user needs an immediate report/deck and is not trying to maintain code. The agent reads files, generates analysis, builds charts, and produces the final artifact directly.

**Template reuse**

Use when the user can update a fixed spreadsheet or prompt each period. Create stable templates, input instructions, and a run prompt.

**Engineered rerun**

Use when data sources are stable enough for scripts or registered queries. Create query handles, field mappings, validations, output templates, cleanup rules, and a runbook.

## 7. Solidify State

End Build Mode with:

- A validated sample report/deck.
- A data source list.
- A field dictionary.
- An evidence map.
- Style constraints.
- A runbook.
- A resurrection prompt.
- A cleanup policy.

The resurrection prompt should be plain language, not only JSON. It should tell a future agent what to load, what to ask, and what not to redesign.
