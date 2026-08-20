# EDU_Agents

面向 AI 教育培训的成熟 Agent 仓库。项目按受众分为 `Teenager` 和 `Entrepreneur`，每个能够稳定交付结果的 Agent 都以独立目录维护，并在自身的 `AGENT/` 目录中记录功能、使用方法、验收标准和迭代记录。

## 当前目录

- [项目级 Agent 说明](AGENT/README.md)：项目定位、路由方式和文档驱动的迭代流程。
- [Teenager](Teenager/README.md)：青少年方向，当前用于承接后续 Agent。
- [Entrepreneur](Entrepreneur/README.md)：企业家方向，当前包含两个成熟 Agent。
- [全仓库贡献规范](AGENTS.md)：复制迁移、隐私、安全和文档同步规则。

## 当前成熟 Agent

| Agent | 位置 | 交付结果 |
|---|---|---|
| 视频助教 | [`Entrepreneur/video-teaching-assistant`](Entrepreneur/video-teaching-assistant/) | 可验证、可复用的分章课程视频生产流程和发布包 |
| Vibestar 教学前端维护 | [`Entrepreneur/vibestar-frontend-maintainer`](Entrepreneur/vibestar-frontend-maintainer/) | VitePress 学习资料站源码、导航维护和 GitHub Pages 发布流程 |

## 如何使用

1. 先阅读项目级 [`AGENT/`](AGENT/) 说明。
2. 按受众进入 `Teenager/` 或 `Entrepreneur/`。
3. 阅读目标 Agent 的 `AGENT/README.md` 和 `AGENT/usage.md`。
4. 按 Agent 功能目录中的工作流执行，并运行该 Agent 的验收命令。
5. 修改 Agent 时，同步更新项目层、受众层和 Agent 层说明文档及 `CHANGELOG.md`。

本仓库只提交可复用的源码、配置、模板、文档和小型示例。依赖、缓存、原始媒体和生成视频不进入 Git。
