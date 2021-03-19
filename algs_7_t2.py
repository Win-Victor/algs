""" 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random, timeit

MIN_ITEM = 0
MAX_ITEM = 50 - 1
SIZE = 10

array = [round(random.random() * MAX_ITEM, 2) for i in range(SIZE)]
print(f'исходный массив:\n{array}\nсортированный массив:')


def merge_sort(arr):
    def merge(left_list, right_list):
        sorted_list = []
        left_list_ind = right_list_ind = 0
        left_list_len, right_list_len = len(left_list), len(right_list)

        for _ in range(left_list_len + right_list_len):
            if left_list_ind < left_list_len and right_list_ind < right_list_len:
                if left_list[left_list_ind] <= right_list[right_list_ind]:
                    sorted_list.append(left_list[left_list_ind])
                    left_list_ind += 1
                else:
                    sorted_list.append(right_list[right_list_ind])
                    right_list_ind += 1
            elif left_list_ind == left_list_len:
                sorted_list.append(right_list[right_list_ind])
                right_list_ind += 1
            elif right_list_ind == right_list_len:
                sorted_list.append(left_list[left_list_ind])
                left_list_ind += 1

        return sorted_list

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)


print(merge_sort(array))
