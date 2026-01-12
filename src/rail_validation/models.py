from dataclasses import dataclass
from enum import Enum
from typing import List


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"


@dataclass
class ValidationIssue:
    rule_name: str
    severity: Severity
    message: str
    affected_rows: List[int]
