"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

companies = Counter()

while True:
    try:
        register = int(input('Сколько компаний будем анализировать?\n'))
        count = 0
        all_income = 0
        break
    except Exception:
        print('Нужно ввести натуральное число')
        continue

while count < register:
    name = input(f'Введите название {count + 1} компании:\n')
    quarter = 1
    sum_income = 0
    count += 1
    while quarter <= 4:
        income = float(input(f'Введите доход {name} за {quarter} квартал:\n'))
        quarter += 1
        sum_income += income
    companies[name] = sum_income
    all_income += sum_income

average_income = all_income / register

print(f'Средний доход этих компаний составляет: {average_income}')

favorite_companies = []
soso_companies = []

for i in companies:
    if companies[i] > average_income:
        favorite_companies.append(i)
    else:
        soso_companies.append(i)

if len(companies) > 1:
    if len(favorite_companies) > 0 and len(soso_companies) > 0:
        print(f'Доходы выше среднего у компаний: ')
        for i in favorite_companies:
            print(i)
        print(f'Доход ниже среднего или равный среднему у компаний: ')
        for i in soso_companies:
            print(i)
    else:
        print('Доходы компаний равны')
else:
    print("Для сравнение нужно минимум 2 компании")
