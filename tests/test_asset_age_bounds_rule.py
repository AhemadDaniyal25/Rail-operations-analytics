import pandas as pd

from rail_validation.rules.numeric_rules import AssetAgeBoundsRule
from rail_validation.models import Severity


def test_valid_asset_age_passes():
    df = pd.DataFrame({
        "asset_age_years": [1, 10, 25, 50]
    })

    rule = AssetAgeBoundsRule()
    issues = rule.validate(df)

    assert issues == []


def test_negative_asset_age_fails():
    df = pd.DataFrame({
        "asset_age_years": [-1, 5, 10]
    })

    rule = AssetAgeBoundsRule()
    issues = rule.validate(df)

    assert issues[0].affected_rows == [0]
    assert issues[0].severity == Severity.WARNING


def test_asset_age_above_upper_bound_fails():
    df = pd.DataFrame({
        "asset_age_years": [10, 60]
    })

    rule = AssetAgeBoundsRule()
    issues = rule.validate(df)

    assert issues[0].affected_rows == [1]


def test_missing_asset_age_column_is_ignored():
    df = pd.DataFrame({
        "energy_kwh": [10, 20]
    })

    rule = AssetAgeBoundsRule()
    issues = rule.validate(df)

    assert issues == []
