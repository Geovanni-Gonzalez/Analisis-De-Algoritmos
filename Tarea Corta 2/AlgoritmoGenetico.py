import random

# Funcion: ingresar_limite
# Esta función pide al usuario ingresar el valor límite 'L', que será el tope máximo
# para la suma de los subconjuntos generados.
def ingresar_limite():
    L = int(input("Ingrese el valor límite L: "))
    return L

# Funcion: generar_conjunto
# Esta función genera un conjunto de números aleatorios dentro de un rango.
# Los valores por defecto son 10 números entre 1 y 50.
def generar_conjunto(n=10, min_val=1, max_val=50):
    return [random.randint(min_val, max_val) for i in range(n)]

# Funcion: calcular_aptitud (fitness)
# Esta función calcula la aptitud de un subconjunto basado en la suma de sus elementos.
# Si la suma es menor o igual al límite 'L', la aptitud será la suma.
# Si la suma excede el límite, se retorna 0 para una mal aptitud.
def calcular_aptitud(subconjunto, L, conjunto):
    suma = sum([conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1])
    return suma if suma <= L else 0

# Funcion: evaluar
# Similar a la función de calcular aptitud, pero enfocada en validar si la suma del
# subconjunto excede 'L'. Si lo excede, se retorna 0, de lo contrario se retorna la suma.
def evaluar(subconjunto):
    suma = sum([conjunto[i] for i in range(len(conjunto)) if subconjunto[i] == 1])
    if suma > L:
        return 0  
    return suma

# Funcion: generar_poblacion
# Genera una población inicial de subconjuntos aleatorios. Cada subconjunto
# está representado como una lista de 0's y 1's, donde 1 indica que el elemento correspondiente
# del conjunto original está presente en el subconjunto, y 0 indica que no lo está.
# 1's posibles respuestas 0's poblacion descartada
def generar_poblacion(tamano_poblacion):
    return [[random.randint(0, 1) for i in range(len(conjunto))] for i in range(tamano_poblacion)]

# Funcion: cruzar
# Realiza un cruce entre dos subconjuntos (padres). El cruce intercambia parte de los genes
# (bits) de los padres para producir dos nuevos subconjuntos (hijos).
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(conjunto) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Funcion: mutar
# Función que muta un subconjunto cambiando aleatoriamente algunos de sus genes de 0 a 1 o viceversa,
# según la tasa de mutación dada. 
# Ayuda a introducir diversidad en la población.
def mutar(subconjunto, tasa_mutacion):
    for i in range(len(subconjunto)):
        if random.random() < tasa_mutacion:
            subconjunto[i] = 1 - subconjunto[i]  

# Funcion: genetica
# Esta función implementa el proceso del algoritmo genético:
# - Inicializa una población de subconjuntos aleatorios.
# - A lo largo de las generaciones, selecciona subconjuntos, realiza cruces y mutaciones,
#   y reemplaza la población con nuevas generaciones.
# - En cada generación, se busca el mejor subconjunto en funcion de la suma de sus elementos
#   sin exceder el límite 'L'.
# Nota: La funcion max(), sirve para encontrar el valor maximo de una secuencia 
# en este caso en la poblacion.
def genetica(tamano_poblacion, num_generaciones, tasa_mutacion):
    poblacion = generar_poblacion(tamano_poblacion)
    mejor_subconjunto = max(poblacion, key=evaluar)  
    
    for generacion in range(num_generaciones):
        nueva_poblacion = []
        
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = max(random.sample(poblacion, 3), key=evaluar)
            padre2 = max(random.sample(poblacion, 3), key=evaluar)
            
            hijo1, hijo2 = cruzar(padre1, padre2)
            
            mutar(hijo1, tasa_mutacion)
            mutar(hijo2, tasa_mutacion)
            
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
        
        mejor_subconjunto_generacion = max(poblacion, key=evaluar)
        
        if evaluar(mejor_subconjunto_generacion) > evaluar(mejor_subconjunto):
            mejor_subconjunto = mejor_subconjunto_generacion
        
        print(f"Generación {generacion + 1}: Mejor suma = {evaluar(mejor_subconjunto)} con subconjunto {mejor_subconjunto}")
    
    solucion_final = [conjunto[i] for i in range(len(conjunto)) if mejor_subconjunto[i] == 1]
    return solucion_final

L = int(input("Ingrese el valor límite L: "))

conjunto = [random.randint(1, 50) for i in range(10)]
print(f"Conjunto generado: {conjunto}")

mejor_solucion = genetica(10, 50, 0.1)

print(f"La mejor solución es: {mejor_solucion}, con una suma de {sum(mejor_solucion)}")
