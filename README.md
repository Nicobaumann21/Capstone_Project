# 🚀 Capstone Project – Projektmanagement Datenbank

![GitHub Repo Size](https://img.shields.io/github/repo-size/Nicobaumann21/Capstone_Project)
![GitHub last commit](https://img.shields.io/github/last-commit/Nicobaumann21/Capstone_Project)

Dieses Projekt ist Teil des Data-Science-/KI-Studiums an der DHBW.  
Ziel ist die Erstellung einer **PostgreSQL-Datenbank für Projektmanagement-Daten** mit **CSV-Import**, Docker-Setup und Validierungsscripts.

---

## 📂 Projektstruktur

Capstone_Project/
│
├─ data/ # CSV-Dateien für Tabellen
│ ├─ clients.csv
│ ├─ employees.csv
│ ├─ projects.csv
│ ├─ tasks.csv
│ ├─ tags.csv
│ ├─ project_tags.csv
│ └─ time_logs.csv
│
├─ validations/ # SQL-Scripts zur Datenvalidierung
│ └─ validate.sql
│
├─ sql/ # SQL-Scripts zur DB-Struktur
│ └─ schema.sql
│
├─ venv/ # Virtuelle Python-Umgebung (ignoriert in Git)
├─ .gitignore
└─ README.md

yaml
Code kopieren

---

## 🛠 Setup-Anleitung

### 1️⃣ Docker-Container starten

```bash
docker run --name pg-dev -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=pmdb -p 5432:5432 -d postgres:15
2️⃣ CSV-Dateien in den Container kopieren
bash
Code kopieren
docker cp data/clients.csv pg-dev:/data/clients.csv
docker cp data/employees.csv pg-dev:/data/employees.csv
docker cp data/projects.csv pg-dev:/data/projects.csv
docker cp data/tasks.csv pg-dev:/data/tasks.csv
docker cp data/tags.csv pg-dev:/data/tags.csv
docker cp data/project_tags.csv pg-dev:/data/project_tags.csv
docker cp data/time_logs.csv pg-dev:/data/time_logs.csv
3️⃣ Datenbank-Schema erstellen
bash
Code kopieren
docker exec -it pg-dev psql -U postgres -d pmdb -f /sql/schema.sql
4️⃣ CSVs importieren
bash
Code kopieren
docker exec -it pg-dev psql -U postgres -d pmdb
Im psql-Prompt:

sql
Code kopieren
\copy clients(client_id,name,industry) FROM '/data/clients.csv' CSV HEADER
\copy teams(team_id,name) FROM '/data/teams.csv' CSV HEADER
\copy employees(employee_id,name,team_id,hire_date,leave_date,role) FROM '/data/employees.csv' CSV HEADER
\copy projects(project_id,name,client_id,start_date,end_date,status) FROM '/data/projects.csv' CSV HEADER
\copy tasks(task_id,project_id,assignee_id,status,created_at,closed_at,estimated_hours) FROM '/data/tasks.csv' CSV HEADER
\copy tags(tag_id,tag) FROM '/data/tags.csv' CSV HEADER
\copy project_tags(project_id,tag_id) FROM '/data/project_tags.csv' CSV HEADER
\copy time_logs(log_id,employee_id,project_id,date,hours,type) FROM '/data/time_logs.csv' CSV HEADER
5️⃣ Daten validieren
bash
Code kopieren
docker cp validations/validate.sql pg-dev:/validations/validate.sql
docker exec -it pg-dev psql -U postgres -d pmdb -f /validations/validate.sql
✅ Features
FK-Constraints und Zeitdimension sind im Datenmodell berücksichtigt

Tabellen: Projects, Clients, Employees, Teams, Tasks, Tags, Project_Tags, Time_Logs

n:m Beziehung: projects ↔ tags über project_tags

JOIN-Kette über 3 Tabellen möglich: projects → tasks → time_logs

Saubere Validierung der Daten via validate.sql

⚡ Hinweise
.gitignore schließt venv, Logs und große CSV-Dateien aus

SQL- und Python-Skripte sowie Dokumentation werden versioniert

Docker & PostgreSQL Setup ermöglicht lokale Reproduzierbarkeit

📫 Kontakt
Projekt von Nicobaumann21
GitHub: https://github.com/Nicobaumann21/Capstone_Project
