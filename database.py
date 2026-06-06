import os
import psycopg2

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def conectar_postgres():
    return psycopg2.connect(
        os.getenv("DATABASE_URL")
    )

cliente = MongoClient(
    os.getenv("MONGO_URI")
)

db = cliente["becas"]

coleccion_estudiantes = db["estudiantes"]