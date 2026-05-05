#!/usr/bin/env python3
"""Create a neutral reporting workflow workspace skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "workflow_state.md": """# Workflow State

## Mode
Build Mode

## Output
- Type:
- Cadence:
- Audience:
- Future run environment:

## Constraints
- Data boundary:
- Evidence rules:
- Style rules:
""",
    "data_sources.md": """# Data Sources

| Source | Type | Owner | Refresh cadence | Key fields | Notes |
|---|---|---|---|---|---|
""",
    "field_dictionary.md": """# Field Dictionary

| Field | Meaning | Source | Required | Notes |
|---|---|---|---|---|
""",
    "evidence_map.md": """# Evidence Map

| Claim | Output section | Source | Required fields | Evidence level | Gap/action |
|---|---|---|---|---|---|
""",
    "outline.md": """# Output Outline

## Sections or Slides
""",
    "deck_plan.md": """# Deck Plan

| Slide | Title | Main point | Visual | Evidence |
|---|---|---|---|---|
""",
    "runbook.md": """# Runbook

## Current-period run
1. Place new input files in `inputs/`.
2. Validate required fields.
3. Run the established analysis path.
4. Generate the requested output.
5. Review evidence gaps and QA notes.
""",
    "resurrection_prompt.md": """# Resurrection Prompt

I need to continue or run the saved reporting workflow in this folder.
Load the workflow state, data sources, field dictionary, evidence map, output outline, style constraints, and runbook.
Use the current-period data I provide.
Do not redesign the workflow unless required fields are missing or I explicitly request a redesign.
Generate the requested report or presentation and list unresolved evidence gaps.
""",
    "cleanup_policy.md": """# Cleanup Policy

Keep final outputs and latest workflow state.
Clean temporary charts, cache files, previews, and stale intermediate data after each validated run.
Never delete source inputs or final outputs without explicit approval.
""",
}


DIRS = ["inputs", "outputs", "artifacts", "templates", "scripts"]


def scaffold(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for dirname in DIRS:
        (target / dirname).mkdir(exist_ok=True)
    for filename, content in FILES.items():
        path = target / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Target folder for the reporting workflow workspace")
    args = parser.parse_args()
    scaffold(Path(args.target).resolve())
    print(f"Created reporting workflow workspace at {Path(args.target).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
