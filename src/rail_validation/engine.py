import pandas as pd

from rail_validation.rules.numeric_rules import *
from rail_validation.rules.completeness_rules import *
from rail_validation.rules.consistency_rules import *


class ValidationEngine:

    def __init__(self):
        self.rules = [
            NonNegativeDelayRule(),
            PositiveEnergyConsumptionRule(),
            AssetAgeBoundsRule(),
            RealisticDelayUpperBoundRule(),
            ValidRouteIdRule(),

            NoMissingDelayRule(),
            NoMissingEnergyRule(),
            NoMissingRouteRule(),
            NoMissingTrainIdRule(),

            MaintenanceEventBinaryRule(),
            NonEmptyRegionRule(),
            RouteSingleRegionRule(),
        ]

    def run(self, df: pd.DataFrame):
        issues = []
        for rule in self.rules:
            issues.extend(rule.validate(df))
        return issues
