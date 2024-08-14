#E: Una lista y un objetivo
#S: Un indice o -1
#R: La lista debe de tener algun elemento 
def busquedaLineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  
    return -1  

# Lista de ejemplo:
lista = [4, 2, 7, 1, 3]
objetivo = 7
resultado = busqueda_lineal(lista, objetivo)

if resultado != -1:
    print(f'Elemento encontrado en la posición {resultado}')
else:
    print('Elemento no encontrado')
