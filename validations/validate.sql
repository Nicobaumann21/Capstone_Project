-- validations/validate.sql
SELECT 'projects' AS table_name, COUNT(*) FROM projects;
SELECT 'employees' AS table_name, COUNT(*) FROM employees;
SELECT 'time_logs_orphans' AS check, COUNT(*) FROM time_logs tl LEFT JOIN employees e ON tl.employee_id = e.employee_id WHERE tl.employee_id IS NOT NULL AND e.employee_id IS NULL;
