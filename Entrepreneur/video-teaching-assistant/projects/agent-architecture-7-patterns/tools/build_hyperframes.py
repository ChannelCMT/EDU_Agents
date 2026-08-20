"""Generate deterministic HyperFrames compositions for the five chapters."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


COMMON_CSS = r"""
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #06182A; color: #F7FBFF; font-family: "Microsoft YaHei", "Noto Sans SC", sans-serif; }
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #06182A; }
.clip { position: absolute; inset: 0; display: block; overflow: hidden; }
.fill { position: absolute; inset: 0; background: #06182A; }
.grid { position: absolute; inset: 0; opacity: .09; background-image: linear-gradient(rgba(142,214,255,.32) 1px, transparent 1px), linear-gradient(90deg, rgba(142,214,255,.32) 1px, transparent 1px); background-size: 80px 80px; mask-image: linear-gradient(to bottom, rgba(0,0,0,.8), transparent 88%); }
.glow { position: absolute; border-radius: 50%; filter: blur(10px); }
.glow.a { width: 720px; height: 720px; left: -220px; top: -280px; background: radial-gradient(circle, rgba(45,124,196,.28), transparent 70%); }
.glow.b { width: 680px; height: 680px; right: -240px; bottom: -260px; background: radial-gradient(circle, rgba(44,101,162,.24), transparent 72%); }
.topbar { position: absolute; left: 76px; right: 76px; top: 50px; display: flex; justify-content: space-between; align-items: center; color: #B8C4D2; font-size: 22px; letter-spacing: .12em; text-transform: uppercase; }
.eyebrow { color: #8ED6FF; font-weight: 700; }
.chapter-no { color: #FFD66F; font-weight: 700; }
.rule { position: absolute; left: 76px; right: 76px; top: 104px; height: 2px; background: rgba(142,214,255,.35); transform-origin: left center; }
.title { position: absolute; left: 96px; top: 142px; max-width: 1250px; font-size: 76px; line-height: 1.08; font-weight: 800; letter-spacing: -.025em; }
.subtitle { position: absolute; left: 100px; top: 240px; color: #B8C4D2; font-size: 30px; line-height: 1.3; }
.section-label { position: absolute; color: #8ED6FF; font-size: 24px; letter-spacing: .08em; font-weight: 700; }
.panel { position: absolute; border: 2px solid rgba(142,214,255,.5); border-radius: 24px; background: rgba(10,47,78,.86); box-shadow: 0 20px 50px rgba(0,0,0,.28); }
.panel.warm { border-color: rgba(255,214,111,.62); }
.panel.alert { border-color: rgba(255,152,152,.66); background: rgba(74,30,47,.78); }
.panel.green { border-color: rgba(160,230,191,.65); background: rgba(22,65,70,.78); }
.panel-title { color: #F7FBFF; font-size: 34px; font-weight: 750; }
.panel-copy { color: #B8C4D2; font-size: 25px; line-height: 1.38; white-space: pre-line; }
.node { position: absolute; display: flex; align-items: center; justify-content: center; border-radius: 999px; border: 3px solid #8ED6FF; color: #F7FBFF; background: #0C2B49; font-size: 27px; font-weight: 750; box-shadow: 0 12px 24px rgba(0,0,0,.25); }
.node.hot { border-color: #FFD66F; color: #FFD66F; }
.node.done { border-color: #A0E6BF; color: #A0E6BF; }
.arrow { position: absolute; height: 4px; background: #8ED6FF; transform-origin: left center; border-radius: 2px; }
.arrow::after { content: ""; position: absolute; right: -2px; top: -7px; border-left: 15px solid #8ED6FF; border-top: 9px solid transparent; border-bottom: 9px solid transparent; }
.chip { position: absolute; padding: 14px 22px; border-radius: 14px; border: 2px solid rgba(142,214,255,.48); color: #F7FBFF; background: rgba(12,43,73,.88); font-size: 24px; font-weight: 700; }
.chip.hot { color: #FFD66F; border-color: rgba(255,214,111,.68); }
.chip.gray { color: #B8C4D2; border-color: rgba(184,196,210,.44); }
.metric { position: absolute; color: #8ED6FF; font-family: "JetBrains Mono", monospace; font-size: 22px; letter-spacing: .08em; }
.caption { position: absolute; top: auto; left: 220px; right: 220px; bottom: 46px; height: 76px; display: flex; align-items: center; justify-content: center; padding: 0 28px; border-radius: 16px; border: 2px solid rgba(142,214,255,.48); background: rgba(12,43,73,.72); color: #FFFFFF; font-size: 36px; font-weight: 650; white-space: nowrap; text-align: center; box-shadow: 0 10px 26px rgba(0,0,0,.22); }
.caption span { display: block; }
.caption-safe-line { position: absolute; left: 76px; right: 76px; bottom: 150px; height: 2px; background: rgba(184,196,210,.15); }
.small-note { position: absolute; color: #B8C4D2; font-size: 22px; }
.axis { position: absolute; background: rgba(142,214,255,.66); transform-origin: left center; }
.axis.x { height: 3px; }
.axis.y { width: 3px; transform-origin: center bottom; }
.axis.x::after { content: ""; position: absolute; right: -2px; top: -7px; border-left: 15px solid rgba(142,214,255,.66); border-top: 9px solid transparent; border-bottom: 9px solid transparent; }
.axis.y::after { content: ""; position: absolute; left: -7px; top: -15px; border-bottom: 15px solid rgba(142,214,255,.66); border-left: 9px solid transparent; border-right: 9px solid transparent; }
.axis-label { position: absolute; color: #B8C4D2; font-size: 24px; font-weight: 700; }
.loop { position: absolute; border: 4px solid #8ED6FF; border-radius: 50%; }
.loop-arrow { position: absolute; width: 0; height: 0; border-left: 20px solid #FFD66F; border-top: 12px solid transparent; border-bottom: 12px solid transparent; }
.state-line { position: absolute; height: 2px; background: rgba(142,214,255,.45); }
.state-dot { position: absolute; width: 18px; height: 18px; border-radius: 50%; background: #8ED6FF; box-shadow: 0 0 24px rgba(142,214,255,.8); }
"""


def caption_html(captions: list[dict]) -> str:
    return "\n".join(
        f'<div id="caption-{i:03d}" class="clip caption" data-start="{c["start"]:.3f}" data-duration="{max(c["end"]-c["start"], 0.08):.3f}" data-track-index="{40+i}"><span>{c["text"]}</span></div>'
        for i, c in enumerate(captions)
    )


def html_for(chapter: int, duration: float, scenes: str, timeline: str, captions: list[dict], with_captions: bool) -> str:
    subtitle = caption_html(captions) if with_captions else ""
    gsap_src = "vendor/gsap.min.js"
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<title>Agent 架构选型｜第 {chapter} 章</title>
<script src="{gsap_src}"></script>
<style>@font-face {{ font-family: "Microsoft YaHei"; src: local("Microsoft YaHei"); }} @font-face {{ font-family: "Noto Sans SC"; src: local("Noto Sans SC"); }}{COMMON_CSS}</style>
</head>
<body>
<div id="root" data-composition-id="agent-architecture-ch{chapter:02d}" data-start="0" data-width="1920" data-height="1080" data-duration="{duration:.3f}" data-fps="30" data-subtitle-safe-band="900-1080">
  <div class="fill"></div><div id="grid" class="grid"></div><div id="glow-a" class="glow a"></div><div id="glow-b" class="glow b"></div>
  <div class="topbar"><span class="eyebrow">AGENT ARCHITECTURE / COURSE LOOP</span><span class="chapter-no">CHAPTER {chapter:02d} / 05</span></div>
  <div id="rule" class="rule"></div><div class="caption-safe-line"></div>
  <audio id="narration" src="audio/chapter-final.wav" data-start="0" data-duration="{duration:.3f}" data-track-index="10" data-volume="1"></audio>
{scenes}
{subtitle}
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
tl.to("#glow-a", {{scale: 1.12, opacity: .85, duration: {max(duration-1, 1):.3f}, ease: "sine.inOut"}}, 0);
tl.to("#glow-b", {{scale: 1.08, opacity: .78, duration: {max(duration-1.5, 1):.3f}, ease: "sine.inOut"}}, 0.4);
tl.fromTo("#rule", {{scaleX: 0}}, {{scaleX: 1, duration: .65, ease: "power3.out"}}, .12);
{timeline}
window.__timelines["agent-architecture-ch{chapter:02d}"] = tl;
</script>
</body></html>'''


def make_captions(groups: list[tuple[float, float, list[str]]]) -> list[dict]:
    out: list[dict] = []
    for start, end, texts in groups:
        weights = [max(len("".join(ch for ch in text if not ch.isspace())), 1) for text in texts]
        total = sum(weights)
        cursor = start
        for text, weight in zip(texts, weights):
            span = (end - start) * weight / total
            out.append({"text": text, "start": max(cursor - 0.05, 0), "end": min(cursor + span - 0.08, end)})
            cursor += span
    return out


def configs() -> dict[int, tuple[float, str, str, list[dict]]]:
    c1_scenes = '''
    <section id="c1-scene" class="clip" data-start="0" data-duration="31.894" data-track-index="1">
    <div class="section-label" style="left:100px;top:240px;">SELECTION COORDINATES</div>
    <div id="c1-title" class="title" style="top:282px;">先选型，再上架构</div>
    <div id="c1-sub" class="subtitle" style="top:382px;max-width:780px;">先不要急着让AI干活，先看任务复杂度与控制力。</div>
    <div id="c1-axis-x" class="axis x" style="left:220px;top:812px;width:1010px;"></div>
    <div id="c1-axis-y" class="axis y" style="left:220px;top:530px;height:282px;"></div>
    <div id="c1-x-label" class="axis-label" style="left:1080px;top:832px;">场景复杂度 →</div>
    <div id="c1-y-label" class="axis-label" style="left:42px;top:560px;transform:rotate(-90deg);">控制力 ↑</div>
    <div id="c1-q1" class="chip hot" style="left:420px;top:700px;">快速验证</div>
    <div id="c1-q2" class="chip" style="left:820px;top:560px;">拆分与路由</div>
    <div id="c1-evo" class="panel" style="left:1460px;top:210px;width:390px;height:410px;padding:22px;">
      <div class="panel-title" style="font-size:26px;">七种架构演进线</div>
      <div id="c1-evo-1" class="small-note" style="left:24px;top:66px;font-size:20px;">01 · 单 Agent</div><div id="c1-evo-2" class="small-note" style="left:24px;top:106px;font-size:20px;">02 · ReAct</div><div id="c1-evo-3" class="small-note" style="left:24px;top:146px;font-size:20px;">03 · Plan and Execute</div><div id="c1-evo-4" class="small-note" style="left:24px;top:186px;font-size:20px;">04 · Multi-Agent</div><div id="c1-evo-5" class="small-note" style="left:24px;top:226px;font-size:20px;">05 · Route + Skill</div><div id="c1-evo-6" class="small-note" style="left:24px;top:266px;font-size:20px;">06 · Blackboard</div><div id="c1-evo-7" class="small-note" style="left:24px;top:306px;font-size:20px;">07 · Graph Workflow</div>
    </div>
    <div id="c1-note" class="small-note" style="left:100px;top:840px;">先问两件事：任务有多复杂？哪里必须可控？</div>
  </section>'''
    c1_tl = '''
tl.fromTo("#c1-title", {opacity:0, y:30}, {opacity:1, y:0, duration:.7, ease:"expo.out"}, .12);
tl.fromTo("#c1-sub", {opacity:0, x:-38}, {opacity:1, x:0, duration:.55, ease:"power3.out"}, .65);
tl.fromTo("#c1-axis-x", {scaleX:0}, {scaleX:1, duration:.7, ease:"power2.out"}, 5.14);
tl.fromTo("#c1-axis-y", {scaleY:0}, {scaleY:1, duration:.7, ease:"power3.out"}, 5.27);
tl.fromTo(["#c1-x-label","#c1-y-label"], {opacity:0}, {opacity:1, duration:.35, ease:"sine.out"}, 5.94);
tl.fromTo("#c1-q1", {opacity:0, scale:.82}, {opacity:1, scale:1, duration:.5, ease:"back.out(1.6)"}, 10.51);
tl.fromTo("#c1-q2", {opacity:0, x:40}, {opacity:1, x:0, duration:.48, ease:"power3.out"}, 14.00);
tl.fromTo("#c1-evo", {opacity:0, y:28}, {opacity:1, y:0, duration:.6, ease:"power2.out"}, 16.54);
tl.fromTo(["#c1-evo-1","#c1-evo-2","#c1-evo-3","#c1-evo-4","#c1-evo-5","#c1-evo-6","#c1-evo-7"], {opacity:0, x:-18}, {opacity:1, x:0, duration:.28, ease:"power2.out", stagger:.32}, 16.90);
tl.to("#c1-evo", {opacity:0, y:-16, duration:.35, ease:"sine.in"}, 23.99);
tl.fromTo("#c1-note", {opacity:0}, {opacity:1, duration:.4, ease:"sine.out"}, 24.47);
'''
    c1_caps = make_captions([(0, 2.951, ["你是不是想到什么，就让AI做什么？"]),(2.951,5.067,["先不要急着让AI干活"]),(5.067,10.407,["真正要回答的是","任务有多复杂","以及你需要多强的控制力"]),(10.407,16.427,["轻任务只要快速验证","复杂任务才需要拆分","路由和状态管理"]),(16.427,24.147,["七种架构不是排行榜","而是一条演进线","从单 Agent 到协作系统"]),(24.467,31.894,["先记住两个判断轴","复杂度和控制力","再放回坐标系选择"])])

    c2_scenes = '''
  <section id="c2-single" class="clip" data-start="0" data-duration="15.260" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">01 / SINGLE AGENT</div><div id="c2-title" class="title" style="top:210px;">一个模型包揽全部任务</div>
    <div id="c2-input" class="panel" style="left:120px;top:470px;width:280px;height:160px;padding:34px;"><div class="panel-title">输入</div><div class="panel-copy">用户任务</div></div>
    <div id="c2-think" class="panel" style="left:580px;top:400px;width:300px;height:230px;padding:34px;"><div class="panel-title">LLM</div><div class="panel-copy">思考&#10;调用工具</div></div>
    <div id="c2-output" class="panel warm" style="left:1090px;top:470px;width:300px;height:160px;padding:34px;"><div class="panel-title">输出</div><div class="panel-copy">结果交付</div></div>
    <div id="c2-warn" class="panel alert" style="left:1450px;top:390px;width:340px;height:260px;padding:34px;"><div class="panel-title">复杂后</div><div class="panel-copy">认知过载&#10;上下文污染</div></div>
    <div id="c2-a1" class="arrow" style="left:402px;top:548px;width:160px;"></div><div id="c2-a2" class="arrow" style="left:884px;top:548px;width:190px;"></div><div id="c2-a3" class="arrow" style="left:1394px;top:548px;width:48px;"></div>
    <div class="small-note" style="left:120px;top:850px;">适合：概念验证、简单对话</div>
  </section>
  <section id="c2-react" class="clip" style="opacity:0" data-start="15.260" data-duration="17.128" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">02 / REACT</div><div id="c2r-title" class="title" style="top:210px;">Reason + Action：让 Agent 会探索</div>
    <div id="c2r-reason" class="node hot" style="left:460px;top:460px;width:210px;height:110px;">Reason</div><div id="c2r-action" class="node" style="left:850px;top:340px;width:210px;height:110px;">Action</div><div id="c2r-observe" class="node" style="left:1200px;top:460px;width:210px;height:110px;">Observe</div>
    <div id="c2r-loop" class="loop" style="left:710px;top:430px;width:500px;height:250px;"></div><div id="c2r-arrow" class="loop-arrow" style="left:1180px;top:434px;"></div>
    <div id="c2r-cost" class="panel alert" style="left:400px;top:760px;width:1080px;height:120px;padding:28px 38px;"><div class="panel-title" style="font-size:30px;">更会探索，但不适合直接承担大规模生产流程</div></div>
  </section>'''
    c2_tl = '''
tl.to("#c2-single", {opacity:0, duration:.01, ease:"none"}, 15.260);
tl.fromTo("#c2-react", {opacity:0}, {opacity:1, duration:.01, ease:"none"}, 15.260);
tl.fromTo("#c2-title", {opacity:0, x:-50}, {opacity:1, x:0, duration:.6, ease:"power3.out"}, .12);
tl.fromTo(["#c2-input","#c2-think","#c2-output"], {opacity:0, y:32}, {opacity:1, y:0, duration:.5, ease:"power2.out", stagger:.16}, 1.8);
tl.fromTo(["#c2-a1","#c2-a2","#c2-a3"], {scaleX:0}, {scaleX:1, duration:.45, ease:"expo.out", stagger:.18}, 2.55);
tl.fromTo("#c2-warn", {opacity:0, scale:.86}, {opacity:1, scale:1, duration:.55, ease:"back.out(1.4)"}, 10.20);
tl.fromTo("#c2r-title", {opacity:0, y:30}, {opacity:1, y:0, duration:.58, ease:"expo.out"}, 15.32);
tl.fromTo(["#c2r-reason","#c2r-action","#c2r-observe"], {opacity:0, scale:.75}, {opacity:1, scale:1, duration:.52, ease:"back.out(1.5)", stagger:.55}, 15.62);
tl.fromTo("#c2r-loop", {opacity:0, scale:.88}, {opacity:1, scale:1, duration:.7, ease:"power2.out"}, 17.45);
tl.fromTo("#c2r-arrow", {opacity:0, x:-18}, {opacity:1, x:0, duration:.35, ease:"power3.out"}, 18.20);
tl.fromTo("#c2r-cost", {opacity:0, y:28}, {opacity:1, y:0, duration:.5, ease:"power2.out"}, 27.0);
'''
    c2_caps = make_captions([(0,4.94,["单 Agent","就是一个大模型","包揽输入、思考和工具调用","最后输出结果"]),(4.94,10.18,["简单、便宜、延迟低","适合概念验证和简单对话"]),(10.18,15.517,["任务变复杂就会认知过载","出现上下文污染"]),(15.697,22.52,["ReAct 是 Reason","加 Action","思考、行动、观察","再决定下一步"]),(22.52,26.82,["更适合多步探索","也更容易解释过程"]),(26.82,32.388,["但 Token 消耗大","容易跑偏","不适合直接承担","大规模生产流程"])])

    c3_scenes = '''
  <section id="c3-plan" class="clip" data-start="0" data-duration="15.569" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">03 / PLAN AND EXECUTE</div><div id="c3-title" class="title" style="top:210px;">先规划，再执行</div>
    <div id="c3-plan-card" class="panel" style="left:150px;top:420px;width:420px;height:260px;padding:38px;"><div class="panel-title">Plan</div><div class="panel-copy">步骤 1&#10;步骤 2&#10;步骤 3</div></div>
    <div id="c3-exec-card" class="panel warm" style="left:850px;top:420px;width:420px;height:260px;padding:38px;"><div class="panel-title">Execute</div><div class="panel-copy">按计划逐步落地</div></div>
    <div id="c3-p-arrow" class="arrow" style="left:576px;top:550px;width:250px;"></div>
    <div id="c3-fail" class="panel alert" style="left:1360px;top:420px;width:380px;height:260px;padding:34px;"><div class="panel-title">计划错</div><div class="panel-copy">错误会被放大</div></div>
    <div class="small-note" style="left:150px;top:850px;">稳定性更高，灵活性低于 ReAct</div>
  </section>
  <section id="c3-multi" class="clip" style="opacity:0" data-start="15.749" data-duration="18.860" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">04 / MULTI-AGENT</div><div id="c3m-title" class="title" style="top:210px;">把任务分给不同角色</div>
    <div id="c3m-router" class="node hot" style="left:820px;top:360px;width:280px;height:110px;">Coordinator</div>
    <div id="c3m-planner" class="panel" style="left:250px;top:600px;width:320px;height:170px;padding:30px;"><div class="panel-title">Planner</div><div class="panel-copy">拆解任务</div></div>
    <div id="c3m-executor" class="panel" style="left:800px;top:600px;width:320px;height:170px;padding:30px;"><div class="panel-title">Executor</div><div class="panel-copy">执行步骤</div></div>
    <div id="c3m-reviewer" class="panel green" style="left:1350px;top:600px;width:320px;height:170px;padding:30px;"><div class="panel-title">Reviewer</div><div class="panel-copy">复核结果</div></div>
    <div id="c3m-a1" class="arrow" style="left:920px;top:478px;width:180px;transform:rotate(138deg);"></div><div id="c3m-a2" class="arrow" style="left:960px;top:478px;width:145px;transform:rotate(90deg);"></div><div id="c3m-a3" class="arrow" style="left:1040px;top:478px;width:180px;transform:rotate(42deg);"></div>
    <div id="c3m-cost" class="small-note" style="left:250px;top:860px;">上下文边界更清楚，但调用成本与协作协议都会增加</div>
  </section>'''
    c3_tl = '''
tl.to("#c3-plan", {opacity:0, duration:.01, ease:"none"}, 15.749);
tl.fromTo("#c3-multi", {opacity:0}, {opacity:1, duration:.01, ease:"none"}, 15.749);
tl.fromTo("#c3-title", {opacity:0, y:30}, {opacity:1, y:0, duration:.6, ease:"expo.out"}, .12);
tl.fromTo(["#c3-plan-card","#c3-exec-card"], {opacity:0, y:30}, {opacity:1, y:0, duration:.55, ease:"power3.out", stagger:.25}, 1.8);
tl.fromTo("#c3-p-arrow", {scaleX:0}, {scaleX:1, duration:.5, ease:"expo.out"}, 2.5);
tl.fromTo("#c3-fail", {opacity:0, x:44}, {opacity:1, x:0, duration:.5, ease:"power2.out"}, 8.70);
tl.fromTo("#c3m-title", {opacity:0, x:-40}, {opacity:1, x:0, duration:.58, ease:"power3.out"}, 15.35);
tl.fromTo("#c3m-router", {opacity:0, scale:.8}, {opacity:1, scale:1, duration:.55, ease:"back.out(1.5)"}, 15.90);
tl.fromTo(["#c3m-planner","#c3m-executor","#c3m-reviewer"], {opacity:0, y:34}, {opacity:1, y:0, duration:.48, ease:"power2.out", stagger:.45}, 19.30);
tl.fromTo(["#c3m-a1","#c3m-a2","#c3m-a3"], {scaleX:0}, {scaleX:1, duration:.38, ease:"power3.out", stagger:.2}, 20.1);
tl.fromTo("#c3m-cost", {opacity:0}, {opacity:1, duration:.45, ease:"sine.out"}, 26.00);
'''
    c3_caps = make_captions([(0,4.42,["Plan and","Execute","先生成完整计划"]),(4.42,8.64,["再按步骤执行","流程更稳定"]),(8.64,13.40,["计划一开始就错","错误会被放大"]),(13.40,15.569,["灵活性也不如 ReAct"]),(15.749,19.30,["Multi-Agent","再进一步把","任务分给不同角色"]),(19.30,26.00,["Planner","Executor","Reviewer","上下文边界更清楚"]),(26.00,30.54,["复杂流程更容易扩展","调用成本也会增加"]),(30.54,34.609,["流程一致性要求高","但要准备失败处理"])])

    c4_scenes = '''
  <section id="c4-route" class="clip" data-start="0" data-duration="17.946" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">05 / ROUTE + SKILL</div><div id="c4-title" class="title" style="top:210px;">不让模型想，让模型选</div>
    <div id="c4-input" class="panel" style="left:120px;top:470px;width:300px;height:170px;padding:34px;"><div class="panel-title">Intent</div><div class="panel-copy">用户输入</div></div>
    <div id="c4-router" class="node hot" style="left:640px;top:480px;width:280px;height:130px;">Router</div>
    <div id="c4-skill1" class="chip" style="left:1130px;top:410px;">Skill A · 查询</div><div id="c4-skill2" class="chip hot" style="left:1130px;top:520px;">Skill B · 执行</div><div id="c4-skill3" class="chip gray" style="left:1130px;top:630px;">Skill C · 复核</div>
    <div id="c4-ra1" class="arrow" style="left:425px;top:550px;width:190px;"></div><div id="c4-ra2" class="arrow" style="left:928px;top:550px;width:170px;"></div>
    <div id="c4-cache" class="panel green" style="left:1350px;top:760px;width:400px;height:110px;padding:26px;"><div class="panel-title" style="font-size:28px;">可缓存 · 可评估</div></div>
    <div id="c4-cost" class="panel alert" style="left:760px;top:750px;width:520px;height:120px;padding:24px;"><div class="panel-title" style="font-size:28px;">设计成本 ↑ · 路由冲突 ↑</div><div class="panel-copy" style="font-size:22px;">规则需要维护、评估和追踪</div></div>
  </section>
  <section id="c4-board" class="clip" style="opacity:0" data-start="18.126" data-duration="14.602" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">06 / BLACKBOARD</div><div id="c4b-title" class="title" style="top:210px;">多个 Agent，共享一份状态</div>
    <div id="c4b-board" class="panel" style="left:560px;top:390px;width:800px;height:340px;padding:34px;"><div class="panel-title">SHARED STATE</div><div class="state-line" style="left:40px;right:40px;top:120px;"></div><div class="state-dot" style="left:120px;top:112px;"></div><div class="state-dot" style="left:380px;top:112px;"></div><div class="state-dot" style="left:640px;top:112px;"></div><div class="small-note" style="left:40px;top:170px;">任务状态</div><div class="small-note" style="left:300px;top:170px;">中间证据</div><div class="small-note" style="left:560px;top:170px;">下一步动作</div></div>
    <div id="c4b-a1" class="arrow" style="left:300px;top:420px;width:180px;transform:rotate(22deg);"></div><div id="c4b-a2" class="arrow" style="left:1510px;top:420px;width:180px;transform:rotate(158deg);"></div>
    <div id="c4b-warn" class="panel alert" style="left:540px;top:800px;width:840px;height:100px;padding:24px 34px;"><div class="panel-title" style="font-size:28px;">状态模型、权限和追踪要先设计好</div></div>
  </section>'''
    c4_tl = '''
tl.to("#c4-route", {opacity:0, duration:.01, ease:"none"}, 18.126);
tl.fromTo("#c4-board", {opacity:0}, {opacity:1, duration:.01, ease:"none"}, 18.126);
tl.fromTo("#c4-title", {opacity:0, y:30}, {opacity:1, y:0, duration:.6, ease:"expo.out"}, .12);
tl.fromTo(["#c4-input","#c4-router"], {opacity:0, x:-34}, {opacity:1, x:0, duration:.5, ease:"power3.out", stagger:.22}, 4.10);
tl.fromTo(["#c4-skill1","#c4-skill2","#c4-skill3"], {opacity:0, x:38}, {opacity:1, x:0, duration:.4, ease:"power2.out", stagger:.28}, 5.44);
tl.fromTo(["#c4-ra1","#c4-ra2"], {scaleX:0}, {scaleX:1, duration:.42, ease:"expo.out", stagger:.2}, 4.76);
tl.fromTo("#c4-cache", {opacity:0, y:22}, {opacity:1, y:0, duration:.45, ease:"power2.out"}, 9.46);
tl.fromTo("#c4-cost", {opacity:0, y:28, scale:.96}, {opacity:1, y:0, scale:1, duration:.5, ease:"back.out(1.2)"}, 13.80);
tl.fromTo("#c4b-title", {opacity:0, x:-44}, {opacity:1, x:0, duration:.55, ease:"power3.out"}, 18.11);
tl.fromTo("#c4b-board", {opacity:0, scale:.88}, {opacity:1, scale:1, duration:.65, ease:"back.out(1.3)"}, 19.6);
tl.fromTo(["#c4b-a1","#c4b-a2"], {scaleX:0}, {scaleX:1, duration:.45, ease:"power3.out", stagger:.2}, 22.56);
tl.fromTo("#c4b-warn", {opacity:0, y:28}, {opacity:1, y:0, duration:.5, ease:"power2.out"}, 24.98);
'''
    c4_caps = make_captions([(0,4.6,["Route+Skill的关键","不是让模型自由发挥"]),(4.6,9.2,["先让意图路由器","选中 Skill","再执行可复用能力"]),(9.2,14.6,["稳定、可缓存、可评估","代价是设计成本和路由冲突"]),(14.6,17.946,["先把控制点写清楚"]),(18.126,22.2,["Blackboard","让多个 Agent","共同读写共享状态"]),(22.2,27.0,["状态变化推动下一步执行","适合复杂协作"]),(27.0,32.728,["状态模型、权限和追踪","必须先设计好"])])

    c5_scenes = '''
  <section id="c5-graph" class="clip" data-start="0" data-duration="13.819" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">07 / GRAPH WORKFLOW</div><div id="c5-title" class="title" style="top:210px;">用图，把长流程变成可治理的系统</div>
    <div id="c5-n1" class="node hot" style="left:260px;top:500px;width:210px;height:110px;">输入</div><div id="c5-n2" class="node" style="left:620px;top:360px;width:210px;height:110px;">计划</div><div id="c5-n3" class="node" style="left:620px;top:640px;width:210px;height:110px;">执行</div><div id="c5-n4" class="node done" style="left:1020px;top:500px;width:210px;height:110px;">验证</div><div id="c5-n5" class="node" style="left:1450px;top:500px;width:210px;height:110px;">交付</div>
    <div id="c5-a1" class="arrow" style="left:472px;top:540px;width:135px;transform:rotate(-22deg);"></div><div id="c5-a2" class="arrow" style="left:472px;top:575px;width:135px;transform:rotate(22deg);"></div><div id="c5-a3" class="arrow" style="left:835px;top:420px;width:185px;transform:rotate(21deg);"></div><div id="c5-a4" class="arrow" style="left:835px;top:690px;width:185px;transform:rotate(-21deg);"></div><div id="c5-a5" class="arrow" style="left:1232px;top:548px;width:200px;"></div>
    <div id="c5-features" class="panel green" style="left:1280px;top:760px;width:520px;height:120px;padding:28px;"><div class="panel-title" style="font-size:29px;">分支 · 并行 · 回溯 · 重试</div></div>
  </section>
  <section id="c5-choice" class="clip" style="opacity:0" data-start="13.999" data-duration="30.588" data-track-index="1">
    <div class="section-label" style="left:100px;top:160px;">THE EVOLUTION LINE</div><div id="c5c-title" class="title" style="top:210px;">七种架构，七个控制层级</div>
    <div id="c5c-line" class="state-line" style="left:180px;right:180px;top:500px;"></div>
    <div id="c5c1" class="node" style="left:150px;top:445px;width:180px;height:110px;">单 Agent</div><div id="c5c2" class="node" style="left:390px;top:445px;width:180px;height:110px;">ReAct</div><div id="c5c3" class="node" style="left:630px;top:445px;width:180px;height:110px;">Plan</div><div id="c5c4" class="node" style="left:870px;top:445px;width:180px;height:110px;">Multi</div><div id="c5c5" class="node" style="left:1110px;top:445px;width:180px;height:110px;">Skill</div><div id="c5c6" class="node" style="left:1350px;top:445px;width:180px;height:110px;">Blackboard</div><div id="c5c7" class="node hot" style="left:1590px;top:445px;width:180px;height:110px;">Graph</div>
    <div id="c5-check" class="panel" style="left:250px;top:700px;width:1420px;height:160px;padding:28px 40px;"><div class="panel-title" style="font-size:32px;">三问：任务有多复杂？哪里必须可控？失败后能否重试和回滚？</div></div>
  </section>'''
    c5_tl = '''
tl.to("#c5-graph", {opacity:0, duration:.01, ease:"none"}, 13.999);
tl.fromTo("#c5-choice", {opacity:0}, {opacity:1, duration:.01, ease:"none"}, 13.999);
tl.fromTo("#c5-title", {opacity:0, y:30}, {opacity:1, y:0, duration:.6, ease:"expo.out"}, .12);
tl.fromTo(["#c5-n1","#c5-n2","#c5-n3","#c5-n4","#c5-n5"], {opacity:0, scale:.72}, {opacity:1, scale:1, duration:.45, ease:"back.out(1.45)", stagger:.34}, 1.6);
tl.fromTo(["#c5-a1","#c5-a2","#c5-a3","#c5-a4","#c5-a5"], {scaleX:0}, {scaleX:1, duration:.35, ease:"expo.out", stagger:.22}, 6.04);
tl.fromTo("#c5-features", {opacity:0, y:24}, {opacity:1, y:0, duration:.5, ease:"power2.out"}, 10.10);
tl.fromTo("#c5c-title", {opacity:0, x:-40}, {opacity:1, x:0, duration:.58, ease:"power3.out"}, 14.12);
tl.fromTo("#c5c-line", {scaleX:0}, {scaleX:1, duration:.6, ease:"power2.out"}, 15.2);
tl.fromTo("#c5c1", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 15.90);
tl.fromTo("#c5c2", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 19.12);
tl.fromTo("#c5c3", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 21.18);
tl.fromTo("#c5c4", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 23.24);
tl.fromTo("#c5c5", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 26.10);
tl.fromTo("#c5c6", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 28.40);
tl.fromTo("#c5c7", {opacity:0, y:28}, {opacity:1, y:0, duration:.38, ease:"power2.out"}, 30.80);
tl.fromTo("#c5-check", {opacity:0, y:28}, {opacity:1, y:0, duration:.55, ease:"back.out(1.2)"}, 34.20);
'''
    c5_caps = make_captions([(0,3.20,["Graph","Workflow 用图","编排长流程"]),(3.20,6.04,["节点代表步骤","边代表条件"]),(6.04,10.10,["支持分支、并行","回溯和重试"]),(10.10,13.819,["最适合流程自动化","和生产环境"]),(13.999,18.96,["七种架构是一条演进线","单 Agent 做最小验证"]),(18.96,25.98,["ReAct 做多步探索","Plan and","Execute 做工程化","Multi-Agent","做角色协作"]),(25.98,33.58,["Route+Skill","做精准技能系统","Blackboard","管共享状态","Graph Workflow","承载长流程"]),(34.12,44.587,["任务有多复杂？","哪里必须可控？","失败后能不能重试和回滚？","没有最好的架构","只有最合适的架构"])])
    return {1:(31.894,c1_scenes,c1_tl,c1_caps),2:(32.388,c2_scenes,c2_tl,c2_caps),3:(34.609,c3_scenes,c3_tl,c3_caps),4:(32.728,c4_scenes,c4_tl,c4_caps),5:(44.587,c5_scenes,c5_tl,c5_caps)}


def main() -> int:
    for chapter, (duration, scenes, timeline, captions) in configs().items():
        ch_dir = ROOT / f"chapter-{chapter:02d}"
        (ch_dir / "captions").mkdir(exist_ok=True)
        existing_path = ch_dir / "captions" / "captions.json"
        if existing_path.exists():
            try:
                existing = json.loads(existing_path.read_text(encoding="utf-8"))
                if isinstance(existing, list) and existing and all(item.get("timing_method") == "word_alignment" for item in existing if isinstance(item, dict)):
                    captions = existing
            except (OSError, ValueError):
                pass
        existing_path.write_text(json.dumps(captions, ensure_ascii=False, indent=2), encoding="utf-8")
        (ch_dir / "index.html").write_text(html_for(chapter, duration, scenes, timeline, captions, False), encoding="utf-8")
        subtitle_dir = ch_dir / "subtitled"
        subtitle_dir.mkdir(exist_ok=True)
        (subtitle_dir / "index.html").write_text(html_for(chapter, duration, scenes, timeline, captions, True), encoding="utf-8")
        print(f"generated chapter-{chapter:02d}: {duration:.3f}s, {len(captions)} captions")


if __name__ == "__main__":
    raise SystemExit(main())
