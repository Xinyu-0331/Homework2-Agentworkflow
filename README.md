## Simple Workflow MVP：代码审查 Agent 流水线

### 项目简介

本项目实现一个简易的 Multi-Agent Workflow：由三个 Agent（编码 Agent → 审查 Agent → 修复 Agent）**顺序协作**完成一条完整的「生成代码 → 代码评审 → 修复代码」业务流程，作为"简易 Workflow"课程作业的 MVP 实现。

### 功能特性

* 3 个 Agent 协同完成端到端业务闭环 
*  通过共享状态对象实现 Agent 之间消息传递与状态共享 
*  顺序（串行）流程控制 
*  全流程执行日志记录 

### 技术栈

* Python 3.8+ 
*  python-dotenv（读取环境变量配置） 
* requests（调用 OpenAI 兼容的大模型 API）

### 项目结构目录

├── main.py              # Workflow 调度入口（按顺序编排 Agent） 

├── agents.py            # 三个 Agent 实现 + LLM 调用函数 

├── workflow_state.py    # 全局共享状态类 WorkflowState 

├── requirements.txt     # 依赖清单 

├── .env.example         # 环境变量配置模板（不含真实密钥） 

├── README.md            # 项目说明文档 

└── Design.md            # 架构设计文档