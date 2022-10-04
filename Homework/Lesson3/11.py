# # Задайте список из нескольких чисел.
# # Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.

# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import random

list_len = int(input("Введите длину списка:"))
my_list = []
for i in range(0, list_len):
    my_list.append(int(random()*10-5))
print(my_list)
result = 0
for i in range(0, len(my_list)):
    if i % 2 == 0:
        i = i + 1
    else:
        result = result + my_list[i]
        i = i + 2
print(result)
