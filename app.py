from flask import Flask, render_template, request
from database import conectar_postgres

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
            ficha = request.form["ficha"]
            puntaje = float(request.form["puntaje"])

            aplica_beca = "SI" if puntaje >= 85 else "NO"

            conexion = conectar_postgres()
            cursor = conexion.cursor()

            cursor.execute("SELECT NOW();")
            resultado = cursor.fetchone()

            cursor.close()
            conexion.close()

            mensaje = (
                f"Conexión exitosa con PostgreSQL. "
                f"Aplica a beca: {aplica_beca}. "
                f"Servidor respondió: {resultado[0]}"
            )

        except Exception as e:
            mensaje = f"Error: {str(e)}"

    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)