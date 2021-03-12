"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

"""E меня только сложение"""

from collections import deque

def add_hex(a, b):
    hex_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    a = deque(a)
    b = deque(b)
    c = deque()

    if len(a) < len(b):
        a, b = b, a
        b.appendleft('0' * (len(a) - len(b)))
#    print(a)
#    print(b)
    n2 = 0
    while len(a) > 0:
        n = hex_.index(a.pop()) + hex_.index(b.pop()) + n2
        if n > 15:
            n1 = n % 16
            n2 = n // 16
        else:
            n1 = n
            n2 = 0
        c.appendleft(hex_[n1])
    if len(a) == 0 and n2 > 0:
        c.appendleft(hex_[n2])

    return c


print(add_hex("A2", "C4F"))
