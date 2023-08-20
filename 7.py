'''
Декларативное программирование:
Задача 7: Поиск подстроки. Напишите программу, 
которая находит все вхождения заданной подстроки в 
строке с использованием встроенных функций.
'''
def found(str, podstr):
    count = str.count(podstr)
    return count


str = 'Hello world! Goodbye world!'
podstr = 'wor'
print(found(str, podstr))