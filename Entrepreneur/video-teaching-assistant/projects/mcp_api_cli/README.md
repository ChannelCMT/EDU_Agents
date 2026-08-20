# MCP / API / SDK / CLI / Function Calling / Tool Calling / ADK

这是一个基于 `course-videoLoop` 的审核稿项目，目标是把 7 个容易混淆的术语放回同一张 Agent 技术栈地图。

## 当前交付

- `SCRIPT.md`：3 分 30 秒讲稿审核稿。
- `script/voiceover-v01.md`：后续 Fish Audio 的唯一文本源，按完整语义句切分。
- `storyboard/semantic-beat-manifest.yaml`：9 个场景、时间窗口、动画顺序和审查门禁。
- `hyperframes/index.html`：1920×1080 HyperFrames 动画草稿，暂不含音频、字幕和 MP4。
- `ppt/AgentTechStack_review.pptx`：可编辑 PPT 审核稿，含演讲者备注。
- `ppt/QA`：每页 PNG、布局 JSON 和拼图，便于逐页检查。
- `HARNESS.md`：PPT 背景网格对比度、分隔线和移动端缩略图审查规则。

## 审核顺序

1. 先看 `SCRIPT.md`：确认总论点、术语解释和 3 分 30 秒节奏。
2. 再看 `ppt/AgentTechStack_review.pptx`：重点检查第 1、2、5、7、9 页。
3. 打开 `hyperframes/index.html`：确认“总图 → 局部放大 → 回到总图”的动画顺序。
4. 审核通过后，才进入 Fish Audio 配音、词级对齐、字幕和 MP4 渲染。

## 本阶段明确不做

- 不生成配音。
- 不生成数字人。
- 不添加最终字幕。
- 不渲染 MP4。

## 运行动画草稿

使用 HyperFrames CLI 对 `hyperframes/index.html` 做 lint/check；通过后再进入配音和渲染阶段。动画稿已经预留底部 `900–1080px` 字幕安全区。
