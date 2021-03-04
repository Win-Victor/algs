"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

SIZE = 10
MIN_ITEM = 99
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num = array[0]
min_num = array[0]
pos_max = 0
pos_min = 0

for i, num in enumerate(array):
    if num > max_num:
        max_num = num
        pos_max = i
    elif num < min_num:
        min_num = num
        pos_min = i

sum_ = 0
for i, num in enumerate(array):
    if pos_min < pos_max:
        if i > pos_min and i < pos_max:
            sum_ += num
    else:
        if i < pos_min and i > pos_max:
            sum_ += num

# print(f'{min_num=}, {pos_min=}, {max_num=}, {pos_max=}')

print(f'\nМинимальное число в этом массиве: {min_num}, максимальное число: {max_num}.\n'
      f'Между ними в массиве чисел: {abs((pos_max - pos_min)) - 1},\n'
      f'сумма которых: {sum_}')
