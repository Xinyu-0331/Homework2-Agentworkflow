import os
from dotenv import load_dotenv
import requests
from workflow_state import WorkflowState

load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL = os.getenv("LLM_MODEL")


def llm_call(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


class CodingAgent:
    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log("[CodingAgent] 接收需求，开始生成代码")
        prompt = f"""
你是一名程序员，根据下面需求写出完整可运行Python代码，不要多余解释，只输出代码：
需求：{state.user_requirement}
"""
        code = llm_call(prompt)
        state.raw_code = code
        state.add_log("[CodingAgent] 原始代码生成完成")
        return state


class ReviewAgent:
    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log("[ReviewAgent] 开始代码审查")
        prompt = f"""
你是代码评审专家，对下面这段Python代码做审查，严格按照格式输出：
【缺陷】
【风险】
【改进建议】

待审查代码：
{state.raw_code}
"""
        report = llm_call(prompt)
        state.review_report = report
        state.add_log("[ReviewAgent] 审查报告生成完成")
        return state


class FixAgent:
    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log("[FixAgent] 根据评审报告修复代码")
        prompt = f"""
原始代码：
{state.raw_code}

评审报告：
{state.review_report}

请输出修复后的完整代码，附带简短修复说明。
"""
        res = llm_call(prompt)
        state.fixed_code = res
        state.add_log("[FixAgent] 代码修复完成")
        return state
