import psycopg2
import os
from pymongo import MongoClient



DATABASE_URL = "postgresql://becas_user:JFVShlF84qF3k47N2ZBlliUXrOWsXPN1@dpg-d8hnbl3tqb8s73a9t6tg-a.oregon-postgres.render.com/becas"


def conectar_postgres():

    conexion = psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )

    return conexion


MONGO_URI = "mongodb+srv://Estudiantes:REQ35wocsM8bisYx@cluster0.qyuyvw5.mongodb.net/?appName=Cluster0"

def conectar_mongo():

    cliente = MongoClient(MONGO_URI)

    return cliente