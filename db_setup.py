import psycopg2
import subprocess
from decouple import config

SUPERUSER = config("DB_SUPERUSER", default="postgres")
SUPERPASS = config("DB_SUPERPASS", default="your_superuser_password")
HOST = config("DB_HOST", default="localhost")
PORT = config("DB_PORT", default="5432")
TARGET_DB = config("DB_NAME")
APP_USER = config("DB_USER")
APP_PASS = config("DB_PASSWORD")

def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=SUPERUSER,
        password=SUPERPASS,
        host=HOST,
        port=PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{TARGET_DB}'")
    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {TARGET_DB}")

    cursor.execute(f"SELECT 1 FROM pg_roles WHERE rolname = '{APP_USER}'")
    if not cursor.fetchone():
        cursor.execute(f"CREATE USER {APP_USER} WITH PASSWORD '{APP_PASS}'")

    cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {TARGET_DB} TO {APP_USER}")

    cursor.execute(f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '{TARGET_DB}' AND pid <> pg_backend_pid()")
    cursor.close()
    conn.close()

    conn = psycopg2.connect(
        dbname=TARGET_DB,
        user=SUPERUSER,
        password=SUPERPASS,
        host=HOST,
        port=PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE SCHEMA IF NOT EXISTS public")
    cursor.execute(f"GRANT USAGE ON SCHEMA public TO {APP_USER}")
    cursor.execute(f"GRANT CREATE ON SCHEMA public TO {APP_USER}")

    cursor.close()
    conn.close()

def run_migrations_and_load_data():
    subprocess.run(["python", "manage.py", "migrate"])
    subprocess.run(["python", "manage.py", "loaddata", "quotes.json"])

if __name__ == "__main__":
    create_database()
    run_migrations_and_load_data()
    print("Setup complete.")
