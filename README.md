# Capstone Project – Projektmanagement Datenbank

Dieses Projekt entstand im Fach Datenbanken und DB-Programmierung: Relational, NoSQL, New SQL

Dieser Link ist für eine Notion-Seite, auf der alle relevanten Schritte, Queries und sonstige step-by-step aufgeführt sind:
[Notion-Link](https://www.notion.so/Portfolio-Schenk-2be53dc6cef980239683e799d5455edd?source=copy_link)

## Projektstruktur

```
├── .env
├── .gitignore
├── Executive_Summary.md
├── Präsentation
│   └── Präsentation.pdf
├── README.md
├── data
│   ├── Database_data_csv
│   │   ├── clients_202512091650.csv
│   │   ├── employees_202512091650.csv
│   │   ├── project_tags_202512091650.csv
│   │   ├── projects_202512091650.csv
│   │   ├── tags_202512091650.csv
│   │   ├── tasks_202512091650.csv
│   │   ├── teams_202512091650.csv
│   │   └── time_logs_202512091650.csv
│   ├── data_for_generation
│   │   ├── clients.csv
│   │   ├── employees.csv
│   │   ├── project_tags.csv
│   │   ├── projects.csv
│   │   ├── tags.csv
│   │   ├── tasks.csv
│   │   ├── teams.csv
│   │   └── time_logs.csv
│   └── data_generate_code
│       └── genData.py
├── generate_readme.py
├── mongodb
│   └── mongodb Beispiel
├── queries
│   ├── Datenqualität und Null
│   │   └── NULL_beispiel.md
│   ├── Geschäftsführer
│   │   ├── explain_analyze_output_optimiert.txt
│   │   ├── explain_analyze_output_unoptimiert.txt
│   │   ├── output_Geschäftsführer.png
│   │   ├── querie_optimiert.sql
│   │   └── querie_unoptimiert.sql
│   ├── HR
│   │   ├── explain_analyze_output_optimiert.txt
│   │   ├── explain_analyze_output_unoptimiert.txt
│   │   ├── output_HR.png
│   │   ├── querie_optimierungen.sql
│   │   └── querie_unoptimiert.sql
│   └── PMO
│       ├── explain_analyze_output_optimiert.txt
│       ├── explain_analyze_output_unoptimiert.txt
│       ├── output_PMO.png
│       ├── querie_optimiert.sql
│       └── querie_unoptimiert.sql
├── sql
│   ├── create_indexes.sql
│   ├── pmdb_backup.sql
│   └── schema.sql
├── validations
│   └── validate.sql
```
