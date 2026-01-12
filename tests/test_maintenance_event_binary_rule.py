import pandas as pd
from rail_validation.rules.consistency_rules import MaintenanceEventBinaryRule


def test_valid_maintenance_event_passes():
    df = pd.DataFrame({"maintenance_event": [0, 1, 0]})
    assert MaintenanceEventBinaryRule().validate(df) == []


def test_invalid_maintenance_event_fails():
    df = pd.DataFrame({"maintenance_event": [0, 2, -1]})
    issues = MaintenanceEventBinaryRule().validate(df)
    assert issues[0].affected_rows == [1, 2]
