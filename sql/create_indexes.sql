CREATE INDEX idx_time_logs_date ON time_logs(date);
CREATE INDEX idx_time_logs_employee ON time_logs(employee_id);
CREATE INDEX idx_tasks_assignee ON tasks(assignee_id);
