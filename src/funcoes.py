import time
import math
import numpy as np
from algoritmos import bubble_sort, quicksort, linear_search, binary_search
import random
def func_log(valores : dict):
    u_1 = np.array(list(valores.keys())) # conjunto dos x
    w = np.array(list(valores.values())) # conjunto dos y
    u_o = np.array([1 for _ in range(len(w))]) # conjunto neutro

    # montando a matriz do sistema linear, cada bloco do tipo v1 @ v2 é o produto escalar,
    # ou seja, a soma da multiplicação das respectivas posições nos vetores/arrays.

    mat = np.array([[u_o @ u_o, u_o @ u_1, u_o @ w],
                    [u_1 @ u_o, u_1 @ u_1, u_1 @ w]])

    mat[1] = mat[1] - ((mat[1][0]/mat[0][0])*mat[0])
    mat[1] *= (1/mat[1][1])

    mat[0] -= mat[1]*(mat[0][1]/mat[1][1])
    mat[0] *= (1/mat[0][0])

    return [mat[0][2],mat[1][2]]

def func_poli(valores : dict):
    u_o = (np.array([1 for _ in range(len(valores))]))
    u_1 = np.array(list(valores.keys()))                # vetores para os produtos do sistema
    u_2 = np.array(list(valores.keys()))
    u_2 = np.power(u_2,2)
    y = np.array(list(valores.values()))

    u_o.astype(float)
    u_1.astype(float)       # conversão para float para evitar problemas de contass
    u_2.astype(float)
    y.astype(float)

    mat = np.array(
        [[u_o@u_o, u_o@u_1, u_o@u_2, u_o@y],
         [u_1@u_o, u_1@u_1, u_1@u_2, u_1@y],            # sistema montado
         [u_2@u_o, u_2@u_1, u_2@u_2, u_2@y]]
    )
    
    mat[1] -= (mat[1][0] / mat[0][0]) * mat[0]
    mat[2] -= (mat[2][0] / mat[0][0]) * mat[0]

    mat[2] -= (mat[2][1] / mat[1][1]) * mat[1]

    mat[2] /= mat[2][2]
    mat[1] -= mat[1][2] * mat[2]                                 # resolução do sistema
    mat[1] /= mat[1][1]

    mat[0] /= mat[0][0]
    mat[0] -= mat[0][2] * mat[2]
    mat[0] -= mat[0][1] * mat[1]

    return [mat[0][3],mat[1][3],mat[2][3]]


def tempo(arr : list, func : str, target=None):
    if target is None and func == quicksort:
        inicio = time.perf_counter()
        func(arr,0,len(arr)-1)
        fim = time.perf_counter()
        return fim - inicio,None
    elif target is None and func == bubble_sort:
        inicio = time.perf_counter()                        # função para achar o tempo de execução do algoritmo.
        index = func(arr)
        fim = time.perf_counter()
        return fim - inicio, None
    else:
        inicio = time.perf_counter()
        index = func(arr,target)
        fim = time.perf_counter()
        return fim - inicio,index

def analise_quicksort():
    q = 100
    x = []
    dict_xy = {}
    for _ in range(1,9):

        arr = list(range(q+1))
        random.shuffle(arr)

        time , _ = tempo(arr,quicksort)

        x.append(q)

        dict_xy[q] = time
        q *= 2

    return func_log(dict_xy), dict_xy

def analise_bubble_sort():
    n = 10

    for _ in range(1,21):
        x =[]
        dict_xy = {}
        arr = list(range(n+1))
        random.shuffle(arr)

        time , _ = tempo(arr,bubble_sort)

        x.append(n)

        dict_xy[n] = time
        n += 20


    return func_poli(dict_xy), dict_xy


# ver o que cada função precisa/deve retornar