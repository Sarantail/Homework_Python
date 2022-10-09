# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

numbers = list(map(int, input("Введите числа через пробел:").split()))
new_numbers = []
[new_numbers.append(i) for i in numbers if i not in new_numbers]
print(new_numbers)
