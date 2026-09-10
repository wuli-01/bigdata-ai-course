# 大数据与人工智能 · 课程学习仓库

个人课程学习仓库：用来**学习 AI 概念**（Agent、大模型的上下文、Agent Skill），
并把每个概念整理成一份可以反复打开、随时自测的单页学习资料。

> 📌 本仓库于 2026-09-08 按"重新完成作业"的要求清空后重建，
> 现已按作业要求补齐：项目级 Skill、三份概念学习资料、概念关系说明、README、.gitignore。

## 当前仓库内容

```
bigdata-ai-course/
├── .workbuddy/
│   └── skills/
│       └── concept-crash-course/
│           └── SKILL.md            # 项目级 Skill：概念速成卡片生成器
├── learning-materials/
│   ├── agent.html                  # 概念资料：AI Agent（智能体）
│   ├── llm-context.html            # 概念资料：大模型的上下文
│   ├── skill.html                  # 概念资料：Agent Skill（智能体技能）
│   └── concept-relationship.html   # 三概念关系说明
├── README.md
└── .gitignore
```

| 文件 | 说明 |
|------|------|
| `.workbuddy/skills/concept-crash-course/SKILL.md` | 项目级 Agent Skill：接收任意新概念，产出"单页 HTML 学习卡 + 闯关测试"的完整流程规范 |
| `learning-materials/agent.html` | AI Agent：外卖店员类比 + 规划/工具/记忆机制 + 我的仓库实战场景 + 与聊天机器人/工作流的辨析 + 3 条来源 + 闯关测试 |
| `learning-materials/llm-context.html` | 大模型的上下文：厨师操作台类比 + token 计量与位置偏差 + push 实战场景 + 与记忆/微调的辨析 + 3 条来源 + 闯关测试 |
| `learning-materials/skill.html` | Agent Skill：奶茶店 SOP 卡类比 + 渐进式加载 + 本仓库 Skill 实战场景 + 与 MCP/RAG 的辨析 + 4 条来源 + 闯关测试 |
| `learning-materials/concept-relationship.html` | 三概念关系：厨师/操作台/菜谱卡类比 + 角色对比表 + 协作流程图 + 两个重点问题（上下文如何影响 Agent、Skill 如何沉淀知识） |

每份资料都包含五项必备内容：**概念的个人解释、核心机制或组成、一个具体应用场景、容易混淆的问题或使用边界、可核查的资料来源链接**；
额外配有**两关六题闯关测试**（答对升级、答错降级、通关后可"再玩一次"）。

### 怎么使用这个 Skill

在 WorkBuddy 中打开本仓库工作区，直接说一句 **"我想学习 XX 概念"**（例如"我想学习 Hadoop"），
智能体会匹配到 `concept-crash-course` 的 description，按 SKILL.md 的流程产出
`learning-materials/<概念英文名>.html` 并更新 README。Skill 是通用的，不是只为某三个概念写的一次性提示词。

### 怎么打开这些学习资料

- **本机双击**：进入 `C:\Users\wuli\WorkBuddy\2026-09-03-09-39-53\bigdata-ai-course\learning-materials\` 双击任意 `.html` 文件
- **在线查看**：https://github.com/wuli-01/bigdata-ai-course → `learning-materials` → 点开文件名 → 右上角 `Raw`

HTML 是普通网页，任何浏览器直接打开即可，不需要安装任何东西。

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
- 我做的**人工核查与修改**：
  1. 逐条点击上表中的来源链接，确认可访问且内容对得上（无法访问的已替换或标注"建议人工复核"）
  2. "个人解释""生活例子"改写为结合自己仓库经历的第一人称表述，避免照抄定义
  3. 用 Node 模拟浏览器跑了一遍闯关逻辑，验证"升级 / 降级 / 通关 / 再玩一次"均正常工作；发现"通关后无法重玩"的问题后补上了"再玩一次"按钮
  4. 按作业要求逐项核查缺漏，修正了三处：① 补建缺失的 `agent.html`、`llm-context.html`、`concept-relationship.html` 与 `.gitignore`；② 把 `agent-skill.html` 改名为规范要求的 `skill.html`；③ 给 `skill.html` 补上缺失的"具体应用场景""容易混淆/使用边界"两个必备板块
  5. 概念关系页的流程图改用纯 HTML/CSS 绘制（不依赖外部 CDN），保证离线可打开
  6. 按用户要求删除了 README 中的作业进度清单；README 内容按仓库真实文件撰写，未虚构不存在的内容
