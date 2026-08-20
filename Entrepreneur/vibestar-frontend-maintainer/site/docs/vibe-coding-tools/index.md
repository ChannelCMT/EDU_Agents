# 工具跑通

这一页先帮助你把 Vibe Coding 的基础工具装好，并建立命令行和环境意识。目标不是一次掌握所有技术细节，而是让电脑具备“能编辑、能运行、能让 AI 接管任务、能保存版本”的基本能力。

## 1. 安装教程

### 你需要安装什么

<table class="tool-table">
  <thead>
    <tr>
      <th>工具</th>
      <th>用途</th>
      <th>官方下载</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>VS Code</td>
      <td>代码编辑器，也是本课程的主要操作界面。</td>
      <td><a href="https://code.visualstudio.com/download" target="_blank" rel="noreferrer">下载 VS Code</a></td>
    </tr>
    <tr>
      <td>Miniconda</td>
      <td>轻量级 Python 与 conda 环境管理工具，用来安装 Python、管理依赖并保持环境干净。</td>
      <td><a href="https://www.anaconda.com/docs/getting-started/miniconda/install" target="_blank" rel="noreferrer">下载 Miniconda</a></td>
    </tr>
    <tr>
      <td>Codex 桌面版</td>
      <td>OpenAI 的 AI 编程助手桌面应用，用来连接项目、对话式修改文件和执行任务。</td>
      <td><a href="https://chatgpt.com/zh-Hans-CN/download/?openaicom_referred=true" target="_blank" rel="noreferrer">下载 Codex 桌面版</a></td>
    </tr>
    <tr>
      <td>Git</td>
      <td>版本管理工具，用来记录修改、回退版本，并把项目上传到 GitHub。</td>
      <td><a href="https://git-scm.com/downloads" target="_blank" rel="noreferrer">下载 Git</a></td>
    </tr>
  </tbody>
</table>

### Windows 安装步骤

<section class="tool-steps">
  <article>
    <strong>01</strong>
    <h3>安装 VS Code</h3>
    <p>打开 VS Code 官方下载页，选择 Windows 版本。安装时建议勾选 <code>Add to PATH</code> 和 <code>Open with Code</code>，方便后续从文件夹或终端打开项目。</p>
  </article>
  <article>
    <strong>02</strong>
    <h3>安装 Miniconda</h3>
    <p>下载 Windows 版 Miniconda。安装时注意勾选添加到环境变量或 PATH 的选项。安装完成后重新打开 PowerShell 或 Miniconda 终端，输入 <code>python --version</code> 和 <code>conda --version</code> 检查环境。</p>
  </article>
  <article>
    <strong>03</strong>
    <h3>安装 Codex 桌面版</h3>
    <p>打开 ChatGPT 下载页，找到 Codex 下载入口，选择 Windows 版本下载安装。安装完成后使用你的 ChatGPT 账号登录，确认可以看到项目列表和新建对话入口。</p>
  </article>
  <article>
    <strong>04</strong>
    <h3>安装 Git</h3>
    <p>从 Git 官网下载 Windows 安装包。大部分选项保持默认即可。安装完成后打开 PowerShell 或 Git Bash，输入 <code>git --version</code> 检查是否安装成功。</p>
  </article>
</section>

### macOS 安装步骤

<section class="tool-steps">
  <article>
    <strong>01</strong>
    <h3>安装 VS Code</h3>
    <p>打开 VS Code 官方下载页，选择 macOS 版本。Apple 芯片选择 Apple silicon，Intel 芯片选择 Intel，也可以使用 Universal 版本。</p>
  </article>
  <article>
    <strong>02</strong>
    <h3>安装 Miniconda</h3>
    <p>从 Miniconda 官方安装页下载 macOS 版本。安装完成后打开 Terminal，输入 <code>python --version</code> 和 <code>conda --version</code> 检查。</p>
  </article>
  <article>
    <strong>03</strong>
    <h3>安装 Codex 桌面版</h3>
    <p>打开 ChatGPT 下载页，找到 Codex 下载入口，选择 macOS 版本下载安装。完成安装后登录 ChatGPT 账号，先确认能创建项目并在对话中读取本地文件夹。</p>
  </article>
  <article>
    <strong>04</strong>
    <h3>安装 Git</h3>
    <p>打开 Terminal，先输入 <code>git --version</code>。如果系统提示安装 Command Line Tools，按提示安装即可；也可以从 Git 官网下载安装包。</p>
  </article>
</section>

::: tip 完成标准
你能打开 VS Code，能在命令行看到 `python --version`、`conda --version`、`git --version` 的结果，并且能登录 Codex 桌面版。
:::

## 2. 认知导入：为什么 AI 学习必须学会环境和 CLI

停留在对话式 AI 阶段，你可以让 AI 写方案、写文案、做总结。但一旦你想让 AI 真正替你完成可运行、可复用、可交付的工作，就必须让它进入你的工作环境。

### 从“会聊天”到“会交付”的关键差异

| 学习阶段 | 你能做什么 | 主要限制 |
| --- | --- | --- |
| 对话式 AI | 提问、写文案、改表达、生成思路。 | 结果多停留在文本，难以直接运行和长期维护。 |
| 本地工具 + AI | 让 AI 读写文件、运行代码、调试错误、整理项目。 | 需要知道文件在哪里、命令怎么跑、错误怎么反馈。 |
| Agent 工作流 | 把重复任务拆成流程，让 AI 按步骤执行和交付。 | 需要环境、依赖、版本和权限管理能力。 |

### 环境是什么

环境不是一个抽象概念，它就是你的电脑当前能使用哪些工具、能找到哪些命令、能读取哪些文件、能运行哪些程序。AI 要帮你做真正的工作，也需要这些环境能力。

- **编辑环境：**用 VS Code 打开项目、查看文件、修改内容。
- **运行环境：**用 Python、Node.js 或其他工具执行程序。
- **依赖环境：**用 conda、npm 等工具安装项目需要的包。
- **版本环境：**用 Git 保存修改记录，避免改坏后无法回退。

### CLI 是什么

CLI 是 Command Line Interface，也就是命令行界面。你可以把它理解成用文字指挥电脑的控制台。很多开发工具、AI 工具和自动化工具，最稳定、最完整的能力都先出现在 CLI 里。

| 问题 | 说明 |
| --- | --- |
| 为什么要学 CLI | 因为它可以精确表达任务：进入哪个文件夹、运行哪个工具、安装哪个依赖、看到什么错误。 |
| 为什么 AI 需要 CLI | AI 可以通过命令行执行检查、测试、构建、部署等步骤，让结果从“写出来”变成“跑起来”。 |

### 学习目标

1. 知道当前项目在哪个文件夹。
2. 能用命令行进入目标文件夹。
3. 能检查一个工具是否安装成功。
4. 能把报错复制给 AI，让 AI 判断下一步。
5. 能理解安装、运行、测试、提交这几个动作的区别。

::: warning 心态提醒
命令行不是程序员专属技能，而是 AI 时代的基础操作能力。你不需要背大量命令，但要学会识别当前路径、复制错误信息、按步骤执行验证。
:::

## 3. Windows 命令行入门

Windows 用户建议先使用 PowerShell。它是系统自带工具，适合检查环境、进入文件夹、运行 Python、使用 Git 和启动 AI 工具。

### 打开 PowerShell

1. 点击开始菜单，搜索 `PowerShell`。
2. 打开后会看到一个可以输入文字的窗口。
3. 第一行通常会显示当前所在文件夹，例如“你的用户目录”。

### 最常用的 8 个命令

| 目的 | 命令 | 说明 |
| --- | --- | --- |
| 创建文件夹 | `mkdir 文件夹名` | 新建一个项目目录。 |
| 查看当前位置 | `Get-Location` | 确认你现在站在哪个文件夹里。 |
| 进入文件夹 | `cd 文件夹路径` | 切换到目标项目文件夹。 |
| 回到上一级 | `cd ..` | 从当前文件夹退回上一层。 |
| 显示当前文件目录 | `ls` | 查看当前文件夹下有什么文件和子文件夹。 |
| 检查 Python | `python --version` | 确认 Python 是否能被系统找到。 |
| 检查 conda | `conda --version` | 确认 Miniconda 是否配置成功。 |
| 检查 Git | `git --version` | 确认 Git 是否安装成功。 |

### 推荐练习：创建一个测试项目

```powershell
mkdir vibe-star-test
cd vibe-star-test
Get-Location
ls
python --version
conda --version
git --version
```

### 运行一段 Python 代码

在 PowerShell 中直接输入 `python` 进入 Python 交互环境：

```powershell
python
```

看到 `>>>` 之后，输入：

```python
print('hi')
```

如果屏幕输出 `hi`，说明 Python 已经可以运行。结束时输入 `exit()` 回到 PowerShell。

### 常见问题

::: tip
**python 无法识别：**可能是 Miniconda 没有加入 PATH，或安装后没有重新打开 PowerShell。先关闭 PowerShell，再重新打开检查。

**cd 失败：**路径里有空格时，用英文引号包住路径，例如 <code>cd "你的课程文件夹"</code>。

**权限问题：**不要把课程项目放在系统目录，建议放在桌面或 Documents。
:::

## 4. Mac 命令行入门

macOS 用户建议使用 Terminal。Terminal 是系统自带的命令行工具，后续安装、运行、检查和 Git 操作都会经常用到。

### 打开 Terminal

1. 按 `Command + Space` 打开 Spotlight 搜索。
2. 输入 `Terminal` 或 `终端`。
3. 回车打开后，你就可以输入命令。

### 最常用的 8 个命令

| 目的 | 命令 | 说明 |
| --- | --- | --- |
| 创建文件夹 | `mkdir 文件夹名` | 新建一个项目目录。 |
| 查看当前位置 | `pwd` | 确认你现在站在哪个文件夹里。 |
| 进入文件夹 | `cd 文件夹路径` | 切换到目标项目文件夹。 |
| 回到上一级 | `cd ..` | 从当前文件夹退回上一层。 |
| 显示当前文件目录 | `ls` | 查看当前文件夹下有什么文件和子文件夹。 |
| 检查 Python | `python3 --version` | macOS 常用 `python3` 检查 Python。 |
| 检查 conda | `conda --version` | 确认 Miniconda 是否配置成功。 |
| 检查 Git | `git --version` | 第一次运行可能会提示安装 Command Line Tools。 |

### 推荐练习：创建一个测试项目

```bash
mkdir vibe-star-test
cd vibe-star-test
pwd
ls
python3 --version
conda --version
git --version
```

### 运行一段 Python 代码

在 Terminal 中直接输入 `python3` 进入 Python 交互环境：

```bash
python3
```

看到 `>>>` 之后，输入：

```python
print('hi')
```

如果屏幕输出 `hi`，说明 Python 已经可以运行。结束时输入 `exit()` 回到 Terminal。

### 常见问题

::: tip
**conda 无法识别：**可能需要关闭 Terminal 后重新打开，或者根据 Miniconda 安装提示执行初始化命令。

**权限弹窗：**如果系统提示 Terminal 或 Codex 访问文件夹权限，需要允许访问课程项目所在目录。

**Apple silicon 与 Intel：**下载工具时注意选择与你电脑芯片匹配的版本。
:::
