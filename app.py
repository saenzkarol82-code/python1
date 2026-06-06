from flask import Flask, render_template, request
from database import conectar_postgres, coleccion_estudiantes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    mensaje = ""

    if request.method == "POST":

        try:

            documento = request.form["documento"]
            nombre = request.form["nombre"]
            correo = request.form["correo"]
            programa = request.form["programa"]
            puntaje = float(request.form["puntaje"])

            # Validaciones
            if not documento or not nombre:
                raise Exception("Documento y nombre son obligatorios")

            if "@" not in correo:
                raise Exception("Correo inválido")

            if puntaje < 0 or puntaje > 100:
                raise Exception("Puntaje fuera de rango")

            aplica_beca = "SI" if puntaje >= 85 else "NO"

            # PostgreSQL
            conexion = conectar_postgres()
            cursor = conexion.cursor()

            cursor.execute("""
                INSERT INTO estudiantes
                (documento,nombre,correo,programa,puntaje,aplica_beca)
                VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                documento,
                nombre,
                correo,
                programa,
                puntaje,
                aplica_beca
            ))

            conexion.commit()

            cursor.close()
            conexion.close()

            # MongoDB
            coleccion_estudiantes.insert_one({
                "documento": documento,
                "nombre": nombre,
                "correo": correo,
                "programa": programa,
                "puntaje": puntaje,
                "aplica_beca": aplica_beca
            })

            mensaje = f"Estudiante registrado. Beca: {aplica_beca}"

        except Exception as e:

            mensaje = f"Error: {str(e)}"

    return render_template(
        "index.html",
        mensaje=mensaje
    )

if __name__ == "__main__":
    app.run(debug=True)