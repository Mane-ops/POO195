from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return '<h1>HOME</h1>'

# Ruta para el formulario
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        return f'<h1>Formulario Enviado</h1><p>Nombre: {nombre}</p><p>Edad: {edad}</p>'
    return render_template('index.html')

# Ruta para calcular el cuadrado de un número
@app.route('/numeroalcuadrado/<int:num>')
def numero_al_cuadrado(num):
    return f'<h1>El cuadrado de {num} es {num**2}</h1>'

# Manejo de errores 404
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return '<h1>Ruta no encontrada. Por favor, verifica la URL.</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)