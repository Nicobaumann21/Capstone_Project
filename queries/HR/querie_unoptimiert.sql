WITH max_date AS (
    SELECT MAX(date) AS latest_date
    FROM time_logs
),
employee_hours AS (
    SELECT
        e.employee_id,
        e.team_id,
        e.role,
        SUM(tl.hours) AS total_hours
    FROM time_logs tl
    JOIN employees e
        ON tl.employee_id = e.employee_id
    CROSS JOIN max_date md
    WHERE tl.date >= md.latest_date - INTERVAL '3 months'
    GROUP BY e.employee_id, e.team_id, e.role
),
team_avg AS (
    SELECT
        team_id,
        role,
        AVG(total_hours) AS avg_hours_per_role
    FROM employee_hours
    GROUP BY team_id, role
)
SELECT
    eh.employee_id,
    eh.team_id,
    eh.role,
    eh.total_hours,
    ta.avg_hours_per_role,
    eh.total_hours - ta.avg_hours_per_role AS deviation_from_role_avg
FROM employee_hours eh
JOIN team_avg ta
    ON eh.team_id = ta.team_id
    AND eh.role = ta.role
WHERE eh.total_hours > ta.avg_hours_per_role * 1.2  -- z. B. 20% über dem Durchschnitt
ORDER BY deviation_from_role_avg DESC;
