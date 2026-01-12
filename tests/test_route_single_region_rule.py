import pandas as pd
from rail_validation.rules.consistency_rules import RouteSingleRegionRule


def test_consistent_route_passes():
    df = pd.DataFrame({
        "route": ["A", "A", "B"],
        "region": ["North", "North", "South"]
    })
    assert RouteSingleRegionRule().validate(df) == []


def test_inconsistent_route_fails():
    df = pd.DataFrame({
        "route": ["A", "A"],
        "region": ["North", "South"]
    })
    issues = RouteSingleRegionRule().validate(df)
    assert issues[0].affected_rows == [0, 1]
