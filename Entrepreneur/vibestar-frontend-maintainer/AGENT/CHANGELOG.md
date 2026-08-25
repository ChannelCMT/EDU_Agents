# Vibestar 教学前端维护 Agent Changelog

## 2026-08-25

- 页首导航新增“老洪课件”，点击直接跳转到 WorkBuddy 课件地址，并放在“Channel课程”左侧。
- 将页首导航显示名从“3小时课程”调整为“Channel课程”，课程路径和页面内容保持不变。
- 同步更新项目层、Entrepreneur 分类层和 Agent manifest 的导航维护边界。
- 已执行 `npm run build`，VitePress 1.6.4 构建通过。
- 已通过 GitHub MCP 更新 `ChannelCMT/vibestar` 的 `main` 分支，提交为 `90a2bef`；GitHub Pages 发布由现有 workflow 继续处理。

## 2026-08-20

- 从来源标识 `knowledge-base-builder` 复制 VitePress 学习资料站源码、锁文件和 GitHub Pages workflow。
- 排除 `.git`、`node_modules`、VitePress 缓存/构建结果、远程快照和未纳入源码维护边界的 Logo；源目录未删除或移动。
- 建立 Agent 功能说明、manifest、使用流程和分层文档维护规则。
- 站点源码结构检查已通过；`npm run build` 在最终验收阶段执行。
- 复制统计：源文件 4,892 个，复制 45 个（0.27 MB），排除 4,847 个（91.33 MB）。
- `npm install` 和 `npm run build` 已完成；VitePress 1.6.4 构建通过。npm 报告 12 个依赖审计告警（9 moderate、3 high），未执行自动升级。
