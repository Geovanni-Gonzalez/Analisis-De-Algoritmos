from flask import Flask, render_template, request
import random
from AlgoritmoGenetico import *  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mejor_solucion = []
    conjunto = []
    limite = 0
    error = None
    
    if request.method == 'POST':
        try:
            # Obtener los valores ingresados por el usuario desde el formulario
            limite = int(request.form['limite'])
            tamano_poblacion = int(request.form['poblacion'])
            num_generaciones = int(request.form['generaciones'])

            # Generar el conjunto aleatorio
            conjunto = generar_conjunto(10, 1, 50)

            # Ejecutar el algoritmo genético con los valores del formulario
            mejor_solucion = genetica(tamano_poblacion, num_generaciones, 0.1, limite, conjunto)

        except ValueError:
            error = "Todos los campos deben contener valores numéricos enteros válidos."
    
    # Renderizar la plantilla con los resultados
    return render_template('index.html', mejor_solucion=mejor_solucion, conjunto=conjunto, limite=limite, error=error)

if __name__ == '__main__':
    app.run(debug=True)
