# 视频助教 Agent 使用说明

## 1. 先确认输入

明确目标受众、课程目标、发布平台、素材版权和需要交付的横竖版规格。建立素材清单和术语表，不要直接把整段文稿交给动画工具。

## 2. 初始化课程项目

在 `Entrepreneur/video-teaching-assistant/` 下执行：

```powershell
python .\course-video-pipeline\scripts\init_course_project.py --output .\work\demo --title "我的课程" --chapters 1
python .\course-video-pipeline\scripts\validate_course_video.py .\work\demo --structure-only
```

## 3. 按固定顺序生产

1. 素材盘点、规范化转录和术语表；
2. 课程结构、章节 `SCRIPT.md` 和语气规划；
3. 生成并人工确认最终配音；
4. 用最终音频建立逐词对齐和语义锚点；
5. 选择高风险片段制作 15–20 秒试片；
6. 通过试片后实现章节动画、布局检查和渲染；
7. 依据真实音频生成字幕、合并媒体并生成发布包。

完整阶段、角色和失败回路以 `workflow/course-video-workflow.yaml` 为准。

## 4. 验收

对 Agent 根目录执行：

```powershell
python .\course-video-pipeline\scripts\validate_course_video.py .
```

验收时还要人工确认：术语读音、语义与画面同步、布局安全区、字幕词序、音频轨道数量、封面裁切和发布文案。

## 5. 交付记录

每次修改完成后，在本目录的 `CHANGELOG.md` 记录改动范围、验证命令、失败证据和后续需要更新的流程规则；如果输入、输出或验收标准变化，还要同步更新 `manifest.yaml` 和上层 Agent 说明。
