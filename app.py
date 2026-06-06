from flask import Flask, render_template, request

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

            aplica_beca = "SI" if puntaje >= 85 else "NO"

            mensaje = (
                f"Estudiante {nombre} registrado correctamente. "
                f"Aplica a beca: {aplica_beca}"
            )

        except Exception as e:

            mensaje = f"Error: {str(e)}"

    return render_template(
        "index.html",
        mensaje=mensaje
    )

if __name__ == "__main__":
    app.run(debug=True)