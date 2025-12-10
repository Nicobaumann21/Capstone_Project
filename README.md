# 🚀 Capstone Project – Projektmanagement Datenbank



Dieses Projekt entstand im Fach Datenbanken und DB-Programmierung: Relational, NoSQL, New SQL

Dieser Link ist für eine Notion seite auf der alle Relevanten Schritte, Queries und sonstige die step für step aufgeführt sind 
https://www.notion.so/Portfolio-Schenk-2be53dc6cef980239683e799d5455edd?source=copy_link

---
```bash
## 📂 Projektstruktur

Capstone_Project/
│
├─ data/
│   ├─ data_for_generation/            # hier sind daten mit denen die Datenbank ürsprünglich aufgesetzt wurde
│   │   ├─ clients.csv
│   │   ├─ employees.csv
│   │   ├─ projects.csv
│   │   ├─ tasks.csv
│   │   ├─ tags.csv
│   │   ├─ project_tags.csv
│   │   ├─ time_logs.csv
│   │   └─ teams.csv
│   │
│   ├─ data_generate_code/             # Code für die Datengenerierung
│   │   └─ genData.py
│   │
│   └─ Database_data_csv/              # aktuell vollständige Datenbank nach generierung
│       ├─ clients.csv
│       ├─ employees.csv
│       ├─ project_tags.csv
│       ├─ projects.csv
│       ├─ tags.csv
│       ├─ tasks.csv
│       ├─ teams.csv
│       └─ time_logs.csv
│
├─ queries/
│   ├─             
│   │   ├─ 
│   │   ├─ 
│   │   ├─ 
│   │   ├─ 
│   │   ├─ 
│   │   ├─ 
│   │   ├─ 
│   │   └─ 
│
│
├─ validations/
│   └─ validate.sql                     # SQL-Skripte zur Validierung
│
├─ sql/
│   └─ schema.sql                       # Datenbankschema
│
├─ venv/                                 
│
├─ .gitignore
│
└─ README.md


