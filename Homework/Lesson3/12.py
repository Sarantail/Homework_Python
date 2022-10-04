# # Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

# new_list = [2, 3, 4, 5, 6]
import random
new = int(input("Введите длину списка: "))
new_list = []
for i in range(new):
    new_n = random.randrange(0, 10)
    new_list.append(new_n)
print(new_list)

result = (len(new_list)+1)//2
result_list = []
for i in range(result):
    result_list.append(new_list[i]*new_list[len(new_list)-1-i])
print(result_list)
