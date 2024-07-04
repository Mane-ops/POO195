from flask import Flask,request,render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('select * from albums')
        consultaA= cursor.fetchall()
        #print(consultaA)
        return render_template('index.html', albums = consultaA)
    except Exception as e:
        print(e)

@app.route('/guardarAlbum',methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        # Tomamos los datos que vienen por POST
        Ftitulo = request.form['txtTitulo']
        Fartista = request.form['txtArtista']
        Fanio = request.form['txtAnio']
        
        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)',(Ftitulo,Fartista,Fanio))
        mysql.connection.commit()
        
        flash('Album guardado correctamente')
        return redirect(url_for('index'))
    
@app.route('/editar/<id>')
def editar(id):
    cur= mysql.connection.cursor()
    cur.execute('select * from albums where idAlbum=%s ', [id])
    albumE= cur.fetchone()
    return render_template('editar.html', album= albumE)

@app.route('/editarAlbum/<id>',methods=['POST'])
def editarAlbum(id):
    if request.method == 'POST':
        # Tomamos los datos que vienen por POST
        Ftitulo = request.form['txtTitulo']
        Fartista = request.form['txtArtista']
        Fanio = request.form['txtAnio']
        
        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute('update albums set titulo= %s,artista= %s,anio= %s where idAlbum= %s',(Ftitulo,Fartista,Fanio,id))
        mysql.connection.commit()
        
        flash('Album editado correctamente')
        return redirect(url_for('index'))
    
@app.route('/eliminarAlbum/<id>')
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('delete from albums where idAlbum= %s',[id])
    mysql.connection.commit()
    return redirect(url_for('index'))

# Manejo de excepciones para rutas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000,debug=True)