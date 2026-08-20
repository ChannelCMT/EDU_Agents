# 4｜Harness 到 Loop：控制数字员工的产出质量

<div class="doc-hero dark">
  <p class="section-kicker">CHAPTER 04 / HARNESS & LOOP</p>
  <h1>不要管理 AI 的自信。<br>要管理它的数据、规则、验证和停机点。</h1>
  <p>我们将进入 50 人爆款小游戏公司“跃点互动”。同一份经营数据先跑出一次失控结果，再逐层加入 Harness，最后面对新数据调整策略。你将看到数字员工不是“开了自动化”，而是一套需要持续经营的控制系统。</p>
  <div class="chapter-kpis"><span>学习目标：设计控制边界</span><span>课堂实操：4 个安全参数</span><span>最终产出：老板决策草稿</span></div>
</div>

## 本章学完能做什么

你能为一个 AI 数字员工写出最小 Harness：允许什么输入、必须遵守哪些规则、怎样验收、哪些动作必须暂停等待人批准，以及新数据进来后怎样更新。

## 痛点：没有 Harness 时，AI 看起来很能干

无 Harness 的 Agent 容易出现四类问题：数据口径混乱；结论错误却很自信；反复重试导致成本失控；把本该由人批准的外部动作直接执行。对于老板，这不是效率问题，而是经营风险。

## 讲师演示：从失控到受控，再到更新

<div class="route-timeline">
  <article><strong>RUN 01</strong><div><h3>没有 Harness</h3><p>输入三个月冻结经营数据，让 Agent 直接给经营建议。观察数据遗漏、重试、成本与不可解释结论。</p></div></article>
  <article><strong>RUN 02</strong><div><h3>加入 Harness</h3><p>明确数据边界、输出样式、业务规则、质量标准、预算上限和人工批准闸门。</p></div></article>
  <article><strong>RUN 03</strong><div><h3>新数据进来</h3><p>新一周证据改变了原判断。不是推翻系统，而是定位哪个规则或阈值需要更新，再跑出新版决策草稿。</p></div></article>
</div>

完整演示与截图兜底在 [小游戏公司 Harness 演示页](/demos/harness)。

## 拆解：Harness 的五层控制

<table class="metric-table">
  <thead><tr><th>层</th><th>要控制什么</th><th>跃点互动案例</th></tr></thead>
  <tbody>
    <tr><td>数据</td><td>允许什么进入；缺什么必须标注</td><td>三个月账单、收入、项目与证据文件。</td></tr>
    <tr><td>规则</td><td>能做什么、不能做什么</td><td>只给继续 / 暂停 / 补证据草稿，不自动改预算或项目状态。</td></tr>
    <tr><td>质量</td><td>什么是合格输出</td><td>必须有证据、口径、风险和待补信息。</td></tr>
    <tr><td>停机点</td><td>何时暂停等待人</td><td>任何外部动作都进入“人工批准”。</td></tr>
    <tr><td>反馈</td><td>新数据如何改变系统</td><td>记录失效阈值，更新策略后再生成报告。</td></tr>
  </tbody>
</table>

## 学员实操：只改四个安全控制项

打开讲师给出的 Harness 沙盒。学员不需要写代码，只调整：

<div class="ops-grid">
  <article class="ops-card"><span class="ops-label">BUDGET</span><h3>预算上限</h3><p>填写 <strong>8000</strong>。</p></article>
  <article class="ops-card"><span class="ops-label">QUALITY</span><h3>完整度阈值</h3><p>填写 <strong>0.90</strong>。</p></article>
  <article class="ops-card"><span class="ops-label">LOOP</span><h3>最大重试</h3><p>填写 <strong>2</strong>。</p></article>
  <article class="ops-card emphasis"><span class="ops-label">GATE</span><h3>外部动作</h3><p>选择 <strong>人工批准</strong>。</p></article>
</div>

然后比较两次报告：哪些建议被暂停？为什么？需要补什么证据才能让老板批准？

## 复盘与延伸

Harness 不是一次写完的 Prompt，而是失败、观察、修正、再验证的 Loop。经过这个闭环，才适合进入下一章：把受控角色放进 Graph 与 Agent Team。
