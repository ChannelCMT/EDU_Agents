"""Merge chapter MP4s with 500ms visual separators and the canonical narration WAV."""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

import av
import numpy as np


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", nargs=5, required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--gap-frames", type=int, default=15)
    args = ap.parse_args()

    out = av.open(args.output, "w")
    video = out.add_stream("libx264", rate=args.fps)
    video.width, video.height = 1920, 1080
    video.pix_fmt = "yuv420p"
    video.options = {"preset": "fast", "crf": "20"}
    audio = out.add_stream("aac", rate=48000)
    audio.layout = "mono"

    video_packets = []
    video_index = 0
    blank = np.zeros((1080, 1920, 3), dtype=np.uint8)
    for index, chapter_path in enumerate(args.chapters):
        container = av.open(chapter_path)
        for frame in container.decode(video=0):
            vf = av.VideoFrame.from_ndarray(frame.to_ndarray(format="rgb24"), format="rgb24")
            vf.pts = video_index
            vf.time_base = Fraction(1, args.fps)
            video_packets.extend(video.encode(vf))
            video_index += 1
        container.close()
        if index < len(args.chapters) - 1:
            for _ in range(args.gap_frames):
                vf = av.VideoFrame.from_ndarray(blank, format="rgb24")
                vf.pts = video_index
                vf.time_base = Fraction(1, args.fps)
                video_packets.extend(video.encode(vf))
                video_index += 1
    video_packets.extend(video.encode(None))

    audio_packets = []
    audio_in = av.open(args.audio)
    for frame in audio_in.decode(audio=0):
        audio_packets.extend(audio.encode(frame))
    audio_packets.extend(audio.encode(None))
    audio_in.close()

    packets = video_packets + audio_packets
    packets.sort(key=lambda p: float(p.dts * p.time_base) if p.dts is not None and p.time_base else 0.0)
    for packet in packets:
        out.mux(packet)
    out.close()
    print(f"merged {video_index} video frames and {len(audio_packets)} audio packets -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
