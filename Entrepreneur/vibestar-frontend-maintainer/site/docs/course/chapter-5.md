# 5｜Graph 与 Agent Team：从一个数字员工到 AI 团队

<div class="doc-hero">
  <p class="section-kicker">CHAPTER 05 / GRAPH & AGENT TEAM</p>
  <h1>多 Agent 不是“多开几个窗口”。<br>是用 Graph 管理角色、证据与决策边界。</h1>
  <p>最后一章不让学员现场部署复杂开源项目。我们通过 TradingAgents 的 NVDA 单只股票演示，理解一个已有多 Agent Graph 怎样分工、怎样并行、怎样汇总，再把 20 只 AI 股作为已经完成的批量扩展示例。</p>
  <div class="chapter-kpis"><span>学习目标：读懂已有 Graph</span><span>完整演示：NVDA</span><span>扩展展示：20 只 AI 股 + 恐慌指数</span></div>
</div>

## 本章学完能做什么

你能以老板视角判断多 Agent 项目是否值得进入：角色是否清楚、输入输出是否可追溯、并行任务是否真的独立、最终决策是否保留了人类责任。

## 痛点：把“多个 Agent”误认为“更多答案”

多个 Agent 只有在角色可拆、证据可合并、冲突可解释、权限可控制时才有价值。否则它只会放大 Token、等待和不一致的结论。

## 讲师演示：先理解，再执行 NVDA

1. 在 GitHub 识别 TradingAgents 的项目结构与多 Agent 思路。
2. 打开讲师准备好的本地副本，要求 Codex **先解释运行原理、角色、输入、输出与风险**，不直接改代码。
3. 对齐范围：课堂只完整运行 NVDA；基本面、技术面、情绪、新闻事件等角色并行形成证据。
4. 观察角色输出如何进入最终报告；区分事实、推断与风险提示。
5. 展示已完成的扩展：20 只 AI 股票逐只运行、标准化提取、横向排名，再加入恐慌指数调整评级、仓位与风险预算。

完整操作顺序、Prompt 与冻结报告兜底在 [TradingAgents 演示页](/demos/tradingagents)。

## 拆解：Agent Boss 的四个问题

<div class="ops-grid">
  <article class="ops-card"><span class="ops-label">ROLE</span><h3>谁负责什么？</h3><p>不要让角色名称漂亮但责任重叠；每个 Agent 都应有明确输入、输出与停止条件。</p></article>
  <article class="ops-card"><span class="ops-label">GRAPH</span><h3>谁依赖谁？</h3><p>并行只用于独立证据；需要判断依赖的步骤必须串行，并把中间产物保留下来。</p></article>
  <article class="ops-card"><span class="ops-label">EVIDENCE</span><h3>结论能否追溯？</h3><p>最终建议必须能看到来自哪些数据、哪个角色、哪个交易日或时间点。</p></article>
  <article class="ops-card emphasis"><span class="ops-label">GATE</span><h3>人何时负责？</h3><p>涉及预算、投资、对外沟通和不可逆动作，Agent 只能提交草稿或建议，不能越过批准闸门。</p></article>
</div>

## 学员实操：为你的 Agent Team 画第一张 Graph

回到自己的数字员工岗位卡。只画 3 个节点：一个负责输入 / 证据，一个负责分析 / 产出，一个负责验收 / 人工批准。标出哪两步能并行，哪一步必须由人决定。

## 复盘与延伸

这堂课的终点不是“部署一个看起来很酷的多 Agent 项目”，而是开始经营一个受控的数字员工系统。下一步按照 [90 天路径](/roadmap-90-days/) 先做一个能量化 ROI 的角色，再逐层添加 Harness 和团队协作。
