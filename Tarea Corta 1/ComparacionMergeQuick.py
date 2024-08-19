from MergeSort import mergeSort
from QuickSort import quickSort
import time
import random

# Función para comparar Merge Sort y Quick Sort
def comparar_eficiencia(tamanos):
    resultados = []
    
    for tamano in tamanos:
        # Generar una lista de números aleatorios de tamaño `tamano`
        lista = [random.randint(0, 10000) for _ in range(tamano)]
        
        # Copia de la lista para usarla en Quick Sort
        lista_copia = lista[:]
        
        # Medir tiempo de ejecución de Merge Sort
        inicio_merge = time.time()
        mergeSort(lista)
        fin_merge = time.time()
        
        # Medir tiempo de ejecución de Quick Sort
        inicio_quick = time.time()
        sorted_list = quickSort(lista_copia)
        fin_quick = time.time()
        
        # Almacenar resultados
        resultados.append({
            'tamaño': tamano,
            'merge_sort': fin_merge - inicio_merge,
            'quick_sort': fin_quick - inicio_quick
        })
    
    return resultados

# Definir los tamaños de lista que deseas probar
tamanos = [100, 1000, 5000, 10000, 20000]

# Realizar la comparación
resultados = comparar_eficiencia(tamanos)

# Mostrar resultados
print(f"{'Tamaño':<10}{'Merge Sort':<15}{'Quick Sort':<15}")
for resultado in resultados:
    print(f"{resultado['tamaño']:<10}{resultado['merge_sort']:<15.6f}{resultado['quick_sort']:<15.6f}")


