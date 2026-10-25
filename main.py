from workflow_state import WorkflowState
from agents import CodingAgent, ReviewAgent, FixAgent


def run_workflow(requirement: str):
    # 初始化全局状态
    state = WorkflowState(user_requirement=requirement)
    # 顺序编排Agent
    agents = [
        CodingAgent(),
        ReviewAgent(),
        FixAgent()
    ]
    for agent in agents:
        state = agent.run(state)

    # 打印最终结果
    print("===== 执行日志 =====")
    for line in state.log:
        print(line)

    print("\n===== 原始代码 =====")
    print(state.raw_code)

    print("\n===== 评审报告 =====")
    print(state.review_report)

    print("\n===== 修复后代码 =====")
    print(state.fixed_code)
    return state


if __name__ == "__main__":
    # 测试需求，你可以修改这里
    test_requirement = "写一个Python函数，读取txt文件，统计里面每个单词出现次数"
    run_workflow(test_requirement)
