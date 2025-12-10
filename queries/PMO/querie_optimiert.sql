
CREATE INDEX idx_tasks_status_assignee ON tasks(status, assignee_id);

WITH task_counts AS (
    SELECT
        e.employee_id,
        e.team_id,
        e.role,
        COUNT(t.task_id) AS task_count
    FROM employees e
    LEFT JOIN tasks t
        ON e.employee_id = t.assignee_id
    WHERE t.status = 'Running'
       OR t.task_id IS NULL
    GROUP BY e.employee_id, e.team_id, e.role
),
team_summary AS (
    SELECT
        tc.team_id,
        tm.name AS team_name,
        AVG(tc.task_count) AS avg_task_per_employee,
        MIN(tc.task_count) AS min_task_per_employee,
        MAX(tc.task_count) AS max_task_per_employee,
        COUNT(tc.employee_id) AS num_employees
    FROM task_counts tc
    JOIN teams tm
        ON tc.team_id = tm.team_id
    GROUP BY tc.team_id, tm.name
)
SELECT *
FROM team_summary
ORDER BY avg_task_per_employee ASC;
