'''
Задача 8: Вычисление суммы цифр числа. Напишите 
программу, которая вычисляет сумму всех цифр заданного 
числа, используя математические операции и деление 
нацело.
'''

def summ(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
    

n = int(input("Введите число: "))
k = summ(n)
print(k)