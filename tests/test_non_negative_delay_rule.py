import pandas as pd

from rail_validation.rules.numeric_rules import NonNegativeDelayRule
from rail_validation.models import Severity


def test_valid_delays_pass():
    df = pd.DataFrame({
        "delay_minutes": [0, 5, 10]
    })

    rule = NonNegativeDelayRule()
    issues = rule.validate(df)

    assert issues == []


def test_negative_delay_fails():
    df = pd.DataFrame({
        "delay_minutes": [5, -3, 2]
    })

    rule = NonNegativeDelayRule()
    issues = rule.validate(df)

    assert len(issues) == 1
    assert issues[0].severity == Severity.ERROR
    assert issues[0].affected_rows == [1]


def test_all_negative_delays():
    df = pd.DataFrame({
        "delay_minutes": [-1, -2, -3]
    })

    rule = NonNegativeDelayRule()
    issues = rule.validate(df)

    assert issues[0].affected_rows == [0, 1, 2]


def test_missing_column_is_ignored():
    df = pd.DataFrame({
        "some_other_column": [1, 2, 3]
    })

    rule = NonNegativeDelayRule()
    issues = rule.validate(df)

    assert issues == []
