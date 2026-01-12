import pandas as pd

from rail_validation.rules.numeric_rules import PositiveEnergyConsumptionRule
from rail_validation.models import Severity


def test_valid_energy_passes():
    df = pd.DataFrame({
        "energy_kwh": [10.5, 3.2, 1.0]
    })

    rule = PositiveEnergyConsumptionRule()
    issues = rule.validate(df)

    assert issues == []


def test_zero_energy_fails():
    df = pd.DataFrame({
        "energy_kwh": [5.0, 0.0, 2.1]
    })

    rule = PositiveEnergyConsumptionRule()
    issues = rule.validate(df)

    assert issues[0].affected_rows == [1]


def test_negative_energy_fails():
    df = pd.DataFrame({
        "energy_kwh": [-1.0, -5.0]
    })

    rule = PositiveEnergyConsumptionRule()
    issues = rule.validate(df)

    assert issues[0].severity == Severity.ERROR
    assert issues[0].affected_rows == [0, 1]


def test_missing_energy_column_is_ignored():
    df = pd.DataFrame({
        "delay_minutes": [1, 2, 3]
    })

    rule = PositiveEnergyConsumptionRule()
    issues = rule.validate(df)

    assert issues == []
