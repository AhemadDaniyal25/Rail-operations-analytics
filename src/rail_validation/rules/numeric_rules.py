import pandas as pd
from typing import List

from rail_validation.models import ValidationIssue, Severity
from rail_validation.rules.rule_base import ValidationRule


class NonNegativeDelayRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NonNegativeDelayRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "delay_minutes" not in df.columns:
            return []

        invalid_rows = df[df["delay_minutes"] < 0].index.tolist()

        if not invalid_rows:
            return []

        issue = ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Delay minutes must be non-negative.",
            affected_rows=invalid_rows
        )

        return [issue]
class PositiveEnergyConsumptionRule(ValidationRule):

    @property
    def name(self) -> str:
        return "PositiveEnergyConsumptionRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "energy_kwh" not in df.columns:
            return []

        invalid_rows = df[df["energy_kwh"] <= 0].index.tolist()

        if not invalid_rows:
            return []

        issue = ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Energy consumption must be greater than zero.",
            affected_rows=invalid_rows
        )

        return [issue]

class AssetAgeBoundsRule(ValidationRule):

    @property
    def name(self) -> str:
        return "AssetAgeBoundsRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "asset_age_years" not in df.columns:
            return []

        invalid_rows = df[
            (df["asset_age_years"] < 0) | (df["asset_age_years"] > 50)
        ].index.tolist()

        if not invalid_rows:
            return []

        issue = ValidationIssue(
            rule_name=self.name,
            severity=Severity.WARNING,
            message="Asset age must be between 0 and 50 years.",
            affected_rows=invalid_rows
        )

        return [issue]

class RealisticDelayUpperBoundRule(ValidationRule):

    @property
    def name(self) -> str:
        return "RealisticDelayUpperBoundRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "delay_minutes" not in df.columns:
            return []

        invalid_rows = df[df["delay_minutes"] > 600].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.WARNING,
            message="Delay minutes exceed realistic upper bound (600).",
            affected_rows=invalid_rows
        )]


class ValidRouteIdRule(ValidationRule):

    @property
    def name(self) -> str:
        return "ValidRouteIdRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "route" not in df.columns:
            return []

        invalid_rows = df[
            ~df["route"].astype(str).str.match(r"^[A-Za-z0-9]+$")
        ].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Route ID must be alphanumeric.",
            affected_rows=invalid_rows
        )]
