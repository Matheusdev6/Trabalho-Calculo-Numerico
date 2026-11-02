import matplotlib.pyplot as plt
import numpy as np
from funcoes import tempo
from algoritmos import quicksort, binary_search
import random


x = []
y = []

n = 10

for _ in range(1,7):

    print(n)

    arr = list(range(1,n+1))

    print("criou")

    target = arr[random.randint(1,n-1)]
    time , c = tempo(arr,binary_search,target)

    print(f"achou em {c} comparações")

    x.append(n)
    y.append(time)
    n *= 10



plt.plot(x,y,'o')

plt.xlabel("input (n)")
plt.ylabel("tempo")
plt.title("Gráfico")
plt.show()