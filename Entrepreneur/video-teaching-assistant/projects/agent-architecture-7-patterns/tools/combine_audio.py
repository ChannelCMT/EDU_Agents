"""Combine Fish Audio segments into one mono WAV with a controlled pause."""

from __future__ import annotations

import argparse
import wave
from pathlib import Path

import av


def decode_pcm(path: Path, sample_rate: int) -> bytes:
    container = av.open(str(path))
    stream = next(s for s in container.streams if s.type == "audio")
    resampler = av.audio.resampler.AudioResampler(format="s16", layout="mono", rate=sample_rate)
    chunks: list[bytes] = []
    for frame in container.decode(stream):
        for converted in resampler.resample(frame):
            chunks.append(converted.to_ndarray().tobytes())
    return b"".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("segments", nargs="+", type=Path)
    parser.add_argument("--gap-ms", type=int, default=180)
    parser.add_argument("--sample-rate", type=int, default=48_000)
    args = parser.parse_args()

    silence = b"\x00\x00" * int(args.sample_rate * args.gap_ms / 1000)
    pcm: list[bytes] = []
    for index, segment in enumerate(args.segments):
        pcm.append(decode_pcm(segment, args.sample_rate))
        if index != len(args.segments) - 1:
            pcm.append(silence)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.output), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(args.sample_rate)
        for chunk in pcm:
            wav.writeframes(chunk)
    print(f"wrote {args.output} ({args.output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

