"""Write a single SRT/VTT from the checked chapter caption cues."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DURATIONS = [31.007, 32.388, 34.609, 32.728, 44.587]
GAP = 0.5


def stamp(seconds: float, vtt: bool = False) -> str:
    ms = max(0, round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, milli = divmod(rem, 1000)
    sep = "." if vtt else ","
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{milli:03d}"


def main() -> int:
    cues = []
    offset = 0.0
    for chapter, duration in enumerate(DURATIONS, 1):
        data = json.loads((ROOT / f"chapter-{chapter:02d}" / "captions" / "captions.json").read_text(encoding="utf-8"))
        for cue in data:
            cues.append({"chapter": chapter, "start": offset + float(cue["start"]), "end": offset + float(cue["end"]), "text": cue["text"]})
        offset += duration
        if chapter < len(DURATIONS):
            offset += GAP
    out_dir = ROOT / "publish-package" / "captions"
    out_dir.mkdir(parents=True, exist_ok=True)
    srt = []
    vtt = ["WEBVTT", ""]
    for i, cue in enumerate(cues, 1):
        srt.extend([str(i), f"{stamp(cue['start'])} --> {stamp(cue['end'])}", cue["text"], ""])
        vtt.extend([f"{stamp(cue['start'], True)} --> {stamp(cue['end'], True)}", cue["text"], ""])
    (out_dir / "agent-architecture-7-patterns.srt").write_text("\n".join(srt), encoding="utf-8")
    (out_dir / "agent-architecture-7-patterns.vtt").write_text("\n".join(vtt), encoding="utf-8")
    (out_dir / "caption-manifest.yaml").write_text(
        "\n".join([
            "version: '1.0'", "language: zh-CN", "source_of_truth: chapter captions.json", "single_line: true",
            "visible_chars_target: 5-14", "subtitle_offset_seconds: -0.05", "safe_band_y: 900-1080",
            "short_exact_terms_allowed: ['容易跑偏']", f"cue_count: {len(cues)}", "files:", "  srt: agent-architecture-7-patterns.srt", "  vtt: agent-architecture-7-patterns.vtt", "",
        ]), encoding="utf-8")
    print(f"wrote {len(cues)} caption cues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
