# macOS｜安装与验证

<div class="doc-hero">
  <p class="section-kicker">MACOS / LEARNER & PRESENTER</p>
  <h1>先完成两份文件，再进入课堂。</h1>
  <p>Mac 上不需要提前安装开发工具。把 Codex、WorkBuddy 和课程文件夹跑通即可；其余复杂环境由讲师现场演示。</p>
</div>

## 0. 网络连接（已有 VPN 请跳过）

<div class="risk-card">
  <strong>跳过条件：</strong>你的 Mac 已有稳定 VPN，且能打开 <a href="https://developers.openai.com/codex/quickstart" target="_blank" rel="noreferrer">Codex 官方快速开始</a>。满足这个条件，请直接进入下一节。<br>
  如果没有，请只从 <a href="https://github.com/2dust/v2rayN/releases" target="_blank" rel="noreferrer">v2rayN 官方 GitHub Release</a> 下载客户端。课程不提供账号、订阅、节点或代充值；请使用你所在组织或你本人已合法取得的连接配置，且不要在课程群或课程文件夹中泄露配置。
</div>

<div class="route-timeline">
  <article><strong>NET 01</strong><div><h3>确认你的 Mac 芯片</h3><p>点击屏幕左上角  →“关于本机”。显示 Apple M 系列芯片，选择 <code>macos-arm64.dmg</code>；显示 Intel，选择 <code>macos-64.dmg</code>。版本名称会变化，以当前 Release 中相同含义的文件为准。</p></div></article>
  <article><strong>NET 02</strong><div><h3>安装 v2rayN</h3><p>打开下载的 dmg，将 <code>v2rayN.app</code> 拖入“应用程序”。首次启动若被 macOS 拦截，请在“系统设置 → 隐私与安全性”中确认打开；只在确认文件来自官方 Release 后操作。</p></div></article>
  <article><strong>NET 03</strong><div><h3>导入已有配置并连接</h3><p>按你的服务提供方或企业 IT 的指引导入订阅或配置，连接可用节点并开启系统代理。不要共享订阅链接、二维码或账户截图。</p></div></article>
  <article><strong>NET 04</strong><div><h3>验证后再安装 Codex</h3><p>打开 Codex 官方快速开始页；能稳定加载后才继续下面步骤。若应用提示“已损坏”或无法打开，先查看 v2rayN 官方 Release 说明与 macOS 的安全提示，再向服务提供方或助教求助。</p></div></article>
</div>

## 学员安装与登录

<div class="route-timeline">
  <article><strong>STEP 01</strong><div><h3>安装 Codex</h3><p>确认网络已连通后，从 <a href="https://developers.openai.com/codex/quickstart" target="_blank" rel="noreferrer">Codex 官方快速开始</a>进入下载与安装，随后登录自己的可用账户。</p></div></article>
  <article><strong>STEP 02</strong><div><h3>安装 WorkBuddy</h3><p>从 <a href="https://www.workbuddy.cn/" target="_blank" rel="noreferrer">WorkBuddy 官网</a>选择与你的 Mac 芯片相匹配的安装包：Apple 芯片选 Apple Silicon，Intel Mac 选 Intel / x64。安装后登录。</p></div></article>
  <article><strong>STEP 03</strong><div><h3>选择最小文件权限</h3><p>在“文稿”中新建 <code>AI-3H-课程资料</code>。当 WorkBuddy 请求文件访问时，只选择这个文件夹；如系统出现权限提示，按提示授予该文件夹所需访问权限。</p></div></article>
  <article><strong>STEP 04</strong><div><h3>完成双文件测试</h3><p>回到 <a href="/preflight/">课前准备页</a>，生成 <code>codex-连通测试.md</code> 与 <code>workbuddy-连通测试.md</code>。</p></div></article>
</div>
