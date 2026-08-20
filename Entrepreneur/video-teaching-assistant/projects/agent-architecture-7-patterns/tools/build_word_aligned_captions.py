"""Build exact caption text from the approved script and raw word timings."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


# (display text, target audio start, target audio end). Targets select raw words;
# final cue seconds are always snapped to the selected word evidence.
CUE_PLANS = {
    1: [
        ("你是不是想到什么，就让AI做什么？", 0.000, 2.951), ("先不要急着让AI干活", 2.951, 5.067),
        ("真正要回答的是", 5.067, 6.807), ("任务有多复杂", 7.227, 8.307), ("以及你需要多强的控制力", 8.567, 10.407),
        ("轻任务只要快速验证", 10.407, 12.507), ("复杂任务才需要拆分", 12.807, 14.407), ("路由和状态管理", 14.647, 16.427),
        ("七种架构不是排行榜", 16.427, 18.447), ("而是一条从单 Agent", 18.727, 20.227), ("到协作系统", 20.227, 21.647),
        ("再到 Graph Workflow", 21.647, 23.287), ("的演进线", 23.287, 24.147), ("本章先记住两个判断轴", 24.467, 26.247),
        ("复杂度和控制力", 26.627, 27.987), ("后面每一种架构都放回", 27.987, 30.047), ("这张坐标系里选择", 30.047, 31.527),
    ],
    2: [
        ("单 Agent", 0.00, 0.60), ("就是一个大模型", 0.60, 1.88), ("包揽输入、思考", 1.88, 3.40),
        ("调用工具和输出", 3.60, 4.94), ("它简单、便宜", 4.94, 6.52), ("延迟低", 6.78, 7.34),
        ("适合做概念验证", 7.76, 9.12), ("和简单对话", 9.12, 10.18), ("一旦任务变复杂", 10.18, 11.76),
        ("模型容易认知过载", 12.08, 13.62), ("出现上下文污染", 13.94, 15.26), ("ReAct 把过程变成", 15.26, 17.14),
        ("Reason 加 Action", 17.14, 18.36), ("的循环：思考、行动", 18.36, 20.46), ("观察，再决定下一步", 20.72, 22.52),
        ("它比单 Agent 更", 22.52, 23.72), ("适合多步探索", 23.72, 25.00), ("也更容易解释过程", 25.34, 26.82),
        ("但 Token 消耗大", 26.82, 28.28), ("容易跑偏", 28.28, 29.18), ("不适合直接承担", 29.46, 30.74),
        ("大规模生产流程", 30.74, 31.96),
    ],
    3: [
        ("Plan and", 0.00, 0.62), ("Execute 先生成完整计划", 0.62, 3.06), ("再按步骤执行", 3.06, 4.42),
        ("它让流程更稳定", 4.42, 6.00), ("适合代码生成", 6.30, 7.32), ("和长流程自动化", 7.32, 8.64),
        ("但计划一开始就错", 8.64, 10.84), ("后面的执行会把", 11.24, 12.50), ("把错误放大", 12.50, 13.40),
        ("灵活性也不如 ReAct", 13.40, 15.28), ("Multi-Agent", 15.28, 16.66), ("再进一步把任务", 16.90, 18.22),
        ("分给不同角色", 18.22, 19.30), ("例如 Planner", 19.30, 20.28), ("Executor 和", 20.58, 21.00),
        ("Reviewer", 21.28, 21.72), ("这样上下文边界", 21.72, 23.16), ("更清楚，复杂流程", 23.16, 25.10),
        ("更容易扩展", 25.10, 26.00), ("代价是调用成本", 26.00, 27.66), ("协作协议", 28.04, 28.36),
        ("和失败处理都会增加", 28.36, 30.54), ("它适合对流程一致性", 30.54, 32.52), ("要求高的行业任务", 32.52, 34.04),
    ],
    4: [
        ("Route+Skill的关键", 0.00, 1.84), ("不是让模型自由发挥", 1.84, 3.48), ("而是先让意图路由器", 3.78, 5.44),
        ("选中一个 Skill", 5.44, 6.52), ("再执行这项可复用能力", 6.94, 9.12), ("这样更稳定、更容易缓存", 9.46, 11.34),
        ("也能用命中率评估效果", 11.64, 13.48), ("代价是 Skill 设计成本高", 13.80, 15.80), ("还要处理路由冲突", 16.16, 17.56),
        ("Blackboard", 18.00, 18.78), ("则让多个 Agent", 19.18, 20.24), ("共同读写一份共享状态", 20.24, 22.34),
        ("状态变化推动下一步", 22.56, 23.96), ("执行，它适合复杂协作", 24.20, 26.26), ("但状态模型、权限和追踪", 26.58, 29.02),
        ("必须先设计好", 29.02, 30.16), ("否则出了问题很难定位", 30.42, 32.18),
    ],
    5: [
        ("Graph Workflow", 0.00, 1.00), ("用图来编排长流程", 1.50, 3.20), ("节点代表步骤", 3.20, 4.80),
        ("边代表条件", 5.12, 6.04), ("它可以支持分支", 6.04, 7.98), ("并行、回溯和重试", 8.26, 10.10),
        ("所以最适合流程", 10.10, 11.92), ("自动化和生产环境", 11.92, 13.46), ("你可以把七种架构", 14.00, 15.68),
        ("排成一条演进线", 15.68, 17.04), ("单 Agent 做最小验证", 17.04, 18.96), ("ReAct 做多步探索", 18.96, 21.08),
        ("Plan and", 21.08, 22.04), ("Execute 做工程化", 22.04, 23.90), ("Multi-Agent", 23.90, 24.76),
        ("做角色协作", 24.96, 25.98), ("Route+Skill", 25.98, 27.14), ("做精准技能系统", 27.50, 28.80),
        ("Blackboard", 28.80, 29.70), ("管共享状态", 30.00, 31.06), ("Graph Workflow", 31.34, 32.22),
        ("承载长流程", 32.54, 33.58), ("最后用三问做选择", 34.12, 35.74), ("任务有多复杂", 36.24, 37.36),
        ("哪里必须可控", 37.62, 38.64), ("失败后能不能", 38.96, 39.92), ("重试和回滚", 39.92, 41.04),
        ("没有最好的架构", 41.38, 42.28), ("只有最合适的架构", 42.74, 44.26),
    ],
}


def select_words(words: list[dict], start: float, end: float) -> list[dict]:
    # Select by word start, not interval overlap. A preceding word can end a
    # few microseconds after a target boundary because of ASR rounding; taking
    # it would silently shift the next cue to the wrong phrase.
    selected = [w for w in words if start - 0.001 <= float(w.get("start", 0)) < end]
    return selected or [min(words, key=lambda w: abs(float(w.get("start", 0)) - start))]


def absolute_words(alignment: dict) -> list[dict]:
    """Flatten words while correcting segment-local timestamps.

    Fish Audio's replacement line in chapter 1 is returned with word times
    relative to that segment, while the surrounding segments use absolute
    project time. Normalize only the anomalous local segment so the first two
    cues cannot be selected from the wrong line.
    """
    out: list[dict] = []
    for segment in alignment.get("segments", []):
        segment_start = float(segment.get("start", 0.0))
        segment_end = float(segment.get("end", segment_start))
        segment_words = [
            dict(word)
            for word in segment.get("words", [])
            if word.get("start") is not None and word.get("end") is not None
        ]
        if not segment_words:
            continue
        first = float(segment_words[0]["start"])
        last = float(segment_words[-1]["end"])
        segment_duration = max(0.0, segment_end - segment_start)
        is_local = (
            segment_start > 0.25
            and first < segment_start - 0.25
            and last <= segment_duration + 0.25
        )
        if is_local:
            for word in segment_words:
                word["start"] = round(float(word["start"]) + segment_start, 6)
                word["end"] = round(float(word["end"]) + segment_start, 6)
        out.extend(segment_words)
    return out


def build_chapter(chapter: int) -> list[dict]:
    ch = ROOT / f"chapter-{chapter:02d}"
    alignment = json.loads((ch / "audio" / "word-alignment-raw.json").read_text(encoding="utf-8"))
    words = absolute_words(alignment)
    duration = float(alignment["duration"])
    out = []
    cursor = 0
    for idx, (text, target_start, target_end) in enumerate(CUE_PLANS[chapter], 1):
        selected = select_words(words, target_start, target_end)
        word_start = float(selected[0]["start"])
        word_end = float(selected[-1]["end"])
        start = max(0.0, word_start - 0.05)
        end = min(duration, word_end + 0.05)
        if out and start <= cursor:
            start = min(duration, cursor + 0.01)
        if end <= start:
            end = min(duration, start + 0.08)
        out.append({
            "id": f"C{idx:03d}",
            "text": text,
            "start": round(start, 3),
            "end": round(end, 3),
            "timing_method": "word_alignment",
            "word_evidence": {
                "source": "audio/word-alignment-raw.json",
                "timebase": "global",
                "word_start": round(word_start, 3),
                "word_end": round(word_end, 3),
                "raw_words": [str(w.get("word", "")) for w in selected],
                "target_window": [target_start, target_end],
            },
            "alignment_error_ms": 50,
        })
        cursor = end
    return out


def main() -> int:
    for chapter in range(1, 6):
        captions = build_chapter(chapter)
        path = ROOT / f"chapter-{chapter:02d}" / "captions" / "captions.json"
        path.write_text(json.dumps(captions, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"chapter-{chapter:02d}: {len(captions)} word-aligned cues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
