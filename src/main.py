import matplotlib.pyplot as plt
from funcoes import tempo
from algoritmos import quicksort, binary_search, bubble_sort
import random


x = []
y = []

dict_xy = {}

n = 10

# Binary Search
# for _ in range(1,7):

#     arr = list(range(1,n+1))

#     target = arr[random.randint(1,n-1)]
#     time , c = tempo(arr,binary_search,target)

#     x.append(n)
#     y.append(time)

#     dict_xy[n] = time
#     n *= 10

# Quick Sort
# q = 100
# for _ in range(1,9):

#     arr = list(range(q+1))
#     random.shuffle(arr)

#     target = arr[random.randint(1,q-1)]
#     time , c = tempo(arr,quicksort)

#     x.append(q)
#     y.append(time)

#     dict_xy[q] = time
#     q *= 2

# Bubble Sort
# for _ in range(1,20):

#     arr = list(range(n+1))
#     random.shuffle(arr)

#     target = arr[random.randint(1,n-1)]
#     time , c = tempo(arr,bubble_sort)

#     x.append(n)
#     y.append(time)

#     dict_xy[n] = time
#     n += 10

print(dict_xy)

plt.plot(x,y,'o')

plt.xlabel("input (n)")
plt.ylabel("tempo")
plt.title("Análise")
plt.show()