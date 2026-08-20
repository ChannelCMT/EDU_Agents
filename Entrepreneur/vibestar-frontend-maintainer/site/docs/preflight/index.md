# 课前准备｜只装两项

<div class="doc-hero dark">
  <p class="section-kicker">10 MINUTES / READY TO LEARN</p>
  <h1>不要把上课时间花在安装环境上。</h1>
  <p>这门 3 小时课程里，学员只需准备 <strong>Codex</strong> 与 <strong>WorkBuddy</strong>。如果你的电脑还没有可用 VPN，先完成网络连接；当两者都能在课程文件夹里完成一次真实任务，你就可以进入课堂。</p>
  <div class="chapter-kpis"><span>主工具仅 2 项</span><span>验证 2 个文件</span><span>不在现场排错</span></div>
</div>

## 0. 先检查网络连接（已有 VPN 请跳过）

<div class="risk-card">
  <strong>先判断：</strong>如果你的电脑已经有稳定可用的 VPN，并能打开 Codex 官方页面，就保留原来的连接方式，<strong>无需安装 v2rayN</strong>。<br>
  如果暂时没有可用 VPN，请先按你的系统安装 v2rayN，再安装 Codex。v2rayN 只是网络连接客户端；订阅或配置信息请使用你所在组织或你本人已合法取得的服务，不在课程群或页面中分享账号、订阅链接和节点信息。
</div>

<div class="ops-grid two">
  <article class="ops-card"><span class="ops-label">WINDOWS</span><h3>Windows 下载与连接</h3><p>从官方 Release 下载 Windows 的完整包，解压后打开 v2rayN；导入你已有的配置，开启系统代理，然后验证能打开 Codex 官方页面。</p><p><a href="/preflight/windows">查看 Windows 具体步骤 →</a></p></article>
  <article class="ops-card"><span class="ops-label">MACOS</span><h3>macOS 下载与连接</h3><p>Apple 芯片与 Intel Mac 需要选择不同的 dmg 安装包。安装、导入你已有的配置并连通后，再继续安装 Codex。</p><p><a href="/preflight/macos">查看 macOS 具体步骤 →</a></p></article>
</div>

## 你需要准备什么

<div class="ops-grid two">
  <article class="ops-card emphasis">
    <span class="ops-label">必须 / 01</span>
    <h3>Codex 桌面端</h3>
    <p>用于课堂中的模型、架构、Prompt、Harness 与项目理解。请安装后用自己的可用账户登录。</p>
    <p><a href="https://developers.openai.com/codex/quickstart" target="_blank" rel="noreferrer">打开 Codex 官方安装与快速开始 →</a></p>
  </article>
  <article class="ops-card emphasis">
    <span class="ops-label">必须 / 02</span>
    <h3>WorkBuddy 桌面端</h3>
    <p>作为办公型 Agent 的课堂对照与本地任务入口。首次使用时只授权课程文件夹，不要授权不相关的个人目录。</p>
    <p><a href="https://www.workbuddy.cn/" target="_blank" rel="noreferrer">打开 WorkBuddy 官方下载页 →</a></p>
  </article>
</div>

## 这次不需要安装什么

<div class="risk-card">
  <strong>不需要：</strong>VS Code、Git、Node.js、Python / Miniconda、Notion 桌面端、MCP、API Key、Docker、TradingAgents。<br>
  Notion 的 GUI / CLI / API / MCP 与 GitHub TradingAgents 都由讲师演示；你在课上要做的是理解判断与边界，而不是配置复杂环境。
</div>

## 10 分钟验收：创建两份真实文件

### 1. 先新建课程文件夹

在“文档”或“文稿”中新建文件夹，名称固定为：

~~~text
AI-3H-课程资料
~~~

后面所有课堂文件都放在这里。不要放在桌面、下载目录或企业同步盘的深层目录中。

### 2. 用 Codex 生成第一份文件

打开 Codex，选择或打开 <code>AI-3H-课程资料</code> 文件夹，发送下面这句话：

<div class="prompt-card"><strong>复制给 Codex</strong>

~~~text
在当前课程文件夹创建 codex-连通测试.md，写入我的姓名，以及我最希望 AI 帮我解决的一个工作问题。
~~~

</div>

确认 <code>codex-连通测试.md</code> 已经真实出现在文件夹中，并且可以打开阅读。

### 3. 用 WorkBuddy 生成第二份文件

打开 WorkBuddy，完成登录。首次提出需要操作文件的任务时，只授权 <code>AI-3H-课程资料</code> 这个文件夹。然后发送：

<div class="prompt-card"><strong>复制给 WorkBuddy</strong>

~~~text
在当前课程文件夹创建 workbuddy-连通测试.md，写入：我希望 AI 协助的一个重复工作。
~~~

</div>

确认 <code>workbuddy-连通测试.md</code> 已经真实出现在同一个文件夹中。

## 完成标准与课堂兜底

<table class="metric-table">
  <thead><tr><th>检查项</th><th>完成标准</th><th>如果没完成</th></tr></thead>
  <tbody>
    <tr><td>Codex</td><td>已登录；能创建并打开 <code>codex-连通测试.md</code></td><td>带着电脑参加；课堂实操时与已连通的同桌共用一台电脑。</td></tr>
    <tr><td>WorkBuddy</td><td>已登录；能创建并打开 <code>workbuddy-连通测试.md</code></td><td>不现场配置模型或权限，先观看讲师演示并记录你的任务想法。</td></tr>
    <tr><td>网络</td><td>两个工具都能完成一次正常对话或任务</td><td>提前联系助教；课堂当天不要把排错留给讲师。</td></tr>
  </tbody>
</table>

> 课堂的目标不是“每个人都装出同样的技术栈”，而是先用两种 Agent 真实完成一件小事，再学习怎样把它变成受控的业务系统。

## 按你的电脑继续

- [Windows 安装与验证](/preflight/windows)
- [macOS 安装与验证](/preflight/macos)
