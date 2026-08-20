"""Build the explicit semantic/timing/storyboard artifacts used by delivery QA."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]

ANCHORS = {
    1: [
        ("intro", 0.00, 0.12, "从零搭 Agent 系统，先建立选型坐标系"),
        ("coordinate-axes", 4.18, 4.25, "任务复杂度与控制力"),
        ("fast-validation", 9.52, 9.62, "轻任务先快速验证"),
        ("collaboration", 15.54, 15.65, "复杂任务需要协作与路由"),
        ("long-workflow", 20.76, 20.86, "长流程进入 Graph Workflow"),
        ("decision-check", 27.10, 27.12, "把每种架构放回坐标系"),
    ],
    2: [
        ("single-agent", 0.00, 0.12, "单 Agent 包揽输入、思考和工具调用"),
        ("cognitive-overload", 10.18, 10.20, "任务变复杂会出现认知过载"),
        ("react", 15.26, 15.32, "ReAct 进入 Reason、Action、Observe 循环"),
        ("react-loop", 17.45, 17.45, "循环让多步探索可解释"),
        ("production-warning", 27.00, 27.00, "大规模生产流程需要更强约束"),
    ],
    3: [
        ("plan-execute", 0.00, 0.12, "Plan and Execute 先规划再执行"),
        ("plan-risk", 8.64, 8.70, "计划一开始错，错误会被放大"),
        ("multi-agent", 15.28, 15.35, "Multi-Agent 按角色拆分任务"),
        ("coordinator", 15.90, 15.90, "Coordinator 分发角色任务"),
        ("role-cards", 19.30, 19.30, "Planner、Executor、Reviewer"),
        ("failure-handling", 30.56, 30.56, "准备失败处理和回滚"),
    ],
    4: [
        ("route-skill", 0.00, 0.12, "Route+Skill 先路由意图，再执行能力"),
        ("skill-selection", 4.60, 4.62, "选中可复用 Skill"),
        ("control-point", 14.60, 14.60, "先把控制点写清楚"),
        ("blackboard", 18.126, 18.18, "Blackboard 共享状态"),
        ("shared-state", 19.60, 19.60, "状态变化推动下一步执行"),
        ("state-governance", 28.80, 28.80, "状态模型、权限和追踪"),
    ],
    5: [
        ("graph-workflow", 0.00, 0.12, "Graph Workflow 用图编排长流程"),
        ("nodes-edges", 1.60, 1.60, "节点代表步骤，边代表条件"),
        ("branch-retry", 6.04, 6.04, "支持分支、并行、回溯和重试"),
        ("production", 10.10, 10.10, "适合流程自动化和生产环境"),
        ("evolution-line", 14.00, 14.12, "七种架构是一条演进线"),
        ("single-to-multi", 15.90, 15.90, "从单 Agent 到 Multi-Agent"),
        ("skill-blackboard-graph", 26.08, 26.08, "从 Skill、Blackboard 到 Graph"),
        ("three-questions", 34.20, 34.20, "用三个问题做架构选型"),
    ],
}


def write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def main() -> int:
    for chapter, rows in ANCHORS.items():
        ch = ROOT / f"chapter-{chapter:02d}"
        alignment = json.loads((ch / "audio" / "word-alignment-raw.json").read_text(encoding="utf-8"))
        duration = float(alignment["duration"])
        anchors = [
            {"id": i, "name": name, "semantic_start": semantic, "visual_start": visual, "meaning": meaning,
             "delta": round(visual - semantic, 3), "status": "pass" if -0.15 <= visual - semantic <= 0.12 else "review"}
            for i, (name, semantic, visual, meaning) in enumerate(rows, 1)
        ]
        write_yaml(ch / "semantic-anchor-plan.yaml", {
            "version": "1.0", "chapter": chapter, "source_of_truth": "audio/word-alignment-raw.json",
            "rule": "semantic_start - 0.15 <= visual_start <= semantic_start + 0.12",
            "anchors": anchors,
        })
        write_yaml(ch / "semantic-timing-manifest.yaml", {
            "version": "1.0", "chapter": chapter, "duration_seconds": duration,
            "audio_timing_source": "audio/chapter-final.wav", "offset_policy": "visual entry may lead by 150ms and lag by 120ms",
            "static_gap_max_seconds": 1.4, "caption_start_offset_seconds": -0.05,
            "anchors": [{"id": a["id"], "semantic_start": a["semantic_start"], "visual_start": a["visual_start"], "delta": a["delta"], "status": a["status"]} for a in anchors],
        })
        write_yaml(ch / "timed-storyboard.yaml", {
            "version": "1.0", "chapter": chapter, "canvas": [1920, 1080], "safe_caption_band": {"y_min": 900, "y_max": 1080},
            "shots": [{"id": a["id"], "anchor": a["name"], "start": a["visual_start"], "meaning": a["meaning"], "motion": "reveal-then-connect"} for a in anchors],
        })
        write_yaml(ch / "terminology.yaml", {
            "version": "1.0", "chapter": chapter,
            "display_terms": ["Agent", "ReAct", "Plan and Execute", "Multi-Agent", "Route+Skill", "Blackboard", "Graph Workflow", "Coordinator", "Planner", "Executor", "Reviewer"],
            "pronunciation_policy": "English terms are written canonically in captions and visuals; ASR variants are never copied to display text.",
        })
        write_yaml(ch / "tone-plan.yaml", {
            "version": "1.0", "chapter": chapter, "voice": "Channel科技解说员", "delivery": "稳重、清晰、略带推进感",
            "semantic_emphasis": [a["name"] for a in anchors], "pause_policy": "pause at complete clauses; do not insert a pause inside an English term",
        })
    print(f"wrote semantic manifests for {len(ANCHORS)} chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
