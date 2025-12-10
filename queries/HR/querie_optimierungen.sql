CREATE INDEX idx_time_logs_date ON time_logs(date);

CREATE INDEX idx_time_logs_employee_id ON time_logs(employee_id);

WHERE tl.date >= (SELECT MAX(date) FROM time_logs) - INTERVAL '3 months'
