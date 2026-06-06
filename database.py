import psycopg2
from pymongo import MongoClient


DATABASE_URL = "postgresql://becas_user:JFVShlF84qF3k47N2ZBlliUXrOWsXPN1@dpg-d8hnbl3tqb8s73a9t6tg-a.oregon-postgres.render.com/becas"


def conectar_postgres():

    conexion = psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )

    return conexion


#def conectar_mongo():

  #  cliente = MongoClient(
   #     "TU_URI_MONGO"
    #)

   # return cliente