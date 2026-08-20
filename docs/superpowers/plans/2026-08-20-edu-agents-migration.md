# EDU_Agents 成熟 Agent 迁移实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在当前工作区建立 `EDU_Agents` 仓库，按 `Teenager` / `Entrepreneur` 分层，并以复制-only 方式迁移视频助教和 Vibestar 教学前端维护两个成熟 Agent。

**Architecture:** 根项目、受众分类和每个成熟 Agent 都拥有自己的 `AGENT/` 说明目录。Agent 原有的工作流、Skill、文档和站点源码作为功能层保留；生成视频、音频、依赖、缓存和大型历史产物不复制。项目层注册表和每层变更记录负责持续迭代，不新增独立运行时或数据库。

**Tech Stack:** Markdown、YAML、PowerShell/Robocopy、Python 结构校验、Node.js/npm、VitePress。

**Spec:** `docs/superpowers/specs/2026-08-20-edu-agents-migration-design.md`

## Global Constraints

- 迁移只复制，不删除、不移动任何源文件。
- 源目录是只读输入；目标路径有冲突时停止并报告，不自动覆盖。
- 精确本机源路径只用于本次执行，不写入仓库文档或 manifest。
- 每个成熟 Agent 主目录必须包含 `AGENT/README.md`、`AGENT/manifest.yaml`、`AGENT/usage.md`、`AGENT/CHANGELOG.md`。
- 根项目和两个受众分类目录都必须有对应的 `AGENT/` 说明层。
- 不复制 `.git`、依赖、缓存、构建结果、临时目录、原始媒体、生成媒体或秘密。
- 不创建或推送 GitHub 远程仓库；只建立本地仓库内容和本地提交。
- 所有验证命令必须从目标 Agent 的新相对路径执行。

---

### Task 1: 建立项目层与受众层骨架

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `AGENT/README.md`
- Create: `AGENT/manifest.yaml`
- Create: `AGENT/usage.md`
- Create: `AGENT/CHANGELOG.md`
- Create: `Teenager/README.md`
- Create: `Teenager/AGENT/README.md`
- Create: `Entrepreneur/README.md`
- Create: `Entrepreneur/AGENT/README.md`
- Create: `Entrepreneur/AGENT/manifest.yaml`
- Create: `Entrepreneur/AGENT/usage.md`
- Create: `Entrepreneur/AGENT/CHANGELOG.md`

**Interfaces:**
- 项目层 `AGENT/manifest.yaml` 注册 `entrepreneur.video-teaching-assistant` 和 `entrepreneur.vibestar-frontend-maintainer`。
- 受众层 `Entrepreneur/AGENT/manifest.yaml` 输出 Entrepreneur Agent 清单和各自目标目录。
- `README.md` 只引用仓库内相对路径，指导贡献者从项目层进入受众层和 Agent 层。

- [ ] **Step 1: 写入项目和分类说明**

  在 `README.md` 说明项目定位、两个受众、当前成熟 Agent 和复制迁移原则；在 `Teenager/README.md` 说明该分类已建立但当前没有成熟 Agent；在 `Entrepreneur/README.md` 说明当前两个 Agent 的交付关系。

- [ ] **Step 2: 写入项目级 Agent 契约**

  `AGENT/README.md` 说明项目级路由和分层文档工作法；`AGENT/manifest.yaml` 写入两个 Agent 的 id、分类、状态、路径、功能摘要和验证命令；`AGENT/usage.md` 写入从受众选择到 Agent 使用的步骤；`AGENT/CHANGELOG.md` 记录首次建立。

- [ ] **Step 3: 写入受众级 Agent 契约**

  `Entrepreneur/AGENT/` 说明 Entrepreneur 的目标、纳入成熟 Agent 的标准、两个 Agent 的协作边界和文档同步规则。`Teenager/AGENT/README.md` 说明当前分类状态和未来新增 Agent 必须遵守的文档模板。

- [ ] **Step 4: 检查骨架路径**

  Run:

  ```powershell
  $required=@(
    'README.md','AGENTS.md','AGENT\README.md','AGENT\manifest.yaml','AGENT\usage.md','AGENT\CHANGELOG.md',
    'Teenager\README.md','Teenager\AGENT\README.md',
    'Entrepreneur\README.md','Entrepreneur\AGENT\README.md','Entrepreneur\AGENT\manifest.yaml',
    'Entrepreneur\AGENT\usage.md','Entrepreneur\AGENT\CHANGELOG.md'
  )
  $missing=$required | Where-Object { -not (Test-Path -LiteralPath $_) }
  if($missing){ throw ('Missing: ' + ($missing -join ', ')) }
  'Project and audience skeleton present'
  ```

  Expected: `Project and audience skeleton present`。

- [ ] **Step 5: Commit**

  ```powershell
  git add -- README.md AGENTS.md AGENT Teenager Entrepreneur
  git commit -m "feat: add EDU_Agents project and audience structure"
  ```

### Task 2: 复制视频助教 Agent 的可复用内容

**Files:**
- Create: `Entrepreneur/video-teaching-assistant/` from source id `courseVedio`
- Preserve: source `AGENTS.md`, `README.md`, `workflow/`, `docs/`, `examples/`, `course-video-pipeline/`, `content/`, `workflow/`
- Exclude from copy: dependency directories, generated media, caches, historical failure archives and build outputs listed below

**Interfaces:**
- Produces a self-contained video Agent functional layer under `Entrepreneur/video-teaching-assistant/`.
- Later Task 4 adds the Agent-level `AGENT/` contract without changing source behavior.

- [ ] **Step 1: Check the destination is absent**

  ```powershell
  $dst='Entrepreneur\video-teaching-assistant'
  if(Test-Path -LiteralPath $dst){ throw "Destination already exists: $dst" }
  New-Item -ItemType Directory -Force -Path $dst | Out-Null
  ```

  Expected: the destination is created only after confirming it did not exist.

- [ ] **Step 2: Copy with explicit exclusions**

  ```powershell
  $src='C:\Users\HI\Documents\ABC_E\Course1\HarnessEngineeringPPT\courseVedio'
  $dst=(Resolve-Path 'Entrepreneur\video-teaching-assistant').Path
  robocopy $src $dst /E /COPY:DAT /DCOPY:DAT /R:0 /W:0 /XJ `
    /XD '.git' 'node_modules' '.npm-cache' '.cache' 'cache' '__pycache__' `
        'PastUselessDoc' 'raw' 'audio' 'publish-package' 'renders' 'frames' `
        'snapshots' 'tmp' 'temp' 'output' 'outputs' 'dist' 'build' 'coverage' `
    /XF '*.mp4' '*.mov' '*.mkv' '*.wav' '*.mp3' '*.m4a' '*.aac' '*.dll' `
        '*.dylib' '*.so' '*.exe' '*.wasm' '*.node' '*.pyc'
  if($LASTEXITCODE -gt 7){ throw "Robocopy failed with exit code $LASTEXITCODE" }
  ```

  Expected: Robocopy exit code 0–7; no source file is modified or removed.

- [ ] **Step 3: Confirm reusable pipeline files are present**

  ```powershell
  $required=@(
    'Entrepreneur\video-teaching-assistant\AGENTS.md',
    'Entrepreneur\video-teaching-assistant\README.md',
    'Entrepreneur\video-teaching-assistant\workflow',
    'Entrepreneur\video-teaching-assistant\course-video-pipeline\SKILL.md',
    'Entrepreneur\video-teaching-assistant\course-video-pipeline\scripts\validate_course_video.py',
    'Entrepreneur\video-teaching-assistant\examples\harness-engineering\artifact-map.yaml'
  )
  $missing=$required | Where-Object { -not (Test-Path -LiteralPath $_) }
  if($missing){ throw ('Missing video Agent files: ' + ($missing -join ', ')) }
  ```

- [ ] **Step 4: Commit the copied functional layer**

  ```powershell
  git add -- Entrepreneur/video-teaching-assistant
  git commit -m "feat: migrate reusable video teaching assistant"
  ```

### Task 3: 复制 Vibestar 教学前端维护 Agent

**Files:**
- Create: `Entrepreneur/vibestar-frontend-maintainer/site/` from `vibestar-github-pages-knowledge-base`
- Preserve: `package.json`, `package-lock.json`, `docs/`, `.github/workflows/`
- Exclude: `.git`, `node_modules`, `docs/.vitepress/cache`, `docs/.vitepress/dist`, `logo.png`

**Interfaces:**
- Produces a standalone VitePress site that can be installed and built from `site/`.
- The Agent-level docs in Task 4 describe site maintenance without relying on source absolute paths.

- [ ] **Step 1: Check the destination is absent**

  ```powershell
  $dst='Entrepreneur\vibestar-frontend-maintainer\site'
  if(Test-Path -LiteralPath $dst){ throw "Destination already exists: $dst" }
  New-Item -ItemType Directory -Force -Path $dst | Out-Null
  ```

- [ ] **Step 2: Copy the VitePress source**

  ```powershell
  $src='C:\Users\HI\Documents\New project 5\agents\knowledge-base-builder\deliverables\vibestar-github-pages-knowledge-base'
  $dst=(Resolve-Path 'Entrepreneur\vibestar-frontend-maintainer\site').Path
  robocopy $src $dst /E /COPY:DAT /DCOPY:DAT /R:0 /W:0 /XJ `
    /XD '.git' 'node_modules' 'cache' 'dist' `
    /XF 'logo.png' '*.zip'
  if($LASTEXITCODE -gt 7){ throw "Robocopy failed with exit code $LASTEXITCODE" }
  ```

- [ ] **Step 3: Confirm VitePress source files are present**

  ```powershell
  $required=@(
    'Entrepreneur\vibestar-frontend-maintainer\site\package.json',
    'Entrepreneur\vibestar-frontend-maintainer\site\package-lock.json',
    'Entrepreneur\vibestar-frontend-maintainer\site\docs\index.md',
    'Entrepreneur\vibestar-frontend-maintainer\site\docs\.vitepress\config.mts',
    'Entrepreneur\vibestar-frontend-maintainer\site\.github\workflows\deploy.yml'
  )
  $missing=$required | Where-Object { -not (Test-Path -LiteralPath $_) }
  if($missing){ throw ('Missing Vibestar files: ' + ($missing -join ', ')) }
  ```

- [ ] **Step 4: Commit the copied site source**

  ```powershell
  git add -- Entrepreneur/vibestar-frontend-maintainer/site
  git commit -m "feat: migrate Vibestar frontend source"
  ```

### Task 4: 为两个成熟 Agent 补齐分层说明和注册信息

**Files:**
- Create: `Entrepreneur/video-teaching-assistant/AGENT/README.md`
- Create: `Entrepreneur/video-teaching-assistant/AGENT/manifest.yaml`
- Create: `Entrepreneur/video-teaching-assistant/AGENT/usage.md`
- Create: `Entrepreneur/video-teaching-assistant/AGENT/CHANGELOG.md`
- Create: `Entrepreneur/vibestar-frontend-maintainer/AGENT/README.md`
- Create: `Entrepreneur/vibestar-frontend-maintainer/AGENT/manifest.yaml`
- Create: `Entrepreneur/vibestar-frontend-maintainer/AGENT/usage.md`
- Create: `Entrepreneur/vibestar-frontend-maintainer/AGENT/CHANGELOG.md`
- Modify: `AGENT/manifest.yaml`
- Modify: `Entrepreneur/AGENT/manifest.yaml`
- Modify: `AGENT/CHANGELOG.md`
- Modify: `Entrepreneur/AGENT/CHANGELOG.md`

**Interfaces:**
- `video-teaching-assistant/AGENT/usage.md` describes the fixed order: inventory → transcript → script → voice → word alignment → semantic timing → pilot → render → subtitles → release QA.
- `vibestar-frontend-maintainer/AGENT/usage.md` describes: classify update → edit VitePress source → update navigation → run install/build → record handoff → review deploy workflow.
- Both manifests use the fields `id`, `audience`, `status`, `source_id`, `capabilities`, `inputs`, `outputs`, `validation_commands`, `excluded_from_copy`, `privacy_boundary`, and `documentation_layers`.
- No manifest contains a local absolute path.

- [ ] **Step 1: Write the video Agent contract**

  State that the Agent owns reproducible course-video production and its output is a validated project/release package, not an automatic guarantee of a finished public video. Include inputs, canonical artifacts, quality gates, human approval points, tool dependencies, prohibited secrets/media, and the copied source id `courseVedio`.

- [ ] **Step 2: Write the Vibestar Agent contract**

  State that the Agent owns the learning knowledge base and GitHub Pages VitePress site. Include page categories, inputs, outputs, Windows/Mac command documentation requirements, `npm run build` as the acceptance command, deployment boundary, and copied source id `knowledge-base-builder`.

- [ ] **Step 3: Add usage examples and change records**

  Each `usage.md` must show commands relative to its target directory and a minimum successful handoff. Each `CHANGELOG.md` must record the initial migration, excluded generated files, validation status, and next documented change rule.

- [ ] **Step 4: Update both registries**

  Add paths, capabilities, maturity status, and validation commands to project and Entrepreneur manifests. Keep the Teenager registry empty but documented.

- [ ] **Step 5: Verify documentation links and fields**

  ```powershell
  $required=@(
    'Entrepreneur\video-teaching-assistant\AGENT\README.md',
    'Entrepreneur\video-teaching-assistant\AGENT\manifest.yaml',
    'Entrepreneur\video-teaching-assistant\AGENT\usage.md',
    'Entrepreneur\video-teaching-assistant\AGENT\CHANGELOG.md',
    'Entrepreneur\vibestar-frontend-maintainer\AGENT\README.md',
    'Entrepreneur\vibestar-frontend-maintainer\AGENT\manifest.yaml',
    'Entrepreneur\vibestar-frontend-maintainer\AGENT\usage.md',
    'Entrepreneur\vibestar-frontend-maintainer\AGENT\CHANGELOG.md'
  )
  $missing=$required | Where-Object { -not (Test-Path -LiteralPath $_) }
  if($missing){ throw ('Missing Agent docs: ' + ($missing -join ', ')) }
  $absolute=rg -n 'C:\\Users\\HI\\Documents\\(ABC_E|New project 5)' --glob '*.md' --glob '*.yaml' . 2>$null
  if($LASTEXITCODE -eq 0){ throw "Absolute source path found:`n$absolute" }
  ```

- [ ] **Step 6: Commit the Agent contracts**

  ```powershell
  git add -- AGENT Entrepreneur/AGENT Entrepreneur/video-teaching-assistant/AGENT Entrepreneur/vibestar-frontend-maintainer/AGENT
  git commit -m "docs: add layered Agent usage contracts"
  ```

### Task 5: 固化 Git 忽略规则和迁移来源记录

**Files:**
- Create: `.gitignore`
- Modify: `AGENTS.md`
- Modify: both Agent manifests and changelogs when the final copied counts are known

**Interfaces:**
- `.gitignore` protects future iterations from committing generated media, dependencies, caches, secrets and local build output.
- `AGENTS.md` documents copy-only migration, per-layer documentation updates, and no-source-deletion policy.

- [ ] **Step 1: Add repository-wide ignore rules**

  Ignore `.env*` except `.env.example`, all `node_modules`, `.git` below imported content, VitePress cache/dist, video/audio extensions, raw media, renders, frames, caches, `PastUselessDoc`, `.npm-cache`, Python caches and OS metadata.

- [ ] **Step 2: Add contributor rules**

  `AGENTS.md` must require updating project, audience and Agent documentation for each new Agent; require relative paths and secrets hygiene; and forbid deleting or moving source files during future migrations.

- [ ] **Step 3: Record final copy statistics**

  Use `Get-ChildItem` to record source id, copied file count, excluded categories and target file count in each Agent manifest without writing local absolute paths.

- [ ] **Step 4: Commit repository policy**

  ```powershell
  git add -- .gitignore AGENTS.md AGENT Entrepreneur/AGENT Entrepreneur/*/AGENT
  git commit -m "chore: enforce repository migration and hygiene rules"
  ```

### Task 6: Run full migration verification

**Files:**
- Verify: all repository files and both source directories
- No source file is modified by this task.

**Interfaces:**
- Produces evidence for structural integrity, exclusion policy, source preservation and Agent-specific build checks.

- [ ] **Step 1: Verify source directories still exist**

  ```powershell
  $sources=@(
    'C:\Users\HI\Documents\ABC_E\Course1\HarnessEngineeringPPT\courseVedio',
    'C:\Users\HI\Documents\New project 5\agents\knowledge-base-builder'
  )
  foreach($source in $sources){ if(-not (Test-Path -LiteralPath $source)){ throw "Source missing: $source" } }
  'Both source directories remain present'
  ```

- [ ] **Step 2: Check forbidden files are absent from the target**

  ```powershell
  $bad=Get-ChildItem -Recurse -File -Force | Where-Object {
    $_.FullName -notmatch '\\.git\\' -and (
      $_.FullName -match '\\(node_modules|PastUselessDoc|\.npm-cache|\.cache|cache|dist|build|raw|renders?|frames|audio_alignment)(\\|$)' -or
      $_.Extension.ToLower() -in @('.mp4','.mov','.mkv','.wav','.mp3','.m4a','.aac','.dll','.dylib','.so','.exe','.wasm','.node','.pyc')
    )
  }
  if($bad){ $bad | Select-Object -ExpandProperty FullName; throw 'Forbidden generated/dependency files found in target' }
  'Target exclusion check passed'
  ```

- [ ] **Step 3: Run video Agent structure validation**

  ```powershell
  python .\Entrepreneur\video-teaching-assistant\course-video-pipeline\scripts\validate_course_video.py .\Entrepreneur\video-teaching-assistant
  ```

  Expected: the validator exits 0 in repository mode and checks the copied workflow, Skill references and public YAML/JSON artifacts.

- [ ] **Step 4: Install and build the Vibestar site**

  ```powershell
  Push-Location .\Entrepreneur\vibestar-frontend-maintainer\site
  npm install
  npm run build
  Pop-Location
  ```

  Expected: npm install completes from `package-lock.json`; VitePress build exits 0. Generated `node_modules` and `.vitepress/dist` remain ignored and are not committed.

- [ ] **Step 5: Run repository checks**

  ```powershell
  git diff --check
  git status --short --branch
  $absolute=rg -n 'C:\\Users\\HI\\Documents\\(ABC_E|New project 5)|/Users/|/home/|[A-Za-z]:\\Users\\' --glob '*.md' --glob '*.yaml' --glob '*.json' . 2>$null
  if($LASTEXITCODE -eq 0){ throw "Local absolute path found:`n$absolute" }
  ```

  Expected: no whitespace errors, no local absolute paths in tracked documentation/configuration, and only intended files are present.

- [ ] **Step 6: Commit the verified baseline**

  ```powershell
  git add --all
  git commit -m "chore: verify EDU_Agents migrated baseline"
  ```

  Do not run `git push` or add a remote.

## Verification Checklist

- [ ] Root project, `Teenager`, `Entrepreneur`, and both mature Agent directories have the required `AGENT/` documentation.
- [ ] Project and Entrepreneur manifests locate both Agent directories.
- [ ] Video pipeline source and reusable Skill files exist; generated media and dependencies are absent.
- [ ] Vibestar VitePress source, lock file and deployment workflow exist; dependencies and build output are absent from Git.
- [ ] Both source directories still exist after migration.
- [ ] Video structure validation exits 0.
- [ ] Vibestar `npm run build` exits 0.
- [ ] `git diff --check` and absolute-path scan are clean.
- [ ] Local commits exist; no remote is created or pushed.
