# 演示 03｜TradingAgents：从 GitHub 到 NVDA 多 Agent 研究

<a class="resource-callout" href="https://chatgpt.com/s/cx_6a913752d7dc81918329a6522e62f9e2" target="_blank" rel="noopener noreferrer">
  <span class="resource-callout-copy">
    <small>CHATGPT / COMPLETE RESEARCH THREAD</small>
    <strong>打开 TradingAgents 完整研究对话</strong>
    <em>从数据层、Agent Graph 到 NVDA 最新分析</em>
  </span>
  <span class="resource-callout-arrow" aria-hidden="true">↗</span>
</a>

<div class="doc-hero">
  <p class="section-kicker">CHAPTER 05 / GRAPH & AGENT TEAM</p>
  <h1>先让 AI 解释已有系统，<br>再讨论让它为你工作。</h1>
  <p>讲师以开源 TradingAgents 为例，展示怎样从 GitHub 识别一个多 Agent 项目、在本地让 Codex 先解释 Graph，再完整运行 NVDA 的研究路径。20 只 AI 股票与恐慌指数只用于说明项目如何批量扩展，不在课堂实时运行。</p>
  <div class="chapter-kpis"><span>课堂完整运行：NVDA</span><span>先理解、后改动</span><span>不构成投资建议</span></div>
</div>

## 课堂边界

<div class="risk-card">
  <strong>重要：</strong>本演示用于理解多 Agent、Graph、证据与风险管理，不构成任何投资建议。展示的价格、新闻、恐慌指数与报告必须标注供应商、交易日、时区与 as-of 日期。实时网络或行情失败时，只展示数据缓存与冻结报告。
</div>

## 痛点：开源项目不是复制下来就能变成数字员工

很多人看到 GitHub 项目会直接运行或直接让 AI 改代码。正确顺序相反：先理解系统的角色、输入输出、并行与依赖、风险边界，再把自己的需求限制到一个可验证的最小范围。

## 演示：NVDA 的最小完整链路

<div class="route-timeline">
  <article><strong>01 / GITHUB</strong><div><h3>识别项目</h3><p>打开 TradingAgents，先看目录、角色、Graph 入口与已有说明；不急着安装更多依赖。</p></div></article>
  <article><strong>02 / CODEX</strong><div><h3>先解释，不直接改</h3><p>让 Codex 用业务语言说明运行原理：哪些 Agent 负责基本面、技术面、情绪、新闻事件，如何汇总。</p></div></article>
  <article><strong>03 / ALIGN</strong><div><h3>把课堂范围锁成 NVDA</h3><p>只分析 NVDA；明确输入时间、输出格式、风险提示与不做交易执行的边界。</p></div></article>
  <article><strong>04 / GRAPH</strong><div><h3>观察并行证据</h3><p>展示角色调用或报告中的分工，再汇总为可解释结论、证据缺口和风险提醒。</p></div></article>
  <article><strong>05 / EXTEND</strong><div><h3>展示已完成的 20 股项目</h3><p>逐只运行原版 Graph、保存完整报告、标准化提取、横向排名，再加入市场恐慌指数调整评级 / 仓位 / 风险预算。</p></div></article>
</div>

## 讲师 Prompt：先读懂项目

<div class="prompt-card"><strong>复制给 Codex（讲师准备好的本地项目中执行）</strong>

~~~text
请先不要修改任何代码，也不要运行会下载大量数据或产生外部动作的命令。
请阅读这个项目的 README、入口文件和关键目录，用企业主能听懂的语言解释：
1. 它的 Graph / 多 Agent 角色如何分工；
2. 每个角色的输入、输出和依赖；
3. 一只股票从开始到最终报告的运行链路；
4. 课堂只演示 NVDA 时，应该锁住哪些时间范围、成本、风险与停止条件；
5. 如果后续扩展到 20 只 AI 股票，哪些结果需要标准化，哪些必须增加人工审核。
先给出计划和风险清单，等待我确认后再建议下一步。
~~~

</div>

## 拆解：什么时候多 Agent 才成立

<table class="metric-table">
  <thead><tr><th>条件</th><th>TradingAgents 中的体现</th><th>老板要验收</th></tr></thead>
  <tbody>
    <tr><td>角色可拆</td><td>基本面、技术面、情绪、新闻事件是不同证据源。</td><td>每个角色是否有独立输入、输出与停止条件？</td></tr>
    <tr><td>并行有意义</td><td>独立证据可以同时收集，最后统一汇总。</td><td>并行是否减少等待，还是只增加了噪音与 Token？</td></tr>
    <tr><td>结论可追溯</td><td>最终报告能回到角色输出、数据源与时间点。</td><td>事实、推断与未知项是否被分开？</td></tr>
    <tr><td>人保留责任</td><td>模型给出研究草稿与风险提醒。</td><td>任何交易、预算或外部动作是否仍有人工批准？</td></tr>
  </tbody>
</table>

## 学员实操

学员不部署 TradingAgents。请拿自己的业务任务画一个 3 节点 Graph：证据输入 Agent、分析产出 Agent、验收 / 人工批准节点。标出哪个节点可以并行、谁负责最终批准、失败时回到哪里。

## 失败兜底与复盘

<div class="fallback-card">
  <span class="ops-label">FALLBACK</span>
  <h3>实时运行、数据下载或报告仍在执行时</h3>
  <p>直接切换 NVDA 的已完成报告、角色输出截图和 20 股横向排名结果。不要为了等待实时结果拖慢课堂；重点仍是“先理解 Graph、锁住边界、保存证据、保留人工责任”。</p>
</div>

复盘问题：当你的业务从一个数字员工升级到 Agent Team 时，最先应该新增的是角色，还是验收与批准节点？
