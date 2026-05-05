# Reporting Workflow Builder Skill

把周期性周报、月报、经营复盘和 PPT 汇报，沉淀成可复用的 AI 工作流。

`reporting-workflow-builder` 是一个面向 Codex / Claude Code 等智能体环境的 Skill。它用于帮助用户从零散材料中搭建可复用的报告生产流程，而不是只生成一次性的报告文本或 PPT。

它可以处理的输入包括：历史周报、历史 PPT、表格文件、看板导出、数据库查询结果、日志、CRM 导出、工单、人工备注、会议纪要，以及其他能支撑分析结论的证据材料。

## 这个 Skill 解决什么问题

很多周期性汇报都会遇到类似问题：

- 数据很多，但不知道哪些数据能支撑哪些结论。
- 历史周报和 PPT 有参考价值，但结构可能陈旧、分析深度不足。
- 汇总指标只能说明“发生了什么”，却经常被强行写成“为什么发生”。
- 搭建自动化流程时，对话太长，用户还没看到产物就失去耐心。
- 在 Codex / Claude Code 里跑通过一次，但交给轻量 cowork 环境后无法稳定复跑。
- 每周都在重复找数据、做图表、写分析、调 PPT。

这个 Skill 的目标是把这些工作拆清楚，并沉淀成一套可以持续复用的流程。

## 核心原则

这个 Skill 的核心原则是：

> 先确认资源边界，再设计报告结构。

也就是说，不先画一套看起来很高级但数据支撑不了的汇报框架。它会先判断用户有什么数据、能取到什么字段、有没有明细证据、后续在哪个环境里复跑，再决定报告或 PPT 可以做到什么深度。

## 三种运行模式

### Build Mode：搭建模式

适合第一次搭建工作流，或者当数据源、汇报对象、报告结构、输出格式发生明显变化时使用。

在搭建模式中，智能体会：

1. 确认汇报目标、受众、周期、输出形态和可用数据。
2. 审核历史报告、历史 PPT、模板和看板截图，但不被旧材料限制上限。
3. 尽早生成一个低保真报告大纲或 PPT 页序，让用户先看到方向。
4. 把数据源拆成“结构化经营数据”和“明细证据数据”两层。
5. 建立“结论 - 数据源 - 字段 - 证据等级 - 缺口”的证据地图。
6. 删除或降级缺少数据支撑的模块。
7. 选择落地路径：智能体直接交付、模板复用、工程化复跑。
8. 保存工作流状态、运行说明、视觉约束、证据规则和下次启动用的复活 Prompt。

### Run Mode：运行模式

适合工作流已经搭好之后，每周或每月只替换新数据，生成当前周期的正式输出。

在运行模式中，智能体会：

1. 读取已有的工作流状态、运行说明或复活 Prompt。
2. 检查当前周期输入文件和必要字段是否齐全。
3. 按既定分析路径执行，不重新设计报告结构。
4. 生成本期周报、月报、PPT、表格汇总或其他指定产物。
5. 检查日期、占位符、图表、字体、可读性和无证据归因问题。
6. 返回正式产物、简短运行摘要和未解决的数据缺口。

运行模式应该尽量少提问，只在关键字段缺失或输出会误导时打断用户。

### Repair Mode：修复模式

适合原本能跑的工作流突然失败，或输出质量明显漂移。

常见触发场景包括：

- 本周数据表字段变了。
- 查询结果不再返回预期字段。
- 图表为空。
- 报告日期仍然是上期。
- PPT 出现占位符未替换。
- 字体太小或图表文字重叠。
- 某个原因分析模块缺少明细证据。

修复模式的目标是先定位问题，再修补工作流，最后重新生成产物。

## 数据分层与证据规则

这个 Skill 会把数据源分成两层。

| 数据层 | 回答的问题 | 常见例子 |
|---|---|---|
| 结构化经营数据 | 发生了什么 | KPI 导出、看板表格、周期汇总、数据库查询结果、固定表格模板 |
| 明细证据数据 | 为什么发生 | 交易明细、客户/账号记录、CRM 动作、工单、跟进记录、取消原因、评论、事件记录 |

结构化数据可以支撑：

- 趋势变化
- 排名
- 环比/同比
- 结构占比
- 异常波动
- Top/Bottom 对象

但仅靠汇总数据，不能直接支撑：

- 用户意图
- 客户原因
- 流程质量判断
- 具体失败故事
- 代表性案例
- 细颗粒度归因

如果缺少明细证据，智能体必须降级表达，比如写成“现象”“待验证假设”或“数据缺口”，而不是编出一个看似合理的原因。

## 可以沉淀哪些资产

这个 Skill 不只是输出一份报告，而是帮助用户沉淀一组可复用资产：

- `workflow_state.md` 或 `workflow_state.json`：工作流状态
- `data_sources.md`：数据源清单
- `field_dictionary.md`：字段字典
- `evidence_map.md`：证据地图
- `outline.md`：报告大纲
- `deck_plan.md`：PPT 页序和页面规划
- `runbook.md`：运行说明
- `resurrection_prompt.md`：下次启动用的复活 Prompt
- `cleanup_policy.md`：缓存和中间文件清理规则

这些资产可以让后续复跑更稳定，也能降低用户每周重新解释需求的成本。

## 安装方式

把 `reporting-workflow-builder` 文件夹复制到你的智能体 skills 目录。

Codex：

```text
~/.codex/skills/reporting-workflow-builder
```

Claude Code：

```text
~/.claude/skills/reporting-workflow-builder
```

Windows 上通常是：

```text
C:\Users\<你的用户名>\.codex\skills\reporting-workflow-builder
C:\Users\<你的用户名>\.claude\skills\reporting-workflow-builder
```

复制完成后，重启智能体工具，或新开一个会话。

## 目录结构

```text
reporting-workflow-builder/
  SKILL.md
  agents/
    openai.yaml
  references/
    build-mode.md
    run-mode.md
    evidence-rules.md
  scripts/
    scaffold_reporting_workspace.py
```

## 示例用法

第一次搭建工作流：

```text
使用 reporting-workflow-builder skill，帮我搭建一个可复用的周期性汇报工作流。
我会上传历史报告、历史 PPT 和本期数据。
请先判断我的数据边界和输出需求，再设计报告结构。
```

使用已有工作流生成本期输出：

```text
使用这个文件夹里保存的 reporting workflow。
当前周期数据已经上传。
请沿用已有结构和样式生成本期报告/PPT。
只有在必要字段缺失时再问我。
```

修复失败的工作流：

```text
这个报告工作流之前能跑，但这次输出里有空图表和旧日期。
请使用 reporting-workflow-builder 的 Repair Mode 定位问题，修复后重新生成。
```

## 可选脚手架

Skill 内置了一个通用脚手架脚本，可以生成一个空的报告工作流目录：

```bash
python scripts/scaffold_reporting_workspace.py ./my-reporting-workflow
```

它会创建：

- `workflow_state.md`
- `data_sources.md`
- `field_dictionary.md`
- `evidence_map.md`
- `outline.md`
- `deck_plan.md`
- `runbook.md`
- `resurrection_prompt.md`
- `cleanup_policy.md`

这些文件不绑定任何行业，需要根据具体项目继续补充。

## 设计原则

- 先确认资源边界，再设计报告结构。
- 历史材料只做参考，不做上限。
- 尽早交付低保真骨架，避免长时间空聊。
- 区分“发生了什么”和“为什么发生”。
- 没有证据就降级表达，不编原因。
- 搭建模式和运行模式分离。
- 让后续复跑尽可能简单，适合非技术用户使用。
- Skill 层保持跨行业，不写入具体公司的内部规则。

## 开源卫生

这个 Skill 应保持行业中立。

不要把以下内容写进通用 skill 层：

- 具体公司名称
- 客户名称
- 内部表名
- 私有指标
- 专有渠道名
- 特定行业黑话
- 某个项目独有的潜规则

这些内容应该放在用户自己的项目工作区里，而不是放进可复用 skill。

## 验证方式

如果你有 Codex 的 skill creator 工具，可以运行：

```bash
python <path-to-skill-creator>/scripts/quick_validate.py ./reporting-workflow-builder
```

也可以测试脚手架脚本：

```bash
python reporting-workflow-builder/scripts/scaffold_reporting_workspace.py ./tmp-reporting-workflow
```

## 当前状态

这是一个早期可复用 Skill 草案，适合拿真实场景测试。建议先用不同类型的周期性汇报场景验证，比如销售周报、客服复盘、项目进度汇报、投放复盘、运营月报等，再逐步稳定规则。
