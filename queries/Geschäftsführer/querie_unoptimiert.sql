
SELECT
    c.industry,
    c.name,
    COUNT(p.project_id) AS project_count
FROM clients c
JOIN projects p ON c.client_id = p.client_id
GROUP BY c.industry, c.name
HAVING COUNT(p.project_id) = (
    SELECT MAX(sub.project_count)
    FROM (
        SELECT COUNT(*) AS project_count
        FROM projects p2
        WHERE p2.client_id IN (
            SELECT client_id
            FROM clients
            WHERE industry = c.industry
        )
        GROUP BY p2.client_id
    ) sub
)
OR COUNT(p.project_id) = (
    SELECT MIN(sub.project_count)
    FROM (
        SELECT COUNT(*) AS project_count
        FROM projects p2
        WHERE p2.client_id IN (
            SELECT client_id
            FROM clients
            WHERE industry = c.industry
        )
        GROUP BY p2.client_id
    ) sub
)
ORDER BY c.industry, project_count DESC;

