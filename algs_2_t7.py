"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число."""


def func(n):
    if n == 1:
        return n
    else:
        return n + func(n - 1)


def func2(n):
    equality = "1 + 2 + ... + n = n(n + 1) / 2"
    res1 = func(n)
    res2 = n * (n + 1) / 2
    if res1 == res2:
        return f'1 + 2 + ... + {n} = {res1}' \
               f'\n\n{n}({n} + 1) / 2 = {res2}' \
               f'\n\n{res1} == {res2} =>>>>>' \
               f'\n\nДоказано равенство: {equality} для n = {n}'
    else:
        return f'Опровергнуто равенство: {equality} для n = {n}' \
               f'\t\t{res1} < > {res2}' \
               f'n1 + 2 + ... + {n} = {n}({n} + 1) / 2'


n = int(input('Введите число n для проверки равенста\n\tn = '))
equ = (func2(n))

print(equ)
