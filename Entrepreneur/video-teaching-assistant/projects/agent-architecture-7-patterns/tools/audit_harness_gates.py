"""Run the new source-level Harness gates and write an evidence report."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from audit_caption_alignment import audit_chapter as audit_caption_chapter
from audit_rendered_layout import audit_chapter as audit_layout_chapter


ROOT = Path(__file__).resolve().parents[1]

# A chapter may contain multiple full-canvas sections. Secondary sections must
# start hidden and be explicitly revealed at their semantic start; otherwise
# labels/titles from the next section sit on top of the current one.
SECTION_GATES = {
    2: [("c2-single", "c2-react", 15.260)],
    3: [("c3-plan", "c3-multi", 15.749)],
    4: [("c4-route", "c4-board", 18.126)],
    5: [("c5-graph", "c5-choice", 13.999)],
}


def run() -> dict:
    chapters = []
    for number in range(1, 6):
        ch = ROOT / f"chapter-{number:02d}"
        html = (ch / "index.html").read_text(encoding="utf-8")
        captions = json.loads((ch / "captions" / "captions.json").read_text(encoding="utf-8"))
        beats = yaml.safe_load((ch / "semantic-beat-manifest.yaml").read_text(encoding="utf-8"))
        coverage = yaml.safe_load((ch / "visual-coverage-matrix.yaml").read_text(encoding="utf-8"))
        failures = []
        failures.extend(f"caption_alignment:{failure}" for failure in audit_caption_chapter(ch))
        failures.extend(f"rendered_layout:{failure}" for failure in audit_layout_chapter(ch))
        if not all(c.get("timing_method") == "word_alignment" and c.get("word_evidence") for c in captions):
            failures.append("caption_timing_not_word_aligned")
        if len(coverage.get("rows", [])) != len(captions):
            failures.append("caption_visual_coverage_count_mismatch")
        for beat in beats.get("beats", []):
            delta = float(beat["visual_start"]) - float(beat["semantic_start"])
            if not -0.15 <= delta <= 0.12:
                failures.append(f"semantic_window:{beat['id']}")
            if f'id="{beat["visual_event"]}"' not in html:
                failures.append(f"missing_visual_object:{beat['visual_event']}")
        for previous_id, next_id, start in SECTION_GATES.get(number, []):
            next_match = re.search(rf'<section id="{re.escape(next_id)}"[^>]*>', html)
            if not next_match or 'style="opacity:0"' not in next_match.group(0):
                failures.append(f"section_not_hidden:{next_id}")
            reveal = re.search(rf'tl\.fromTo\("#{re.escape(next_id)}"[^;]*,\s*{start:.3f}\)', html)
            hide = re.search(rf'tl\.to\("#{re.escape(previous_id)}"[^;]*,\s*{start:.3f}\)', html)
            if not reveal:
                failures.append(f"section_reveal_not_timeline_bound:{next_id}")
            if not hide:
                failures.append(f"previous_section_not_hidden:{previous_id}")
        if number == 1:
            script_text = (ch / "SCRIPT.md").read_text(encoding="utf-8")
            opening_window = script_text[:260]
            normalized_opening = re.sub(r"\s+", "", opening_window)
            if "你是不是想到什么" not in normalized_opening or not re.search(r"先不要急着让AI干活", normalized_opening):
                failures.append("opening_hook_missing")
            if any(term in opening_window for term in ("ReAct", "Multi-Agent")):
                failures.append("opening_hook_uses_unintroduced_architecture_term")
            if 'data-subtitle-safe-band="900-1080"' not in html:
                failures.append("subtitle_safe_band_not_declared_on_root")
            if "拆分与路由" not in html:
                failures.append("chapter1_split_route_visual_missing")
            if 'id="c1-q3"' in html or "长流程生产" in html:
                failures.append("chapter1_removed_visual_still_present")
            if not all(f'id="c1-evo-{idx}"' in html for idx in range(1, 8)):
                failures.append("chapter1_seven_model_list_incomplete")
            audit = beats.get("first_30_seconds_layer_audit", {})
            if audit.get("status") != "pass":
                failures.append("first_30_layer_audit")
            theme = audit.get("theme_bounds", {})
            theme_label = re.search(r'class="section-label"[^>]*style="[^"]*top:(\d+)px[^"]*">SELECTION COORDINATES', html)
            theme_title = re.search(r'id="c1-title"[^>]*style="[^"]*top:(\d+)px', html)
            theme_sub = re.search(r'id="c1-sub"[^>]*style="[^"]*top:(\d+)px', html)
            if not theme_label or int(theme_label.group(1)) > int(theme.get("label_top", 260)):
                failures.append("c1_theme_label_too_low")
            if not theme_title or int(theme_title.group(1)) > int(theme.get("title_top", 300)):
                failures.append("c1_theme_title_too_low")
            if not theme_sub or int(theme_sub.group(1)) > int(theme.get("subtitle_top", 410)):
                failures.append("c1_theme_subtitle_too_low")
            theme_bottom = int(theme.get("bottom_estimate", 500))
            axis_origin = int(audit.get("axis_direction", {}).get("origin_y", 812))
            min_axis_clearance = int(audit.get("theme_axis_clearance", {}).get("min_clearance", 180))
            if theme_bottom + min_axis_clearance > axis_origin:
                failures.append("c1_theme_axis_clearance_below_minimum")
            caption_top = int(audit.get("subtitle_band_y", [900, 1080])[0])
            min_caption_clearance = int(audit.get("theme_caption_clearance", {}).get("min_clearance", 260))
            if theme_bottom + min_caption_clearance > caption_top:
                failures.append("c1_theme_caption_clearance_below_minimum")
            # This is the layer that previously sat inside the caption band.
            note = re.search(r'id="c1-note"[^>]*style="[^"]*top:(\d+)px', html)
            if not note or int(note.group(1)) >= 870:
                failures.append("c1_note_enters_caption_band")
            axis = re.search(r'id="c1-axis-y"[^>]*style="[^"]*top:(\d+)px;height:(\d+)px', html)
            if not axis or int(axis.group(1)) + int(axis.group(2)) > 812 or int(axis.group(1)) >= 812:
                failures.append("c1_y_axis_direction_down")
            if ".axis.y::after" not in html and ".axis.y::after" not in (ROOT.parent / "tools" / "build_hyperframes.py").read_text(encoding="utf-8"):
                failures.append("c1_y_axis_arrow_missing")
            panel = re.search(r'id="c1-evo"[^>]*style="[^"]*left:(\d+)px;top:(\d+)px;width:(\d+)px;height:(\d+)px', html)
            if not panel or int(panel.group(3)) > 420 or int(panel.group(4)) > 450:
                failures.append("c1_evolution_panel_too_large")
            if 'tl.to("#c1-evo"' not in html or not any(mark in html for mark in ('23.10', '24.53', '23.99')):
                failures.append("c1_evolution_panel_exit_missing")
            q2 = re.search(r'tl\.fromTo\("#c1-q2"[^;]*\},\s*([0-9.]+)\)', html)
            q2_target = float(audit.get("auxiliary_visual_timing", {}).get("c1-q2", {}).get("target_start", 14.0))
            if not q2 or abs(float(q2.group(1)) - q2_target) > 0.01:
                failures.append("c1_q2_timing_not_14s")
        if number == 4:
            if 'id="c4-cost"' not in html:
                failures.append("missing_cost_animation")
            if 'c4-cost", {opacity:0' not in html:
                failures.append("cost_animation_not_timeline_bound")
        chapters.append({
            "chapter": number,
            "caption_count": len(captions),
            "beat_count": len(beats.get("beats", [])),
            "coverage_count": len(coverage.get("rows", [])),
            "failures": failures,
            "status": "pass" if not failures else "fail",
        })
    return {
        "version": "v06",
        "source_of_truth": ["audio/word-alignment-raw.json", "semantic-beat-manifest.yaml", "visual-coverage-matrix.yaml"],
        "root_causes_addressed": [
            "proportional_caption_timing_replaced_by_word_evidence",
            "sentence_level_visual_coverage_added",
            "first_30_second_layer_audit_added",
            "route_skill_design_cost_has_explicit_c4_cost_animation",
            "tone_plan_is_sentence_level_and_non_generic",
            "multi_scene_previous_exit_and_next_entry_are_explicit",
            "caption_panel_uses_single_line_translucent_safe_band",
            "chapter_one_y_axis_points_up_and_stays_inside_canvas",
            "chapter_one_evolution_panel_is_compact_and_exits_before_closing_note",
            "chapter_one_theme_group_is_above_axes_and_caption_band",
            "chapter_one_theme_group_has_explicit_visual_clearance_bounds",
        ],
        "chapters": chapters,
        "status": "pass" if all(row["status"] == "pass" for row in chapters) else "fail",
    }


def main() -> int:
    report = run()
    path = ROOT / "content" / "harness-audit-v06.yaml"
    path.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(yaml.safe_dump(report, allow_unicode=True, sort_keys=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
