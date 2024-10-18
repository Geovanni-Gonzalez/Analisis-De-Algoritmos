import random

# Función: ingresar_datos
# Esta función solicita al usuario que ingrese un valor límite 'L', el valor de la poblacion y el numero de gerneraciones.
# Este límite se utiliza para determinar la suma máxima permitida de los subconjuntos generados.
def ingresar_datos():
    L = int(input("Ingrese el valor límite L: "))
    tamano_poblacion = int(input("Ingrese el tamaño de la población: "))
    num_generaciones = int(input("Ingrese el número de generaciones: "))
    return L, tamano_poblacion, num_generaciones

# Función: generar_conjunto
# Esta función genera un conjunto de números aleatorios dentro de un rango.
# Los valores por defecto son 10 números entre 1 y 50. (tamaño ajustable)
def generar_conjunto(n=10, min_val=1, max_val=50):
    return [random.randint(min_val, max_val) for i in range(n)]

# Función: calcular_aptitud (fitness)
# Esta función calcula la aptitud de un subconjunto basado en la suma de sus elementos.
# Si la suma es menor o igual al límite 'L', se retorna la suma como aptitud.
# Si la suma excede el límite, se retorna 0, indicando que la solución es inviable.
def calcular_aptitud(subconjunto, L, conjunto):
    suma = sum([conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1])
    return suma if suma <= L else 0

# Función: evaluar
# Esta función evalúa un subconjunto para determinar su aptitud.
# Retorna la suma de los elementos del subconjunto si no excede el límite 'L', de lo contrario retorna 0.
def evaluar(subconjunto, L, conjunto):
    suma = sum([conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1])
    return suma if suma <= L else 0

# Función: generar_poblacion
# Esta función crea una población inicial de subconjuntos aleatorios.
# Cada subconjunto está representado como una lista de 0's y 1's,
# donde 1 indica que el elemento correspondiente del conjunto original está presente en el subconjunto.
def generar_poblacion(tamano_poblacion, conjunto):
    return [[random.randint(0, 1) for i in range(len(conjunto))] for i in range(tamano_poblacion)]

# Función: cruzar
# Esta función realiza un cruce entre dos subconjuntos (padres).
# El cruce se lleva a cabo en un punto aleatorio, intercambiando partes de los padres para producir dos nuevos subconjuntos (hijos).
def cruzar(padre1, padre2, conjunto):
    punto_cruce = random.randint(1, len(conjunto) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Función: mutar
# Esta función muta un subconjunto, cambiando aleatoriamente algunos de sus genes de 0 a 1 o viceversa,
# según la tasa de mutación especificada. Esto introduce diversidad en la población.
def mutar(subconjunto, tasa_mutacion):
    for i in range(len(subconjunto)):
        if random.random() < tasa_mutacion:
            subconjunto[i] = 1 - subconjunto[i]

# Función: genetica
# Esta función implementa el algoritmo genético:
# - Inicializa una población de subconjuntos aleatorios.
# - A lo largo de las generaciones, selecciona subconjuntos, realiza cruces y mutaciones,
#   y reemplaza la población con nuevas generaciones.
# - En cada generación, se busca el mejor subconjunto en función de la suma de sus elementos
#   sin exceder el límite 'L'.
def genetica(tamano_poblacion, num_generaciones, tasa_mutacion, L, conjunto):
    poblacion = generar_poblacion(tamano_poblacion, conjunto)
    mejor_subconjunto = max(poblacion, key=lambda sub: evaluar(sub, L, conjunto))
    
    for generacion in range(num_generaciones):
        nueva_poblacion = []
        
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = max(random.sample(poblacion, 3), key=lambda sub: evaluar(sub, L, conjunto))
            padre2 = max(random.sample(poblacion, 3), key=lambda sub: evaluar(sub, L, conjunto))
            
            # Cruce
            hijo1, hijo2 = cruzar(padre1, padre2, conjunto)
            
            # Mutación
            mutar(hijo1, tasa_mutacion)
            mutar(hijo2, tasa_mutacion)
            
            nueva_poblacion.append(hijo1)
            if len(nueva_poblacion) < tamano_poblacion:
                nueva_poblacion.append(hijo2)
        
        # Reemplazo de la población
        poblacion = nueva_poblacion[:tamano_poblacion]  # Asegurarse de no exceder el tamaño de la población
        
        mejor_subconjunto_generacion = max(poblacion, key=lambda sub: evaluar(sub, L, conjunto))
        
        # Actualización del mejor subconjunto si encontramos uno mejor
        if evaluar(mejor_subconjunto_generacion, L, conjunto) > evaluar(mejor_subconjunto, L, conjunto):
            mejor_subconjunto = mejor_subconjunto_generacion
        
        print(f"Generación {generacion + 1}: Mejor suma = {evaluar(mejor_subconjunto, L, conjunto)} con subconjunto {mejor_subconjunto}")
    
    # Retorna el subconjunto final con los elementos originales
    solucion_final = [conjunto[i] for i in range(len(conjunto)) if mejor_subconjunto[i] == 1]
    return solucion_final


# Entrada del usuario
L, tamano_poblacion, num_generaciones = ingresar_datos()

conjunto = generar_conjunto(n=tamano_poblacion)
print(f"Conjunto generado: {conjunto}")

# Ejecutar el algoritmo genético
mejor_solucion = genetica(tamano_poblacion, num_generaciones, 0.1, L, conjunto)

# Mostrar la solución final
print(f"La mejor solución es: {mejor_solucion}, con una suma de {sum(mejor_solucion)}")

#Autor: Daryll Martinez 
#Autor: Geovanni Gonzales

