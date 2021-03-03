"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число."""

import random

print("Компьютером загадано число от 1 до 100. Постарайтесь угадать число за 10 попыток.")

num = round(random.random() * 100)
print(num)
user_num = None
try_count = 0
level = 10
while True:
    try_count += 1
    if try_count > level:
        print(f'Попытки закончились. Вы не угадали. Загаданное число - {num}')
        break
    user_num = int(input(f'\n{try_count}. Введите число, назовем его "x"\n\tx = '))
    if num == user_num:
        print(f'Вы угадали. Загаданное число: {num}')
        break
    elif user_num > num:
        print(f'Загаданное число меньше {user_num}')
        print(f'У Вас осталось {level - try_count} попыток')
        continue
    print(f'Загаданное число больше {user_num}')
    print(f'У Вас осталось {level - try_count} попыток')
    continue
