import random

# Función: ingresar_limite
# Esta función solicita al usuario que ingrese un valor límite 'L'.
# Este límite se utiliza para determinar la suma máxima permitida de los subconjuntos generados.
def ingresar_limite():
    L = int(input("Ingrese el valor límite L: "))
    return L

# Función: generar_conjunto
# Esta función genera un conjunto de números aleatorios dentro de un rango.
# Los valores por defecto son 10 números entre 1 y 50.
def generar_conjunto(n=10, min_val=1, max_val=50):
    # Usar un conjunto para garantizar que los números sean únicos
    conjunto = set()
    
    while len(conjunto) < n:
        numero = random.randint(min_val, max_val)
        conjunto.add(numero)  # Agrega el número al conjunto (solo se agregará si no está ya presente)

    return list(conjunto)  # Convertir de nuevo a lista para el resto del programa
# Función: calcular_aptitud (fitness)
# Esta función calcula la aptitud de un subconjunto basado en la suma de sus elementos.
# Si la suma es menor o igual al límite 'L', se retorna la suma como aptitud.
# Si la suma excede el límite, se retorna 0, indicando que la solución es inviable.
def calcular_aptitud(subconjunto, L, conjunto):
    suma = sum(conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1)
    return suma if suma <= L else 0

# Función: evaluar
# Esta función evalúa un subconjunto para determinar su aptitud.
# Retorna la suma de los elementos del subconjunto si no excede el límite 'L', de lo contrario retorna 0.
def evaluar(subconjunto, L, conjunto):
    suma = sum(conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1)
    return suma if suma <= L else 0

# Función: generar_poblacion
# Esta función crea una población inicial de subconjuntos aleatorios.
# Cada subconjunto está representado como una lista de 0's y 1's,
# donde 1 indica que el elemento correspondiente del conjunto original está presente en el subconjunto.
def generar_poblacion(tamano_poblacion, conjunto):
    return [[random.randint(0, 1) for _ in range(len(conjunto))] for _ in range(tamano_poblacion)]

# Función: cruzar
# Esta función realiza un cruce entre dos subconjuntos (padres).
# El cruce se lleva a cabo en un punto aleatorio, intercambiando partes de los padres para producir dos nuevos subconjuntos (hijos).
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)  # Seleccionar un punto de cruce aleatorio
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]  # Crear el primer hijo
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]  # Crear el segundo hijo
    return hijo1, hijo2

# Función: mutar
# Esta función muta un subconjunto, cambiando aleatoriamente algunos de sus genes de 0 a 1 o viceversa,
# según la tasa de mutación especificada. Esto introduce diversidad en la población.
def mutar(subconjunto, tasa_mutacion):
    for i in range(len(subconjunto)):
        if random.random() < tasa_mutacion:  # Verificar si se debe mutar el gen
            subconjunto[i] = 1 - subconjunto[i]  # Cambiar el valor del gen

# Función: genetica
# Esta función implementa el algoritmo genético:
# - Inicializa una población de subconjuntos aleatorios.
# - A lo largo de las generaciones, selecciona subconjuntos, realiza cruces y mutaciones,
#   y reemplaza la población con nuevas generaciones.
# - En cada generación, se busca el mejor subconjunto en función de la suma de sus elementos
#   sin exceder el límite 'L'.
def genetica(tamano_poblacion, num_generaciones, tasa_mutacion, L, conjunto):
    poblacion = generar_poblacion(tamano_poblacion, conjunto)  # Generar la población inicial
    mejor_subconjunto = max(poblacion, key=lambda x: evaluar(x, L, conjunto), default=None)

    for generacion in range(num_generaciones):
        nueva_poblacion = []  # Inicializar la nueva población

        # Crear nuevos hijos hasta alcanzar el tamaño de la población
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = max(random.sample(poblacion, 3), key=lambda x: evaluar(x, L, conjunto))  # Seleccionar el mejor padre
            padre2 = max(random.sample(poblacion, 3), key=lambda x: evaluar(x, L, conjunto))  # Seleccionar el segundo padre

            hijo1, hijo2 = cruzar(padre1, padre2)  # Realizar el cruce

            mutar(hijo1, tasa_mutacion)  # Mutar el primer hijo
            mutar(hijo2, tasa_mutacion)  # Mutar el segundo hijo

            nueva_poblacion.extend([hijo1, hijo2])  # Agregar los hijos a la nueva población

        poblacion = nueva_poblacion  # Actualizar la población

        mejor_subconjunto_generacion = max(poblacion, key=lambda x: evaluar(x, L, conjunto), default=None)  # Encontrar el mejor subconjunto de la nueva generación

        # Actualizar el mejor subconjunto si se encuentra uno mejor
        if mejor_subconjunto_generacion is not None and evaluar(mejor_subconjunto_generacion, L, conjunto) > evaluar(mejor_subconjunto, L, conjunto):
            mejor_subconjunto = mejor_subconjunto_generacion

        suma_mejor = evaluar(mejor_subconjunto, L, conjunto)
        print(f"Generación {generacion + 1}: Mejor suma = {suma_mejor} con subconjunto {mejor_subconjunto}")

    # Crear la solución final a partir del mejor subconjunto
    solucion_final = [conjunto[i] for i in range(len(conjunto)) if mejor_subconjunto[i] == 1]
    return solucion_final

# Ejemplo de uso
limite = ingresar_limite()  # Solicitar límite al usuario
conjunto = generar_conjunto()  # Generar un conjunto aleatorio
mejor_solucion = genetica(10, 50, 0.1, limite, conjunto)  # Ejecutar el algoritmo genético

# Imprimir resultados finales
print("Conjunto Generado:", conjunto)
print("Mejor Solución Encontrada:", mejor_solucion)
print("Suma de la Mejor Solución:", sum(mejor_solucion))
print("Límite:", limite)
