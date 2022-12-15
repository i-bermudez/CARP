import numpy as np #Vamos a utilizar la libreria numpy
import operator #Paquete para ordenar un diccionario
import time #Paquete para medir el tiempo computacional
import matplotlib.pyplot as plt
import networkx as nx
import sys 
from heapq import heapify, heappush, heappop

# with open("gdb2.dat",mode = "r") as instancias:
#     print(instancias.read())

# ========================================
# GDB 1
# ========================================

# vertices = 12
# aristas_req = 22
# aristas_noreq = 0
# vehiculos = 5
# capacidad = 5
# costo_total = 252
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,10):1,(1,12):1,
#             (2,1):1,(2,3):1,(2,4):1,(2,9):1,
#             (3,2):1,(3,4):1,(3,5):1,
#             (4,1):1,(4,2):1,(4,3):1,
#             (5,3):1,(5,6):1,(5,11):1,(5,12):1,
#             (6,5):1,(6,7):1,(6,12):1,
#             (7,1):1,(7,6):1,(7,8):1,(7,12):1,
#             (8,7):1,(8,10):1,(8,11):1,
#             (9,2):1,(9,10):1,(9,11):1,
#             (10,1):1,(10,8):1,(10,9):1,(10,11):1,
#             (11,5):1,(11,8):1,(11,9):1,(11,10):1,
#             (12,1):1,(12,5):1,(12,6):1,(12,7):1}

# vecinos = {1:{2:13,4:17,7:19,10:19,12:4},
#             2:{1:13,3:18,4:9,9:2},
#             3:{2:18,4:20,5:5},
#             4:{1:17,2:9,3:20},
#             5:{3:5,6:7,11:20,12:11},
#             6:{5:7,7:4,12:3},
#             7:{1:19,6:4,8:8,12:18},
#             8:{7:8,10:3,11:10},
#             9:{2:2,10:16,11:14},
#             10:{1:19,8:3,9:16,11:12},
#             11:{5:20,8:10,9:14,10:12},
#             12:{1:4,5:11,6:3,7:18}}

# ========================================
# GDB 2
# ========================================

# vertices = 12
# aristas_req = 26
# aristas_noreq = 0
# vehiculos = 6
# capacidad = 5
# costo_total = 291
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,9):1,(1,10):1,(1,12):1,
#             (2,1):1,(2,3):1,(2,4):1,(2,9):1,
#             (3,2):1,(3,4):1,(3,5):1,
#             (4,1):1,(4,2):1,(4,3):1,(4,12):1,
#             (5,3):1,(5,6):1,(5,11):1,(5,12):1,
#             (6,5):1,(6,7):1,(6,8):1,(6,12):1,
#             (7,1):1,(7,6):1,(7,8):1,(7,10):1,(7,12):1,
#             (8,6):1,(8,7):1,(8,10):1,(8,11):1,
#             (9,1):1,(9,2):1,(9,10):1,(9,11):1,
#             (10,1):1,(10,7):1,(10,8):1,(10,9):1,(10,11):1,
#             (11,5):1,(11,8):1,(11,9):1,(11,10):1,
#             (12,1):1,(12,4):1,(12,5):1,(12,6):1,(12,7):1,}

# vecinos = {1:{2:13,4:17,7:19,9:11,10:19,12:4},
#             2:{1:13,3:18,4:9,9:2},
#             3:{2:18,4:20,5:5},
#             4:{1:17,2:9,3:20,12:5},
#             5:{3:5,6:7,11:20,12:11},
#             6:{5:7,7:4,8:14,12:3},
#             7:{1:19,6:4,8:8,10:9,12:18},
#             8:{6:14,7:8,10:3,11:10},
#             9:{1:11,2:2,10:16,11:14},
#             10:{1:19,7:9,8:3,9:16,11:12},
#             11:{5:20,8:10,9:14,10:12},
#             12:{1:4,4:5,5:11,6:3,7:18}}

# ========================================
# GDB 3
# ========================================

# vertices = 12
# aristas_req = 22
# aristas_noreq = 0
# vehiculos = 5
# capacidad = 5
# costo_total = 233
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,9):1,(1,10):1,(1,12):1,
#             (2,1):1,(2,4):1,(2,9):1,
#             (3,4):1,(3,5):1,(3,12):1,
#             (4,1):1,(4,2):1,(4,3):1,
#             (5,3):1,(5,6):1,(5,11):1,(5,12):1,
#             (6,5):1,(6,7):1,(6,12):1,
#             (7,1):1,(7,6):1,(7,8):1,
#             (8,7):1,(8,10):1,(8,11):1,
#             (9,1):1,(9,2):1,(9,10):1,(9,11):1,
#             (10,1):1,(10,8):1,(10,9):1,(10,11):1,
#             (11,5):1,(11,8):1,(11,9):1,(11,10):1,
#             (12,1):1,(12,3):6,(12,5):1,(12,6):1}

# vecinos = {1:{2:13,4:17,7:19,9:11,10:19,12:4},
#             2:{1:13,4:9,9:2},
#             3:{4:20,5:5,12:6},
#             4:{1:17,2:9,3:20},
#             5:{3:5,6:7,11:20,12:11},
#             6:{5:7,7:4,12:3},
#             7:{1:19,6:4,8:8},
#             8:{7:8,10:3,11:10},
#             9:{1:11,2:2,10:16,11:14},
#             10:{1:19,8:3,9:16,11:12},
#             11:{5:20,8:10,9:14,10:12},
#             12:{1:4,3:6,5:11,6:3}}

# ========================================
# GDB 4
# ========================================

vertices = 11
aristas_req = 19
aristas_noreq = 0
vehiculos = 4
capacidad = 5
costo_total = 238
deposito = 1

demandas = {(1,2):1,(1,4):1,(1,6):1, (1,7):1,(1,10):1,
            (2,1):1,(2,3):1,(2,4):1,(2,9):1,
            (3,2):1,(3,4):1,(3,5):1,
            (4,1):1,(4,2):1,(4,3):1,
            (5,3):1,(5,6):1,(5,11):1,
            (6,1):1,(6,5):1,(6,7):1,
            (7,1):1,(7,6):1,(7,8):1,
            (8,7):1,(8,10):1,(8,11):1,
            (9,2):1,(9,10):1,(9,11):1,
            (10,1):1,(10,8):1,(10,9):1,(10,11):1,
            (11,5):1,(11,8):1,(11,9):1,(11,10):1}

vecinos = {1:{2:13,4:17,6:4,7:19,10:19},
            2:{1:13,3:18,4:9,9:2},
            3:{2:18,4:20,5:5},
            4:{1:17,2:9,3:20},
            5:{3:5,6:11,11:20},
            6:{1:4,5:11,7:18},
            7:{1:19,6:18,8:8},
            8:{7:8,10:3,11:10},
            9:{2:2,10:16,11:14},
            10:{1:19,8:3,9:16,11:12},
            11:{5:20,8:10,9:14,10:12}}

# ========================================
# GDB 5
# ========================================

# vertices = 13
# aristas_req = 26
# aristas_noreq = 0
# vehiculos = 6
# capacidad = 5
# costo_total = 316
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,10):1,(1,12):1,
#             (2,1):1,(2,3):1,(2,4):1,(2,9):1,
#             (3,2):1,(3,4):1,(3,5):1,(3,13):1,
#             (4,1):1,(4,2):1,(4,3):1,(4,13):1,
#             (5,3):1,(5,6):1,(5,11):1,(5,12):1,(5,13):1,
#             (6,5):1,(6,7):1,(6,12):1,
#             (7,1):1,(7,6):1,(7,8):1,(7,12):1,
#             (8,7):1,(8,10):1,(8,11):1,
#             (9,2):1,(9,10):1,(9,11):1,
#             (10,1):1,(10,8):1,(10,9):1,(10,11):1,
#             (11,5):1,(11,8):1,(11,9):1,(11,10):1,
#             (12,1):1,(12,5):1,(12,6):1,(12,7):1,(12,13):1,
#             (13,3):1,(13,5):1,(13,12):1}

# vecinos = {1:{2:13,4:17,7:19,10:19,12:4},
#             2:{1:13,3:18,4:9,9:2},
#             3:{2:18,4:20,5:5,13:22},
#             4:{1:17,2:9,3:20,13:6},
#             5:{3:5,6:7,11:20,12:11,13:17},
#             6:{5:7,7:4,12:3},
#             7:{1:19,6:4,8:8,12:18},
#             8:{7:8,10:3,11:10},
#             9:{2:2,10:16,11:14},
#             10:{1:19,8:3,9:16,11:12},
#             11:{5:20,8:10,9:14,10:12},
#             12:{1:4,5:11,6:3,7:18,13:19},
#             13:{3:22,4:6,5:17,12:19}}

# ========================================
# GDB 6
# ========================================

# vertices = 12
# aristas_req = 22
# aristas_noreq = 0
# vehiculos = 5
# capacidad = 5
# costo_total = 260
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,10):1,(1,12):1,
#             (2,1):1,(2,3):1,(2,4):1,(2,9):1,
#             (3,2):1,(3,4):1,(3,5):1,(3,11):1,
#             (4,1):1,(4,2):1,(4,3):1,(4,11):1,
#             (5,3):1,(5,6):1,(5,11):1,(5,12):1,
#             (6,5):1,(6,7):1,(6,12):1,
#             (7,1):1,(7,6):1,(7,8):1,(7,12):1,
#             (8,7):1,(8,10):1,
#             (9,2):1,(9,10):1,
#             (10,1):1,(10,8):1,(10,9):1,
#             (11,3):1,(11,4):1,(11,5):1,(11,12):1,
#             (12,1):1,(12,5):1,(12,6):1,(12,7):1,(12,11):1}

# vecinos = {1:{2:13,4:17,7:19,10:19,12:4},
#             2:{1:13,3:18,4:9,9:2},
#             3:{2:18,4:20,5:5,11:22},
#             4:{1:17,2:9,3:20,11:6},
#             5:{3:5,6:7,11:17,12:11},
#             6:{5:7,7:4,12:3},
#             7:{1:19,6:4,8:8,12:18},
#             8:{7:8,10:3},
#             9:{2:2,10:16},
#             10:{1:19,8:3,9:16},
#             11:{3:22,4:6,5:17,12:19},
#             12:{1:4,5:11,6:3,7:18,11:19}}

# ========================================
# GDB 7
# ========================================

# vertices = 12
# aristas_req = 22
# aristas_noreq = 0
# vehiculos = 5
# capacidad = 5
# costo_total = 262
# deposito = 1

# demandas = {(1,2):1,(1,4):1,(1,7):1,(1,10):1,(1,11):1,(1,12):1,
#             (2,1):1,(2,3):1,(2,4):1,(2,9):1,
#             (3,2):1,(3,4):1,(3,5):1,
#             (4,1):1,(4,2):1,(4,3):1,
#             (5,3):1,(5,11):1,(5,12):1,
#             (6,7):1,(6,11):1,
#             (7,1):1,(7,6):1,(7,8):1,(7,12):1,
#             (8,7):1,(8,10):1,(8,11):1,
#             (9,2):1,(9,10):1,(9,11):1,
#             (10,1):1,(10,8):1,(10,9):1,(10,11):1,
#             (11,1):1,(11,5):1,(11,6):1,(11,8):1,(11,9):1,(11,10):1,
#             (12,1):1,(12,5):1,(12,7):1}

# vecinos = {1:{2:13,4:17,7:19,10:19,11:17,12:4},
#             2:{1:13,3:18,4:9,9:2},
#             3:{2:18,4:20,5:5},
#             4:{1:17,2:9,3:20},
#             5:{3:5,11:20,12:11},
#             6:{7:4,11:3},
#             7:{1:19,6:4,8:8,12:18},
#             8:{7:8,10:3,11:10},
#             9:{2:2,10:16,11:14},
#             10:{1:19,8:3,9:16,11:12},
#             11:{1:17,5:20,6:3,8:10,9:14,10:12},
#             12:{1:4,5:11,7:18}}

# =================================
# DIJKSTRA
# =================================

def dijkstra (vecinos,origen,destino,opc):
    inf = sys.maxsize
    
    registro={1:{'costo':inf,'pred':[]},
              2:{'costo':inf,'pred':[]},
              3:{'costo':inf,'pred':[]},
              4:{'costo':inf,'pred':[]},
              5:{'costo':inf,'pred':[]},
              6:{'costo':inf,'pred':[]},
              7:{'costo':inf,'pred':[]},
              8:{'costo':inf,'pred':[]},
              9:{'costo':inf,'pred':[]},
              10:{'costo':inf,'pred':[]},
              11:{'costo':inf,'pred':[]},
              12:{'costo':inf,'pred':[]}}
    
    registro[origen]['costo']=0
    visitados=[]
    temp = origen
    for i in range(vertices-1):
        if temp not in visitados:
            visitados.append(temp)        
            for j in vecinos[temp]:
                if j not in visitados:
                    min_heap = []
                    costo = registro[temp]['costo']+vecinos[temp][j]
                    if costo < registro[j]['costo']:
                        registro[j]['costo'] = costo
                        registro[j]['pred'] = registro[temp]['pred'] + [temp]
                    heappush(min_heap, (registro[j]['costo'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    
    if opc == 1:
        return(registro[destino]['pred']+[destino])
    else:
        return(registro[destino]['costo'])

# =================================
# ALGORITMO DE RUTAS
# =================================

t_inicial = time.time()
rutas = 0
fo = 0
Sfin= []
requeridos = []

for d in demandas:
    valor = demandas[d]
    if valor > 0:
        requeridos = requeridos + [d]

while (rutas < vehiculos and len(requeridos)>0):
    Scur = []
    cap_rest = capacidad
    cabeza = deposito
    cabezaPasada = deposito
    
    while (cap_rest > 0):
        
        minimo = 99999
        requeridos = []
        for d in demandas:
            valor = demandas[d]
            if valor > 0:
                requeridos = requeridos + [d]
        
        if requeridos ==[]:
            break
                
        entro = False
        
        # Seleccionar el nodo más cercano (si es vecino)
        for i in requeridos:         
            if i[0] != cabeza and i[0] != cabezaPasada and (cabeza,i[0]) in requeridos:
                if vecinos[cabeza][i[0]] < minimo:
                    minimo = vecinos[cabeza][i[0]]
                    camino = [cabeza,i[0]]
                    siguiente = i[0]
                    entro = True
                    
        # Seleccionar el nodo más cercano (si NO es vecino)
        if entro == False:            
            for i in requeridos:
                if i[0] != cabeza and i[0] != cabezaPasada:
                    if dijkstra(vecinos,cabeza,i[0],2) < minimo:
                        minimo = dijkstra(vecinos,cabeza,i[0],2)
                        camino = dijkstra(vecinos,cabeza,i[0],1)
                        siguiente = i[0]
                        
        # Actualizar demandas y capacidad restante.
        for i in range(len(camino)-1):
            if cap_rest >= demandas[camino[i],camino[i+1]]:
                cap_rest = cap_rest - demandas[camino[i],camino[i+1]]
                demandas[camino[i],camino[i+1]]=0
                demandas[camino[i+1],camino[i]]=0
                
                
        fo += minimo
        cabezaPasada = camino[-2]
        #camino.pop(0)
        if entro == True:
            Scur = Scur + (camino)
            Scur.append("Recojer")
        else:
            Scur = Scur + (camino) 
            Scur.append("NO recojer")
        cabeza = siguiente
            
    
    dijks = dijkstra(vecinos, cabeza, deposito,1)
    fo += dijkstra(vecinos, cabeza, deposito,2)
    
    rutas += 1
    print("Ruta " + str(rutas) + ":")
    Scur = Scur + dijks 
    Scur.append("NO recoger")
    print(Scur)
    print('\n')

t_total = time.time()-t_inicial

print("Costo total: ",fo)
print("Tiempo CPU: ",t_total)






