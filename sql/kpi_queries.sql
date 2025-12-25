-- ======================================================
-- Rail Operations Analytics KPIs
-- Purpose: Decision-support metrics for operations teams
-- ======================================================

-- 1. On-Time Performance (% of trips with delay <= 5 minutes)
SELECT
    ROUND(
        SUM(CASE WHEN delay_minutes <= 5 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS on_time_performance_pct
FROM fact_operations;

-- 2. Average delay per route
SELECT
    r.route_name,
    ROUND(AVG(f.delay_minutes), 2) AS avg_delay_minutes
FROM fact_operations f
JOIN dim_route r ON f.route_id = r.route_id
GROUP BY r.route_name
ORDER BY avg_delay_minutes DESC;

-- 3. Energy consumption vs average delay per route
SELECT
    r.route_name,
    ROUND(AVG(f.energy_kwh), 2) AS avg_energy_kwh,
    ROUND(AVG(f.delay_minutes), 2) AS avg_delay_minutes
FROM fact_operations f
JOIN dim_route r ON f.route_id = r.route_id
GROUP BY r.route_name;

-- 4. Maintenance impact analysis
SELECT
    maintenance_event,
    ROUND(AVG(delay_minutes), 2) AS avg_delay_minutes
FROM fact_operations
GROUP BY maintenance_event;
