# Evidence Rules

Use this reference whenever the workflow includes analysis, root-cause statements, process-quality claims, or examples from detail records.

## Evidence Levels

| Level | Meaning | Allowed language |
|---|---|---|
| Strong | Direct source fields support the claim | "The largest decline came from..." |
| Medium | Direction is supported but cause is partial | "The data suggests..." |
| Weak | Only aggregate movement or incomplete detail exists | "This is a hypothesis to verify..." |
| Missing | No supporting source | Do not make the claim |

## What Aggregate Data Can Support

Aggregate data can support:

- Volume changes
- Rate changes
- Ranking
- Mix shift
- Period-over-period movement
- Segment contribution
- Top/bottom entities
- Anomaly flags

Aggregate data cannot by itself support:

- Human intent
- User/customer reasons
- Process quality
- Scripted causal explanations
- Specific failure stories
- Representative examples

## What Detail Evidence Can Support

Detail evidence can support:

- Reason clustering
- Text-backed examples
- Process or activity quality
- Owner/team behavior patterns
- Bottleneck diagnosis
- Risk signal extraction

Only cite example IDs or records that were actually read from the source. If no text/detail field is returned, say that concrete examples cannot be produced from the current data.

## Anti-Hallucination Rules

- Do not infer reasons from labels alone if the label does not encode the reason.
- Do not convert a correlation into a cause.
- Do not invent a "typical case" without a record ID or source row.
- Do not reuse old-period explanations for current-period data unless the current data supports them.
- Do not hide missing data behind polished prose.
- If a section would be misleading, downgrade or remove it.

## Recommended Evidence Map Fields

Use these fields in `evidence_map.md` or equivalent:

- `claim`
- `output_section`
- `source_name`
- `source_type`
- `required_fields`
- `available_fields`
- `join_keys`
- `date_field`
- `filters`
- `evidence_level`
- `known_gaps`
- `allowed_wording`
- `blocked_wording`
