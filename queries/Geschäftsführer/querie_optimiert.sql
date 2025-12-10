WITH project_counts AS (
    SELECT client_id, COUNT(*) AS project_count
    FROM projects
    GROUP BY client_id
)
SELECT
    c.industry,
    c.name,
    pc.project_count
FROM clients c
JOIN project_counts pc ON c.client_id = pc.client_id
JOIN (
    -- Max / Min pro Industry
    SELECT
        c2.industry,
        MAX(pc2.project_count) AS max_projects,
        MIN(pc2.project_count) AS min_projects
    FROM clients c2
    JOIN project_counts pc2 ON c2.client_id = pc2.client_id
    GROUP BY c2.industry
) agg ON c.industry = agg.industry
WHERE pc.project_count = agg.max_projects OR pc.project_count = agg.min_projects
ORDER BY c.industry, pc.project_count DESC;