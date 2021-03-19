"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

m = 5
MIN_ITEM = 1
MAX_ITEM = 500 - 1
SIZE = m * 2 + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array, ' - это начальный массив')
array_s = array
array_s.sort()
print(array_s, ' - он отсортирован для наглядности')


def median_odd_arr(arr, k=len(array) // 2):
    pivot = random.choice(arr)
    if len(arr) == 1:
        assert k == 0
        return arr[0]

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return median_odd_arr(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_odd_arr(highs, k - len(lows) - len(pivots))


print('Это медиана массива:', median_odd_arr(array))
