from flask import Flask, request

app= Flask(__name__)

# Paso 1: Crear una Ruta Simple
@app.route('/')
def principal():
    return 'Hola Mundo Flask!'

# Paso 2: Crear una Ruta Doble
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Mane Rosellón'

# Paso 3: Crear Rutas con Parámetros
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola '+ nombre + '!!!'

# Paso 4: Definición de métodos de trabajo
@app.route('/formulario',methods=['GET','POST'] )
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar passwords por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para passwords' 
    
# Paso 5: Manejo de excepciones para rutas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000, debug= True)