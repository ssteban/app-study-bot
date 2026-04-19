import psycopg2
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Carga el .env que está en la carpeta app/ sin importar desde dónde se lanza uvicorn
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")


class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=os.getenv("PGHOST"),
                user=os.getenv("PGUSER"),
                password=os.getenv("PGPASSWORD"),
                dbname=os.getenv("PGDATABASE"),
                sslmode=os.getenv("PGSSLMODE", "require"),
            )
            return self.conn
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            sys.exit(1)

    def close(self):
        self.conn.close()


