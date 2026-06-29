# 版本记录

本文记录 `jay-first-cli-text-tool` 的主要版本变化。这个项目仍处于学习与工程化整理阶段，版本号用于标记阶段性能力边界，不代表生产级稳定承诺。

## 0.3.0 - 计划中

### 目标
- 完成 core layer 与 I/O 解耦，让核心文本处理函数只接收普通文本数据，不直接读取文件或输出到终端。
- 完善 CLI parser 的可测试性，支持 `parse_args(argv=None)` 传入假参数进行 pytest 测试。
- 收口错误处理测试，覆盖文件权限、解码失败、非法参数和未选择输出操作等情况。

### 当前状态
- `word_freq_cnt(text, top_n)` 已开始改为接收文本而不是文件路径。
- `TextStats(text)` 已开始改为统计传入文本而不是自己读取文件。
- 相关测试正在从“造临时文件”迁移到“直接传文本”。

### 验证计划
- 全量 pytest 通过。
- 真实 CLI 命令验证 `--summary`、`--freq`、`--status`、`--word`、`--createjson`。
- GitHub Actions 在 Python 3.11 和 3.13 上通过。

## 0.2.0 - 2026-06-28

### 新增
- 增加 `--word`，用于查询单个目标词在文本中的出现次数。
- 增加 `--top`，用于控制高频词输出数量。
- 增加 `top < 0` 的非法参数检查。
- 增加文件不存在、空文件、权限错误、解码失败等错误处理方向。
- 增加“没有选择任何输出操作”时的用户提示。

### 变更
- 将 CLI 入口从单一 `main()` 拆成 `main()`、`run(args)` 和多个 `handle_xxx()` 函数。
- 将文件读取逻辑集中到 `load_input_text()`。
- 将参数合法性检查集中到 `validate_args()`。
- 开始建立 application layer，让测试可以绕过真实命令行直接构造参数对象。

### 修复
- 修复 `--word` 对大小写和首尾空格敏感的问题。
- 修复 `--top` 大于词表容量时的边界行为，只返回实际存在的词。
- 移除非 `--word` 输出中的额外完成提示，避免污染 stdout。

### 测试
- 本阶段主要验证结果：`35 passed, 1 xfailed`。
- 预期失败测试用于记录尚未实现的中文无空格分词能力。

## 0.1.0 - 2026-06-21

### 新增
- 将早期练习脚本整理为独立 Python 包。
- 使用 `src/first_cli/` 包结构。
- 增加 `pyproject.toml`。
- 增加 console script：`first-cli`。
- 增加 GitHub Actions CI。
- 保留文本统计、词频统计、字符分块、JSON 输出和 mock summary 功能。

### 项目定位
- 这是 Python 工程化学习阶段的第一个 CLI 项目。
- 重点不是文本处理功能本身，而是练习包结构、pytest、CLI 参数、GitHub Issue / PR 和 CI 流程。

### 测试
- 迁移时记录的验证结果：`30 passed, 1 xfailed`。
