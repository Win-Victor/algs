"""4. Определить, какое число в массиве встречается чаще всего."""

import random

SIZE = 10
MIN_ITEM = -1
MAX_ITEM = 52
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 0
max_number = None
for i in range(MIN_ITEM, MAX_ITEM + 1):
    i_sum = array.count(i)
    if i_sum > max_count:
        max_count = i_sum
        max_number = i

if max_count == 1:
    print("Ни одно число не встречается в этом массиве более 1 раза")
else:
    print(f'Цифра {max_number} встечается в массиве чаще всего, а именно {max_count} раз(а)')
