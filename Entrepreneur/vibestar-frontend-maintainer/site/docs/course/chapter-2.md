# 2｜选择合适架构：先给任务打分，再升级

<div class="doc-hero">
  <p class="section-kicker">CHAPTER 02 / TASK ARCHITECTURE</p>
  <h1>不是所有任务都值得做成 Agent。<br>先评分，再决定怎么做。</h1>
  <p>做一张 PPT，可能只是一次分享，也可能是每周 20 页、需要统一风格的系列课件；做一张图，可能是一张海报，也可能是 100 张品牌资产。重复次数、复杂度、风险与验证难度，决定架构而不是模型名称。</p>
  <div class="chapter-kpis"><span>学习目标：任务评分</span><span>演示：7 种架构选择</span><span>产出：数字员工岗位卡</span></div>
</div>

## 本章学完能做什么

你能把“我想做个 AI 员工”变成一个可讨论的任务合同，并知道什么时候停在单 Agent，什么时候升级为 ReAct、Plan & Execute、Route + Skill、Blackboard 或 Graph Workflow。

## 痛点：把所有任务都交给一个聊天框

低频、低风险任务，强模型直接处理通常最快。高频、跨材料、有外部动作或需要稳定复用的任务，如果仍然靠同一个聊天框临时描述，结果会越来越不可控。

## 讲师演示：7 种架构不是菜单，而是升级阶梯

这七种是本课程采用的 Agent 架构演进线。它不是“越往后越先进”的菜单，而是根据任务是否需要行动、规划、分工、共享状态和固定流程逐步升级：

<table class="metric-table">
  <thead><tr><th>架构</th><th>适用信号</th><th>此课的关键判断</th></tr></thead>
  <tbody>
    <tr><td>01｜单 Agent</td><td>单一任务、单一责任人、结果可直接验收</td><td>先把输入、输出和人工批准写清楚；不要为了“像 Agent”而加复杂度。</td></tr>
    <tr><td>02｜ReAct</td><td>需要“观察 → 推理 → 调用工具 → 再观察”的即时循环</td><td>给它少而清晰的工具；每一步动作都要能看到结果并可停止。</td></tr>
    <tr><td>03｜Plan and Execute</td><td>任务多步骤、目标明确，先规划能减少返工</td><td>计划与执行分开；允许根据新证据改计划，但不要让执行偏离目标。</td></tr>
    <tr><td>04｜Multi-Agent</td><td>确实需要不同专业视角、独立证据或并行分析</td><td>先从 2–4 个角色开始；每个角色只对一种输入和输出负责。</td></tr>
    <tr><td>05｜Route + Skill</td><td>任务来源或类型不同，且每类有稳定、可复用的方法</td><td>先定路由条件，再给每类任务匹配 Skill；不能让 Agent 随意选路或乱加载能力。</td></tr>
    <tr><td>06｜Blackboard</td><td>多个 Agent 要围绕同一份持续更新的事实、假设和任务状态协作</td><td>定义唯一事实板、字段格式和写入权限；避免各角色各自保存一套“真相”。</td></tr>
    <tr><td>07｜Graph Workflow</td><td>流程节点、条件分支、重试与人工批准需要长期稳定复用</td><td>把节点、边、状态和停止条件画清楚；Graph 是可审计的业务流程，不是无限自主循环。</td></tr>
  </tbody>
</table>

## 拆解：先用四个维度给任务打分

<div class="ops-grid">
  <article class="ops-card"><span class="ops-label">REPEAT</span><h3>重复次数</h3><p>一次性的工作，通常不需要搭系统；每周、每天、批量发生，才有升级价值。</p></article>
  <article class="ops-card"><span class="ops-label">COMPLEXITY</span><h3>复杂度</h3><p>是否需要多资料、多步骤、多角色或不同专业视角？</p></article>
  <article class="ops-card emphasis"><span class="ops-label">RISK</span><h3>风险与可验证性</h3><p>错了会怎样？谁能验收？没有验收标准的任务，不要先自动化。</p></article>
</div>

## 学员实操：将任务升级成 AI 数字员工

使用 Codex 创建一张岗位卡，而不是直接要求它“帮我自动完成”：

<div class="prompt-card"><strong>课堂 Prompt</strong>

~~~text
你是我的 AI 组织设计顾问。请把我下面的工作任务整理成一张“AI 数字员工岗位卡”。
必须输出：岗位名称、业务目标、输入材料、输出物、每周重复次数、复杂度、风险、必须由人批准的动作、AI 还需要学习的知识、第一版最小任务。
如果信息不足，先问我不超过 5 个关键问题，不要直接假设。

我的任务是：［粘贴你的真实任务］
~~~

</div>

## 复盘与延伸

架构不是一次性选对，而是随着任务重复、证据和风险逐步升级。下一章我们让 Agent 真正获得能力：通过 GUI、CLI、API 与 MCP 使用工具。
