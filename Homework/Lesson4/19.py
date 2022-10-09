# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите число k:"))

lists = []
for i in range(k + 1):
    lists.append(random.randint(0, 100))
print(lists)
text = ''
for j in range(k + 1):
    if j < k:
        text = text + f'{lists[j]}x^{k-j} + '
    else:
        text = text + f'{lists[j]}x^{k-j} = 0'

with open('file4.txt', 'w') as data:
    data.write(text)
