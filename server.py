from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "llave super duper secreta" #establecemos una llave secreta para dar mas seguridad a los datos almacenados en sesión



#Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')


#Necesitamos una ruta que vincule con action
@app.route('/proceso', methods=['POST']) #la accion del formulario, aquí se proceso lo que recibimos
def proceso():
    print(request.form)

    #Guardamos en sesion
    session['nombre'] = request.form['nombre']
    session['apellido'] = request.form['apellido']
    session['email'] = request.form['email']
    
    return redirect('/exito') #la redireccion nos lleva a la nueva URL

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__== "__main__":
    app.run(debug=True)

