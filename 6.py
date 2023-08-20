'''
Задача 6: Упорядочивание списка. Напишите программу, 
которая сортирует список чисел в порядке возрастания 
с использованием пузырьковой сортировки или другого 
метода сортировки.

def buble_sort(arr):
    n = len(arr)


    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

myy_arr = [62, 25, 12, 22, 11]
sorted_arr = buble_sort(myy_arr)
print(sorted_arr)

'''

def bubl(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [5, 10, 15, 7, 3, 9, 4, 7, 10, 4, 99, 8, 3]
arr2 = bubl(arr)
print(arr)
