# 第 3 章｜Plan and Execute 与 Multi-Agent：把复杂任务拆开

版本：v02  
状态：已批准  
章节学习结果：能判断何时需要计划或角色协作

## 段落 1｜Plan and Execute

Plan and Execute 先生成完整计划，再按步骤执行。它让流程更稳定，适合代码生成和长流程自动化；但计划如果一开始就错，后面的执行会把错误放大，灵活性也不如 ReAct。

## 段落 2｜Multi-Agent

Multi-Agent 再进一步，把任务分给不同角色，例如 Planner、Executor 和 Reviewer。这样上下文边界更清楚，复杂流程更容易扩展，代价是调用成本、协作协议和失败处理都会增加。它适合对流程一致性要求高的行业任务。

## 动画意图

- 先画出计划树，再沿步骤 1、2、3 顺序执行。
- 计划错误时只让错误标记沿执行链传播，避免整页突然跳变。
- Multi-Agent 先出现协调器，再逐个出现 Planner、Executor、Reviewer，最后显示成本提示。
