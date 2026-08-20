# 3｜让 AI 会用工具：从 GUI 到 MCP

<div class="doc-hero">
  <p class="section-kicker">CHAPTER 03 / TOOLS</p>
  <h1>会回答，不等于会完成。<br>工具决定 AI 能把答案变成什么。</h1>
  <p>这一章不要求你配置 Notion、API 或 MCP。你要学的是判断接口：人怎样操作、脚本怎样复用、程序怎样调用、Agent 怎样连接工具；并理解便利性和 Token 成本为什么同时上升。</p>
  <div class="chapter-kpis"><span>学习目标：接口判断</span><span>主演示：同一篇文章四种保存方式</span><span>下一章：Harness</span></div>
</div>

## 本章学完能做什么

你能解释下图的执行主体差异，并为自己的任务选一个不超前的工具入口：

~~~text
人 → GUI
脚本 → CLI
程序 → API
Agent → MCP
~~~

## 痛点：把工具名当成能力

“接了 MCP”不等于业务已经自动化；“有 API”不等于所有人都该写程序。真正要问的是：谁在执行？任务是否需要重复？有没有结构化输入与输出？调用成本、权限和失败谁负责？

## 讲师演示：同一篇文章，四种方式保存到 Notion

讲师以 Anthropic 的文章为输入，目标保持一致：**保存标题 + 不超过 200 字中文总结** 到同一个 Notion 数据库。

<div class="ops-grid">
  <article class="ops-card"><span class="ops-label">GUI</span><h3>人操作界面</h3><p>最直观，适合低频、一次性或需要人判断的操作。</p></article>
  <article class="ops-card"><span class="ops-label">CLI</span><h3>人和 Agent 都可调用</h3><p>把已验证的动作变成命令；可复制、可批量，也可被 Agent 使用。</p></article>
  <article class="ops-card"><span class="ops-label">API / MCP</span><h3>程序与 Agent 调用</h3><p>API 适合程序稳定调用；MCP 让 Agent 使用工具，但上下文和工具往返会带来更高 Token 成本。</p></article>
</div>

完整的讲师操作顺序、Prompt 与失败截图兜底在 [Notion 演示页](/demos/notion)。

## 拆解：选择工具的四个问题

1. 这一步是否需要人看见界面并做判断？需要，就先 GUI。
2. 这一步是否会被人或 Agent 反复执行？会，就把它沉淀为 CLI。
3. 系统间是否需要稳定传递结构化数据？需要，才考虑 API。
4. Agent 是否真的需要跨工具自主取数、翻译、保存？需要，才接 MCP，并提前算 Token 与权限成本。

## 学员实操：画出你的一个工具链

选你的数字员工岗位卡中的一个输出，画三列：输入来自哪里、AI 需要做什么、最终要写到哪里。只标出目前你最合适的一种入口：GUI、CLI、API 或 MCP。不要为了“高级”而跳级。

## 复盘与延伸

工具让 Agent 能够行动，但工具越多，错误的路径也越多。下一章进入真正的经营问题：怎样用 Harness 控制结果、成本、权限与失败。
