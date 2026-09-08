# 大数据与人工智能 · 课程学习仓库

个人课程学习仓库，两部分内容：

1. **learning-materials/** — AI 概念学习资料库（按统一模板生成的单页 HTML，逐个概念积累）
2. **.workbuddy/skills/concept-explainer/** — 一个项目级 Agent Skill，定义"概念学习资料"的标准化生成流程

## 仓库结构

```
bigdata-ai-course/
├── .workbuddy/
│   └── skills/
│       └── concept-explainer/
│           └── SKILL.md          # 项目级 Skill：概念学习资料生成器
├── learning-materials/
│   ├── agent.html                # 概念资料：AI Agent（智能体）
│   ├── llm-context.html          # 概念资料：大模型的上下文
│   ├── skill.html                # 概念资料：Agent Skill
│   └── concept-relationship.html # 三概念关系说明（表格 + Mermaid 流程图）
├── README.md
└── .gitignore
```

## Skill 说明

| 项 | 内容 |
|----|------|
| 名称 | `concept-explainer`（概念学习资料生成器） |
| 存放路径 | `.workbuddy/skills/concept-explainer/SKILL.md` |
| 类型 | 项目级 Skill（仅在本仓库工作区内生效） |
| 功能 | 接收任意一个新概念，按固定流水线生成结构化学习资料：研究核实 → 五板块结构化 → 生成卡片式 HTML → 标注可核查来源 → 自检交付 |

### 在 WorkBuddy 中如何调用

1. 用 WorkBuddy 打开本仓库所在的工作区（项目级 Skill 会被自动识别加载）
2. 直接说一句话，例如：**"我想学习 Hadoop 这个概念"** 或 **"用 concept-explainer 生成'上下文工程'的学习资料"**
3. 智能体匹配到 Skill 的 description 后，会按 SKILL.md 的步骤执行，产出保存到 `learning-materials/<概念英文名>.html`，并同步更新 README 的资料列表

> Skill 是通用的：它接收"任意新概念"作为输入，而不是只为某三个概念写的一次性提示词。

## 已生成的学习资料

| 文件 | 概念 | 核心内容 |
|------|------|---------|
| `agent.html` | AI Agent（智能体） | 规划-工具-记忆-循环机制；与 Chatbot/Workflow 的区别；用本课程"AI 助手帮我搭环境推仓库"的经历作应用场景 |
| `llm-context.html` | 大模型的上下文 | 上下文窗口的组成与 token 计量；Lost in the Middle 位置偏差；上下文 ≠ 记忆 ≠ 微调 |
| `skill.html` | Agent Skill | SKILL.md 结构与渐进式披露三层加载；与 MCP/RAG/一次性提示词的区别 |
| `concept-relationship.html` | 三概念关系 | 厨师/操作台/菜谱卡类比；Mermaid 协作流程图；上下文如何影响 Agent、Skill 如何沉淀知识 |

## 使用 AI 后的人工核查与修改

资料由 AI（按 Skill 流程）生成初稿，我做了以下人工核查与修改：

1. **来源链接逐条核实**：用浏览器实际访问了引用的全部来源（Anthropic 工程博客×2、agentskills.io、Claude Code 文档、IBM、arXiv、Prompting Guide），确认可访问且内容对得上，并标注核查日期；个别因网络/区域无法访问的候选链接已替换或明确标注"建议人工复核"
2. **"个人解释"改写**：五份资料中的"个人解释"和应用场景均改写为结合我自己仓库经历（搭环境、被网络问题折腾、创建 Skill）的第一人称表述，避免 AI 腔的定义复述
3. **事实性校对**：对"渐进式披露三层加载""Agent vs Workflow 区分""Lost in the Middle 结论"等关键论断，与来源原文逐条比对后保留/修正
4. **结构调整**：按作业要求重组了目录（删除了早期的 `notes/`、`homework/` 旧结构与初版单页 `agent-skill-60s.html`，其内容拆解并入新的 `skill.html`），统一了页面风格与命名
5. **待复核项**：各模型"上下文窗口大小"的具体数值随版本变化较快，资料中未写死数字，建议使用前查看各厂商官方模型页

## 相关课程

大数据与人工智能课程作业 · 环境搭建记录（Git 2.55 / Python 3.12 / VS Code）见 git 提交历史。
