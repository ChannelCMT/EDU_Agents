# EDU_Agents 成熟 Agent 迁移设计

## 目标

从零建立一个可持续迭代的 `EDU_Agents` Git 仓库，按受众分为 `Teenager` 和 `Entrepreneur`，先迁移两个已经能够交付结果的 Entrepreneur Agent：

1. `courseVedio`：视频助教，负责把原始视频、音频、访谈或长文转成可验证、可复用的分章课程视频生产流程。
2. `knowledge-base-builder`：Vibestar 教学前端维护 Agent，负责维护 VitePress 学习资料站和 GitHub Pages 发布流程。

迁移采用复制方式。源目录中的文件不得被删除、移动或清理；不纳入新仓库的文件只是不复制，继续保留在源目录。

## 源目录

| Agent | 源目录 | 目标目录 |
|---|---|---|
| 视频助教 | `C:\Users\HI\Documents\ABC_E\Course1\HarnessEngineeringPPT\courseVedio` | `Entrepreneur/video-teaching-assistant/` |
| Vibestar 教学前端维护 | `C:\Users\HI\Documents\New project 5\agents\knowledge-base-builder` | `Entrepreneur/vibestar-frontend-maintainer/` |

源目录是只读输入。迁移脚本或命令只能执行复制和校验，不得使用移动或删除操作，也不得覆盖源文件。

## 仓库结构

```text
EDU_Agents/
├─ AGENT/
│  ├─ README.md
│  ├─ manifest.yaml
│  ├─ usage.md
│  └─ CHANGELOG.md
├─ README.md
├─ AGENTS.md
├─ Teenager/
│  ├─ README.md
│  └─ AGENT/
│     └─ README.md
└─ Entrepreneur/
   ├─ README.md
   ├─ AGENT/
   │  ├─ README.md
   │  ├─ manifest.yaml
   │  ├─ usage.md
   │  └─ CHANGELOG.md
   ├─ video-teaching-assistant/
   │  ├─ AGENT/
   │  │  ├─ README.md
   │  │  ├─ manifest.yaml
   │  │  ├─ usage.md
   │  │  └─ CHANGELOG.md
   │  ├─ workflow/
   │  ├─ docs/
   │  ├─ examples/
   │  └─ course-video-pipeline/
   └─ vibestar-frontend-maintainer/
      ├─ AGENT/
      │  ├─ README.md
      │  ├─ manifest.yaml
      │  ├─ usage.md
      │  └─ CHANGELOG.md
      └─ site/
         ├─ package.json
         ├─ package-lock.json
         ├─ docs/
         └─ .github/workflows/
```

目录职责分为四层：

- 项目层 `EDU_Agents/AGENT/`：项目定位、受众路由、Agent 注册表和全局迭代规则。
- 受众层 `Teenager/AGENT/`、`Entrepreneur/AGENT/`：该受众的目标、Agent 清单、纳入标准和协作规则。
- Agent 层 `<agent>/AGENT/`：具体 Agent 的功能、边界、输入输出、使用流程、验收标准、依赖和版本记录。
- 功能层：Agent 原有的 `workflow/`、`docs/`、Skill、站点源码和示例，是 Agent 工作流程的详细执行材料。

## 分层文档作为迭代记录

新增或修改成熟 Agent 时，文档同步是交付的一部分，不另建独立数据库。每次变更至少检查以下内容：

1. 项目层注册表是否新增或更新 Agent 路径、状态、受众和最后验证命令。
2. 受众层清单是否说明该 Agent 的定位和与其他 Agent 的关系。
3. Agent 层 `AGENT/README.md` 是否描述当前功能和使用方式。
4. Agent 层 `manifest.yaml` 是否记录输入、输出、依赖、禁止事项和验收命令。
5. Agent 层 `CHANGELOG.md` 是否记录本次变更、影响范围和验证结果。
6. 功能层文档是否与实际命令、目录和交付物保持一致。

所有新 Agent 的主目录都必须包含 `AGENT/`，并至少有功能与使用说明。根项目和受众分类也保持同样的 `AGENT/` 文档层级，以便从项目总览逐层找到可执行工作流。

## 视频助教迁移边界

保留 `courseVedio` 中的可复用生产能力，包括：

- `AGENTS.md`、`README.md`、`workflow/`、`docs/`、`examples/`；
- `course-video-pipeline/` Skill、参考资料、脚本和项目模板；
- 小型、脱敏的流程图、示例清单和机器可读质量门禁；
- 必要的轻量示例工程，不携带其依赖安装目录和渲染产物。

不复制以下内容：

- 任意 `.git/` 目录；
- `node_modules/`、`.npm-cache/`、`.cache/`、`__pycache__/` 和 `.pyc`；
- `PastUselessDoc/`、临时目录、失败归档、缓存、构建目录和发布输出目录；
- 原始媒体、生成媒体和大体积媒体：`.mp4`、`.mov`、`.mkv`、`.wav`、`.mp3`、`.m4a`、`.aac`；
- 章节渲染、临时帧、音频对齐和数字人/对嘴视频；
- 含私人凭据、Voice ID、Token 或本机绝对路径的文件；
- 不属于可复用 Agent 契约的巨大历史案例输出。

`examples/harness-engineering/artifact-map.yaml` 等脱敏索引可以保留，用来解释完整案例而不提交成片。

## Vibestar Agent 迁移边界

从 `knowledge-base-builder/deliverables/vibestar-github-pages-knowledge-base/` 复制可维护的 VitePress 项目到 `site/`，保留：

- `package.json`、`package-lock.json`；
- `docs/` 与 `docs/.vitepress/config.mts`；
- `.github/workflows/deploy.yml`；
- GitHub Pages 发布所需的小型源码资源和文档内容。

不复制：

- 源项目 `.git/`；
- `node_modules/`；
- `docs/.vitepress/cache/`、`docs/.vitepress/dist/`；
- `_remote_compare/` 及其压缩包和远程比较快照；
- 根目录未纳入源码维护边界的生成 Logo 文件；
- 任何本机绝对路径、秘密或临时交付包。

站点 Agent 的说明需要把旧文档中的源路径改写为新仓库中的相对路径，且不能继续把 `New project 3`、`New project 5` 等历史本机路径作为运行前提。

## 复制安全规则

迁移必须满足以下约束：

- 只复制，不删除、不移动源文件。
- 源目录文件数量、源目录总大小和目标复制清单在迁移前后可核对。
- 目标路径如已有同名文件，不自动覆盖；先停止并报告冲突。
- 排除项写入目标 Agent 的 `AGENT/manifest.yaml`，说明它们未复制但仍保留在源目录。
- 不把本机绝对路径、密钥、Token、私人 Voice ID 或个人素材带入新仓库。
- 初始迁移完成后，只提交源代码、配置、文档、模板和小型示例；依赖通过锁文件重新安装。

## 验收标准

### 结构验收

- 根目录、受众目录和两个 Agent 主目录均存在对应 `AGENT/` 说明目录。
- 项目层和受众层可以通过注册表定位到两个 Agent。
- 两个 Agent 的说明文档都能独立解释功能、输入、输出、命令和验收方式。
- 源目录仍然存在，且迁移未对其执行删除或移动。

### 视频助教验收

- `course-video-pipeline/scripts/validate_course_video.py` 可以对模板或结构样例执行结构校验。
- 公开仓库内容不包含视频、音频、缓存、依赖目录、私人凭据或本机绝对路径。
- workflow、README、Agent 说明和实际目录路径一致。

### Vibestar 验收

- 在 `site/` 中执行 `npm install` 后，`npm run build` 成功。
- VitePress 配置、页面导航和 GitHub Pages workflow 路径有效。
- 站点源码不依赖源目录的绝对路径。

### 文档验收

- 每一层 `AGENT/` 文档内容与实际结构一致。
- 每次迁移或修改都有对应的 `CHANGELOG.md` 条目。
- 根 README 能引导新贡献者从项目层进入受众层，再进入具体 Agent。

## Git 边界

当前工作区 `C:\Users\HI\Documents\ChatGPT\EDU_Agent` 是目标仓库。迁移只在该目录内创建和修改文件，不自动创建或推送 GitHub 远程仓库。完成验证后创建本地 Git 提交；远程仓库创建、绑定和推送由用户另行决定。
