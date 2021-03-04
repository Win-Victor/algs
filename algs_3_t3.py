"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

SIZE = 1_0
MIN_ITEM = 0
MAX_ITEM = 1_0_0_0  # <- так тоже работает... o_O
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


max_num = array[0]
min_num = array[0]
for i, num in enumerate(array):
    if i > 0:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

poz_min = array.index(min_num)
poz_max = array.index(max_num)

array.pop(array.index(min_num))
array.pop(array.index(max_num))

array.insert(poz_min, max_num)
array.insert(poz_max, min_num)

print(f'\n{min_num = }, {max_num = }')

print(f'\n{array}')
