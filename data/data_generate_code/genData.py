import psycopg2
from faker import Faker
import random
from datetime import timedelta, date
import time

faker = Faker()

# --- DATEN ---

industries = [
    "Agriculture","Automotive","Aerospace","Banking","Biotechnology","Chemical Industry",
    "Construction","Consumer Electronics","Consulting","E-Commerce","Education","Energy",
    "Entertainment","Environmental Services","Fashion","Financial Services","Food and Beverage",
    "Healthcare","Hospitality","Insurance","Information Technology","Logistics","Manufacturing",
    "Marketing","Media","Mining","Nonprofit","Oil and Gas","Pharmaceuticals","Public Sector",
    "Real Estate","Renewable Energy","Retail","Robotics","Software Development","Sports",
    "Telecommunications","Tourism"
]

client_names = [
    "Apexion Labs","Bluecrest Dynamics","NovaCore Solutions","Vertexon Industries",
    "Silverline Systems","CloudForge Technologies","Everbright Analytics","LuminaWorks",
    "Starwave Innovations","QuantumPeak Software","Greenridge Manufacturing"
]

project_tags = [
    "High Priority","Medium Priority","Low Priority","Urgent","Critical",
    "Prototype","Pilot","Rollout","R&D"
]

# --- HILFSFUNKTIONEN ---
def sync_sequence(cur, table, column):
    cur.execute(f"""
        SELECT setval(
            pg_get_serial_sequence('{table}', '{column}'),
            COALESCE((SELECT MAX({column}) FROM {table}), 0)
        );
    """)


def get_random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

def get_ids(cur, table):
    cur.execute(f"SELECT {table[:-1]}_id FROM {table}")
    return [row[0] for row in cur.fetchall()]

def get_next_id(cur, table, id_column):
    cur.execute(f"SELECT COALESCE(MAX({id_column}), 0) FROM {table}")
    return cur.fetchone()[0] + 1

# --- GENERATOREN ---

def generate_clients(cur, n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO clients (name, industry)
            VALUES (%s, %s)
        """, (
            random.choice(client_names),
            random.choice(industries),
        ))

def generate_projects(cur, n):
    client_ids = get_ids(cur, "clients")
    for _ in range(n):
        start = get_random_date(date(2022, 1, 1), date(2024, 10, 1))
        end = start + timedelta(days=random.randint(60, 300))

        cur.execute("""
            INSERT INTO projects (name, client_id, start_date, end_date, status) 
            VALUES (%s, %s, %s, %s, %s)
        """, (
            f"Project {faker.word()}",
            random.choice(client_ids),
            start,
            end,
            random.choice(["Running", "Finished", "Planned"])
        ))

# ✅ VOLLSTÄNDIG ID-SICHER & DUPLIKAT-SICHER
def generate_tags(cur):
    cur.execute("SELECT tag FROM tags")
    existing_tags = {row[0] for row in cur.fetchall()}

    next_id = get_next_id(cur, "tags", "tag_id")

    for tag in project_tags:
        if tag not in existing_tags:
            cur.execute("""
                INSERT INTO tags (tag_id, tag)
                VALUES (%s, %s)
            """, (
                next_id,
                tag
            ))
            next_id += 1

def generate_project_tags(cur, existing_project_ids):
    project_ids = get_ids(cur, "projects")
    tag_ids = get_ids(cur, "tags")

    for project_id in project_ids:
        if project_id not in existing_project_ids:
            for tag_id in random.sample(tag_ids, random.randint(1, 3)):
                cur.execute("""
                    INSERT INTO project_tags (project_id, tag_id)
                    VALUES (%s, %s)
                """, (
                    project_id,
                    tag_id
                ))

def generate_teams(cur, n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO teams (name)
            VALUES (%s)
        """, (
            f"Team {faker.word()}",
        ))

def generate_employees(cur, n):
    team_ids = get_ids(cur, "teams")

    for _ in range(n):
        cur.execute("""
            INSERT INTO employees (
                name, team_id, hire_date, leave_date, role)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.first_name(),
            random.choice(team_ids),
            get_random_date(date(2020, 1, 1), date(2024, 1, 1)),
            date(2028, 1, 1),
            random.choice(["Manager", "Project-Leader", "Software-Developer", "Secretary", "Human-Resources"])
        ))

def generate_tasks(cur, n):
    employee_ids = get_ids(cur, "employees")
    project_ids = get_ids(cur, "projects")

    for _ in range(n):
        start = get_random_date(date(2022, 1, 1), date(2024, 10, 1))
        estimated_hours = random.randint(1, 30)
        end = start + timedelta(hours=estimated_hours + random.randint(-5, 5))

        cur.execute("""
            INSERT INTO tasks (project_id, assignee_id, status, created_at, closed_at, estimated_hours)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            random.choice(project_ids),
            random.choice(employee_ids),
            random.choice(["Running", "Finished", "Planned"]),
            start,
            end,
            estimated_hours
        ))

def generate_time_logs(cur, n):
    project_ids = get_ids(cur, "projects")
    employee_ids = get_ids(cur, "employees")

    for _ in range(n):
        cur.execute("""
            INSERT INTO time_logs (employee_id, project_id, date, hours, type)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            random.choice(employee_ids),
            random.choice(project_ids),
            get_random_date(date(2023, 1, 1), date(2024, 1, 1)),
            random.randint(1,  8),
            random.choice(["Design", "Planning", "Research", "Development", "Meeting"])
        ))

# --- MAIN ---

def main(n_clients, n_projects, n_employees, n_tasks, n_teams, n_time_logs):

    conn = psycopg2.connect(
        dbname="pmdb",
        user="postgres",
        password="",
        host="localhost"
    )
    cur = conn.cursor()

    # ✅ AUTOMATISCHER SEQUENZ-SYNC (entscheidend!)
    sync_sequence(cur, "clients", "client_id")
    sync_sequence(cur, "teams", "team_id")
    sync_sequence(cur, "employees", "employee_id")
    sync_sequence(cur, "projects", "project_id")
    sync_sequence(cur, "tasks", "task_id")
    sync_sequence(cur, "time_logs", "log_id")
    start = time.time()

    generate_tags(cur)                  # ID-sicher
    generate_clients(cur, n_clients)
    generate_teams(cur, n_teams)
    generate_employees(cur, n_employees)

    existing_project_ids = get_ids(cur, "projects")
    generate_projects(cur, n_projects)
    generate_project_tags(cur, existing_project_ids)

    generate_tasks(cur, n_tasks)
    generate_time_logs(cur, n_time_logs)

    conn.commit()
    cur.close()
    conn.close()

    print(f"Time to generate: {time.time() - start:.2f} sec")


if __name__ == "__main__":
    main(1000, 10000, 20000, 200000, 1000, 500000)
