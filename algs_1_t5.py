"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв"""

print("Введите поочередно две латинские буквы в нижнем регистре")

letter1 = input()
letter2 = input()

num1 = ord(letter1)
num2 = ord(letter2)

serial1 = num1 - 96
serial2 = num2 - 96
count = abs(num1 - num2) - 1

print(f"Буквы {letter1} и {letter2} стоят на местах {serial1} и {serial2} в алфавите и между ними {count} букв(ы-а)")
