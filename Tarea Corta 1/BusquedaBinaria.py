#E: Una lista de numeros y un objetivo de tipo entero
#S: -1 si no se encuentra o un elemento encontrado
#R: La lista debe de estar ordenada, el target debe de ser entero
def busquedaBinaria(lista, target):
    bot = 0
    top = len(lista) - 1
    while bot <= top:
        mid = (bot + top) // 2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            bot = mid + 1
        else:
            top = mid - 1
    return -1

#E: Una lista de numeros y un objetivo de tipo entero
#S: (-1, -1) si no se encuentra o un par de elementos (lista, pos)
#R: La lista debe de estar ordenada, el target debe de ser entero
def busquedaBinariaEnListaDeListas(lista, target):
    for i, lis in enumerate(lista):
        index = busquedaBinaria(lis, target)
        if index != -1:
            return i, index
    return -1, -1

#Lista de listas (ejemplo):
lista = [
            [1, 3, 5, 7, 8],     
            [10, 9, 8, 7],    
            [2, 4, 6, 8]     
        ]

target = 5
resultado = busquedaBinariaEnListaDeListas(lista, target)
if resultado != (-1, -1):
    print(f"Objetivo encontrado en la lista {resultado[0]} en la posición {resultado[1]}.")
else:
    print("Objetivo no encontrado.")
