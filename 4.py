'''
Декларативное программирование:
Задача 4: Поиск уникальных элементов в списке. 
Напишите программу, которая создает новый список, 
содержащий только уникальные элементы из исходного 
списка.


'''
arr = [5, 10, 15, 7, 3, 9, 4, 7, 10, 4, 99, 8, 3]
new_arr = list(set(arr))
print(new_arr)

