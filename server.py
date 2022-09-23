from flask import Flask, render_template, request, redirect

app = Flask(__name__)


#Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')


#Necesitamos una ruta que vincule con action
@app.route('/proceso', methods=['POST']) #la accion del formulario, aquí se proceso lo que recibimos
def proceso():
    print(request.form)
    return redirect('/exito') #la redireccion nos lleva a la nueva URL

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__== "__main__":
    app.run(debug=True)

