import pandas as pd
from rail_validation.rules.completeness_rules import NoMissingRouteRule


def test_valid_routes_pass():
    df = pd.DataFrame({"route": ["A", "B"]})
    assert NoMissingRouteRule().validate(df) == []


def test_missing_route_fails():
    df = pd.DataFrame({"route": [None, "A"]})
    issues = NoMissingRouteRule().validate(df)
    assert issues[0].affected_rows == [0]


def test_empty_route_fails():
    df = pd.DataFrame({"route": [" ", "B"]})
    issues = NoMissingRouteRule().validate(df)
    assert issues[0].affected_rows == [0]
