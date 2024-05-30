from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app= Flask(__name__)
# Paso 6: Crear conexión con la nueva base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

mysql = MySQL(app)


# Paso 7: Crear una Ruta Simple para probar la conexión a la base de datos
@app.route('/pruebaConexion')
def pruebaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("select 1")
        datos = cursor.fetchone()
        return jsonify({'status':'Conexion exitosa','data':datos})
    except Exception as ex:
        return jsonify({'status':'Error de Conexion','mensaje':str(ex)})

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