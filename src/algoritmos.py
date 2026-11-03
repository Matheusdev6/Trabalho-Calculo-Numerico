# Bubble Sort

def bubble_sort(array : list):
    size = len(array)
    for i in range(size):
        for j in range(i):    
            if array[j] > array[i]:
                array[i],array[j] = array[j],array[i]

# Quick Sort

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
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)

# Linear Search

def linear_search(array : list, target : int):
    for i in range(len(array)):
        if array[i] == target:
            return i

# Binary Search

def binary_search(array : list, target : int):
    c = 0
    l = 0
    r = len(array) - 1
    p = (l+r)//2
    while array[p] != target:
        c+=1
        if array[p] > target:
            r = p - 1
        else:
            l = p + 1
        p = (l + r) // 2

    return p,c
