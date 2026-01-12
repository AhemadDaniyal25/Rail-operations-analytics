import pandas as pd
from typing import List

from rail_validation.models import ValidationIssue, Severity
from rail_validation.rules.rule_base import ValidationRule


class NoMissingDelayRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NoMissingDelayRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "delay_minutes" not in df.columns:
            return []

        invalid_rows = df[df["delay_minutes"].isna()].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Delay minutes must not be missing.",
            affected_rows=invalid_rows
        )]


class NoMissingEnergyRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NoMissingEnergyRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "energy_kwh" not in df.columns:
            return []

        invalid_rows = df[df["energy_kwh"].isna()].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Energy consumption must not be missing.",
            affected_rows=invalid_rows
        )]


class NoMissingRouteRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NoMissingRouteRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "route" not in df.columns:
            return []

        invalid_rows = df[
            df["route"].isna() | (df["route"].astype(str).str.strip() == "")
        ].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Route must not be missing or empty.",
            affected_rows=invalid_rows
        )]


class NoMissingTrainIdRule(ValidationRule):

    @property
    def name(self) -> str:
        return "NoMissingTrainIdRule"

    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        if "train_id" not in df.columns:
            return []

        invalid_rows = df[df["train_id"].isna()].index.tolist()

        if not invalid_rows:
            return []

        return [ValidationIssue(
            rule_name=self.name,
            severity=Severity.ERROR,
            message="Train ID must not be missing.",
            affected_rows=invalid_rows
        )]
