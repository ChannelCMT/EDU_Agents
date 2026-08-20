# Windows｜安装与验证

<div class="doc-hero">
  <p class="section-kicker">WINDOWS / LEARNER & PRESENTER</p>
  <h1>只把两项工具装到能用。</h1>
  <p>安装完成后，重点不是研究设置，而是确认 Codex 和 WorkBuddy 能在 <code>AI-3H-课程资料</code> 中各自生成一份 Markdown 文件。</p>
</div>

## 0. 网络连接（已有 VPN 请跳过）

<div class="risk-card">
  <strong>跳过条件：</strong>你的电脑已经有稳定 VPN，且能打开 <a href="https://developers.openai.com/codex/quickstart" target="_blank" rel="noreferrer">Codex 官方快速开始</a>。满足这个条件，请直接进入下一节安装 Codex。<br>
  如果没有，请只从 <a href="https://github.com/2dust/v2rayN/releases" target="_blank" rel="noreferrer">v2rayN 官方 GitHub Release</a> 下载客户端。课程不提供账号、订阅、节点或代充值；请使用你所在组织或你本人已合法取得的连接配置，且不要把配置截图、复制到课程群中。
</div>

<div class="route-timeline">
  <article><strong>NET 01</strong><div><h3>下载完整 Windows 包</h3><p>在 Release 页面展开最新版本的 Assets，优先选择名称中带 <code>windows</code>、<code>64</code> 与 <code>SelfContained</code> 的完整压缩包；它通常自带运行所需组件。大多数 Windows 电脑选 x64；只有 Windows on ARM 设备才选择 arm64。</p></div></article>
  <article><strong>NET 02</strong><div><h3>解压并启动 v2rayN</h3><p>把压缩包解压到一个固定、无敏感文件的位置，例如“文档 / 网络工具”。打开其中的 <code>v2rayN.exe</code>；不要在压缩包内直接运行，也不要把订阅链接写入课程文件夹。</p></div></article>
  <article><strong>NET 03</strong><div><h3>导入已有配置并连接</h3><p>按你的服务提供方或企业 IT 给出的方式导入订阅或配置，选择可用节点并开启系统代理。客户端连通不等于可用，下一步必须验证网页访问。</p></div></article>
  <article><strong>NET 04</strong><div><h3>验证后再安装 Codex</h3><p>打开 Codex 官方快速开始页；能稳定加载后再继续下面步骤。打不开时先检查 v2rayN 状态、配置有效性和系统代理，不要在课堂现场排错。</p></div></article>
</div>

## 学员安装与登录

<div class="route-timeline">
  <article><strong>STEP 01</strong><div><h3>安装 Codex</h3><p>确认网络已连通后，从 <a href="https://developers.openai.com/codex/quickstart" target="_blank" rel="noreferrer">Codex 官方快速开始</a>进入下载与安装。打开后用自己的可用账户登录。</p></div></article>
  <article><strong>STEP 02</strong><div><h3>安装 WorkBuddy</h3><p>从 <a href="https://www.workbuddy.cn/" target="_blank" rel="noreferrer">WorkBuddy 官网</a>下载 Windows 版本，按安装向导完成安装并登录。</p></div></article>
  <article><strong>STEP 03</strong><div><h3>只授权课程文件夹</h3><p>在“文档”中新建 <code>AI-3H-课程资料</code>。首次需要文件操作时，只选择这个文件夹，不给课程无关目录权限。</p></div></article>
  <article><strong>STEP 04</strong><div><h3>完成双文件测试</h3><p>回到 <a href="/preflight/">课前准备页</a>，生成 <code>codex-连通测试.md</code> 与 <code>workbuddy-连通测试.md</code>。</p></div></article>
</div>
