import pandas as pd
from rail_validation.rules.completeness_rules import NoMissingEnergyRule


def test_no_missing_energy_passes():
    df = pd.DataFrame({"energy_kwh": [5, 10]})
    assert NoMissingEnergyRule().validate(df) == []


def test_missing_energy_fails():
    df = pd.DataFrame({"energy_kwh": [None, 2]})
    issues = NoMissingEnergyRule().validate(df)
    assert issues[0].affected_rows == [0]
