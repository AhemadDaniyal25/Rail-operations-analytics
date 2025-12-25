# Rail Operations Analytics Platform

## Overview
This project demonstrates an end-to-end analytics platform for rail operations, transforming raw operational data into decision-ready insights to improve punctuality, energy efficiency, and asset reliability.

The project simulates challenges commonly faced by rail operators such as delay analysis, energy optimization, and maintenance prioritization.

## Business Problem
Rail operations generate large volumes of data, but insights are often fragmented across teams. This project addresses:
- Identifying root causes of delays
- Balancing punctuality and energy consumption
- Understanding the impact of maintenance events
- Communicating insights clearly to non-technical stakeholders

## Architecture
- **Python**: Data ingestion, validation, and transformation
- **SQL**: Dimensional data modeling and KPI queries
- **Power BI**: Interactive dashboards for decision support

## Key KPIs
- On-Time Performance (%)
- Average Delay by Route
- Energy Consumption vs Delay
- Maintenance Impact on Delays

## Results & Insights
- Certain routes show higher energy consumption without proportional punctuality gains.
- Maintenance events correlate with higher short-term delays but reduce long-term risk.
- Clear KPI visualization enables faster operational decision-making.

## Dashboards
Screenshots of the Power BI dashboards are available in the `powerbi/dashboard_screenshots/` folder.

## How to Run
```bash
pip install -r requirements.txt
python src/pipeline.py
