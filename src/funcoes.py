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

    # perguntar para a prof sobre log n vs n*log n
    return mat

def func_poli(valores : dict, func : str):
    pass
def tempo(arr : list, func : str, target=None):
    if target is None and func == quicksort:
        inicio = time.perf_counter()
        func(arr,0,len(arr)-1)
        fim = time.perf_counter()
        return fim - inicio,None
    elif target is None and func == bubble_sort:
        inicio = time.perf_counter()
        index = func(arr)
        fim = time.perf_counter()
        return fim - inicio,index
    else:
        inicio = time.perf_counter()
        index = func(arr,target)
        fim = time.perf_counter()
        return fim - inicio,index

def analise_quicksort():
    q = 100
    x = []
    y =[]
    dict_xy = {}
    for _ in range(1,9):

        arr = list(range(q+1))
        random.shuffle(arr)

        time , c = tempo(arr,quicksort)

        x.append(q)
        y.append(time)

        dict_xy[q] = time
        q *= 2

    func_log(dict_xy) # verificar duvida com a professora
