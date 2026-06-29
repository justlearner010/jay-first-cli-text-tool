# 项目开发流程回顾

项目名称：`jay-first-cli-text-tool`

开发周期：2026-05-14 至 2026-06-28

项目定位：Python CLI 工程化入门项目。它记录了我从 Python 基础脚本练习，逐步走向可安装、可测试、有 GitHub Issue / PR / CI 流程的小型命令行工具的过程。

## 阶段一：脚本练习阶段

时间：2026-05-14 起

最早的版本保存在 [`jay-ai-agent-roadmap-archive/python-foundations/first-CLI`](https://github.com/justlearner010/jay-ai-agent-roadmap-archive/tree/main/python-foundations/first-CLI)。

这一阶段的项目还不是标准 Python 包，更像是 Python 基础阶段的综合练习。入口是 `src/main.py`，通过 `argparse` 读取命令行参数，然后调用多个模块完成文本处理任务。

当时已经实现的能力包括：

- 读取文本文件。
- 统计行数、单词数、空格数、数字数。
- 统计高频词。
- 按固定字符长度切分文本。
- 生成 JSON 输出。
- 使用 mock summary 模拟后续 LLM 总结能力。

这一阶段的重点不是架构，而是把文件读取、字符串处理、`argparse`、`pytest`、`pathlib`、`json`、`logging` 等基础能力串起来。

这个阶段已经开始有测试意识。归档版本 README 中记录的测试状态是：

```text
30 passed, 1 xfailed
```

这说明项目已经不是一次性脚本，而是开始向“可验证的小工具”过渡。

## 阶段二：独立仓库与包结构整理

后续项目从归档仓库中的练习目录，迁移为独立仓库：

[`jay-first-cli-text-tool`](https://github.com/justlearner010/jay-first-cli-text-tool)

这一阶段的核心目标是工程化整理，而不是大幅改变功能逻辑。

主要变化包括：

- 使用 `src/first_cli/` 作为标准包结构。
- 增加 `pyproject.toml`。
- 配置 console script：`first-cli`。
- 增加 GitHub Actions CI。
- 整理 README，让项目边界更清楚。
- 保留原有文本统计、词频、分块、JSON 和 mock summary 逻辑。

这个阶段的意义是：项目从“本地练习目录”变成了“可以安装、可以测试、可以公开展示的小型 Python 包”。

## 阶段三：CLI 功能增强

这个阶段开始围绕 GitHub Issue 和 PR 推进开发。

主要完成的功能包括：

- 增加 `--word`，查询单个目标词频。
- 增加 `--top`，控制高频词输出数量。
- 为 `--word` 和 `--top` 补充 pytest 测试。
- 处理 `top < 0` 的非法输入。
- 处理 `top` 大于词表容量的情况。
- 对 `--word` 输入做空格裁剪和大小写归一。

这个阶段的关键收获是：功能不只是“能跑”，还需要明确输入边界和测试契约。

例如，`--word " Apple "` 不应该因为用户多输入空格或大小写不同就统计失败；`--top -1` 也不应该返回误导性的结果，而应该明确报错。

## 阶段四：Parser 可测试化

随着 CLI 功能增多，我发现原来的 `parse_args()` 直接读取真实命令行参数，导致测试很难传入“假参数”。

这个阶段引入了两个重要改动：

- `build_parser()`：专门负责创建 `argparse.ArgumentParser`。
- `parse_args(argv=None)`：允许测试传入参数列表。

这样测试就可以写成：

```python
args = parse_args(["sample.txt", "--summary"])
```

而不是必须依赖真实终端输入。

这个阶段的核心收获是：CLI 入口也可以被测试。命令行工具不应该只能靠手动运行验证，参数解析本身也应该有清晰的测试入口。

## 阶段五：Application Layer 拆分

早期 `main()` 同时负责：

- 配置 logging。
- 解析命令行参数。
- 读取文件。
- 校验输入。
- 调用核心函数。
- 打印结果。
- 处理错误。

这让 `main()` 变得越来越重，也不利于测试。

后续我把入口拆成：

```text
main()
  -> parse_args()
  -> run(args)
```

其中：

- `main()` 负责真实 CLI 入口和退出码。
- `run(args)` 负责 application layer 调度。
- `handle_summary()`、`handle_freq()`、`handle_status()`、`handle_createjson()`、`handle_word()` 分别处理不同命令选项。

这个阶段的意义是：测试可以绕过真实命令行，直接构造假参数对象调用 `run(args)`。

## 阶段六：错误处理增强

错误处理阶段补充了更多真实使用中会遇到的边界情况：

- 文件不存在。
- 空文件。
- 文件无读取权限。
- 文件解码失败。
- `chunk_size <= 0`。
- `top < 0`。
- 没有选择任何输出操作。

这一阶段也经历了一次真实的 Git 分支合并冲突。

错误处理分支和 parser 重构分支都修改了 `app.py` 的核心流程。Git 无法自动判断应该保留哪一边，所以产生了 merge conflict。

最终的解决方式不是简单选择某一边，而是重新整理职责：

- 保留 `main` 中已经合并的 `run + handle_xxx` 结构。
- 把文件读取错误处理放入 `load_input_text()`。
- 把参数合法性和“必须选择至少一个输出操作”的逻辑放入 `validate_args()`。

这个阶段的关键经验是：冲突解决不是机械地选代码，而是把两个分支的设计意图重新整合。

## 阶段七：Core Layer 与 I/O 解耦

项目后期开始关注 core layer 和 I/O 解耦。

早期很多函数直接接收 `filename` 并在内部 `open()` 文件，例如：

- `word_freq_cnt(fname)`
- `TextStats(fname)`
- `Wordchunk(fname, chunk_size)`

这意味着核心逻辑和文件 I/O 绑在一起，测试时必须造临时文件，函数本身也不够纯。

后续重构方向是：

```text
I/O 层：
filename -> text

Core 层：
text -> result

CLI / handler 层：
result -> stdout / JSON
```

具体变化包括：

- `word_freq_cnt(text, top_n)`：只接收文本并返回词频结果。
- `TextStats(text)`：只统计传入文本，不再负责读文件。
- `chunk_text(text, chunk_size)`：只接收文本和 chunk 大小，返回结构化 chunks。
- `load_input_text(filename)`：集中负责文件读取和文件相关错误。

这个阶段的判断标准是：

```text
core 不接收 filename。
core 不 print。
core 不 write json。
core 只接收普通数据，返回普通数据。
```

这一步让测试变得更轻，也让项目更接近真实工程中的分层方式。

## 阶段八：当前状态与收尾判断

截至 2026-06-28，项目已经基本完成了它作为“第一个 Python CLI 工程化项目”的使命。

当前已经覆盖的能力包括：

- Python CLI 参数解析。
- 小型 `src/` 包结构。
- pytest 单元测试。
- GitHub Issue / PR 开发流程。
- GitHub Actions CI。
- 错误处理。
- parser 可测试化。
- application layer 拆分。
- 初步 core / I/O 解耦。

这个项目最重要的价值不是文本处理功能本身，而是完整走过了一遍工程化闭环：

```text
脚本功能实现
-> 模块拆分
-> pytest 覆盖
-> CLI 参数设计
-> GitHub Issue 拆任务
-> PR 合并和 CI 验证
-> 错误处理
-> parser 可测试化
-> core / I/O 解耦
-> 项目文档收口
```

后续如果继续深挖，还可以做：

- 更新 README 当前状态。
- 增加 `CHANGELOG.md`。
- 更新版本号。
- 明确 JSON / chunk 输出边界。
- 补充更完整的端到端 CLI 测试。

但从学习路线看，这个项目已经适合进入收尾阶段。它可以作为 Python 工程化入门作品保留在 GitHub 上，下一阶段更适合转向 RAG demo。

## 对下一阶段的迁移价值

这个 CLI 项目的经验可以直接迁移到 RAG demo。

对应关系如下：

```text
CLI 项目中的 load_input_text
-> RAG demo 中的 document loader

CLI 项目中的 chunk_text
-> RAG demo 中的 chunker

CLI 项目中的 summarize_text / MOCKLLM
-> RAG demo 中的 LLM interface

CLI 项目中的 core / I/O 解耦
-> RAG demo 中的 loader / retriever / generator 分层

CLI 项目中的 pytest
-> RAG demo 中对 chunk、retrieval、prompt assembly 的测试
```

因此，这个项目不是孤立结束，而是为下一阶段 RAG 应用工程打下了基础。
