"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

START = 2
END1 = 9
END2 = 99

print(f'В диапазоне натуральных чисел от {START} до {END2}:')

for i in range(START, END1 + 1):
    sum_i = 0
    for num in range(START, END2 + 1):
        if num % i == 0:
            sum_i += 1
    print(f'{sum_i} чисел кратно {i}')
