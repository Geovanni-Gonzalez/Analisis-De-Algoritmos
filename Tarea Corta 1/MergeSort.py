import time
import random

# Función para ordenar una lista usando el algoritmo Merge Sort
def mergeSort(lista):
    if len(lista) > 1:
        # Calcular el punto medio de la lista
        medio = len(lista) // 2
        # Se divide la lista en dos mitades
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]
        # Se aplica recursivamente la función merge_sort a cada mitad
        mergeSort(mitad_izquierda)
        mergeSort(mitad_derecha)
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
"""
#Aplicar para diferentes casos de prueba

#Lista mejor caso
lista_mejor_caso = [i for i in range(10000)]

#Lista peor caso
lista_peor_caso = [i for i in range(10000, 0, -1)]

#Lista caso promedio
lista_caso_promedio = [random.randint(0, 1000) for _ in range(10000)]



#Tamaño de la lista
print(f"Tamaño de la lista (mejor caso): {len(lista_mejor_caso)}")

#Mejor caso
start_time = time.time()
mergeSort(lista_mejor_caso)
end_time = time.time()


print(f"Tiempo de ejecución (mejor caso): {end_time - start_time} segundos")


#Tamaño de la lista
print(f"Tamaño de la lista (peor caso): {len(lista_peor_caso)}")

#Peor caso
start_time = time.time()
mergeSort(lista_peor_caso)
end_time = time.time()


print(f"Tiempo de ejecución (peor caso): {end_time - start_time} segundos")


#Tamaño de la lista
print(f"Tamaño de la lista (caso promedio): {len(lista_caso_promedio)}")

#Caso promedio
start_time = time.time()
mergeSort(lista_caso_promedio)
end_time = time.time()

print(f"Tiempo de ejecución (caso promedio): {end_time - start_time} segundos")

"""