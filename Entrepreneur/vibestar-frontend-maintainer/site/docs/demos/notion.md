# 演示 01｜Notion：同一篇文章的四种保存方式

<div class="doc-hero">
  <p class="section-kicker">CHAPTER 03 / GUI → CLI → API → MCP</p>
  <h1>目标不变，执行主体不同。</h1>
  <p>讲师用同一篇固定文章、同一张 Notion 数据库、同一套字段，依次展示人工 GUI、CLI、API 与 MCP。学员不配置 Notion、API 或 MCP；只需要理解什么时候该选择哪种方式。</p>
  <div class="chapter-kpis"><span>固定输出：标题 + 200 字中文总结</span><span>固定目标：同一数据库</span><span>重点：边界与成本</span></div>
</div>

## 演示合同

<table class="metric-table">
  <thead><tr><th>项目</th><th>固定内容</th></tr></thead>
  <tbody>
    <tr><td>输入</td><td>Anthropic 的 <a href="https://www.anthropic.com/engineering/building-effective-agents" target="_blank" rel="noreferrer">Building Effective Agents</a> 文章；讲师使用已准备的文章卡。</td></tr>
    <tr><td>输出</td><td>文章标题、原文链接、中文总结（不超过 200 字）、写入方式；收录时间由 Notion 自动生成。</td></tr>
    <tr><td>目标</td><td>唯一的课程 Notion 数据库“AI 文章数据库”。不搜索、不打开、不写入其他页面或数据库。</td></tr>
    <tr><td>批准闸门</td><td>任何真实写入前先预览；只有讲师说出“确认写入”才尝试一次创建。失败不重试。</td></tr>
  </tbody>
</table>

## 痛点：同样是“保存一篇文章”，为什么要四种方式

因为“保存”不是一个抽象动作。低频时，人直接点 GUI 最快；动作稳定且要反复调用时，CLI 能让人和 Agent 使用同一条命令；程序间需要稳定数据交换时才用 API；只有当 Agent 真的要跨工具读取、翻译、预览、保存时，才值得接 MCP。

## 演示：四种方式依次走一遍

<div class="route-timeline">
  <article><strong>GUI</strong><div><h3>人工保存</h3><p>讲师在 Notion 手动新建记录、填入同一标题、链接与中文总结。镜头停在字段合同一致的结果。</p></div></article>
  <article><strong>CLI</strong><div><h3>可复制的命令</h3><p>先运行已准备的健康检查，只做 payload 预览。强调 CLI 同时可以被人和 Agent 调用。讲师确认后，最多尝试一次写入。</p></div></article>
  <article><strong>API</strong><div><h3>程序调用</h3><p>先运行 dry-run，展示脱敏 payload 与四个可写字段；讲师确认后才让程序尝试一次保存。</p></div></article>
  <article><strong>MCP</strong><div><h3>Agent 使用工具</h3><p>Agent 读取固定文章卡，预览数据库、字段和值及字数；它必须停下来等“确认写入”。MCP 更灵活，也会消耗更多 Token。</p></div></article>
</div>

## 拆解：四个接口的经营判断

<table class="metric-table">
  <thead><tr><th>方式</th><th>谁执行</th><th>最适合</th><th>要注意</th></tr></thead>
  <tbody>
    <tr><td>GUI</td><td>人</td><td>低频、一次性、需要肉眼判断的操作</td><td>难批量、难复用，但最容易发现错误。</td></tr>
    <tr><td>CLI</td><td>人或 Agent</td><td>已验证的固定动作、批量或可复制操作</td><td>命令要有 dry-run、固定输入和停止条件。</td></tr>
    <tr><td>API</td><td>程序</td><td>系统之间稳定传递结构化数据</td><td>要管理权限、字段契约与调用失败。</td></tr>
    <tr><td>MCP</td><td>Agent</td><td>Agent 需要跨工具理解、生成、预览、保存</td><td>工具往返与上下文会提高 Token 成本；权限必须最小化。</td></tr>
  </tbody>
</table>

## 讲师 Prompt 与操作入口

<div class="prompt-card"><strong>MCP 演示的最小任务口令</strong>

~~~text
读取固定文章卡。先预览：目标数据库、四个可写字段、字段值与中文总结字数。
此时不得创建记录。只有收到“确认写入”后，才可在唯一课程数据库中尝试一次创建；失败立即停止，不重试。
~~~

</div>

讲师离线素材位于课程案例包的 <code>notion_article_demo</code>：文章卡、CLI / API / MCP Prompt、dry-run 脚本、预检清单与成功截图都已分开保存。录制时只使用这些固定文件，不把真实凭据写入页面或镜头。

## 学员实操

学员不做 Notion 配置。请用自己的岗位卡回答：这项工作此刻应该停在 GUI、升级到 CLI、由程序 API 处理，还是值得交给 MCP？写出理由，并列出一个你担心的成本或权限问题。

## 失败兜底与复盘

<div class="fallback-card">
  <span class="ops-label">FALLBACK</span>
  <h3>认证、权限、字段或网络失败时</h3>
  <p>停止真实写入，打开对应方式的冻结截图或验证输出。继续讲字段合同、预览、确认写入与“不自动重试”的控制逻辑；不要在课堂临时授权、切换数据库或展示密钥。</p>
</div>

复盘问题：为什么 CLI 是“人和 Agent 都能使用”的桥梁？为什么 MCP 不是所有任务的默认答案？
