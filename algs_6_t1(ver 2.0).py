"""
6. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти."""

"""
Python 3.9.0 [MSC v.1927 64 bit (AMD64)] on win32
Для работы я выбрал то же задание, что и для задания 4.1.
Для работы я выбрал то же задание, что и для задания 4.1.
Попробовал с другими задачами - вышло неинтересно.
1. Я добился правильного вычисления, которое было необходимо для задачи 4.1. И это я считаю большим достижением.
Я прошлых результатах при изменении n различия в скорости алгоритмов не находились.
Картина была смазана необходимостью в каждом алгоритме рассчитывать массив. После того как я убрал эти расчёты из 
тела алгоритма - увидел существенные различия в скорости работы алгоритмов.
Теперь мне понятно замечание относительно моего кода в задании 3.3.
График прилагаю: https://drive.google.com/file/d/1o-MgLMe0_U0VUBn_Y4Odoyos3mUUmOXX/view?usp=sharing
"""

import random, timeit, sys

def my_old_min_max(n):
    """ Первый код для обработки"""
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

    return f'\n{array}'




def my_new_min_max(n):
    """Вторй код для обработки"""
    max_num, poz_max = array[0], 0
    min_num, poz_min = array[0], 0
    for i, num in enumerate(array):
        if num > max_num:
            max_num = num
            poz_max = i
            continue
        elif num < min_num:
            min_num = num
            poz_min = i

    array[poz_min], array[poz_max] = array[poz_max], array[poz_min]
    return array


def prep_1(n):
    """Третий код ля обработки"""
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            ind_min = i
        elif array[i] > array[idx_max]:
            idx_max = i
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array


def prep_2(n):
    """Четвертый код для обработки"""
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array

"""Код для проверки времени исполнения алгоритма"""

n = 100
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 500
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 1000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 5000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 10000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 50000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 100000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 500_000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 1_000_000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

n = 5_000_000
SIZE = n
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))

"""
n = 100
old 0.0030740999999999963
new 0.0016342000000000023
prep_1 0.0007271999999999973
prep_2 0.0004335999999999923
n = 500
old 0.012337199999999993
new 0.0054327000000000125
prep_1 0.007823899999999995
prep_2 0.0033762999999999987
n = 1000
old 0.022265999999999994
new 0.011747800000000003
prep_1 0.009593600000000008
prep_2 0.0033581000000000027
n = 5000
old 0.11690290000000003
new 0.0497552
prep_1 0.04954209999999998
prep_2 0.013324000000000003
n = 10_000
old 0.18018630000000002
new 0.08583890000000005
prep_1 0.09137299999999993
prep_2 0.024480500000000016
n = 50_000
old 1.0294831000000002
new 0.45880450000000006
prep_1 0.46748350000000016
prep_2 0.13061849999999975
n = 100_000
old 1.9468781999999996
new 0.8165092000000005
prep_1 0.9023298999999998
prep_2 0.2712559999999993
n = 500_000
old 9.747652000000002
new 4.311693099999999
prep_1 4.776233300000001
prep_2 1.3283598000000012
n = 1_000_000
old 19.488132900000004
new 8.331525
prep_1 9.430640799999999
prep_2 2.6482988000000063
n = 5_000_000
old 97.1481927
new 42.38230530000001
prep_1 48.11242580000001
prep_2 13.385791799999993
"""

"""
Функция для оценки памяти, выделенной под переменные.
Доделал функцию с урока, чтоб обрабатывала функции.
"""

def sum_show(obj):
    sum_ = 0
    def show(obj):
        print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
        size_obj = sys.getsizeof(obj)
        nonlocal sum_
        sum_ += size_obj
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    show(key)
                    show(value)

            elif not isinstance(obj, str):
                for item in obj:
                    show(item)
    show(obj)
    return f'{sum_= }'

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'{"*" * 50} \nsum_show(my_old_min_max(100))')
print(sum_show(my_old_min_max(100)))
print(f'{"*" * 50} \nsum_show(my_new_min_max(100))')
print(sum_show(my_new_min_max(100)))
print(f'{"*" * 50} \nsum_show(prep_1(100))')
print(sum_show(prep_1(100)))
print(f'{"*" * 50} \nsum_show(prep_2(100))')
print(sum_show(prep_2(100)))

"""
************************************************** 
sum_show(my_old_min_max(100))
type(obj)=<class 'str'>, sys.getsizeof(obj)=73, obj='\n[677, 305, 84, 84, 698]'
sum_= 73
************************************************** 
sum_show(my_new_min_max(100))
type(obj)=<class 'list'>, sys.getsizeof(obj)=120, obj=[677, 305, 698, 84, 84]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=677
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=305
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=698
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
sum_= 260
************************************************** 
sum_show(prep_1(100))
type(obj)=<class 'list'>, sys.getsizeof(obj)=120, obj=[698, 305, 677, 84, 84]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=698
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=305
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=677
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
sum_= 260
************************************************** 
sum_show(prep_2(100))
type(obj)=<class 'list'>, sys.getsizeof(obj)=120, obj=[84, 305, 677, 698, 84]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=305
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=677
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=698
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=84
sum_= 260
"""
"""
Мне кажется отрабатывает как-то неправильно.
В 3 из алгоритмов одинаковые суммарные значения, в 1-м, где я ожидал самые "плохие" значения они минимальные.
Похоже на то, что функция показывает память, выделенную под массив, а он во всех 4 случаях одинаковый,
но не показывает выделенную память под работу функции.
Думаю функция требует доработки.
"""
