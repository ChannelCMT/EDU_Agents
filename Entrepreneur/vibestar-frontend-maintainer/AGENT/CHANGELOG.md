# Vibestar 教学前端维护 Agent Changelog

## 2026-08-25

- 页首导航新增“老洪课件”，点击直接跳转到 WorkBuddy 课件地址，并放在“Channel课程”左侧。
- 将页首导航显示名从“3小时课程”调整为“Channel课程”，课程路径和页面内容保持不变。
- 同步更新项目层、Entrepreneur 分类层和 Agent manifest 的导航维护边界。
- 已执行 `npm run build`，VitePress 1.6.4 构建通过。
- 已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `90a2bef`；GitHub Pages 发布由现有 workflow 继续处理。
- 根据《AI Builder Camp AI创造者实训营出行手册 V1.1》更新课前准备页，并以《南沙行程须知》补充跨境乘车、行前检查和酒店备选信息。
- 课前准备页新增活动地点、去程与返程、D1和D2完整逐时段课表、住宿建议及行前检查；保留原有Codex和WorkBuddy安装与验收流程。
- 采用主手册中的两天行程及穗港科技和产业融合创新中心地址，未采用辅手册中已冲突的“一日行程”和“越秀N+聚所”集合信息。
- 公开页面不写入活动联系人个人电话、邮箱、实时票价或酒店价格，也不发布第三方票务和酒店平台截图。
- 课前准备侧栏入口同步改为“出行与课前准备”；手机端四列课表改为内部横向滑动并增加查看提示，避免中文逐字换行；已执行 `npm run build`，VitePress 1.6.4 构建通过，并完成桌面端与390px手机宽度页面检查。
- 已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，最新提交为 `3c8b0a8`；GitHub Pages 线上页面已确认出现新标题、完整课表及侧栏入口。
- 按最新需求删除课前准备首页、Windows 和 macOS 页面中的 VPN、v2rayN 及网络连接专属内容，同时保留 Codex、WorkBuddy 和双文件验收流程。
- 删除页首“老洪课件”导航入口，并移除 manifest 中对应的外部入口注册信息。
- 本地执行 `npm run build`，VitePress 1.6.4 构建通过；已通过 GitHub MCP 将精确段落删除同步到 `ChannelCMT/vibestar` 的 `main` 分支，远端生成 4 个连续维护提交，GitHub Pages workflow run `32801916696` 已成功。
- D1 课表将 16:00—18:00 的文字、图片、视频三行合并为“多模态控制与内容整合”，并将 19:00—21:00 更新为“AI使用场景交流与助教协助安装所需工具”。
- 本地 `npm run build` 通过；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `e1bfe98`。
- 修复移动端暗色模式下自定义课程组件文字对比度不足：为 `--ink`、`--ink-2`、`--muted`、`--line` 和 `--paper` 增加 VitePress 暗色变量映射，并覆盖首页标题、提示卡、指标表、路线卡片及学习地图标签的暗色背景/文字。
- 已执行 `git diff --check` 和 `npm run build`，VitePress 1.6.4 构建通过；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `4858f7b`，等待现有 GitHub Pages workflow 发布。
- 在 Agent 使用说明补充主题修改的验收流程：检查 `html.dark` 自定义变量，并在约 390px 移动端确认标题、正文、表格和卡片文字可读。
- 更新 D1 课表：10:30—11:30 改为“人工智能未来应用趋势及案例”，在香港科技大学（广州）上课；11:30—12:15 改为校园参观，包含“嗨贝天地”和“校园大脑”；午餐段顺延为 12:15—13:30。
- 已执行课表内容检索、`git diff --check` 和 `npm run build`，VitePress 1.6.4 构建通过；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `5a4dcef`，等待 GitHub Pages workflow 发布。
- 修复课前准备页活动基本信息表右侧空白：VitePress 默认 `.vp-doc table { display: block }` 的选择器优先级覆盖了自定义表格布局；提升 `metric-table`、`tool-table` 和 `lm-audience` 的表格选择器优先级，并保留手机端 `metric-table` 横向滚动。
- 已执行 `git diff --check` 和 `npm run build`，生成 CSS 已包含桌面端与移动端表格规则；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `a8e0375`，等待 GitHub Pages workflow 发布。
- 在课前准备页“活动基本信息”之后新增简短讲师介绍：高宇博，香港科技大学（广州）博士，主要研究 Hermes Agent、LLM Efficient 和 Multimodal LLM。
- 已执行 `git diff --check` 和 `npm run build`，VitePress 1.6.4 构建通过；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `eaa42d9`，等待 GitHub Pages workflow 发布。
- 按反馈移除独立的讲师介绍段落，将同一简短介绍移动到 D1 10:30—11:30 课表行的“主要安排”中。
- 已执行课表定位检查、`git diff --check` 和 `npm run build`，VitePress 1.6.4 构建通过；已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `e5c6934`，等待 GitHub Pages workflow 发布。

## 2026-08-20

- 从来源标识 `knowledge-base-builder` 复制 VitePress 学习资料站源码、锁文件和 GitHub Pages workflow。
- 排除 `.git`、`node_modules`、VitePress 缓存/构建结果、远程快照和未纳入源码维护边界的 Logo；源目录未删除或移动。
- 建立 Agent 功能说明、manifest、使用流程和分层文档维护规则。
- 站点源码结构检查已通过；`npm run build` 在最终验收阶段执行。
- 复制统计：源文件 4,892 个，复制 45 个（0.27 MB），排除 4,847 个（91.33 MB）。
- `npm install` 和 `npm run build` 已完成；VitePress 1.6.4 构建通过。npm 报告 12 个依赖审计告警（9 moderate、3 high），未执行自动升级。
