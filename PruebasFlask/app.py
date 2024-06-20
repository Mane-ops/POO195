from flask import Flask,request,render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectomateria'

app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/consulta')
def consulta():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('select * from tbmedicos')
        consultaM= cursor.fetchall()
        return render_template('consultaMedicos.html', medicos = consultaM)
    except Exception as e:
        print(e)
    

@app.route('/registro')
def registro():
    return render_template('formularioMedicos.html')

@app.route('/guardarMedico',methods=['POST'])
def medico():
    if request.method == 'POST':
        # Tomamos los datos que vienen por POST
        Frfc = request.form['txtRFC']
        Fnombre = request.form['txtNombre']
        Fapp = request.form['txtApp']
        Fapm = request.form['txtApm']
        Fcedula = request.form['txtCedula']
        Fcorreo = request.form['txtCorreo']
        Fcontra = request.form['txtContra']
        Frol = request.form['txtRol']
        
        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute('insert into tbmedicos(rfc,nombre,app,apm,cedula,correo,password,rol) values(%s,%s,%s,%s,%s,%s,%s,%s)',(Frfc,Fnombre,Fapp,Fapm,Fcedula,Fcorreo,Fcontra,Frol))
        mysql.connection.commit()
        
        flash('Medico registrado correctamente')
        return redirect(url_for('consulta'))

# Manejo de excepciones para rutas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000,debug=True)