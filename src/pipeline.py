import pandas as pd
from rail_validation.engine import ValidationEngine
from rail_validation.report import generate_quality_report

df = pd.read_csv("data/raw/rail_operations.csv")

engine = ValidationEngine()
issues = engine.run(df)

generate_quality_report(issues)

print(f"Validation completed with {len(issues)} issues.")
