"""Create deterministic navy/light-blue covers for the release package."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "publish-package" / "assets"
FONT = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def make_cover(size: tuple[int, int], name: str, portrait: bool) -> None:
    w, h = size
    im = Image.new("RGB", size, "#06182A")
    px = im.load()
    for y in range(h):
        for x in range(w):
            glow = max(0, 1 - (((x - w * 0.76) ** 2 + (y - h * 0.48) ** 2) ** 0.5) / (w * 0.85))
            px[x, y] = (6 + int(10 * glow), 24 + int(45 * glow), 42 + int(80 * glow))
    d = ImageDraw.Draw(im)
    for x in range(0, w, 80): d.line((x, 0, x, h), fill=(22, 52, 75), width=1)
    for y in range(0, h, 80): d.line((0, y, w, y), fill=(22, 52, 75), width=1)
    margin = 74 if not portrait else 60
    d.rounded_rectangle((margin, margin, w - margin, h - margin), radius=28, outline="#2F6C98", width=2)
    d.text((margin + 38, margin + 34), "AGENT ARCHITECTURE / COURSE LOOP", font=font(24 if not portrait else 20, True), fill="#8ED6FF")
    d.text((w - margin - 120, margin + 36), "01 / 05", font=font(22, True), fill="#FFD66F")
    d.rectangle((margin + 40, margin + 130, margin + 52, margin + (400 if not portrait else 520)), fill="#FFD66F")
    title_x = margin + 78
    title_y = margin + 142
    title_size = 78 if not portrait else 66
    d.text((title_x, title_y), "Agent系统", font=font(title_size, True), fill="#F7FBFF")
    d.text((title_x, title_y + title_size + 12), "主流7种架构", font=font(title_size, True), fill="#8ED6FF")
    d.text((title_x, title_y + 2 * title_size + 38), "从单 Agent 到 Graph Workflow", font=font(30 if not portrait else 26), fill="#B8C4D2")
    d.text((title_x, title_y + 2 * title_size + 88), "五章拆解 · 企业家实践视角", font=font(26 if not portrait else 24, True), fill="#FFD66F")
    if portrait:
        base_y = h - 620
        node_w, node_h = 350, 78
        labels = ["单 Agent", "ReAct", "Plan", "Multi-Agent", "Route + Skill", "Blackboard", "Graph Workflow"]
        for i, label in enumerate(labels):
            yy = base_y + i * 62
            xx = 120 + (i % 2) * 330
            if i >= 6: xx = 285
            d.rounded_rectangle((xx, yy, xx + node_w, yy + node_h), radius=18, outline="#8ED6FF" if i < 6 else "#FFD66F", width=3, fill="#0C2B49")
            d.text((xx + 26, yy + 19), label, font=font(27, True), fill="#F7FBFF" if i < 6 else "#FFD66F")
    else:
        cx, cy = int(w * 0.72), int(h * 0.60)
        labels = ["单 Agent", "ReAct", "Plan", "Multi", "Skill", "Graph"]
        pts = [(cx - 270, cy - 120), (cx - 90, cy - 120), (cx + 90, cy - 120), (cx - 180, cy + 30), (cx, cy + 30), (cx + 180, cy + 30)]
        for a, b in zip(pts, pts[1:]): d.line((a[0] + 75, a[1] + 34, b[0], b[1] + 34), fill="#8ED6FF", width=4)
        for (x, y), label in zip(pts, labels):
            d.rounded_rectangle((x, y, x + 150, y + 68), radius=18, outline="#FFD66F" if label == "Graph" else "#8ED6FF", width=3, fill="#0C2B49")
            d.text((x + 14, y + 18), label, font=font(24, True), fill="#FFD66F" if label == "Graph" else "#F7FBFF")
    d.text((margin + 40, h - margin - 58), "任务复杂度 × 控制力 · 选择最合适的架构", font=font(22), fill="#B8C4D2")
    OUT.mkdir(parents=True, exist_ok=True)
    im.save(OUT / name, optimize=True)


def main() -> int:
    make_cover((1600, 1200), "cover_4x3.png", False)
    make_cover((1200, 1600), "cover_3x4.png", True)
    print("covers written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
