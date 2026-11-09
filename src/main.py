import matplotlib.pyplot as plt
from funcoes import func_poli, bubble_sort, tempo
import numpy as np
import random 
import math

time_matrix = []
median_array = []
x = []
for i in range(101):
    n = 10
    dict_xy = {}
    for _ in range(1,21):
        arr = list(range(n+1))
        random.shuffle(arr)

        time_exec = tempo(arr)

        dict_xy[n] = time_exec

        if n not in x:
            x.append(n)
        n += 20
    
    time_matrix.append(list(dict_xy.values()))

median_array = np.median(time_matrix,axis=0)

y = median_array

valores = func_poli(x,y)

x = np.array(x)
y = np.array(y)



x_fit = np.linspace(x.min(), x.max(), 200)
y_fit = valores[0] + valores[1] * x_fit + valores[2] * x_fit**2

y_func = [valores[0] + valores[1] * xi + valores[2] * xi**2 for xi in x]

erro = sum((math.pow(y_func[i] - y[i],2)) for i in range(len(y)))
print(f"Erro da função : {erro}")

plt.scatter(x, y, label="Medições (mediana)")
plt.plot(x_fit, y_fit, color="red", label="Ajuste quadrático")
plt.plot(x, y,'o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Análise")
plt.show()