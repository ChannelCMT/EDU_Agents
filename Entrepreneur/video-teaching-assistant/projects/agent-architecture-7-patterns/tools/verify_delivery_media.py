"""Verify final MP4 streams/duration and save transition frame evidence."""

from __future__ import annotations

from pathlib import Path

import av
import yaml


ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "publish-package" / "video" / "agent-architecture-7-patterns_final_subtitled.mp4"
EXPECTED = 177.319


def main() -> int:
    qa = ROOT / "publish-package" / "qa"
    qa.mkdir(parents=True, exist_ok=True)
    container = av.open(str(VIDEO))
    vs = container.streams.video[0]
    aus = container.streams.audio[0]
    duration = float(container.duration / 1_000_000)
    info = {
        "file": str(VIDEO.relative_to(ROOT)).replace("\\", "/"),
        "duration_seconds": round(duration, 3),
        "expected_duration_seconds": EXPECTED,
        "duration_delta_seconds": round(duration - EXPECTED, 3),
        "video": {"codec": vs.codec_context.name, "width": vs.width, "height": vs.height, "fps": float(vs.average_rate), "frames": int(vs.frames)},
        "audio": {"codec": aus.codec_context.name, "sample_rate": aus.rate, "channels": aus.codec_context.channels},
        "status": "pass" if abs(duration - EXPECTED) <= 0.5 and vs.width == 1920 and vs.height == 1080 and aus.codec_context.name == "aac" else "review",
    }
    yaml.safe_dump(info, (qa / "media-report.yaml").open("w", encoding="utf-8"), allow_unicode=True, sort_keys=False)
    # Save evidence at the start of each chapter and near the final decision card.
    for t in (0.5, 31.5, 64.5, 99.6, 132.8, 174.0):
        container.seek(int(t / vs.time_base), stream=vs)
        frame = next(container.decode(video=0), None)
        if frame is not None:
            frame.to_image().save(qa / f"frame_{t:06.1f}.jpg", quality=90)
    container.close()
    print(info)
    return 0 if info["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
