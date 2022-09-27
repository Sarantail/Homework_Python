# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 4, 5, 6, 3]
print("Исходный список: " + str(list))
res = random.sample(list, len(list))
print("Перемешанный список: " + str(res))
