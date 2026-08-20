# EDU_Agents Contributor Rules

## 项目工作法

- 本仓库按 `Teenager` 和 `Entrepreneur` 管理教育培训 Agent。
- 每个成熟 Agent 的主目录必须包含 `AGENT/`，至少提供功能与使用说明。
- 新增或修改 Agent 时，必须同步检查项目层、受众层、Agent 层和功能层文档。
- `AGENT/manifest.yaml` 是 Agent 的机器可读注册信息；`AGENT/README.md` 是功能说明；`AGENT/usage.md` 是操作说明；`AGENT/CHANGELOG.md` 是迭代记录。

## 复制迁移规则

- 迁移只允许复制，不允许删除或移动源文件。
- 源目录只作为只读输入；目标路径发生冲突时先停止并报告，不自动覆盖。
- 迁移时可以排除依赖、缓存、构建结果、原始媒体、生成媒体和失败归档，但排除不等于删除，源文件必须继续保留。
- 仓库文档和 manifest 不写入本机绝对路径；使用 `source_id`、相对路径和目录名称描述来源。

## 安全与提交边界

- 不提交 API Token、密钥、私人 Voice ID、个人声纹、未授权媒体或本机配置。
- 不提交 `node_modules`、视频/音频、临时帧、VitePress 构建目录和工具缓存。
- 修改前后运行对应 Agent 的验证命令，并在 Agent 层 `CHANGELOG.md` 写明结果。
- 公开仓库发布前，检查绝对路径、秘密、第三方素材许可和大文件。

## 新增 Agent 的最小流程

1. 在项目层注册 Agent 和受众路由。
2. 在受众层补充定位、清单和协作边界。
3. 创建 Agent 主目录和 `AGENT/` 说明目录。
4. 写清输入、输出、使用流程、验收命令、隐私边界和排除项。
5. 迁移或创建功能层源码，运行验证并记录变更。
