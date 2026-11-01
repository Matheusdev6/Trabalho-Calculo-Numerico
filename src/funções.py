import time
from algoritmos import bubble_sort, quicksort, linear_search, binary_search
def func_log(valores : dict, func : str):
    pass

def func_polinomial(valores : dict, func : str):
    pass

def tempo(arr : list, func : str, target=None):
    if target is None:
        inicio = time.perf_counter()
        func(arr,0,len(arr)-1)
        fim = time.perf_counter()
        return fim - inicio,None
    else:
        inicio = time.perf_counter()
        index = func(arr,target)
        fim = time.perf_counter()
        return fim - inicio,index

