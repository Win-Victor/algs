"""Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random
print("введите два числа или два символа для определения границ")

symbol1 = input()
symbol2 = input()

if symbol1.isdigit() and symbol2.isdigit():
    symbol1 = int(symbol1)
    symbol2 = int(symbol2)
    if symbol2 < symbol1:
        symbol1, symbol2 = symbol2, symbol1
    num1 = random.randrange(symbol1, symbol2 + 1)
    num2 = random.uniform(symbol1, symbol2)
    print(f"случайное целое число в определенных границах - {num1}")
    print(f"случайное вещественное число в определенных границах - {round(num2, 4)}")

else:
    position1 = ord(symbol1)
    position2 = ord(symbol2)
    if position2 < position1:
        position1, position2 = position2, position1
    new_num = random.randrange(position1, position2 + 1)
    new_symbol = chr(new_num)
    print(f"случайный символ в определенных границах - {new_symbol}")
