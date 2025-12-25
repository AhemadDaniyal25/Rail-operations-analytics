# Rail Operations Analytics Platform

## Overview
This project demonstrates an end-to-end analytics platform for rail operations, transforming raw operational data into decision-ready insights to improve punctuality, energy efficiency, and asset reliability.

The project simulates challenges commonly faced by rail operators and mobility companies, such as delay analysis, energy optimization, and maintenance prioritization.

## Business Problem
Rail operations generate large volumes of data, but insights are often fragmented across teams. This project addresses:
- Identifying root causes of delays across routes
- Balancing punctuality with energy consumption
- Understanding the operational impact of maintenance events
- Communicating insights clearly to non-technical stakeholders

## Architecture
- **Python**: Data ingestion, validation, and transformation
- **SQL**: Dimensional data modeling and KPI definitions
- **Power BI**: Interactive dashboards for operational decision support

## Key KPIs
- Average delay by route
- On-time performance indicators
- Energy consumption vs delay trade-offs
- Maintenance impact on operational delays

## Results & Insights
- Certain routes show higher energy consumption without proportional punctuality improvements, indicating optimization potential.
- Maintenance events correlate with higher short-term delays, highlighting the need for proactive planning.
- Clear KPI visualization enables faster and more informed operational decision-making.

## Dashboards
Power BI dashboard screenshots are available in the `powerbi/dashboard_screenshots/` folder:
- Operations Overview
- Energy & Sustainability
- Maintenance Insights

## How to Run
```bash
pip install -r requirements.txt
python src/pipeline.py
