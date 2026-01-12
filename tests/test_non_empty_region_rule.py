import pandas as pd
from rail_validation.rules.consistency_rules import NonEmptyRegionRule


def test_valid_region_passes():
    df = pd.DataFrame({"region": ["North", "South"]})
    assert NonEmptyRegionRule().validate(df) == []


def test_empty_region_fails():
    df = pd.DataFrame({"region": [" ", "East"]})
    issues = NonEmptyRegionRule().validate(df)
    assert issues[0].affected_rows == [0]
