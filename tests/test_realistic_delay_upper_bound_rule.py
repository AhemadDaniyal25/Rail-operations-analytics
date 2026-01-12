import pandas as pd
from rail_validation.rules.numeric_rules import RealisticDelayUpperBoundRule


def test_realistic_delay_passes():
    df = pd.DataFrame({"delay_minutes": [10, 200, 600]})
    assert RealisticDelayUpperBoundRule().validate(df) == []


def test_excessive_delay_fails():
    df = pd.DataFrame({"delay_minutes": [100, 700]})
    issues = RealisticDelayUpperBoundRule().validate(df)
    assert issues[0].affected_rows == [1]


def test_missing_delay_column_ignored():
    df = pd.DataFrame({"energy_kwh": [10]})
    assert RealisticDelayUpperBoundRule().validate(df) == []
