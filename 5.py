'''
Императивное программирование:
Задача 5: Поиск простых чисел. Напишите программу, 
которая находит все простые числа в заданном диапазоне 
от 1 до N.
'''
def search_prost(n):
    for i in range(n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)


n = int(input("Введите число: "))
search_prost(n)
