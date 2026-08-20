#!/usr/bin/env python3
"""Validate the course-video repository or a generated project."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml


CHAPTER_FILES = [
    "SCRIPT.md",
    "terminology.yaml",
    "tone-plan.yaml",
    "voice-manifest.yaml",
    "audio_meta.json",
    "word-alignment.yaml",
    "semantic-anchor-plan.yaml",
    "semantic-beat-manifest.yaml",
    "visual-coverage-matrix.yaml",
    "semantic-timing-manifest.yaml",
    "timed-storyboard.yaml",
    "layout-audit.md",
    "qa-report.md",
]


def load_data(path: Path, errors: list[str]):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"not UTF-8: {path}")
        return None
    try:
        if path.suffix == ".json":
            return json.loads(text)
        return yaml.safe_load(text)
    except Exception as exc:  # report all parse failures together
        errors.append(f"parse failed: {path}: {exc}")
        return None


def require(path: Path, errors: list[str]) -> bool:
    if not path.exists():
        errors.append(f"missing: {path}")
        return False
    return True


def validate_repository(root: Path, errors: list[str]) -> None:
    workflow_paths = [
        root / "workflow" / "course-video-workflow.yaml",
        root / "workflow" / "role-routing.yaml",
        root / "workflow" / "master-harness.yaml",
    ]
    for path in workflow_paths:
        if require(path, errors):
            load_data(path, errors)

    workflow = load_data(workflow_paths[0], errors) if workflow_paths[0].exists() else None
    roles = load_data(workflow_paths[1], errors) if workflow_paths[1].exists() else None
    harness = load_data(workflow_paths[2], errors) if workflow_paths[2].exists() else None
    if workflow:
        stages = workflow.get("stages", [])
        ids = [stage.get("id") for stage in stages]
        if len(stages) < 15:
            errors.append("workflow must contain S00-S14 stages")
        if len(ids) != len(set(ids)):
            errors.append("workflow stage ids are not unique")
        role_ids = set((roles or {}).get("roles", {}).keys())
        for stage in stages:
            owner = stage.get("owner")
            if owner and owner not in role_ids:
                errors.append(f"unknown owner {owner} in {stage.get('id')}")
            for field in ("inputs", "outputs", "exit_gate", "on_failure"):
                if not stage.get(field):
                    errors.append(f"{stage.get('id')} missing {field}")
    if harness:
        for key in ("content", "voice", "semantic_animation", "visual_style", "subtitles", "render", "cover", "publish", "loop"):
            if key not in harness:
                errors.append(f"master harness missing section: {key}")

    skill = root / "course-video-pipeline"
    for relative in (
        "SKILL.md",
        "agents/openai.yaml",
        "references/workflow.md",
        "references/harness.md",
        "references/artifact-contracts.md",
        "references/role-routing.md",
        "assets/project-template/project.yaml",
        "scripts/init_course_project.py",
        "scripts/validate_course_video.py",
    ):
        require(skill / relative, errors)

    # Parse every public machine-readable artifact. Template YAML intentionally
    # contains replacement tokens and is validated after project generation.
    template_root = skill / "assets" / "project-template"
    for path in sorted(list(root.rglob("*.yaml")) + list(root.rglob("*.yml")) + list(root.rglob("*.json"))):
        try:
            path.relative_to(template_root)
            continue
        except ValueError:
            pass
        load_data(path, errors)


def contains_todo(path: Path) -> bool:
    if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json"}:
        return False
    return "TODO" in path.read_text(encoding="utf-8")


def validate_project(root: Path, errors: list[str], structure_only: bool) -> None:
    project_path = root / "project.yaml"
    if not require(project_path, errors):
        return
    project = load_data(project_path, errors)
    if not isinstance(project, dict):
        errors.append("project.yaml must be a mapping")
        return
    chapter_count = project.get("chapter_count")
    if not isinstance(chapter_count, int) or not 1 <= chapter_count <= 20:
        errors.append("project.yaml chapter_count must be 1..20")
        return

    for relative in ("asset-inventory.yaml", "canonical-transcript.md", "chapter-plan.yaml", "visual-style.yaml", "RUN_STATE.yaml", "subtitle-manifest.yaml", "publish-package.yaml"):
        path = root / relative
        if require(path, errors) and path.suffix in {".yaml", ".yml", ".json"}:
            load_data(path, errors)

    for number in range(1, chapter_count + 1):
        chapter = root / f"chapter-{number:02d}"
        if not require(chapter, errors):
            continue
        for filename in CHAPTER_FILES:
            path = chapter / filename
            if not require(path, errors):
                continue
            if path.suffix in {".yaml", ".yml", ".json"}:
                load_data(path, errors)
            if not structure_only and contains_todo(path):
                errors.append(f"unfinished TODO: {path}")
        if not structure_only:
            tone_path = chapter / "tone-plan.yaml"
            tone = load_data(tone_path, errors) if tone_path.exists() else None
            sentences = tone.get("sentences") if isinstance(tone, dict) else None
            required_tone = {"sentence_id", "source_text", "delivery_intent", "energy_1_to_5", "pace", "emphasis_terms", "pause_after_ms", "breath_points", "pronunciation", "visual_sync"}
            if not isinstance(sentences, list) or not sentences:
                errors.append(f"tone plan must contain sentence-level rows: {tone_path}")
            else:
                for idx, row in enumerate(sentences, 1):
                    if not isinstance(row, dict):
                        errors.append(f"tone plan row {idx} is not a mapping: {tone_path}")
                        continue
                    missing = sorted(required_tone - set(row))
                    if missing:
                        errors.append(f"tone plan row {idx} missing {missing}: {tone_path}")
            captions_path = chapter / "captions" / "captions.json"
            if captions_path.exists():
                captions = load_data(captions_path, errors)
                if isinstance(captions, list):
                    for idx, cue in enumerate(captions, 1):
                        if not isinstance(cue, dict) or cue.get("timing_method") != "word_alignment":
                            errors.append(f"caption {idx} must use word_alignment timing: {captions_path}")
                        if isinstance(cue, dict) and not cue.get("word_evidence"):
                            errors.append(f"caption {idx} missing word_evidence: {captions_path}")
                    coverage_path = chapter / "visual-coverage-matrix.yaml"
                    coverage = load_data(coverage_path, errors) if coverage_path.exists() else None
                    rows = coverage.get("rows") if isinstance(coverage, dict) else None
                    if not isinstance(rows, list) or len(rows) != len(captions):
                        errors.append(f"visual coverage must have one row per caption cue: {coverage_path}")
                    elif any(not row.get("visual_event_ids") or row.get("coverage") == "voice_only" for row in rows if isinstance(row, dict)):
                        errors.append(f"named/claim caption is missing a visual event: {coverage_path}")
            beat_path = chapter / "semantic-beat-manifest.yaml"
            beat = load_data(beat_path, errors) if beat_path.exists() else None
            beat_rows = beat.get("beats") if isinstance(beat, dict) else None
            if not isinstance(beat_rows, list) or not beat_rows:
                errors.append(f"semantic beat manifest must contain sentence-level rows: {beat_path}")
            else:
                required_beats = {"sentence_id", "source_text", "semantic_start", "visual_start", "visual_event"}
                for idx, row in enumerate(beat_rows, 1):
                    if not isinstance(row, dict) or not required_beats.issubset(row):
                        errors.append(f"semantic beat {idx} missing required fields: {beat_path}")
                html_path = chapter / "index.html"
                if html_path.exists():
                    html_text = html_path.read_text(encoding="utf-8")
                    for row in beat_rows:
                        event = row.get("visual_event")
                        if event and f'id="{event}"' not in html_text:
                            errors.append(f"semantic beat points to missing visual object {event}: {html_path}")
            if number == 1 and isinstance(beat, dict):
                audit = beat.get("first_30_seconds_layer_audit", {})
                if audit.get("status") != "pass" or audit.get("key_visual_max_y", 9999) > 870:
                    errors.append(f"first-30-second layer audit failed: {beat_path}")

    if not structure_only:
        for path in (project_path, root / "asset-inventory.yaml", root / "chapter-plan.yaml", root / "publish-package.yaml"):
            if path.exists() and contains_todo(path):
                errors.append(f"unfinished TODO: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Repository root or generated project root")
    parser.add_argument("--structure-only", action="store_true", help="Check files and syntax without requiring completed content")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    errors: list[str] = []
    if (root / "workflow").exists() and (root / "course-video-pipeline").exists():
        validate_repository(root, errors)
        mode = "repository"
    else:
        validate_project(root, errors, args.structure_only)
        mode = "project"

    if errors:
        print(f"FAIL ({mode}): {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS ({mode}): {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
