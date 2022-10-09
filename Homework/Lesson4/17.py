# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def find_numbers(n):
    i = 2
    number = []
    while i * i <= n:
        while n % i == 0:
            number.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        number.append(int(n))
    return number


num = int(input("Введите число:"))
print(find_numbers(num))
