# 90 天 AI 数字员工经营手册

<div class="doc-hero dark">
  <p class="section-kicker">CEO PLAYBOOK / 90 DAYS</p>
  <h1>把 AI 从一次热闹的尝试，<br>变成一套有边界、有证据的经营能力。</h1>
  <p>这份手册服务于完成本课程后的企业主。你不需要成为工程师；你需要在 90 天内完成一个数字员工、一个 Harness 与 Loop，以及一个边界清晰的 Agent Team 项目。</p>
  <div class="chapter-kpis"><span>每周 20–60 分钟</span><span>每阶段一个决策门</span><span>所有投入都能复盘</span></div>
</div>

## 这份手册从哪里来

<div class="ops-grid two">
  <article class="ops-card emphasis"><span class="ops-label">BUSINESS LENS</span><h3>MIT Sloan 课程框架</h3><p>保留机会审计、Tool vs. Teammate、工作流与编排、多 Agent、迭代、风险治理和 ROI 叙事这条经营主线。</p></article>
  <article class="ops-card emphasis"><span class="ops-label">ENGINEERING LENS</span><h3>AgenticLoops 工程教材</h3><p>提取架构模式、结构化输出、评测、Harness、MCP、可观测性与成本控制；它是工程参考，不要求学员照着配置代码环境。</p></article>
</div>

<div class="risk-card">
  <strong>边界说明：</strong>这不是 MIT 课程的翻译或复刻。MIT Sloan 的样例课表提供经营问题的顺序；<a href="https://github.com/agenticloops-ai/agentic-ai-engineering" target="_blank" rel="noreferrer">AgenticLoops AI 的开源教材</a>提供工程概念。这里将两者转写成面向企业主的行动手册。
</div>

## 先定一条总规则

<div class="decision-card">
  <span class="ops-label">START SMALL</span>
  <h3>每一次升级，只增加一个变量。</h3>
  <p>先用最强模型完成一个任务；再增加结构、工具、规则、评价或角色。若某一步失败，先回到上一层，而不是同时换模型、换 Prompt、加工具和加 Agent。</p>
</div>

## Day 01–30｜交付一个数字员工

<div class="route-timeline">
  <article><strong>WEEK 01</strong><div><h3>做一次机会审计</h3><p>列出团队近两周反复出现的工作，按「频率 × 标准化程度 × 可验收性 × 风险」打分。只选第一名；不要从“做一个万能 AI 助手”开始。</p></div></article>
  <article><strong>WEEK 02</strong><div><h3>把岗位写成一页合同</h3><p>写清岗位名称、输入、输出、不能做什么、谁批准、失败如何处理。输出必须是一份文件、表格、报告或可检查的下一步，而不是一句“看起来不错”的回答。</p></div></article>
  <article><strong>WEEK 03</strong><div><h3>选择最小架构</h3><p>优先使用单 Agent；只有需要边观察边调用工具时才升级 ReAct，需要稳定多步骤时才使用 Plan and Execute。此时不做多 Agent 或自动执行。</p></div></article>
  <article><strong>WEEK 04</strong><div><h3>做第一次老板验收</h3><p>用 5 个真实样本运行。记录节省时间、交付数量或返工率中的一个指标，判断：保留、调整，或停止。</p></div></article>
</div>

<table class="metric-table">
  <thead><tr><th>本阶段应学概念</th><th>翻译成老板动作</th><th>必须留下的证据</th></tr></thead>
  <tbody>
    <tr><td>Tool vs. Teammate</td><td>判断它是一次性辅助，还是需要稳定岗位责任。</td><td><code>01-机会审计.xlsx</code></td></tr>
    <tr><td>单 Agent / ReAct / Plan and Execute</td><td>先选最小可行架构：直接交付、边做边观察，或先计划再执行。</td><td><code>02-岗位卡.md</code></td></tr>
    <tr><td>结构化输出</td><td>把输出写成固定字段、表头或检查清单。</td><td><code>03-输入输出样例/</code></td></tr>
  </tbody>
</table>

> Day 30 决策门：这个角色是否稳定省下时间或提升交付？如果不能，不进入 Harness 阶段；先改岗位定义、输入样本或输出标准。

## Day 31–60｜从 Harness 走到 Loop

<div class="route-timeline">
  <article><strong>WEEK 05</strong><div><h3>把 Harness 写出来</h3><p>补齐五项：知识与数据边界、可用工具、禁止动作、输出质量标准、人工批准点。把“不要出错”改写成可检查的规则。</p></div></article>
  <article><strong>WEEK 06</strong><div><h3>建立 20 个验收样本</h3><p>收集 10 个正常样本、5 个边界样本、5 个失败样本。每个样本只标记通过 / 不通过，以及不通过的原因；这就是你的最小 Eval 集。</p></div></article>
  <article><strong>WEEK 07</strong><div><h3>设计停机与升级规则</h3><p>规定什么情况必须停下：信息不全、金额超过阈值、涉及客户承诺、置信不足、出现敏感数据。停止后交给谁、补什么证据，也要写清楚。</p></div></article>
  <article><strong>WEEK 08</strong><div><h3>形成每周经营 Loop</h3><p>每周用同一张表查看投入、产出、错误、人工介入和下周一个实验。一次只改一个 Harness 变量，并保留前后版本。</p></div></article>
</div>

<table class="metric-table">
  <thead><tr><th>工程概念</th><th>经营化翻译</th><th>CEO 要问的问题</th></tr></thead>
  <tbody>
    <tr><td>Evaluator / Optimizer、Evals</td><td>用样本集和评分标准验证输出，而非凭感觉优化 Prompt。</td><td>20 个样本里，哪类错误最多？</td></tr>
    <tr><td>Human in the Loop、Guardrails</td><td>把高风险动作前置为人工批准，不让 Agent 自动越权。</td><td>它在哪一步必须停下来找人？</td></tr>
    <tr><td>Tracing、成本与上下文管理</td><td>保留输入、输出、耗时、用量和失败原因，才能判断是否真的有 ROI。</td><td>成本上升，是因为任务变复杂，还是流程失控？</td></tr>
  </tbody>
</table>

### 15 分钟 Rogue Agent 桌面演练

<div class="ops-grid two">
  <article class="ops-card"><span class="ops-label">SCENE</span><h3>数据不完整，却要求立刻决策</h3><p>Agent 生成了一份看似完整的报告，但关键来源缺失。你的规则应该让它标红证据缺口、停止推荐，并要求补数。</p></article>
  <article class="ops-card"><span class="ops-label">SCENE</span><h3>权限正确，却做了错误动作</h3><p>Agent 能发邮件、改表或调用工具，但即将对外作出承诺。你的 Harness 应让它生成草稿，等待负责人批准后才执行。</p></article>
</div>

> Day 60 决策门：在固定样本集上，质量、人工介入率与成本是否可接受？不通过时优先补 Harness 与证据，不要急着增加更多 Agent。

## Day 61–90｜启动一个有边界的 Agent Team

<div class="route-timeline">
  <article><strong>WEEK 09</strong><div><h3>只画 2–4 个角色的 Graph</h3><p>分开“找证据、做分析、汇总建议、最终批准”。每一个节点都有明确输入和输出；不要按部门名称拆 Agent。</p></div></article>
  <article><strong>WEEK 10</strong><div><h3>只让必要的节点并行</h3><p>Multi-Agent 中，独立证据可以并行；需要统一判断时必须汇总。当工具数量开始影响角色清晰度时，先减少复杂度，而不是继续加 Agent。</p></div></article>
  <article><strong>WEEK 11</strong><div><h3>运行小批量项目</h3><p>选择一个有结束条件的项目，设置预算、周期和人工批准。课堂 TradingAgents 的 NVDA → 20 股扩展，就是“单个可复盘任务 → 有边界批量项目”的示例。</p></div></article>
  <article><strong>WEEK 12</strong><div><h3>提交项目立项或停止报告</h3><p>用事实向管理层说明：解决了什么、投入多少、质量怎样、哪些风险仍需人工承担，以及下一季度是否值得扩大预算。</p></div></article>
</div>

<table class="metric-table">
  <thead><tr><th>架构模式</th><th>什么时候才使用</th><th>不可省略的控制</th></tr></thead>
  <tbody>
    <tr><td>Multi-Agent</td><td>一个角色无法同时承担证据、判断和批准，且多种专业视角可独立贡献。</td><td>角色输入输出、统一汇总与最终人工责任。</td></tr>
    <tr><td>Route + Skill</td><td>不同类型项目或请求，需要不同的稳定方法与工具组合。</td><td>路由条件、Skill 边界与错误分流记录。</td></tr>
    <tr><td>Blackboard</td><td>多个角色必须反复读取和更新共同的事实、假设与项目状态。</td><td>唯一事实板、数据新鲜度和写入权限。</td></tr>
    <tr><td>Graph Workflow</td><td>流程要长期重复，且包含条件分支、重试和批准节点。</td><td>节点状态、停止条件、审计记录与人工批准。</td></tr>
  </tbody>
</table>

> Day 90 决策门：这个项目是否进入正式预算？答案不是“模型很聪明”，而是“在明确边界内，它以可接受成本稳定创造了可复核的业务价值”。

## 一页 CEO ROI 叙事模板

<div class="decision-card">
  <span class="ops-label">EXECUTIVE NARRATIVE</span>
  <h3>用六句话，而不是一堆截图，决定下季度是否投入。</h3>
  <ol>
    <li><strong>业务问题：</strong>过去哪个重复工作消耗了谁、多久、造成什么风险？</li>
    <li><strong>数字员工：</strong>它接收什么输入，交付什么可验收输出？</li>
    <li><strong>经营结果：</strong>过去 4 周节省了什么、增加了什么、减少了什么？</li>
    <li><strong>成本：</strong>模型 / 工具 / 人工审核分别投入多少？</li>
    <li><strong>风险控制：</strong>它在哪些情况必须停机、上报或由人批准？</li>
    <li><strong>下一步决策：</strong>扩大、保持、补证据，还是停止？负责人和截止日是什么？</li>
  </ol>
</div>

## 延伸学习地图：学什么，不必一次全做完

<table class="metric-table">
  <thead><tr><th>你现在的阶段</th><th>推荐主题</th><th>暂时不需要做</th></tr></thead>
  <tbody>
    <tr><td>完成第一个岗位</td><td>单 Agent、ReAct、Plan and Execute、结构化输出、Token 与成本记录。</td><td>RAG、复杂框架、多 Agent 编排。</td></tr>
    <tr><td>开始 Harness 与 Loop</td><td>评测样本、Human in the Loop、Guardrails、追踪与失败复盘。</td><td>单元测试、CI/CD、生产部署。</td></tr>
    <tr><td>准备团队项目</td><td>Multi-Agent、Route + Skill、Blackboard、Graph Workflow、MCP、权限边界与预算控制。</td><td>让多个 Agent 无限自主运行。</td></tr>
  </tbody>
</table>

<div class="risk-card">
  <strong>工程附注：</strong>AgenticLoops 的 Loop Engineering 与 Production 模块目前仍标注为开发中。可以用它们理解 Skills、MCP、Sandbox、监控和成本治理的方向，但本课程不把尚未稳定的工程教程设为企业主的必修作业。
</div>

## 最后一次自检

<ul class="check-list">
  <li>我是否已经交付了一个真实、可验收的数字员工，而不只是一个聊天窗口？</li>
  <li>我是否能指出它的输入、输出、权限、质量标准与停止条件？</li>
  <li>我是否保留了样本、失败记录、成本与人工介入数据？</li>
  <li>我是否只在单 Agent 已无法承担时，才引入 Graph 和更多角色？</li>
  <li>我能否用六句话向合伙人说明下一阶段的 ROI 决策？</li>
</ul>

> 90 天的目标不是“拥有很多 AI 工具”，而是拥有第一套能被管理、被验证、也能被停止的 AI 工作系统。
