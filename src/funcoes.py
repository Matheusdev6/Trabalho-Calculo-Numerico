import time
import math
import numpy as np
from algoritmos import bubble_sort
import random


def func_poli(x : list, y : list):
    u_o = (np.array([1 for _ in range(len(x))]))
    u_1 = np.array(x)                # vetores para os produtos do sistema
    u_2 = np.array(x)
    u_2 = np.power(u_2,2)

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


def tempo(arr : list):
    inicio = time.perf_counter()
    bubble_sort(arr)                       # função para achar o tempo de execução do algoritmo.
    fim = time.perf_counter()
    return fim - inicio



