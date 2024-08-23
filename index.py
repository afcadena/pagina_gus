from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo="Internet de las Cosas")

@app.route('/iot')
def iot():
    return render_template('iot.html', titulo="¿Qué es el Internet de las Cosas?")

@app.route('/ventajas-desventajas')
def ventajas_desventajas():
    return render_template('ventajas_desventajas.html', titulo="Ventajas y Desventajas")

@app.route('/empresas')
def empresas():
    return render_template('empresas.html', titulo="Empresas vinculadas")

@app.route('/formulario', methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        return f"¡Gracias por registrarte, {nombre}! Te contactaremos en {correo}."
    return render_template('formulario.html', titulo="Formulario de inscripción")

if __name__ == '__main__':
    app.run(debug=True)
