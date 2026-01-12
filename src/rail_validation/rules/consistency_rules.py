import pandas as pd
from typing import List

from rail_validation.models import ValidationIssue, Severity
from rail_validation.rules.rule_base import ValidationRule


class MaintenanceEventBinaryRule(ValidationRule):

    @property
    def name(self) -> str:
        return "MaintenanceEventBinaryRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "maintenance_event" not in df.columns:
            return []

        invalid_rows = df[~df["maintenance_event"].isin([0, 1])].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Maintenance event must be 0 or 1.",
            affected_rows=invalid_rows
        )]


class NonEmptyRegionRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NonEmptyRegionRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "region" not in df.columns:
            return []

        invalid_rows = df[
            df["region"].isna() | (df["region"].astype(str).str.strip() == "")
        ].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Region must not be empty.",
            affected_rows=invalid_rows
        )]


class RouteSingleRegionRule(ValidationRule):

    @property
    def name(self) -> str:
        return "RouteSingleRegionRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if not {"route", "region"}.issubset(df.columns):
            return []

        inconsistent_routes = (
            df.groupby("route")["region"].nunique()
            .loc[lambda x: x > 1]
            .index
        )

        invalid_rows = df[df["route"].isin(inconsistent_routes)].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Route must map to a single region.",
            affected_rows=invalid_rows
        )]
