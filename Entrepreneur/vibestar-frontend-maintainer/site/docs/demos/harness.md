# 演示 02｜跃点互动：Harness 控制经营数字员工

<div class="doc-hero dark">
  <p class="section-kicker">CHAPTER 04 / HARNESS → LOOP</p>
  <h1>如果 AI 给出一个很自信的经营建议，<br>你凭什么批准它？</h1>
  <p>你将扮演 50 人爆款小游戏公司“跃点互动”的老板。所有收入、账单、项目和指标都是课堂虚构的冻结数据。目标不是让 AI 替你做经营决策，而是把它训练成能交出证据、边界和待批准方案的数字员工。</p>
  <div class="chapter-kpis"><span>三个月冻结数据</span><span>无 Harness vs 有 Harness</span><span>新数据触发更新</span></div>
</div>

## 演示合同

<table class="metric-table">
  <thead><tr><th>项目</th><th>课堂规定</th></tr></thead>
  <tbody>
    <tr><td>公司</td><td>50 人爆款小游戏公司“跃点互动”，游戏《翻翻羊》；全部为虚构课堂案例。</td></tr>
    <tr><td>输入</td><td>三个月 AI 使用、账单、工程质量、美术评审、增长指标和发布行动证据。</td></tr>
    <tr><td>输出</td><td>事实、信号、未知项、ROI 估算、经营决策草稿、补证据动作、外部动作清单。</td></tr>
    <tr><td>硬边界</td><td>系统只生成继续 / 暂停 / 补证据的草稿；不得自动修改预算、座席、项目状态，任何外部动作均需人工批准。</td></tr>
  </tbody>
</table>

## 痛点：没有 Harness 的“能干”，通常不可经营

同一份数据直接丢给 Agent，它可能会给出漂亮的结论，却混淆数据口径、遗漏证据、反复重试、越过批准闸门。你不该只问“AI 说得像不像”，而要问“它是基于什么证据、在什么预算内、什么时候会停下来”。

## 演示：三次运行

<div class="route-timeline">
  <article><strong>RUN 01</strong><div><h3>没有 Harness</h3><p>加载新证据包，运行“没有 Harness”。记录 6 次重试、¥14,600、72% 完整度与 58% 置信度等失控信号。</p></div></article>
  <article><strong>RUN 02</strong><div><h3>加入控制</h3><p>调整预算、完整度、重试次数与外部动作；保存策略后重跑。结果应进入 <code>paused_draft</code>，等待 CEO 判断。</p></div></article>
  <article><strong>RUN 03</strong><div><h3>新数据进来</h3><p>检查来源、时间、单位与旧数据对账；定位旧策略在哪个环节失效，更新规则或评价标准后再运行。</p></div></article>
</div>

## 拆解：五层 Harness

<div class="ops-grid">
  <article class="ops-card"><span class="ops-label">DATA</span><h3>输入边界</h3><p>允许哪些文件进入；缺失时明确标 unknown，不让模型补齐。</p></article>
  <article class="ops-card"><span class="ops-label">RULES</span><h3>业务规则</h3><p>成本、权限、输出格式和禁止动作写清楚。</p></article>
  <article class="ops-card"><span class="ops-label">EVAL</span><h3>质量验收</h3><p>是否有证据、口径、风险与待补信息，不能凭“看起来不错”。</p></article>
  <article class="ops-card"><span class="ops-label">GATE</span><h3>暂停与批准</h3><p>置信度不足、越过预算或涉及外部动作时必须停下。</p></article>
  <article class="ops-card emphasis"><span class="ops-label">LOOP</span><h3>新数据回归</h3><p>保留旧版本与失败样本，更新规则、评价器或权限后再跑。</p></article>
</div>

## 学员实操：只改四个参数

<div class="decision-card">
  <span class="ops-label">SAFE PRACTICE</span>
  <h3>学员只需要完成这四个操作</h3>
  <p>预算上限 <strong>8000</strong>；数据完整度 <strong>0.90</strong>；最大重试 <strong>2</strong>；外部动作选择 <strong>人工批准</strong>。</p>
</div>

打开讲师提供的 <code>harness_simulator.html</code>，保存策略并按策略重跑。不要改代码、不要增加真实外部工具；只观察哪些建议被暂停、哪些证据仍缺失、老板下一步需要批准什么。

## 讲师素材与兜底

课堂素材在案例包 <code>04_harness_runs</code> 中：模拟器、默认策略、调整后策略、无 Harness 结果、有 Harness 结果、事件卡、教师 Runbook 和学员起步卡。

<div class="fallback-card">
  <span class="ops-label">FALLBACK</span>
  <h3>如果沙盒无法运行</h3>
  <p>依次打开固定的无 Harness 结果、加 Harness 结果和新数据更新后的报告截图。让学员仍然比较预算、完整度、重试与人工批准四项控制，复述“Harness 不是让 Agent 更聪明，而是让它在不确定时停下来”。</p>
</div>

## 复盘

新数据变化时，不是盲目把 Prompt 写得更长。证据缺失，改输入合同；质量反复失败，改评价器；反复越权，收紧工具权限；只有每次更新都有旧版本、失败样本和回归检查，Loop 才值得自动运行。
