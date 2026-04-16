from flask import Flask, render_template, request
import logica

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    active_tab = "generar"

    # para mantener datos en inputs
    datos = {
        "L1": "",
        "L2": "",
        "cadena": "",
        "n": ""
    }

    if request.method == "POST":
        operacion = request.form.get("operacion")

        # guardar datos
        datos["L1"] = request.form.get("L1", "")
        datos["L2"] = request.form.get("L2", "")
        datos["cadena"] = request.form.get("cadena", "")
        datos["n"] = request.form.get("n", "")

        try:
            # ---------------- GENERAR ----------------
            if operacion == "generar":
                active_tab = "generar"
                L1 = datos["L1"].split(",")
                n = int(datos["n"])

                res = logica.generar_cadenas(L1, n)
                resultado = "\n".join(res)

            # ---------------- OPERACIONES ----------------
            elif operacion == "pertenece":
                active_tab = "operaciones"
                L1 = datos["L1"].split(",")
                cadena = datos["cadena"]

                res = logica.pertenece(cadena, L1)
                resultado = str(res)

            elif operacion == "union":
                active_tab = "operaciones"
                L1 = datos["L1"].split(",")
                L2 = datos["L2"].split(",")

                res = logica.union(L1, L2)
                resultado = "\n".join(res)

            elif operacion == "concat":
                active_tab = "operaciones"
                L1 = datos["L1"].split(",")
                L2 = datos["L2"].split(",")

                res = logica.concatenacion(L1, L2)
                resultado = "\n".join(res)

            # ---------------- KLEENE ----------------
            elif operacion == "kleene":
                active_tab = "kleene"
                L1 = datos["L1"].split(",")
                n = int(datos["n"])

                res = logica.kleeneStar(L1, n)
                resultado = "\n".join(res)

            elif operacion == "plus":
                active_tab = "kleene"
                L1 = datos["L1"].split(",")
                n = int(datos["n"])

                res = logica.kleenePlus(L1, n)
                resultado = "\n".join(res)

            elif operacion == "crecimiento":
                active_tab = "kleene"
                L1 = datos["L1"].split(",")

                salida = []
                for i in range(1, 6):
                    r = logica.kleeneStar(L1, i)
                    salida.append(f"Iteracion {i}: {len(r)}")

                resultado = "\n".join(salida)

        except Exception as e:
            resultado = f"Error: {str(e)}"

    return render_template(
        "index.html",
        resultado=resultado,
        active_tab=active_tab,
        datos=datos
    )


if __name__ == "__main__":
    app.run(debug=True)