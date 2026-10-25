from dataclasses import dataclass
from typing import List, Optional

@dataclass
class WorkflowState:
    user_requirement: str = ""
    raw_code: str = ""
    review_report: str = ""
    fixed_code: str = ""
    log: Optional[List[str]] = None

    def __post_init__(self):
        if self.log is None:
            self.log = []

    def add_log(self, msg: str):
        self.log.append(msg)
