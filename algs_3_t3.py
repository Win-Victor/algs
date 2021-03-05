"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

SIZE = 1_0
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num, poz_max = array[0], 0
min_num, poz_min = array[0], 0

for i, num in enumerate(array):
    if num > max_num:
        max_num = num
        poz_max = i
    elif num < min_num:
        min_num = num
        poz_min = i

array[poz_min], array[poz_max] = array[poz_max], array[poz_min]

print(f'\n{min_num = }, {max_num = }')

print(f'\n{array}')
