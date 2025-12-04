import psycopg2
from faker import Faker
import random
from datetime import timedelta, date, datetime
import time

faker = Faker()
# --- Daten ---

industries = [
    "Agriculture",
    "Automotive",
    "Aerospace",
    "Banking",
    "Biotechnology",
    "Chemical Industry",
    "Construction",
    "Consumer Electronics",
    "Consulting",
    "E-Commerce",
    "Education",
    "Energy",
    "Entertainment",
    "Environmental Services",
    "Fashion",
    "Financial Services",
    "Food and Beverage",
    "Healthcare",
    "Hospitality",
    "Insurance",
    "Information Technology",
    "Logistics",
    "Manufacturing",
    "Marketing",
    "Media",
    "Mining",
    "Nonprofit",
    "Oil and Gas",
    "Pharmaceuticals",
    "Public Sector",
    "Real Estate",
    "Renewable Energy",
    "Retail",
    "Robotics",
    "Software Development",
    "Sports",
    "Telecommunications",
    "Tourism",
]
client_names = [
    "Apexion Labs",
    "Bluecrest Dynamics",
    "NovaCore Solutions",
    "Vertexon Industries",
    "Silverline Systems",
    "CloudForge Technologies",
    "Everbright Analytics",
    "LuminaWorks",
    "Starwave Innovations",
    "QuantumPeak Software",
    "Greenridge Manufacturing",
    "Hyperion Commerce",
    "Skyline Robotics",
    "BrightSphere Group",
    "OceanGate Logistics",
    "AuroraHive",
    "FutureEdge Consulting",
    "IronGate Engineering",
    "Northstar Holdings",
    "DreamShift Media",
    "SparkVector",
    "CrimsonLeaf Foods",
    "MetroNova Retail",
    "SummitBridge Finance",
    "PureFlow Biotech",
    "RapidStream Data",
    "OmniPath Mobility",
    "CrystalPeak Medical",
    "UrbanRise Realty",
    "Golden Horizon Energy",
    "DeepWell Resources",
    "OrbitKey Security",
    "CloudNest AI",
    "SilverStream Waterworks",
    "TrueNorth Enterprises",
    "PrimeField Robotics",
    "NextEra Marketing",
    "HorizonWave Travel",
    "BlueNest Hospitality",
    "UrbanSpark Design",
    "ForestMoon Games",
    "MagmaCore Materials",
    "DigitalTrace Networks",
    "EcoSphere Agriculture",
    "BrightFuel Renewables",
    "CobaltBridge Mining",
    "NeonPulse Entertainment",
    "AstralPoint Telecom",
    "Suncrest Insurance",
    "IronRoot Construction",
    "SwiftFox Mobility",
    "Skybound Apparel",
    "GreenPlanet Organics",
    "LunarPeak Ventures",
    "ZenithPath Consulting",
    "Everstone Publishing",
    "BlueTitan Defense",
    "EchoField Analytics",
    "SilverPulse Finance",
    "BrightOcean Ventures",
    "CyberVale Systems",
    "TitanRiver Engineering",
    "NovaForge Architecture",
    "PrimeVista Media",
    "FrostGate Technologies",
    "BoldStone Retail",
    "EcoMind Services",
    "CrystalLeaf Cosmetics",
    "QuantumBridge Banking",
    "UrbanCloud IT",
    "TruePulse Devices",
    "Stormcrest Electronics",
    "GoldenTrail Transport",
    "Wavestone Travel",
    "AetherWorks AI",
    "Firestone Robotics",
    "MoonStar Fashion",
    "NeptuneForge Metals",
    "InfiniteLoop Software",
    "SoftWave Digital",
    "ArcticPeak Solutions",
    "TerraNova Healthcare",
    "OrangeBeam Studios",
    "BlueMosaic Consulting",
    "HorizonRoot Education",
    "Northgate Utilities",
    "SteelWing Aviation",
    "AquaPulse Labs",
    "DataSphere Intelligence",
    "Dynamo Ridge",
    "SilverArrow Motors",
    "UrbanForge Interiors",
    "WindGate Renewables",
    "NightSky Beverages",
    "BrightLine HR",
    "CrystalWorks Pharma",
    "NovaTide Shipping",
    "PeakVision Optics",
    "IronLeaf Hardware"
]
project_tags = [
    "High Priority",
    "Medium Priority",
    "Low Priority",
    "Urgent",
    "Critical", "Prototype", "Pilot", "Rollout","R&D"
]




# --- Hilfsfunktionen ---

def get_random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def get_ids(cur, table):
    cur.execute(f"SELECT {table[:-1]}_id FROM {table}")
    return [row[0] for row in cur.fetchall()]


# --- Generatoren pro Tabelle ---

def generate_clients(cur, n):
    for i in range(n):
        cur.execute("""
            INSERT INTO clients (name, industry)
            VALUES (%s, %s)
        """, (
            random.choice(client_names),
            random.choice(industries),
        ))

def generate_projects(cur, n):
    client_ids = get_ids(cur, "clients")
    for i in range(n):
        start = get_random_date(date(2022, 1, 1), date(2024, 10, 1))
        duration_days = random.randint(60, 300)
        end = start + timedelta(days=duration_days)
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

def generate_tags(cur):
    for i,tag in enumerate(project_tags):
        cur.execute("""
            INSERT INTO tags (tag_id, tag)
            VALUES (%s, %s)
        """, (
            i,
            tag
        ))



def generate_project_tags(cur):
    project_ids = get_ids(cur, "projects")
    tag_ids = get_ids(cur, "tags")
    for project_id in project_ids:
        number_of_tags = random.randint(1, 3)
        tags = random.sample(tag_ids, number_of_tags)
        for tag_id in tags:
            cur.execute("""
                INSERT INTO project_tags (project_id, tag_id)
                VALUES (%s, %s)
            """, (
                project_id,
                tag_id
            ))


def generate_employees(cur, n):
    team_ids = get_ids(cur, "teams")
    for i in range(n):
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
def generate_teams(cur, n):
    for i in range(n):
        cur.execute("""
            INSERT INTO teams (name)
            VALUES (%s)
        """, (
            f"Team {faker.word()}",
        ))

def generate_tasks(cur, n):
    employee_ids = get_ids(cur, "employees")
    project_ids = get_ids(cur, "projects")
    for i in range(n):
        start = get_random_date(date(2022, 1, 1), date(2024, 10, 1))
        estimated_hours = random.randint(1, 30)
        actual_hours = estimated_hours + random.randint(-5, 5)
        end = start + timedelta(hours=actual_hours)
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
    for i in range(n):
        cur.execute("""
            INSERT INTO time_logs (employee_id, project_id, date, hours, type)
            VALUES ( %s, %s, %s, %s, %s)
        """, (
            random.choice(employee_ids),
            random.choice(project_ids),
            get_random_date(date(2023, 1, 1), date(2024, 1, 1)),
            random.randint(1,  8),
            random.choice(["Design", "Planning", "Research", "Development", "Meeting"])
        ))



# --- Main ---

def main(n_clients, n_projekts, n_employees, n_tasks, n_teams, n_time_logs):
    conn = psycopg2.connect(
        dbname="Portfolio",
        user="postgres",
        password="abc123!\"§",
        host="localhost"
    )
    cur = conn.cursor()

    cur.execute("SELECT current_database(), current_schema();")
    db, schema = cur.fetchone()
    print(f"Aktive Datenbank: {db}, Aktives Schema: {schema}")


    start = time.time()

    generate_tags(cur)
    generate_clients(cur, n_clients)
    generate_teams(cur, n_teams)
    generate_employees(cur, n_employees)
    generate_projects(cur, n_projekts)
    generate_project_tags(cur)
    generate_tasks(cur, n_tasks)
    generate_time_logs(cur, n_time_logs)

    print(f"Time to generate: {time.time() - start:.2f} sec")

    conn.commit()
    cur.close()
    conn.close()



if __name__ == "__main__":
    main(10,100,200,2000, 10, 5000)

