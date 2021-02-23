"""
https://drive.google.com/file/d/1j1GBFNSav_8hWioQMwZaOFVWUR2-UDtI/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

print("Введите трехзначное число, от 100 до 999")

num = int(input())

a = num // 100
b = (num - a * 100) // 10
c = num % 10
my_sum = a + b + c
composition = a * b * c

print(f'{my_sum=}, {composition=}')
