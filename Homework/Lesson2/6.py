# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11



a = int(input("Введите число"))
result = 0
while a > 0:
    b = a % 10
    a = a / 10
    result = result + b
print(result)

# Console.WriteLine("Введите число")
# string? numberString = Console.ReadLine()
# var SumNum = int.Parse(numberString)

# int result = 0

# while (SumNum > 0)
# {
#     int num = SumNum % 10
#     SumNum = SumNum / 10
#     result = result + num
# }

# Console.WriteLine(result)
