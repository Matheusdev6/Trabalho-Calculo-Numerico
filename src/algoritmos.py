# Bubble Sort

def bubble_sort(array : list):
    size = len(array)
    for i in range(size):
        for j in range(i):    
            if array[j] > array[i]:
                array[i],array[j] = array[j],array[i]
