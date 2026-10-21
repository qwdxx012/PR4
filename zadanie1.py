# Задание 1. Вариант 8.
a = float(input("Введите число A: "))
n = int(input("Введите целое число N (> 0): "))

while n <= 0:
    n = int(input("N должно быть больше 0, введите снова: "))

result = 1
for i in range(n):
    result = result * a

print("A в степени N =", result)
