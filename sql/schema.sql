-- sql/schema.sql
CREATE TABLE clients (
  client_id   BIGSERIAL PRIMARY KEY,
  name        TEXT NOT NULL,
  industry    TEXT
);

CREATE TABLE teams (
  team_id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE employees (
  employee_id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  team_id BIGINT REFERENCES teams(team_id) ON DELETE SET NULL,
  hire_date DATE,
  leave_date DATE,
  role TEXT
);

CREATE TABLE projects (
  project_id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  client_id BIGINT REFERENCES clients(client_id) ON DELETE SET NULL,
  start_date DATE,
  end_date DATE,
  status TEXT
);

CREATE TABLE tasks (
  task_id BIGSERIAL PRIMARY KEY,
  project_id BIGINT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
  assignee_id BIGINT REFERENCES employees(employee_id) ON DELETE SET NULL,
  status TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  closed_at TIMESTAMP WITH TIME ZONE,
  estimated_hours NUMERIC(6,2)
);

CREATE TABLE time_logs (
  log_id BIGSERIAL PRIMARY KEY,
  employee_id BIGINT REFERENCES employees(employee_id) ON DELETE CASCADE,
  project_id BIGINT REFERENCES projects(project_id) ON DELETE CASCADE,
  date DATE NOT NULL,
  hours NUMERIC(5,2) NOT NULL,
  type TEXT
);

CREATE TABLE tags (
  tag_id BIGSERIAL PRIMARY KEY,
  tag TEXT UNIQUE NOT NULL
);

CREATE TABLE project_tags (
  project_id BIGINT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
  tag_id BIGINT NOT NULL REFERENCES tags(tag_id) ON DELETE CASCADE,
  PRIMARY KEY (project_id, tag_id)
);
