# 视频助教 Agent

## 功能定位

视频助教 Agent 把原始视频、音频、访谈、长文或已有 PPT，整理成可验证、可复用的分章课程视频生产项目。它的核心价值是维护内容、声音、语义时间、动画、字幕和发布之间的质量门禁，而不是直接承诺自动生成最终成片。

## 适用场景

- 需要把一段课程素材拆成章节并形成讲稿；
- 需要根据最终配音建立逐词时间轴和语义锚点；
- 需要制作与讲解同步的 PPT 风格动画和字幕；
- 需要为课程视频建立可复用的发布包、检查表和返工记录。

## 不适用场景

- 只想快速生成一条不需要审核的短视频；
- 没有版权或授权的原始素材；
- 需要把私人 Voice ID、训练音频、数字人源视频或 API Token 放进仓库；
- 需要绕过最终音频、字幕和人工审核直接锁定动画时间。

## 输入

- 原始视频、音频、文章、访谈或已有 PPT；
- 目标受众、发布平台和课程目标；
- 术语表、品牌视觉规范和已批准的声线配置；
- 必要时的转录、时间码和素材版权清单。

## 输出

- `asset-inventory.yaml`、`canonical-transcript.md`、`terminology.yaml`；
- 版本化的 `SCRIPT.md`、`tone-plan.yaml` 和音频 manifest；
- `word-alignment.yaml`、`semantic-anchor-plan.yaml`、`semantic-timing-manifest.yaml`；
- 动画源、布局审查、字幕 manifest、媒体报告和发布包；
- 失败证据、最小返工记录和可回写到 Harness 的规则。

## 工作流入口

- [端到端制作流程](../docs/01_端到端制作流程.md)
- [课程视频工作流](../workflow/course-video-workflow.yaml)
- [可复用 Skill](../course-video-pipeline/SKILL.md)
- [项目模板](../course-video-pipeline/assets/project-template/)

## 验收原则

内容和术语先冻结，最终配音确定后再建立真实时间轴；先完成 15–20 秒高风险试片，再扩展到章节；布局、语义、音频、字幕和发布包分别通过检查后才进入下一阶段。任何返工只修改最小失败 artifact，不通过重做整章掩盖局部问题。

## 维护边界

本 Agent 维护可复用的工作流、Skill、模板、检查脚本和脱敏示例。原始媒体、生成视频/音频、依赖、缓存、失败归档和私人凭据留在源环境，不进入 Git。
