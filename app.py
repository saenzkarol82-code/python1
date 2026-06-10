from flask import Flask, render_template, request
from database import conectar_postgres
from database import conectar_mongo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    mensaje = ""
    
    
    if request.method == "POST":

        try:
            #request.form obtiene datos
            documento = request.form["documento"]
            nombre = request.form["nombre"]
            correo = request.form["correo"]
            programa = request.form["programa"]
            puntaje = float(request.form["puntaje"])
            
            #Calcula beca
            aplica_beca = "SI" if puntaje >= 85 else "NO"

            #Conecta PostgreSQL  
            conexion = conectar_postgres()
            cursor = conexion.cursor()


            #registro estudiantes INSERT
            cursor.execute("""
                INSERT INTO estudiantes
                (documento, nombre, correo, programa, puntaje, aplica_beca)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                documento,
                nombre,
                correo,
                programa,
                puntaje,
                aplica_beca
            ))
            

            #COMMIT
            conexion.commit()

            #Cierra conexión
            mensaje = "Estudiante registrado correctamente"
            cursor.close()
            conexion.close()
            
            

        except Exception as e:
            mensaje = f"Error: {str(e)}"

    #Abre nueva conexión
    conexion = conectar_postgres()
    cursor = conexion.cursor()

    #SELECT estudiantes
    cursor.execute("""
        SELECT
            documento,
            nombre,
            correo,
            programa,
            puntaje,
            aplica_beca
        FROM estudiantes
        ORDER BY id DESC
    """)
    #obtener todos los registros.
    estudiantes = cursor.fetchall()

    # Cerrar conexión
    cursor.close()
    conexion.close()

    return render_template(
        "index.html",
        mensaje=mensaje,
        estudiantes=estudiantes
    )
        
    


@app.route("/test-mongo")
def test_mongo():

    try:

        cliente = conectar_mongo()

        cliente.admin.command("ping")

        return "Conexion exitosa con MongoDB Atlas"

    except Exception as e:

        return f"Error MongoDB: {e}"    
        
if __name__ == "__main__":
    app.run(debug=True)


