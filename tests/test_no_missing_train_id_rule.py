import pandas as pd
from rail_validation.rules.completeness_rules import NoMissingTrainIdRule


def test_no_missing_train_id_passes():
    df = pd.DataFrame({"train_id": ["T1", "T2"]})
    assert NoMissingTrainIdRule().validate(df) == []


def test_missing_train_id_fails():
    df = pd.DataFrame({"train_id": ["T1", None]})
    issues = NoMissingTrainIdRule().validate(df)
    assert issues[0].affected_rows == [1]
