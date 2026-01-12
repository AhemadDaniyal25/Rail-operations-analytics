import pandas as pd
from rail_validation.rules.completeness_rules import NoMissingDelayRule


def test_no_missing_delay_passes():
    df = pd.DataFrame({"delay_minutes": [1, 2, 3]})
    assert NoMissingDelayRule().validate(df) == []


def test_missing_delay_fails():
    df = pd.DataFrame({"delay_minutes": [1, None, 3]})
    issues = NoMissingDelayRule().validate(df)
    assert issues[0].affected_rows == [1]


def test_all_missing_delay():
    df = pd.DataFrame({"delay_minutes": [None, None]})
    issues = NoMissingDelayRule().validate(df)
    assert issues[0].affected_rows == [0, 1]
