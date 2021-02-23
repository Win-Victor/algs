"""Определить, является ли год, который ввел пользователь, високосным или не високосным."""

print("Введите год для проверки на високосность")

my_year = int(input())

yes = "год - високосный"
no = "год - НЕ високосный"

if my_year % 400 == 0:
    print(f"{my_year} {yes}")
elif my_year % 100 == 0:
    print(f"{my_year} {no}")
elif my_year % 4 == 0:
    print(f"{my_year} {yes}")
else:
    print(f"{my_year} {no}")
