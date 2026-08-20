"""Source and checkpoint geometry gates for rendered HyperFrames layouts."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
BOX_RE = re.compile(r'id="([^"]+)"[^>]*style="([^"]*)"')
NUM_RE = re.compile(r'(left|top|width|height):\s*([0-9.]+)px')


def boxes(html: str) -> dict[str, dict[str, float]]:
    result: dict[str, dict[str, float]] = {}
    for element_id, style in BOX_RE.findall(html):
        result[element_id] = {key: float(value) for key, value in NUM_RE.findall(style)}
    return result


def audit_chapter(chapter_path: Path) -> list[str]:
    html = (chapter_path / "index.html").read_text(encoding="utf-8")
    failures: list[str] = []
    if 'data-subtitle-safe-band="900-1080"' not in html:
        failures.append("subtitle_safe_band_not_declared")
    root_match = re.search(r'<div id="root"[^>]*data-width="(\d+)"[^>]*data-height="(\d+)"', html)
    if not root_match or (root_match.group(1), root_match.group(2)) != ("1920", "1080"):
        failures.append("canvas_dimensions_not_1920x1080")
    for element_id, box in boxes(html).items():
        if {"left", "top", "width", "height"}.issubset(box):
            if box["left"] < 0 or box["top"] < 0 or box["left"] + box["width"] > 1920 or box["top"] + box["height"] > 1080:
                failures.append(f"off_canvas:{element_id}")
    if chapter_path.name == "chapter-01":
        parsed = boxes(html)
        panel = parsed.get("c1-evo", {})
        axis_y = parsed.get("c1-axis-y", {})
        note = parsed.get("c1-note", {})
        if panel.get("left", 9999) + panel.get("width", 0) > 1850 or panel.get("top", 0) + panel.get("height", 9999) > 870:
            failures.append("evolution_panel_not_clear_of_caption_band")
        if axis_y.get("top", 9999) + axis_y.get("height", 0) > 812:
            failures.append("y_axis_extends_below_origin")
        if note.get("top", 9999) >= 870:
            failures.append("closing_note_enters_caption_band")
        if 'id="c1-q3"' in html or "长流程生产" in html:
            failures.append("removed_q3_visual_present")
        if not all(f'id="c1-evo-{index}"' in html for index in range(1, 8)):
            failures.append("seven_model_list_incomplete")
    return failures


def audit_project(root: Path = ROOT) -> dict:
    chapters = []
    for number in range(1, 6):
        chapter_path = root / f"chapter-{number:02d}"
        failures = audit_chapter(chapter_path)
        chapters.append({"chapter": number, "failures": failures, "status": "pass" if not failures else "fail"})
    return {
        "version": "v01",
        "rule": "source boxes stay on canvas, clear subtitle band, and preserve required chapter-one layers",
        "rendered_frame_evidence_required": True,
        "chapters": chapters,
        "status": "pass" if all(row["status"] == "pass" for row in chapters) else "fail",
    }


def main() -> int:
    report = audit_project()
    path = ROOT / "content" / "rendered-layout-audit-v01.yaml"
    path.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(yaml.safe_dump(report, allow_unicode=True, sort_keys=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
