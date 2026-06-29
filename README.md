# jay-first-cli-text-tool

> A tested Python CLI for text statistics, word frequency, character-based chunking, JSON output and deterministic mock summaries.

这是我在 Python 工程化学习阶段完成的第一个 CLI 项目。迁移只整理了包结构、导入、测试入口与工程元数据，没有改变原有文本统计、词频、分块、JSON 和 mock summary 逻辑。

## 适用对象

- 想查看一个小型 `src/` 布局 Python 包的人。
- 想练习 `argparse`、文件处理、`dataclass`、测试与 CLI 打包的人。
- 想了解我从练习代码过渡到可安装项目的过程的人。

## 功能边界

- `--status`：行数、单词数、数字字符数和空白字符数。
- `--freq`：按空白切词后的前 10 个高频词。
- `--summary`：确定性的简短 mock summary，不调用远程模型。
- `--createjson`：输出 summary、模式和字符数 JSON。
- `--chunk_size`：按字符长度生成内部分块。

不包含语义分块、中文分词、真实 LLM 摘要或复杂编码检测。

## 安装与运行

要求 Python 3.11 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

first-cli examples/sample.txt --status
python -m first_cli examples/sample.txt --summary
first-cli examples/sample.txt --freq --createjson
pytest
```

## 验证证据

Current test status at the time of migration: 30 passed, 1 xfailed.

该数字只记录迁移时的快照；长期状态以 GitHub Actions 为准。预期失败测试记录了尚未实现的中文无空格分词能力。

## 版本状态

当前包版本仍是 `0.1.0`，记录在 `pyproject.toml` 中。后续计划在 parser 可测试化、错误处理测试和 core / I/O 解耦收口后，再统一提升版本号。

- [版本记录](./CHANGELOG.md)：按版本记录新增、变更、修复和测试状态。
- [开发流程回顾](./docs/development-review.md)：记录这个 CLI 项目从脚本练习到工程化小项目的完整演进。

## 当前状态与已知限制

- 当前版本：`0.1.0`，作为可持续迭代的独立项目发布。
- `--summary` 目前只统计空白分隔词数。
- `--chunk_size` 的历史命名保留不变，但实际按字符切分。
- 输入读取沿用系统默认编码；不适合作为生产级文本摄取工具。
- CLI 仍会计算部分未被所选输出使用的数据，这是早期实现留下的优化空间。

## 下一步

- 在不破坏现有接口的前提下改善输入编码与错误信息。
- 为命令入口增加端到端测试。
- 明确字符分块与词分块的命名和契约。

## 关联仓库

- [AI Agent 学习系统](https://github.com/justlearner010/jay-ai-agent-learning-system)
- [AI 工程学习笔记](https://github.com/justlearner010/jay-ai-engineering-notes)
- [历史路线归档](https://github.com/justlearner010/jay-ai-agent-roadmap-archive)
