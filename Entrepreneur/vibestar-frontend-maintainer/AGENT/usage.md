# Vibestar 教学前端维护 Agent 使用说明

## 1. 判断变更归属

先判断需求属于课程章节、课程地图、工具说明、行业场景、演示页面、导航配置还是主题样式。内容变更和导航变更要同时检查，避免页面已存在但用户无法从站点入口找到。

## 2. 修改站点源码

工作目录是 `Entrepreneur/vibestar-frontend-maintainer/site/`。常用入口：

- 页面内容：`docs/`；
- 导航和站点元信息：`docs/.vitepress/config.mts`；
- 主题样式：`docs/.vitepress/theme/`；
- 发布流程：`.github/workflows/deploy.yml`。

页面写作要提供明确的下一步操作、必要的验证命令和平台差异，不把未经验证的安装步骤写成确定结论。

## 3. 本地验证

在 `site/` 目录执行：

```powershell
npm install
npm run build
npm run dev
npm run preview
```

提交前至少运行 `npm run build`。`node_modules`、`.vitepress/cache` 和 `.vitepress/dist` 是可重建产物，不提交到 Git。

## 4. 交付记录

每次更新在本目录 `CHANGELOG.md` 写清：修改了哪些页面或配置、导航是否变化、运行了什么验证命令、是否存在未完成的外部发布动作。内容、导航或部署边界变化时，同步更新 `manifest.yaml` 和上层分类说明。
