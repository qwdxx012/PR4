# Задание 2. Вариант 8.
import math

x = float(input("Введите x (от -1 до 1): "))
e = float(input("Введите погрешность e: "))

while abs(x) > 1:
    x = float(input("Ряд расходится при |x| > 1, введите x снова: "))

s = 0
n = 0
term = x
while abs(term) >= e:
    s = s + term
    n = n + 1
    term = (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)

print("Сумма ряда:", s)
print("math.atan(x):", math.atan(x))
print("Разница:", abs(s - math.atan(x)))
print("Число слагаемых n:", n)
