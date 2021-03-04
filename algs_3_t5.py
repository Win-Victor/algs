"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

minus_array = []

for i in array:
    if i < 0:
        minus_array.append(i)

max_minus = minus_array[0]

for i, num in enumerate(minus_array):
    if num > max_minus:
        max_minus = num

print(f'\nМаксимальный отрицательный элемент в массиве: {max_minus}, его пизиция в массиве: {array.index(max_minus)}.')
