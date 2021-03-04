"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

import random

SIZE = 100
MIN_ITEM = 98
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min1 = array[0]

for i in array:
    if i < min1:
        min1 = i

if array.index(min1) == 0:
    min2 = array[1]
else:
    min2 = array[0]

for i, num in enumerate(array):
    if i != array.index(min1):
        if num < min2:
            min2 = num

print(f'Два минимальных числа этого массива {min1} и {min2}.')
