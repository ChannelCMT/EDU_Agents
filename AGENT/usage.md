# 项目级 Agent 使用说明

## 选择流程

1. 明确学习者类型：青少年进入 `Teenager/`，企业家进入 `Entrepreneur/`。
2. 查看受众目录下的 `AGENT/README.md` 和 `AGENT/manifest.yaml`。
3. 进入具体 Agent 主目录，先读 `AGENT/README.md`，再读 `AGENT/usage.md`。
4. 按功能目录中的原始工作流执行，不能只根据 Agent 名称猜测输入输出。
5. 运行 `manifest.yaml` 中登记的验收命令。
6. 把本次修改写入 Agent 层 `CHANGELOG.md`，必要时同步更新受众层和项目层。

## 新增 Agent 记录流程

新增一个成熟 Agent 时，依次完成：

1. 项目级 `AGENT/manifest.yaml` 增加唯一 id、受众、路径、状态和验证命令。
2. 受众级说明增加 Agent 清单、定位和与现有 Agent 的边界。
3. Agent 主目录创建 `AGENT/README.md`、`manifest.yaml`、`usage.md`、`CHANGELOG.md`。
4. 功能层记录真实工作流、输入、输出、失败回路和验收标准。
5. 运行验证，并在各层文档中更新当前状态。

## 隐私边界

公开仓库只记录来源标识和相对路径，不记录本机绝对路径。大媒体、依赖、缓存、秘密和未授权素材留在源环境，不进入仓库。
