import time
import random

# Función para generar una lista aleatoria de tamaño n
def generar_lista_aleatoria(rango_min, rango_max):
    # Inicializa una lista vacía
    lista_aleatoria = []
    
    # Itera hasta que la lista tenga al menos tamaño_min elementos
    for i in range(random.randint(100,1000)):
        # Genera un número aleatorio dentro del rango especificado
        numero_aleatorio = random.randint(rango_min, rango_max)
        
        # Agrega el número generado a la lista
        lista_aleatoria.append(numero_aleatorio) 

    return lista_aleatoria



# Función para ordenar una lista usando el algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        # Calcular el punto medio de la lista
        medio = len(lista) // 2
        # Se divide la lista en dos mitades
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]
        # Se aplica recursivamente la función merge_sort a cada mitad
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)
        # Inicializar contadores para recorrer las dos mitades
        i = j = k = 0
        # Combinar las dos mitades en la lista original
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            # Comparar los elementos de las dos mitades
            if mitad_izquierda[i] < mitad_derecha[j]:
                # Si el elemento de la mitad izquierda es menor, se agrega a la lista
                lista[k] = mitad_izquierda[i]
                # Se incrementa el contador de la mitad izquierda
                i += 1
            else:
                # Si el elemento de la mitad derecha es menor, se agrega a la lista
                lista[k] = mitad_derecha[j]
                # Se incrementa el contador de la mitad derecha
                j += 1
            # Se incrementa el contador de la lista original
            k += 1
        # Comprobar si quedan elementos en alguna de las dos mitades
        while i < len(mitad_izquierda):
            # Agregar los elementos restantes de la mitad izquierda a la lista
            lista[k] = mitad_izquierda[i]
            # Incrementar los contadores
            i += 1
            k += 1
        # Comprobar si quedan elementos en la mitad derecha
        while j < len(mitad_derecha):
            # Agregar los elementos restantes de la mitad derecha a la lista
            lista[k] = mitad_derecha[j]
            # Incrementar los contadores
            j += 1
            k += 1

#Generar lista aleatoria
lista = generar_lista_aleatoria(1, 1000)

#Tamaño de la lista
print(f"Tamaño de la lista: {len(lista)}")

#Medir tiempo de ejecución
inicio = time.time()
merge_sort(lista)
fin = time.time()
tiempo_total = fin - inicio

print(f"Tiempo de ejecución del Merge Sort: {tiempo_total} segundos")