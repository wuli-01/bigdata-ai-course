# 大数据与人工智能 · 课程学习仓库

个人课程学习仓库：用来**学习 AI 概念**（Agent、大模型的上下文、Agent Skill），
并把每个概念整理成一份可以反复打开、随时自测的单页学习资料。

> 📌 本仓库于 2026-09-08 按"重新完成作业"的要求清空后重建，目前处于**进行中**状态，
> 下方清单会随进度更新。

## 当前仓库内容

```
bigdata-ai-course/
├── .workbuddy/
│   └── skills/
│       └── concept-crash-course/
│           └── SKILL.md      # 项目级 Skill：概念速成卡片生成器
└── learning-materials/
    └── agent-skill.html      # 概念学习资料：Agent Skill（智能体技能）
```

| 文件 | 说明 |
|------|------|
| `.workbuddy/skills/concept-crash-course/SKILL.md` | 项目级 Agent Skill：接收任意新概念，产出"单页 HTML 学习卡 + 闯关测试"的完整流程规范 |
| `learning-materials/agent-skill.html` | Agent Skill 一页速览：奶茶店 SOP 卡类比 + 4 个核心要点 + 4 条已核实来源 + **两关六题闯关测试**（答对升级、答错降级、通关后可点"再玩一次"） |

### 怎么使用这个 Skill

在 WorkBuddy 中打开本仓库工作区，直接说一句 **"我想学习 XX 概念"**（例如"我想学习 Hadoop"），
智能体会匹配到 `concept-crash-course` 的 description，按 SKILL.md 的流程产出
`learning-materials/<概念英文名>.html` 并更新 README。Skill 是通用的，不是只为某三个概念写的一次性提示词。

### 怎么打开这份学习资料

- **本机双击**：`C:\Users\wuli\WorkBuddy\2026-09-03-09-39-53\bigdata-ai-course\learning-materials\agent-skill.html`
- **在线查看**：https://github.com/wuli-01/bigdata-ai-course → `learning-materials` → `agent-skill.html`

HTML 是普通网页，任何浏览器直接打开即可，不需要安装任何东西。

## 作业进度清单

| # | 任务 | 状态 |
|---|------|------|
| 1 | 概念学习资料：Agent Skill | ✅ 已完成（`agent-skill.html`） |
| 2 | 项目级 Skill | ✅ 已完成（`.workbuddy/skills/concept-crash-course/SKILL.md`） |
| 3 | 概念学习资料：AI Agent | ⬜ 待完成 |
| 4 | 概念学习资料：大模型的上下文 | ⬜ 待完成 |
| 5 | 概念关系说明（三概念之间的关系） | ⬜ 待完成 |
| 6 | `.gitignore` | ⬜ 待完成 |

> Skill 的设计要求：能接收**任意一个新概念**作为学习主题，按统一流程产出学习资料，
> 不能只为某三个概念写一次性提示词。

## 已核实的资料来源（供后续资料复用）

以下链接均已实际访问确认可访问（核查日期 2026-09-08）：

| 来源 | 链接 | 用途 |
|------|------|------|
| Agent Skills 开放标准官网 | https://agentskills.io | SKILL.md 格式定义 |
| Anthropic 工程博客（2025-10-16） | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | 渐进式披露三层加载、安全提醒 |
| Claude Code 官方文档 | https://code.claude.com/docs/en/skills | Skill 存放位置与触发排查 |
| Anthropic *Building effective agents* | https://www.anthropic.com/research/building-effective-agents | Agent 与 Workflow 的区别 |
| IBM *What Are AI Agents?* | https://www.ibm.com/think/topics/ai-agents | Agent 定义与分类 |
| arXiv:2307.03172 *Lost in the Middle* | https://arxiv.org/abs/2307.03172 | 上下文位置偏差 |
| Prompt Engineering Guide | https://www.promptingguide.ai/introduction/settings | LLM 参数与上下文控制 |

## AI 使用情况与人工核查说明

- 学习资料的**初稿由 AI 生成**，流程为：核实资料来源 → 按五板块结构化 → 生成单页 HTML → 逐条标注来源 → 自检交付
- 我做的**人工核查**：
  1. 逐条点击上表中的来源链接，确认可访问且内容对得上（无法访问的已替换或标注）
  2. "个人解释""生活例子"部分改写为结合自己仓库经历的第一人称表述，避免照抄定义
  3. 用程序仿真运行闯关逻辑，验证"升级 / 降级 / 通关 / 再玩一次"均正常工作
  4. 本次 README 按仓库**当前真实内容**撰写，未虚构尚未完成的文件
