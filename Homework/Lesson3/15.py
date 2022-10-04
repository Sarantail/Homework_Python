# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))


def fibonacci(n):
    result = []
    num1, num2 = 1, 1
    for i in range(n-1):
        result.append(num1)
        num1, num2 = num2, num1 + num2
    num1, num2 = 0, 1
    for i in range(n):
        result.insert(0, num1)
        num1, num2 = num2, num1 - num2
    return result


print(fibonacci(n))
