import json
from collections import Counter


def generate_quality_report(issues, output_path="quality_report.json"):
    summary = Counter(issue.severity.value for issue in issues)

    report = {
        "summary": dict(summary),
        "issues": [
            {
                "rule": issue.rule_name,
                "severity": issue.severity.value,
                "message": issue.message,
                "affected_rows": issue.affected_rows,
            }
            for issue in issues
        ],
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
