"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


def devilish(n):
    if n == 1:
        return n
    else:
        count = 1
        sum = 1
        num = 1
        while count < n:
            count += 1
            num = (num / 2) * -1
            sum += num
        return sum


print(devilish(1))
print(devilish(2))
print(devilish(3))
print(devilish(4))
print(devilish(5))
print(devilish(6))
print(devilish(7))
print(devilish(8))
print(devilish(9))
print(devilish(10))
print(devilish(11))
print(devilish(12))
print(devilish(13))
print(devilish(14))
print(devilish(15))
print(devilish(1000))
