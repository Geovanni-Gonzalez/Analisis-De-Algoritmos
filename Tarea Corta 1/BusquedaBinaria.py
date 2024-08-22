from BusquedaLineal import busquedaLineal
import time 
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
    [13, 19, 29, 42, 51, 67, 74, 88, 106, 115, 119, 135, 145, 156, 167, 183, 196, 201, 215, 227, 234, 249, 262, 278, 291, 307, 312, 325, 338, 344, 351, 369, 376, 388, 399, 401, 415, 429, 438, 448, 459, 471, 488, 497, 508, 512, 528, 534, 549, 560],
    [1076, 1091, 1102, 1120, 1137, 1150, 1169, 1182, 1204, 1215, 1233, 1250, 1264, 1277, 1285, 1300, 1314, 1328, 1345, 1360, 1374, 1393, 1406, 1417, 1436, 1449, 1460, 1484, 1492, 1505, 1516, 1530, 1542, 1553, 1564, 1582, 1595, 1612, 1624, 1638, 1650, 1662, 1675, 1694, 1705, 1724, 1737, 1746, 1763, 1778],
    [2089, 2103, 2120, 2135, 2149, 2163, 2174, 2189, 2202, 2220, 2236, 2250, 2264, 2278, 2291, 2303, 2315, 2330, 2345, 2357, 2374, 2385, 2398, 2412, 2424, 2436, 2448, 2461, 2476, 2492, 2504, 2518, 2532, 2546, 2559, 2571, 2583, 2597, 2611, 2624, 2636, 2650, 2664, 2677, 2689, 2703, 2715, 2732, 2745, 2759],
    [3087, 3105, 3116, 3134, 3146, 3162, 3177, 3194, 3209, 3222, 3240, 3253, 3271, 3284, 3301, 3315, 3330, 3348, 3360, 3374, 3390, 3411, 3427, 3442, 3457, 3475, 3490, 3504, 3519, 3536, 3552, 3568, 3583, 3599, 3610, 3627, 3643, 3657, 3675, 3689, 3703, 3718, 3733, 3750, 3766, 3780, 3796, 3810, 3825, 3842, 3843],
    [4092, 4106, 4123, 4137, 4150, 4163, 4175, 4191, 4204, 4221, 4237, 4248, 4262, 4275, 4290, 4310, 4326, 4340, 4355, 4370, 4383, 4397, 4413, 4427, 4444, 4458, 4473, 4486, 4503, 4517, 4530, 4547, 4559, 4574, 4589, 4602, 4618, 4633, 4647, 4662, 4675, 4691, 4705, 4720, 4733, 4748, 4763, 4780, 4793, 4809],
    [5113, 5126, 5141, 5157, 5170, 5183, 5195, 5210, 5226, 5239, 5253, 5267, 5281, 5297, 5310, 5322, 5339, 5353, 5367, 5381, 5394, 5407, 5421, 5437, 5450, 5466, 5481, 5494, 5510, 5525, 5540, 5553, 5567, 5581, 5595, 5610, 5623, 5636, 5650, 5665, 5678, 5692, 5707, 5722, 5734, 5749, 5763, 5777, 5792, 5806],
    [6118, 6132, 6145, 6162, 6174, 6187, 6204, 6218, 6233, 6245, 6259, 6276, 6289, 6305, 6320, 6335, 6349, 6362, 6377, 6390, 6406, 6418, 6432, 6447, 6462, 6476, 6490, 6507, 6520, 6534, 6548, 6560, 6577, 6590, 6604, 6621, 6634, 6648, 6661, 6675, 6690, 6703, 6717, 6733, 6745, 6760, 6775, 6789, 6803, 6818],
    [7110, 7126, 7139, 7154, 7169, 7185, 7199, 7212, 7230, 7244, 7258, 7274, 7288, 7303, 7316, 7330, 7346, 7360, 7373, 7390, 7404, 7419, 7433, 7449, 7461, 7475, 7490, 7505, 7518, 7532, 7548, 7560, 7575, 7590, 7603, 7620, 7634, 7649, 7663, 7676, 7691, 7706, 7719, 7732, 7747, 7762, 7775, 7790, 7803, 7818],
    [8120, 8135, 8150, 8164, 8180, 8193, 8209, 8222, 8237, 8253, 8268, 8282, 8296, 8310, 8325, 8339, 8355, 8368, 8383, 8399, 8413, 8428, 8441, 8456, 8472, 8486, 8499, 8514, 8530, 8543, 8557, 8572, 8588, 8602, 8615, 8630, 8646, 8660, 8674, 8688, 8703, 8716, 8732, 8746, 8760, 8775, 8789, 8804, 8818, 8832],
    [9144, 9159, 9174, 9188, 9202, 9218, 9232, 9246, 9262, 9276, 9289, 9305, 9319, 9333, 9348, 9364, 9378, 9393, 9408, 9421, 9437, 9451, 9464, 9478, 9493, 9507, 9522, 9537, 9549, 9563, 9578, 9592, 9606, 9622, 9636, 9650, 9664, 9678, 9692, 9706, 9722, 9736, 9750, 9765, 9778, 9793, 9808, 9822, 9836, 9850]
]

#Pruebas
#Hacer prueba para mejor caso, peor caso y caso promedio

#Mejor caso
target = 13
start_time = time.perf_counter()
resultado_lineal = busquedaLineal(lista, target)
end_time = time.perf_counter()
time_mejor_lineal = end_time - start_time

start_time = time.perf_counter()
resultado_binario = busquedaBinariaEnListaDeListas(lista, target)
end_time = time.perf_counter()
time_mejor_binario = end_time - start_time

#Peor caso

target = 9850
start_time = time.perf_counter()
resultado_lineal = busquedaLineal(lista, target)
end_time = time.perf_counter()
time_peor_lineal = end_time - start_time

start_time = time.perf_counter()
resultado_binario = busquedaBinariaEnListaDeListas(lista, target)
end_time = time.perf_counter()
time_peor_binario = end_time - start_time

#Caso promedio
target = 234
start_time = time.perf_counter()
resultado_lineal = busquedaLineal(lista, target)
end_time = time.perf_counter()
time_promedio_lineal = end_time - start_time

start_time = time.perf_counter()
resultado_binario = busquedaBinariaEnListaDeListas(lista, target)
end_time = time.perf_counter()
time_promedio_binario = end_time - start_time



print(f"{'Algoritmo':<20} {'Mejor caso':<20} {'Peor caso':<20} {'Caso promedio':<20}")
print(f"{'Búsqueda lineal':<20} {time_mejor_lineal:<20.6f} {time_peor_lineal:<20.6f} {time_promedio_lineal:<20.6f}")
print(f"{'Búsqueda binaria':<20} {time_mejor_binario:<20.6f} {time_peor_binario:<20.6f} {time_promedio_binario:<20.6f}")
