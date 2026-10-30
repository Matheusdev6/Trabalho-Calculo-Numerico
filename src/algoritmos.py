def bubble_sort(array : list):
    size = len(array)
    for i in range(size):
        for j in range(i):    
            if array[j] > array[i]:
                array[i],array[j] = array[j],array[i]


def partition(array : list, l : int, r : int):
    i = l - 1

    for j in range(l,r):
        if array[j] < array[r]:
            i += 1
            array[i] , array[j] = array[j] , array[i]

    array[i+1] , array[r] = array[r] , array[i+1]
    return i+1

def quicksort(array : list, left : int, right : int):
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, 0, pivot - 1)
        quicksort(array, pivot + 1, right)
