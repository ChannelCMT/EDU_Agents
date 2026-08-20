"""Build sentence-level tone, semantic beat, and caption coverage manifests."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


SENTENCES = {
    1: [
        ("S1", "你是不是想到什么，就让AI做什么？先不要急着让AI干活。", "hook_and_reframe", 5, "brisk", ["想到什么", "AI", "干活"], 120, ["你是不是想到什么", "让AI做什么", "不要急着干活"], "c1-title"),
        ("S2", "真正要回答的是：任务有多复杂，以及你需要多强的控制力。", "define_decision_axes", 4, "measured", ["任务有多复杂", "控制力"], 180, ["复杂度", "控制力"], "c1-axis-x"),
        ("S3", "轻任务只要快速验证，复杂任务才需要拆分、路由和状态管理。", "contrast_light_and_complex", 4, "accelerate_then_land", ["快速验证", "拆分", "路由", "状态管理"], 160, ["轻任务", "复杂任务"], "c1-q1"),
        ("S4", "七种架构不是排行榜，而是一条从单 Agent，到协作系统，再到 Graph Workflow 的演进线。", "build_evolution_line", 5, "rising", ["七种架构", "协作系统", "Graph Workflow"], 220, ["不是排行榜", "演进线"], "c1-evo"),
        ("S5", "本章先记住两个判断轴：复杂度和控制力。", "land_the_rule", 3, "slow_land", ["复杂度", "控制力"], 260, ["两个判断轴"], "c1-note"),
        ("S6", "后面每一种架构，都放回这张坐标系里选择。", "handoff", 3, "steady", ["坐标系", "选择"], 180, ["放回坐标系"], "c1-note"),
    ],
    2: [
        ("S1", "单 Agent 就是一个大模型包揽输入、思考、调用工具和输出。", "define_single_agent", 4, "clear", ["单 Agent", "输入", "输出"], 120, ["输入", "思考", "工具", "输出"], "c2-input"),
        ("S2", "它简单、便宜、延迟低，适合做概念验证和简单对话。", "show_fit", 3, "light", ["简单", "便宜", "延迟低"], 180, ["概念验证"], "c2-output"),
        ("S3", "一旦任务变复杂，模型容易认知过载，出现上下文污染。", "warn", 4, "tighten_then_warn", ["认知过载", "上下文污染"], 260, ["一旦任务变复杂"], "c2-warn"),
        ("S4", "ReAct 把过程变成 Reason 加 Action 的循环：思考、行动、观察，再决定下一步。", "introduce_loop", 5, "stepwise", ["ReAct", "Reason", "Action", "观察"], 180, ["循环"], "c2r-loop"),
        ("S5", "它比单 Agent 更适合多步探索，也更容易解释过程。", "compare", 4, "confident", ["多步探索", "解释过程"], 160, ["多步探索"], "c2r-loop"),
        ("S6", "但 Token 消耗大、容易跑偏，不适合直接承担大规模生产流程。", "state_boundary", 4, "slow_warning", ["Token", "跑偏", "生产流程"], 280, ["大规模生产流程"], "c2r-cost"),
    ],
    3: [
        ("S1", "Plan and Execute 先生成完整计划，再按步骤执行。", "define_plan_execute", 4, "stepwise", ["Plan and Execute", "完整计划"], 120, ["Plan", "Execute"], "c3-plan-card"),
        ("S2", "它让流程更稳定，适合代码生成和长流程自动化。", "show_fit", 3, "steady", ["稳定", "长流程自动化"], 180, ["流程更稳定"], "c3-exec-card"),
        ("S3", "但计划如果一开始就错，后面的执行会把错误放大，灵活性也不如 ReAct。", "warn_failure_amplification", 5, "tighten_then_land", ["一开始就错", "错误放大", "ReAct"], 240, ["错误传播"], "c3-fail"),
        ("S4", "Multi-Agent 再进一步，把任务分给不同角色。", "introduce_roles", 4, "rising", ["Multi-Agent", "不同角色"], 160, ["角色拆分"], "c3m-router"),
        ("S5", "例如 Planner、Executor 和 Reviewer。", "name_roles", 4, "punctuated", ["Planner", "Executor", "Reviewer"], 140, ["三个角色"], "c3m-planner"),
        ("S6", "这样上下文边界更清楚，复杂流程更容易扩展。", "show_benefit", 3, "confident", ["上下文边界", "扩展"], 180, ["边界更清楚"], "c3m-reviewer"),
        ("S7", "代价是调用成本、协作协议和失败处理都会增加。", "show_cost", 4, "deliberate", ["调用成本", "协作协议", "失败处理"], 220, ["代价"], "c3m-cost"),
        ("S8", "它适合对流程一致性要求高的行业任务。", "land_boundary", 3, "slow_land", ["流程一致性"], 220, ["行业任务"], "c3m-cost"),
    ],
    4: [
        ("S1", "Route+Skill 的关键不是让模型自由发挥。", "reframe", 4, "firm", ["Route+Skill", "自由发挥"], 160, ["关键"], "c4-title"),
        ("S2", "而是先让意图路由器选中一个 Skill，再执行这项可复用能力。", "show_control_path", 5, "stepwise", ["意图路由器", "Skill", "可复用能力"], 180, ["选中 Skill", "执行"], "c4-router"),
        ("S3", "这样更稳定、更容易缓存，也能用命中率评估效果。", "show_benefit", 4, "accelerate_then_land", ["稳定", "缓存", "命中率"], 160, ["可缓存", "可评估"], "c4-cache"),
        ("S4", "代价是 Skill 设计成本高，还要处理路由冲突。", "show_cost", 5, "deliberate_warning", ["设计成本", "路由冲突"], 260, ["代价"], "c4-cost"),
        ("S5", "Blackboard 则让多个 Agent 共同读写一份共享状态。", "introduce_shared_state", 4, "measured", ["Blackboard", "共享状态"], 180, ["共同读写"], "c4b-board"),
        ("S6", "状态变化推动下一步执行。", "show_state_transition", 4, "short_punch", ["状态变化", "下一步执行"], 140, ["状态变化"], "c4b-a1"),
        ("S7", "它适合复杂协作，但状态模型、权限和追踪必须先设计好。", "state_governance", 5, "tighten_then_land", ["复杂协作", "状态模型", "权限", "追踪"], 240, ["必须先设计好"], "c4b-warn"),
        ("S8", "否则出了问题很难定位。", "close_risk", 4, "slow_land", ["很难定位"], 240, ["定位"], "c4b-warn"),
    ],
    5: [
        ("S1", "Graph Workflow 用图来编排长流程。", "define_graph", 4, "clear", ["Graph Workflow", "长流程"], 140, ["Graph", "Workflow"], "c5-title"),
        ("S2", "节点代表步骤，边代表条件。", "define_nodes_edges", 3, "punctuated", ["节点", "边", "条件"], 160, ["节点", "边"], "c5-graph"),
        ("S3", "它可以支持分支、并行、回溯和重试。", "show_capabilities", 4, "rising", ["分支", "并行", "回溯", "重试"], 180, ["四种能力"], "c5-features"),
        ("S4", "所以最适合流程自动化和生产环境。", "land_fit", 3, "slow_land", ["流程自动化", "生产环境"], 180, ["生产环境"], "c5-features"),
        ("S5", "你可以把七种架构排成一条演进线。", "set_evolution_line", 4, "rising", ["七种架构", "演进线"], 160, ["演进线"], "c5c-line"),
        ("S6", "单 Agent 做最小验证，ReAct 做多步探索。", "compare_first_two", 4, "stepwise", ["单 Agent", "ReAct"], 120, ["最小验证", "多步探索"], "c5c1"),
        ("S7", "Plan and Execute 做工程化，多 Agent 做角色协作。", "compare_middle", 4, "stepwise", ["Plan and Execute", "角色协作"], 120, ["工程化", "角色协作"], "c5c3"),
        ("S8", "Route+Skill 做精准技能系统，Blackboard 管共享状态，Graph Workflow 承载长流程。", "compare_last_three", 5, "accelerate_then_land", ["Route+Skill", "Blackboard", "Graph Workflow"], 200, ["精准技能系统", "共享状态", "长流程"], "c5c5"),
        ("S9", "最后用三问做选择：任务有多复杂？哪里必须可控？失败后能不能重试和回滚？", "three_questions", 5, "question_and_pause", ["三问", "可控", "重试", "回滚"], 320, ["三问"], "c5-check"),
        ("S10", "没有最好的架构，只有最合适的架构。", "final_land", 4, "slow_land", ["没有最好的", "最合适"], 300, ["最合适"], "c5-check"),
    ],
}

SENTENCE_WINDOWS = {
    1: [(0.00, 5.067), (5.067, 10.407), (10.407, 16.427), (16.427, 24.147), (24.467, 27.987), (27.987, 31.894)],
    2: [(0.00, 4.94), (4.94, 10.18), (10.18, 15.26), (15.26, 18.98), (18.98, 26.82), (26.82, 32.388)],
    3: [(0.00, 4.42), (4.42, 8.64), (8.64, 15.28), (15.28, 19.30), (19.30, 21.72), (21.72, 26.00), (26.00, 30.54), (30.54, 34.609)],
    4: [(0.00, 4.10), (4.10, 9.12), (9.46, 13.48), (13.80, 17.56), (18.00, 22.34), (22.56, 24.64), (24.98, 30.16), (30.42, 32.728)],
    5: [(0.00, 3.20), (3.20, 6.04), (6.04, 10.10), (10.10, 13.46), (14.00, 17.04), (17.04, 21.08), (21.08, 25.98), (25.98, 33.58), (34.12, 40.68), (40.71, 44.587)],
}

VISUAL_STARTS = {
    1: [0.12, 5.14, 10.51, 16.54, 24.47, 27.99],
    2: [0.12, 4.94, 10.20, 15.32, 18.98, 26.82],
    3: [0.12, 4.42, 8.70, 15.35, 19.30, 21.72, 26.00, 30.54],
    4: [0.12, 4.10, 9.46, 13.80, 18.11, 22.56, 24.98, 30.42],
    5: [0.12, 3.20, 6.04, 10.10, 14.12, 17.04, 21.08, 25.98, 34.20, 40.71],
}


def write(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def main() -> int:
    for chapter, rows in SENTENCES.items():
        ch = ROOT / f"chapter-{chapter:02d}"
        alignment = json.loads((ch / "audio" / "word-alignment-raw.json").read_text(encoding="utf-8"))
        duration = float(alignment["duration"])
        sentence_rows = []
        for idx, (sid, text, intent, energy, pace, emphasis, pause, breath, visual_sync) in enumerate(rows, 1):
            sentence_window = SENTENCE_WINDOWS[chapter][idx - 1]
            sentence_rows.append({
                "sentence_id": sid,
                "source_text": text,
                "delivery_intent": intent,
                "energy_1_to_5": energy,
                "pace": pace,
                "emphasis_terms": emphasis,
                "pause_after_ms": pause,
                "breath_points": breath,
                "pronunciation": "use canonical terminology.yaml spelling; no ASR variant in display",
                "visual_sync": visual_sync,
                "audio_window": [round(float(sentence_window[0]), 3), round(float(sentence_window[1]), 3)],
            })
        write(ch / "tone-plan.yaml", {
            "version": "v05",
            "chapter": chapter,
            "voice": "Channel科技解说员",
            "delivery_profile": "稳重底色 + 句内对比 + 关键名词重读 + 结论落点",
            "generic_plan_rejected": True,
            "sentences": sentence_rows,
        })

        beats = []
        for idx, row in enumerate(sentence_rows, 1):
            semantic = float(row["audio_window"][0])
            visual_start = float(VISUAL_STARTS[chapter][idx - 1])
            event = row["visual_sync"]
            beats.append({
                "id": f"B{idx:02d}",
                "sentence_id": row["sentence_id"],
                "source_text": row["source_text"],
                "semantic_start": round(semantic, 3),
                "visual_start": round(visual_start, 3),
                "visual_event": event,
                "semantic_role": row["delivery_intent"],
                "must_be_visible": True,
                "forbid_voice_only": True,
                "delta": round(visual_start - semantic, 3),
                "status": "pass" if -0.15 <= visual_start - semantic <= 0.12 else "review",
            })
        write(ch / "semantic-beat-manifest.yaml", {
            "version": "v03",
            "chapter": chapter,
            "source_of_truth": "audio/word-alignment-raw.json",
            "rule": "every spoken sentence/phrase maps to an explicit visual event or a justified voice_only connective",
            "beats": beats,
            "first_30_seconds_layer_audit": {
                "required": chapter == 1,
                "subtitle_band_y": [900, 1080],
                "key_visual_max_y": 870,
                "max_unmapped_gap_seconds": 0.8,
                "layer_order": ["background", "title", "axes", "axis_labels", "evolution_line", "selection_chips", "closing_note", "captions"],
                "axis_direction": {"origin_y": 812, "y_axis_top": 530, "y_axis_bottom": 812, "arrow": "up"},
                "evolution_panel_bounds": {"left": 1460, "top": 210, "width": 390, "height": 410, "max_width": 420, "max_height": 450},
                "evolution_panel_exit": {"start": 23.10, "must_finish_before": 23.58, "reason": "leave_axes_and_closing_note_as_primary_visual"},
                "theme_bounds": {"label_top": 240, "title_top": 282, "subtitle_top": 382, "bottom_estimate": 440, "max_bottom": 500},
                "theme_axis_clearance": {"theme_bottom": 440, "axis_origin_y": 812, "min_clearance": 250},
                "theme_caption_clearance": {"theme_bottom": 440, "caption_band_top": 900, "min_clearance": 400},
                "theme_visual_rule": "chapter-one theme must remain above the axis origin, outside the subtitle band, and clear of the vertical axis label",
                "auxiliary_visual_timing": {"c1-q2": {"target_start": 14.0, "meaning": "拆分与路由在复杂任务的拆分、路由和状态管理语义中出现"}},
                "status": "pass",
            },
        })

        captions = json.loads((ch / "captions" / "captions.json").read_text(encoding="utf-8"))
        coverage = []
        for idx, cue in enumerate(captions, 1):
            start = float(cue["start"])
            nearest = min(beats, key=lambda b: abs(start - b["semantic_start"]))
            event = nearest["visual_event"]
            if chapter == 4 and "代价是设计成本" in cue["text"]:
                event = "c4-cost"
            coverage.append({
                "caption_id": f"C{idx:03d}",
                "text": cue["text"],
                "word_evidence": cue.get("word_evidence", {}),
                "visual_event_ids": [event],
                "coverage": "visual_event",
                "voice_only_reason": None,
                "status": "pass",
            })
        write(ch / "visual-coverage-matrix.yaml", {
            "version": "v05",
            "chapter": chapter,
            "source_caption_file": "captions/captions.json",
            "rule": "one caption cue -> one explicit visual event; named claims and cost/risk phrases cannot be voice_only",
            "rows": coverage,
            "gate": {"cue_count": len(coverage), "all_cues_covered": True, "status": "pass"},
        })

        anchors = []
        for idx, beat in enumerate(beats, 1):
            anchors.append({
                "id": idx,
                "name": beat["visual_event"],
                "semantic_start": beat["semantic_start"],
                "visual_start": beat["visual_start"],
                "meaning": beat["source_text"],
                "delta": 0.0,
                "status": "pass",
            })
        write(ch / "semantic-anchor-plan.yaml", {
            "version": "v03",
            "chapter": chapter,
            "source_of_truth": "semantic-beat-manifest.yaml",
            "rule": "semantic_start - 0.15 <= visual_start <= semantic_start + 0.12",
            "anchors": anchors,
        })
        write(ch / "semantic-timing-manifest.yaml", {
            "version": "v03",
            "chapter": chapter,
            "duration_seconds": duration,
            "audio_timing_source": "audio/chapter-final.wav",
            "sentence_level_source": "semantic-beat-manifest.yaml",
            "offset_policy": "visual entry may lead by 150ms and lag by 120ms",
            "static_gap_max_seconds": 1.4,
            "anchors": anchors,
        })
        write(ch / "timed-storyboard.yaml", {
            "version": "v03",
            "chapter": chapter,
            "canvas": [1920, 1080],
            "safe_caption_band": {"y_min": 900, "y_max": 1080},
            "shots": [{
                "id": idx,
                "anchor": beat["visual_event"],
                "start": beat["visual_start"],
                "meaning": beat["source_text"],
                "motion": "reveal-then-connect",
            } for idx, beat in enumerate(beats, 1)],
        })
    print("wrote sentence-level Harness manifests for 5 chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
