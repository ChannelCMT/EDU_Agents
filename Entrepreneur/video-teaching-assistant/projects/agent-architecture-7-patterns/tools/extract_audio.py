"""Extract the first audio stream from a local MP4 using PyAV."""

from __future__ import annotations

import argparse
import wave
from pathlib import Path

import av


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    container = av.open(str(args.source))
    audio = next((stream for stream in container.streams if stream.type == "audio"), None)
    if audio is None:
        raise SystemExit("source has no audio stream")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sample_rate = 16_000
    channels = 1
    resampler = av.audio.resampler.AudioResampler(
        format="s16", layout="mono", rate=sample_rate
    )
    with wave.open(str(args.output), "wb") as wav:
        wav.setnchannels(channels)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for frame in container.decode(audio):
            for converted in resampler.resample(frame):
                wav.writeframes(converted.to_ndarray().tobytes())

    print(f"wrote {args.output} ({args.output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

