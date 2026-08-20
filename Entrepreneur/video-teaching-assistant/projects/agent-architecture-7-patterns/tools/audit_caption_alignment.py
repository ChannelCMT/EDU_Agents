"""Fail-closed checks for global word-time normalization and subtitle cues."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from build_word_aligned_captions import absolute_words


ROOT = Path(__file__).resolve().parents[1]
MAX_DELTA_SECONDS = 0.08


def audit_chapter(chapter_path: Path) -> list[str]:
    failures: list[str] = []
    raw = json.loads((chapter_path / "audio" / "word-alignment-raw.json").read_text(encoding="utf-8"))
    captions = json.loads((chapter_path / "captions" / "captions.json").read_text(encoding="utf-8"))
    words = absolute_words(raw)
    duration = float(raw["duration"])

    previous_word_end = -1.0
    for index, word in enumerate(words):
        start = float(word["start"])
        end = float(word["end"])
        if end <= start:
            failures.append(f"word_non_positive:{index}")
        if start < previous_word_end - 0.02:
            failures.append(f"word_time_reversal:{index}")
        previous_word_end = max(previous_word_end, end)

    previous_cue_end = -1.0
    for cue in captions:
        cue_id = cue.get("id", "unknown")
        start = float(cue["start"])
        end = float(cue["end"])
        evidence = cue.get("word_evidence") or {}
        word_start = float(evidence.get("word_start", -1))
        word_end = float(evidence.get("word_end", -1))
        if not evidence.get("raw_words"):
            failures.append(f"missing_word_evidence:{cue_id}")
        if start < 0 or end > duration + 0.01 or end <= start:
            failures.append(f"cue_out_of_range:{cue_id}")
        if start < previous_cue_end - 0.001:
            failures.append(f"cue_overlap:{cue_id}")
        if abs(start - word_start) > MAX_DELTA_SECONDS or abs(end - word_end) > MAX_DELTA_SECONDS:
            failures.append(f"cue_evidence_delta:{cue_id}")
        if evidence.get("timebase") != "global":
            failures.append(f"non_global_timebase:{cue_id}")
        previous_cue_end = end

    if chapter_path.name == "chapter-01" and len(captions) >= 2:
        first, second = captions[0], captions[1]
        if float(first["start"]) > 0.01 or not 2.50 <= float(first["end"]) <= 2.80:
            failures.append("chapter1_first_hook_window_invalid")
        if not 2.85 <= float(second["start"]) <= 2.96 or not 4.60 <= float(second["end"]) <= 4.80:
            failures.append("chapter1_second_line_window_invalid")
    return failures


def audit_project(root: Path = ROOT) -> dict:
    chapters = []
    for number in range(1, 6):
        chapter_path = root / f"chapter-{number:02d}"
        failures = audit_chapter(chapter_path)
        chapters.append({
            "chapter": number,
            "failures": failures,
            "status": "pass" if not failures else "fail",
        })
    return {
        "version": "v01",
        "rule": "global word evidence, monotonic cues, <=80ms cue/evidence delta",
        "chapters": chapters,
        "status": "pass" if all(row["status"] == "pass" for row in chapters) else "fail",
    }


def main() -> int:
    report = audit_project()
    path = ROOT / "content" / "caption-alignment-audit-v01.yaml"
    path.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(yaml.safe_dump(report, allow_unicode=True, sort_keys=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
