import random
import time


def quickSort(lista):
    if len(lista) <= 1:
        return lista
    
    # Escoger el pivote (aquí, el pivote es el elemento central)
    pivot = lista[len(lista) // 2]
    
    # Dividir la lista en tres partes: menores, iguales y mayores al pivote
    izq = [x for x in lista if x < pivot]
    med = [x for x in lista if x == pivot]
    der = [x for x in lista if x > pivot]
    
    # Aplicar Quick Sort recursivamente y combinar las tres partes
    return quickSort(izq) + med + quickSort(der)




