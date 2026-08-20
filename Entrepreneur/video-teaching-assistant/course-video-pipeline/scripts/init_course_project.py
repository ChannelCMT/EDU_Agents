#!/usr/bin/env python3
"""Create a new course-video project from the bundled template."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

import yaml


TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", value).strip("-").lower()
    return slug or "course-video-project"


def replace_tokens(path: Path, tokens: dict[str, str]) -> None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return
    text = path.read_text(encoding="utf-8")
    for key, value in tokens.items():
        text = text.replace("{{" + key + "}}", value)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Destination project directory")
    parser.add_argument("--title", required=True, help="Course title")
    parser.add_argument("--chapters", type=int, default=5, help="Chapter count")
    args = parser.parse_args()

    if args.chapters < 1 or args.chapters > 20:
        parser.error("--chapters must be between 1 and 20")

    template = Path(__file__).resolve().parents[1] / "assets" / "project-template"
    output = Path(args.output).resolve()
    if output.exists() and any(output.iterdir()):
        parser.error(f"destination is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)

    chapter_template = template / "chapter"
    for item in template.iterdir():
        if item.name == "chapter":
            continue
        destination = output / item.name
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    common = {
        "PROJECT_TITLE": args.title,
        "PROJECT_SLUG": slugify(args.title),
        "CHAPTER_COUNT": str(args.chapters),
    }
    for path in output.rglob("*"):
        if path.is_file():
            replace_tokens(path, common)

    chapter_plan_path = output / "chapter-plan.yaml"
    chapter_plan = yaml.safe_load(chapter_plan_path.read_text(encoding="utf-8"))
    chapter_plan["chapters"] = [
        {
            "number": number,
            "title": "TODO",
            "learner_problem": "TODO",
            "learning_result": "TODO",
            "visual_arc": ["TODO"],
            "status": "draft",
        }
        for number in range(1, args.chapters + 1)
    ]
    chapter_plan_path.write_text(
        yaml.safe_dump(chapter_plan, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )

    for number in range(1, args.chapters + 1):
        chapter_dir = output / f"chapter-{number:02d}"
        shutil.copytree(chapter_template, chapter_dir)
        tokens = {**common, "CHAPTER_NUMBER": str(number)}
        for path in chapter_dir.rglob("*"):
            if path.is_file():
                replace_tokens(path, tokens)
        for subdir in ("audio", "assets", "renders", "snapshots"):
            (chapter_dir / subdir).mkdir(exist_ok=True)

    (output / "PastUselessDoc").mkdir(exist_ok=True)
    print(f"Created course video project: {output}")
    print(f"Chapters: {args.chapters}")
    print("Next: complete project.yaml, chapter-plan.yaml, and each chapter SCRIPT.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
