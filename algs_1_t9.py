"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""


print("Введите три разных числа")

a = float(input())
b = float(input())
c = float(input())

if c > a and a > b or c < a and a < b:
    print(f'среднее число {a}')
else:
    if a > b and b > c or a < b and b < c:
        print(f'среднее число {b}')
    else:
        print(f'среднее число {c}')
