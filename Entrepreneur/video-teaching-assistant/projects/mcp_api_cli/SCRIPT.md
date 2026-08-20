# MCP、API、SDK、CLI、Function Calling、Tool Calling、ADK：一张图看懂 AI Agent 技术栈

版本：v01（3 分 30 秒审核稿）  
用途：先审核讲稿与 PPT/动画分镜，暂不生成配音和 MP4。

## 总纲

这 7 个词不是 7 个互相替代的产品。它们分别回答四个问题：软件怎样提供能力，模型怎样选择能力，AI 怎样标准化连接能力，以及 Agent 怎样被组织起来。

## Scene 01｜开场：为什么总是混在一起（0:00–0:16）

你是不是也遇到过这种情况：刚开始做 Agent，就被 API、SDK、CLI、MCP、Function Calling、Tool Calling、ADK 这几个词绕晕。它们看起来都和“调用工具”有关，但其实根本不在同一层。今天用一张图，把它们放回各自的位置。

## Scene 02｜先看总地图（0:16–0:40）

先记住这条主线：最上面是用户和 Agent 应用，下面是 ADK，负责把模型、工具、状态和流程组织起来。再往下是 LLM 和 Tool Calling，决定模型什么时候要用能力。最底层才是 API、SDK、CLI，以及 MCP 连接的外部系统。这样一来，七个词就不再是并列清单，而是一条调用链上的不同位置。

## Scene 03｜API、SDK、CLI：软件怎样使用能力（0:40–1:03）

API 解决的是：软件 A 怎么调用软件 B。比如程序请求订单接口，得到一段 JSON。SDK 是把 URL、认证、重试和错误处理封装起来，让开发者可以直接写 `client.orders.get`。CLI 则是另一种入口，让人、脚本，甚至 Agent 在终端里执行 `gh pr list` 或 `docker ps`。所以 API、SDK、CLI 通常不是竞争关系，而是同一个服务的三种使用方式。

## Scene 04｜Function Calling、Tool Calling：模型怎样决定调用（1:03–1:28）

普通模型只能输出文字。加入 Function Calling 后，模型可以先输出一个结构化请求：调用 `get_weather`，参数是 Tokyo。真正执行函数的，仍然是应用程序。Tool Calling 是更大的总称，函数、网页搜索、文件搜索、电脑操作和 MCP 工具，都可以被看成 Tool。记住：Function 是 Tool 的一种具体形式。

## Scene 05｜MCP：把外部能力接得更标准（1:28–1:55）

当一个 Agent 要连接 GitHub、Slack、Notion、数据库时，传统做法是每接一个系统，就写一套认证、Schema、调用和错误处理，最后变成一团适配器。MCP 解决的不是某一个 API，而是连接方式。AI 应用通过 MCP Client 连接 MCP Server，统一发现 Tools、Resources 和 Prompts。可以把 MCP 理解成 AI 工具世界的 USB-C：它不是设备本身，而是让连接更标准。

## Scene 06｜MCP 不取代 API，ADK 也不是另一种接口（1:55–2:20）

MCP 往往仍然会调用后面的 API、SDK、CLI、数据库或文件系统。它做的是把这些能力用统一方式交给 AI。ADK 则在更上面：它负责 Agent 的状态、工作流、回调、多 Agent 协作和评测。换句话说，MCP 解决“怎么接工具”，ADK 解决“怎么把 Agent 组织起来”。

## Scene 07｜一个订单案例串起全部层级（2:20–2:50）

用户说：帮我查订单 123，如果还没发货就退款。ADK 负责组织整个流程，LLM 通过 Tool Calling 选择查询订单工具。这个工具可以是 Function，也可以来自 MCP Server。MCP Server 下面再调用订单 SDK 或 API，读取数据库。状态返回未发货后，Agent 再调用退款工具，最后把结果交给用户。你看到的不是七种技术互相替代，而是同一个任务穿过不同层级。

## Scene 08｜七句话记忆法（2:50–3:14）

API，是软件之间的能力契约。SDK，让开发者更方便地使用 API。CLI，让人或脚本通过命令行操作软件。Function Calling，让模型产生结构化函数请求。Tool Calling，是模型使用外部能力的总机制。MCP，让 AI 用统一协议连接工具和数据。ADK，把模型、工具、状态和流程组织成完整 Agent。

## Scene 09｜收束：以后先问它属于哪一层（3:14–3:30）

以后再看到这些词，不要先问谁能替代谁。先问三个问题：它属于哪一层？它连接的是谁？它解决的是调用、连接，还是编排？把它们放回这张地图里，AI Agent 技术栈就清楚了。

## 讲稿审查规则

- 开头 5 秒先讲受众困惑，不先抛陌生术语。
- 所有英文术语第一次出现时，紧跟一句中文解释。
- 口播中的 7 个术语必须和 PPT 文案逐字一致：API、SDK、CLI、Function Calling、Tool Calling、MCP、ADK。
- 每个动画节点只承载一个语义动作；先显示关系，再显示结论。
- 语速目标：约 210–230 个中文字符/分钟；实际配音后必须以词级时间轴重新校准。
- 字幕采用单行、5–14 个汉字或等价短语，底部预留半透明字幕安全区。

