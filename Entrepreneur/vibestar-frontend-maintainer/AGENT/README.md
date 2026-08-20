# Vibestar 教学前端维护 Agent

## 功能定位

Vibestar 教学前端维护 Agent 负责维护 Vibestar 课程知识库和 VitePress 学习资料站，把课程结构、工具安装说明、学习地图、行业场景和演示页面整理成可浏览、可构建、可部署的文档站。

## 适用场景

- 新增或修改课程章节、学习地图和学习任务；
- 更新 Codex、VSCode、GitHub、Windows 或 Mac 的工具安装说明；
- 增加行业场景、案例演示和课程入口；
- 调整 VitePress 导航、主题样式或 GitHub Pages 发布流程。

## 输入

- 已确认的课程结构和页面需求；
- 工具安装步骤、Windows/Mac 差异和可验证命令；
- 行业案例、演示内容、品牌资源和导航变更要求。

## 输出

- `site/docs/` 下的学习资料页面；
- VitePress 配置、导航和主题样式更新；
- GitHub Pages workflow 可部署的站点源码；
- 页面交付说明、构建结果和后续维护记录。

## 维护边界

站点源码位于 `site/`。依赖通过 `package-lock.json` 安装，`node_modules` 和 `.vitepress/dist` 不提交。页面内容必须面向学习者、给出下一步操作和验证命令，不承诺保证收入、保证就业或不受边界约束的交付结果。

## 工作流入口

- [站点首页](../site/docs/index.md)
- [VitePress 配置](../site/docs/.vitepress/config.mts)
- [GitHub Pages workflow](../site/.github/workflows/deploy.yml)
- [站点使用说明](usage.md)
