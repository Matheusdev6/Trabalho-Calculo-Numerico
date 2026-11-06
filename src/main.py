import matplotlib.pyplot as plt
from funcoes import analise_quicksort,analise_bubble_sort
import numpy as np

analise = analise_bubble_sort()

coef = np.array(analise[0])
x = np.array(list(analise[1].keys()))
y = np.array(list(analise[1].values()))

# print(coef)
# print(x)
# print(y)
# Plot
plt.plot(x, y,'o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Análise")
plt.legend()
plt.grid(alpha=0.3)
plt.show()