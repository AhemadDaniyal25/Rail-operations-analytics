import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/rail_operations.csv")

# Data quality checks
df = df.dropna()
df = df[df["delay_minutes"] >= 0]
df = df[df["energy_kwh"] > 0]

# Dimension tables
dim_route = df[["route", "region"]].drop_duplicates().reset_index(drop=True)
dim_route["route_id"] = dim_route.index + 1

dim_asset = df[["train_id", "train_type", "asset_age_years"]].drop_duplicates().reset_index(drop=True)
dim_asset["asset_id"] = dim_asset.index + 1

dim_time = df[["date"]].drop_duplicates().reset_index(drop=True)
dim_time["date_id"] = dim_time.index + 1

# Fact table
fact = df.merge(dim_route, on=["route", "region"])
fact = fact.merge(dim_asset, on=["train_id", "train_type", "asset_age_years"])
fact = fact.merge(dim_time, on=["date"])

fact_operations = fact[
    ["route_id", "asset_id", "date_id", "delay_minutes", "energy_kwh", "maintenance_event"]
]

# Save processed data
dim_route.to_csv("data/processed/dim_route.csv", index=False)
dim_asset.to_csv("data/processed/dim_asset.csv", index=False)
dim_time.to_csv("data/processed/dim_time.csv", index=False)
fact_operations.to_csv("data/processed/fact_operations.csv", index=False)

print("Pipeline executed successfully.")
