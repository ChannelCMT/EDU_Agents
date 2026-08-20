"""Encode captured HyperFrames JPEGs plus chapter WAV into an MP4 using PyAV."""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

import av
from PIL import Image


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    frame_paths = sorted(Path(args.frames).glob("frame_*.jpg"))
    if not frame_paths:
        raise SystemExit("no captured frames")
    audio_in = av.open(args.audio)
    audio_in_stream = audio_in.streams.audio[0]
    out = av.open(args.output, "w")
    video = out.add_stream("libx264", rate=args.fps)
    video.width, video.height = 1920, 1080
    video.pix_fmt = "yuv420p"
    video.options = {"preset": "fast", "crf": "20"}
    audio = out.add_stream("aac", rate=audio_in_stream.rate or 44100)
    audio.layout = "mono" if (audio_in_stream.channels or 1) == 1 else "stereo"
    audio_packets = []
    for frame in audio_in.decode(audio=0):
        for packet in audio.encode(frame):
            audio_packets.append(packet)
    audio_packets.extend(audio.encode(None))
    video_packets = []
    for i, frame_path in enumerate(frame_paths):
        with Image.open(frame_path) as image:
            vf = av.VideoFrame.from_image(image.convert("RGB"))
        vf.pts = i
        vf.time_base = Fraction(1, args.fps)
        video_packets.extend(video.encode(vf))
    video_packets.extend(video.encode(None))
    packets = video_packets + audio_packets
    # Mux order must follow DTS; sorting by PTS breaks H.264 B-frame ordering.
    packets.sort(key=lambda p: float(p.dts * p.time_base) if p.dts is not None and p.time_base else 0.0)
    for packet in packets:
        out.mux(packet)
    out.close()
    audio_in.close()
    print(f"encoded {len(frame_paths)} frames -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
