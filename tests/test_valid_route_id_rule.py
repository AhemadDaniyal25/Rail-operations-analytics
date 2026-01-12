import pandas as pd
from rail_validation.rules.numeric_rules import ValidRouteIdRule


def test_valid_route_ids_pass():
    df = pd.DataFrame({"route": ["A12", "B7"]})
    assert ValidRouteIdRule().validate(df) == []


def test_invalid_route_ids_fail():
    df = pd.DataFrame({"route": ["A-12", "B@7"]})
    issues = ValidRouteIdRule().validate(df)
    assert issues[0].affected_rows == [0, 1]


def test_missing_route_column_ignored():
    df = pd.DataFrame({"delay_minutes": [5]})
    assert ValidRouteIdRule().validate(df) == []
