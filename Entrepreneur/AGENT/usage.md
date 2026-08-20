# Entrepreneur 分类使用说明

## 路由

- 需要把原始素材变成课程视频、字幕或发布包时，使用 `video-teaching-assistant`。
- 需要维护 Vibestar 课程知识库、页面导航或 GitHub Pages 站点时，使用 `vibestar-frontend-maintainer`。
- 同一任务同时涉及两个 Agent 时，先明确内容真相和页面呈现的边界，再分别执行并记录交接。

## 维护顺序

1. 先更新本目录的 Agent 清单和边界说明。
2. 再更新具体 Agent 的 `AGENT/README.md`、`manifest.yaml` 和 `usage.md`。
3. 根据功能层工作流执行修改。
4. 运行 Agent 验收命令。
5. 将结果写入 Agent 层 `CHANGELOG.md`，并同步项目层变更记录。
