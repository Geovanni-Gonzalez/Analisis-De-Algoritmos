from flask import Flask, render_template, request
import random
from AlgoritmoGenetico import *  # Asegúrate de que este archivo contenga las funciones necesarias

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mejor_solucion = []
    conjunto = []
    limite = 0
    
    if request.method == 'POST':
        try:
            limite = int(request.form['limite'])  # Obtener el límite
            conjunto = generar_conjunto(10, 1, 50)  # Generar un conjunto aleatorio
            mejor_solucion = genetica(10, 50, 0.1, limite, conjunto)  # Ejecutar el algoritmo genético
        except ValueError:
            return render_template('index.html', error="El límite debe ser un número entero.")
    
    return render_template('index.html', mejor_solucion=mejor_solucion, conjunto=conjunto, limite=limite)

if __name__ == '__main__':
    app.run(debug=True)