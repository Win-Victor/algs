"""
Запустил процесс. Процесс расчетов идет. Наблюдаю и пишу отчет параллельно.

В качестве объектов исследования выбрал:
Алгоритм решения задачи: «В массиве случайных целых чисел поменять местами минимальный и максимальный элементы».
(Задача №3 урока №3)
1. свой код к задаче №3 урока №3.
Этот код получил комментарии от преподавателя: «С точки зрения асимптотики - кошмар и ужас с 21 по 28 строки.
Урок 4 вам жизненно необходим.». Условно назовем этот образец – О(мно)-код.
Изначальный код переведен в функцию и из него удалены ненужные авторские комментарии (типа о_О).
2. код, который я переделал из О(мно)-кода после прочтения комментария преподавателя о нем.
3. и 4. предоставлены преподавателем в качестве решения вышеупомянутой задачи.
Проведя визуальную оценку экземпляра №1, можно увидеть наличие в коде повторяющихся действия, малообдуманных комбинаций,
которые делают код более громоздким, но при этом читаемость кода явно отличается наглядностью и выраженной
последовательностью.
При изучении экземпляра №2 наблюдается бОльшая лаконичность и отсутствие дублирующих расчетов.
Анализируя экземпляр № 2 и №3 можно увидеть их явное сходство. Несмотря на то, что экземпляр №2 был создан до просмотра
урока №4, где был представлен экземпляр по №3. Об этом факте свидетельствую изменения, внесенные в файл, размещенный
в репозиторий автора статьи (к уроку №3).
В анализе экземпляров №№ 3 и 4 отсутствует необходимость, т.к. они (экземпляры) очень подробно рассмотрены
преподавателем в начале 4-го урока.
В качестве переменной n, изменяющей объем выборки выбрана длина массива случайных чисел.
В качестве методов исследования были выбраны:
1. метод timeit модуля timeit,
2. run модуля сProfile.

Способ исследования:
1. Параллельное измерение времени 100-кратного исполнения кода 4 способами с последовательным
увеличением переменной n. Начальное n = 100. Конечное n = 100_000. Шаг увеличения n, s = 100.
2. Поочередное применение cProfile.run в отношение каждого алгоритма для оценки слабых сторон алгоритма.

Ожидаемый результат:
1. Обнаружить значимые различия во времени исполнения кода между (как минимум) 2 экземплярами кодов
при увеличении значений n.
2. Обнаружить увеличение времени исполнения кода какой-либо частью алгоритма.

Алгоритмы написаны:
1. стр. с 55 по 83,
2. с 86 по 105,
3. с 107 по 122,
4. 124 по 136.

Со 138 строки по 6134 – строки вызова расчетов timeit.timeit.
В строках с 6139 по 11139 показаны результаты этих расчетов.

В строках с 11142 по 11212 написаны вызовы расчетов cProfile.run и их результаты

Далее – выводы.
"""


import random
import timeit
import cProfile

def my_old_min_max(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array

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

    # print(f'\n{min_num = }, {max_num = }')

    return (f'\n{array}')


def my_new_min_max(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array

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
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array

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
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array

    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array

n = 100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(100)', number=100, globals=globals()))
n = 200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(200)', number=100, globals=globals()))
n = 300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(300)', number=100, globals=globals()))
n = 400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(400)', number=100, globals=globals()))
n = 500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(500)', number=100, globals=globals()))
n = 600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(600)', number=100, globals=globals()))
n = 700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(700)', number=100, globals=globals()))
n = 800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(800)', number=100, globals=globals()))
n = 900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(900)', number=100, globals=globals()))
n = 1000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1000)', number=100, globals=globals()))
n = 1100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1100)', number=100, globals=globals()))
n = 1200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1200)', number=100, globals=globals()))
n = 1300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1300)', number=100, globals=globals()))
n = 1400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1400)', number=100, globals=globals()))
n = 1500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1500)', number=100, globals=globals()))
n = 1600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1600)', number=100, globals=globals()))
n = 1700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1700)', number=100, globals=globals()))
n = 1800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1800)', number=100, globals=globals()))
n = 1900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(1900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(1900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(1900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(1900)', number=100, globals=globals()))
n = 2000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2000)', number=100, globals=globals()))
n = 2100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2100)', number=100, globals=globals()))
n = 2200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2200)', number=100, globals=globals()))
n = 2300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2300)', number=100, globals=globals()))
n = 2400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2400)', number=100, globals=globals()))
n = 2500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2500)', number=100, globals=globals()))
n = 2600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2600)', number=100, globals=globals()))
n = 2700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2700)', number=100, globals=globals()))
n = 2800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2800)', number=100, globals=globals()))
n = 2900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(2900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(2900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(2900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(2900)', number=100, globals=globals()))
n = 3000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3000)', number=100, globals=globals()))
n = 3100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3100)', number=100, globals=globals()))
n = 3200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3200)', number=100, globals=globals()))
n = 3300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3300)', number=100, globals=globals()))
n = 3400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3400)', number=100, globals=globals()))
n = 3500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3500)', number=100, globals=globals()))
n = 3600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3600)', number=100, globals=globals()))
n = 3700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3700)', number=100, globals=globals()))
n = 3800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3800)', number=100, globals=globals()))
n = 3900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(3900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(3900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(3900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(3900)', number=100, globals=globals()))
n = 4000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4000)', number=100, globals=globals()))
n = 4100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4100)', number=100, globals=globals()))
n = 4200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4200)', number=100, globals=globals()))
n = 4300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4300)', number=100, globals=globals()))
n = 4400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4400)', number=100, globals=globals()))
n = 4500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4500)', number=100, globals=globals()))
n = 4600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4600)', number=100, globals=globals()))
n = 4700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4700)', number=100, globals=globals()))
n = 4800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4800)', number=100, globals=globals()))
n = 4900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(4900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(4900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(4900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(4900)', number=100, globals=globals()))
n = 5000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5000)', number=100, globals=globals()))
n = 5100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5100)', number=100, globals=globals()))
n = 5200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5200)', number=100, globals=globals()))
n = 5300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5300)', number=100, globals=globals()))
n = 5400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5400)', number=100, globals=globals()))
n = 5500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5500)', number=100, globals=globals()))
n = 5600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5600)', number=100, globals=globals()))
n = 5700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5700)', number=100, globals=globals()))
n = 5800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5800)', number=100, globals=globals()))
n = 5900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(5900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(5900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(5900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(5900)', number=100, globals=globals()))
n = 6000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6000)', number=100, globals=globals()))
n = 6100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6100)', number=100, globals=globals()))
n = 6200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6200)', number=100, globals=globals()))
n = 6300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6300)', number=100, globals=globals()))
n = 6400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6400)', number=100, globals=globals()))
n = 6500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6500)', number=100, globals=globals()))
n = 6600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6600)', number=100, globals=globals()))
n = 6700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6700)', number=100, globals=globals()))
n = 6800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6800)', number=100, globals=globals()))
n = 6900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(6900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(6900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(6900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(6900)', number=100, globals=globals()))
n = 7000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7000)', number=100, globals=globals()))
n = 7100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7100)', number=100, globals=globals()))
n = 7200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7200)', number=100, globals=globals()))
n = 7300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7300)', number=100, globals=globals()))
n = 7400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7400)', number=100, globals=globals()))
n = 7500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7500)', number=100, globals=globals()))
n = 7600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7600)', number=100, globals=globals()))
n = 7700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7700)', number=100, globals=globals()))
n = 7800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7800)', number=100, globals=globals()))
n = 7900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(7900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(7900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(7900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(7900)', number=100, globals=globals()))
n = 8000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8000)', number=100, globals=globals()))
n = 8100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8100)', number=100, globals=globals()))
n = 8200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8200)', number=100, globals=globals()))
n = 8300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8300)', number=100, globals=globals()))
n = 8400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8400)', number=100, globals=globals()))
n = 8500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8500)', number=100, globals=globals()))
n = 8600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8600)', number=100, globals=globals()))
n = 8700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8700)', number=100, globals=globals()))
n = 8800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8800)', number=100, globals=globals()))
n = 8900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(8900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(8900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(8900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(8900)', number=100, globals=globals()))
n = 9000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9000)', number=100, globals=globals()))
n = 9100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9100)', number=100, globals=globals()))
n = 9200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9200)', number=100, globals=globals()))
n = 9300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9300)', number=100, globals=globals()))
n = 9400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9400)', number=100, globals=globals()))
n = 9500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9500)', number=100, globals=globals()))
n = 9600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9600)', number=100, globals=globals()))
n = 9700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9700)', number=100, globals=globals()))
n = 9800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9800)', number=100, globals=globals()))
n = 9900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(9900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(9900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(9900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(9900)', number=100, globals=globals()))
n = 10000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10000)', number=100, globals=globals()))
n = 10100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10100)', number=100, globals=globals()))
n = 10200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10200)', number=100, globals=globals()))
n = 10300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10300)', number=100, globals=globals()))
n = 10400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10400)', number=100, globals=globals()))
n = 10500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10500)', number=100, globals=globals()))
n = 10600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10600)', number=100, globals=globals()))
n = 10700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10700)', number=100, globals=globals()))
n = 10800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10800)', number=100, globals=globals()))
n = 10900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(10900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(10900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(10900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(10900)', number=100, globals=globals()))
n = 11000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11000)', number=100, globals=globals()))
n = 11100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11100)', number=100, globals=globals()))
n = 11200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11200)', number=100, globals=globals()))
n = 11300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11300)', number=100, globals=globals()))
n = 11400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11400)', number=100, globals=globals()))
n = 11500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11500)', number=100, globals=globals()))
n = 11600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11600)', number=100, globals=globals()))
n = 11700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11700)', number=100, globals=globals()))
n = 11800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11800)', number=100, globals=globals()))
n = 11900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(11900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(11900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(11900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(11900)', number=100, globals=globals()))
n = 12000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12000)', number=100, globals=globals()))
n = 12100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12100)', number=100, globals=globals()))
n = 12200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12200)', number=100, globals=globals()))
n = 12300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12300)', number=100, globals=globals()))
n = 12400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12400)', number=100, globals=globals()))
n = 12500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12500)', number=100, globals=globals()))
n = 12600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12600)', number=100, globals=globals()))
n = 12700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12700)', number=100, globals=globals()))
n = 12800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12800)', number=100, globals=globals()))
n = 12900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(12900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(12900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(12900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(12900)', number=100, globals=globals()))
n = 13000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13000)', number=100, globals=globals()))
n = 13100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13100)', number=100, globals=globals()))
n = 13200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13200)', number=100, globals=globals()))
n = 13300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13300)', number=100, globals=globals()))
n = 13400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13400)', number=100, globals=globals()))
n = 13500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13500)', number=100, globals=globals()))
n = 13600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13600)', number=100, globals=globals()))
n = 13700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13700)', number=100, globals=globals()))
n = 13800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13800)', number=100, globals=globals()))
n = 13900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(13900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(13900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(13900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(13900)', number=100, globals=globals()))
n = 14000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14000)', number=100, globals=globals()))
n = 14100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14100)', number=100, globals=globals()))
n = 14200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14200)', number=100, globals=globals()))
n = 14300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14300)', number=100, globals=globals()))
n = 14400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14400)', number=100, globals=globals()))
n = 14500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14500)', number=100, globals=globals()))
n = 14600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14600)', number=100, globals=globals()))
n = 14700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14700)', number=100, globals=globals()))
n = 14800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14800)', number=100, globals=globals()))
n = 14900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(14900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(14900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(14900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(14900)', number=100, globals=globals()))
n = 15000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15000)', number=100, globals=globals()))
n = 15100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15100)', number=100, globals=globals()))
n = 15200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15200)', number=100, globals=globals()))
n = 15300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15300)', number=100, globals=globals()))
n = 15400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15400)', number=100, globals=globals()))
n = 15500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15500)', number=100, globals=globals()))
n = 15600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15600)', number=100, globals=globals()))
n = 15700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15700)', number=100, globals=globals()))
n = 15800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15800)', number=100, globals=globals()))
n = 15900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(15900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(15900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(15900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(15900)', number=100, globals=globals()))
n = 16000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16000)', number=100, globals=globals()))
n = 16100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16100)', number=100, globals=globals()))
n = 16200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16200)', number=100, globals=globals()))
n = 16300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16300)', number=100, globals=globals()))
n = 16400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16400)', number=100, globals=globals()))
n = 16500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16500)', number=100, globals=globals()))
n = 16600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16600)', number=100, globals=globals()))
n = 16700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16700)', number=100, globals=globals()))
n = 16800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16800)', number=100, globals=globals()))
n = 16900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(16900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(16900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(16900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(16900)', number=100, globals=globals()))
n = 17000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17000)', number=100, globals=globals()))
n = 17100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17100)', number=100, globals=globals()))
n = 17200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17200)', number=100, globals=globals()))
n = 17300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17300)', number=100, globals=globals()))
n = 17400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17400)', number=100, globals=globals()))
n = 17500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17500)', number=100, globals=globals()))
n = 17600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17600)', number=100, globals=globals()))
n = 17700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17700)', number=100, globals=globals()))
n = 17800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17800)', number=100, globals=globals()))
n = 17900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(17900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(17900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(17900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(17900)', number=100, globals=globals()))
n = 18000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18000)', number=100, globals=globals()))
n = 18100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18100)', number=100, globals=globals()))
n = 18200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18200)', number=100, globals=globals()))
n = 18300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18300)', number=100, globals=globals()))
n = 18400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18400)', number=100, globals=globals()))
n = 18500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18500)', number=100, globals=globals()))
n = 18600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18600)', number=100, globals=globals()))
n = 18700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18700)', number=100, globals=globals()))
n = 18800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18800)', number=100, globals=globals()))
n = 18900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(18900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(18900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(18900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(18900)', number=100, globals=globals()))
n = 19000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19000)', number=100, globals=globals()))
n = 19100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19100)', number=100, globals=globals()))
n = 19200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19200)', number=100, globals=globals()))
n = 19300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19300)', number=100, globals=globals()))
n = 19400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19400)', number=100, globals=globals()))
n = 19500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19500)', number=100, globals=globals()))
n = 19600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19600)', number=100, globals=globals()))
n = 19700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19700)', number=100, globals=globals()))
n = 19800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19800)', number=100, globals=globals()))
n = 19900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(19900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(19900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(19900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(19900)', number=100, globals=globals()))
n = 20000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20000)', number=100, globals=globals()))
n = 20100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20100)', number=100, globals=globals()))
n = 20200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20200)', number=100, globals=globals()))
n = 20300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20300)', number=100, globals=globals()))
n = 20400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20400)', number=100, globals=globals()))
n = 20500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20500)', number=100, globals=globals()))
n = 20600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20600)', number=100, globals=globals()))
n = 20700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20700)', number=100, globals=globals()))
n = 20800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20800)', number=100, globals=globals()))
n = 20900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(20900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(20900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(20900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(20900)', number=100, globals=globals()))
n = 21000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21000)', number=100, globals=globals()))
n = 21100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21100)', number=100, globals=globals()))
n = 21200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21200)', number=100, globals=globals()))
n = 21300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21300)', number=100, globals=globals()))
n = 21400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21400)', number=100, globals=globals()))
n = 21500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21500)', number=100, globals=globals()))
n = 21600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21600)', number=100, globals=globals()))
n = 21700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21700)', number=100, globals=globals()))
n = 21800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21800)', number=100, globals=globals()))
n = 21900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(21900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(21900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(21900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(21900)', number=100, globals=globals()))
n = 22000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22000)', number=100, globals=globals()))
n = 22100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22100)', number=100, globals=globals()))
n = 22200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22200)', number=100, globals=globals()))
n = 22300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22300)', number=100, globals=globals()))
n = 22400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22400)', number=100, globals=globals()))
n = 22500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22500)', number=100, globals=globals()))
n = 22600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22600)', number=100, globals=globals()))
n = 22700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22700)', number=100, globals=globals()))
n = 22800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22800)', number=100, globals=globals()))
n = 22900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(22900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(22900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(22900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(22900)', number=100, globals=globals()))
n = 23000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23000)', number=100, globals=globals()))
n = 23100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23100)', number=100, globals=globals()))
n = 23200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23200)', number=100, globals=globals()))
n = 23300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23300)', number=100, globals=globals()))
n = 23400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23400)', number=100, globals=globals()))
n = 23500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23500)', number=100, globals=globals()))
n = 23600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23600)', number=100, globals=globals()))
n = 23700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23700)', number=100, globals=globals()))
n = 23800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23800)', number=100, globals=globals()))
n = 23900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(23900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(23900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(23900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(23900)', number=100, globals=globals()))
n = 24000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24000)', number=100, globals=globals()))
n = 24100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24100)', number=100, globals=globals()))
n = 24200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24200)', number=100, globals=globals()))
n = 24300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24300)', number=100, globals=globals()))
n = 24400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24400)', number=100, globals=globals()))
n = 24500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24500)', number=100, globals=globals()))
n = 24600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24600)', number=100, globals=globals()))
n = 24700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24700)', number=100, globals=globals()))
n = 24800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24800)', number=100, globals=globals()))
n = 24900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(24900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(24900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(24900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(24900)', number=100, globals=globals()))
n = 25000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25000)', number=100, globals=globals()))
n = 25100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25100)', number=100, globals=globals()))
n = 25200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25200)', number=100, globals=globals()))
n = 25300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25300)', number=100, globals=globals()))
n = 25400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25400)', number=100, globals=globals()))
n = 25500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25500)', number=100, globals=globals()))
n = 25600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25600)', number=100, globals=globals()))
n = 25700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25700)', number=100, globals=globals()))
n = 25800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25800)', number=100, globals=globals()))
n = 25900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(25900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(25900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(25900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(25900)', number=100, globals=globals()))
n = 26000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26000)', number=100, globals=globals()))
n = 26100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26100)', number=100, globals=globals()))
n = 26200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26200)', number=100, globals=globals()))
n = 26300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26300)', number=100, globals=globals()))
n = 26400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26400)', number=100, globals=globals()))
n = 26500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26500)', number=100, globals=globals()))
n = 26600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26600)', number=100, globals=globals()))
n = 26700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26700)', number=100, globals=globals()))
n = 26800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26800)', number=100, globals=globals()))
n = 26900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(26900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(26900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(26900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(26900)', number=100, globals=globals()))
n = 27000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27000)', number=100, globals=globals()))
n = 27100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27100)', number=100, globals=globals()))
n = 27200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27200)', number=100, globals=globals()))
n = 27300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27300)', number=100, globals=globals()))
n = 27400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27400)', number=100, globals=globals()))
n = 27500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27500)', number=100, globals=globals()))
n = 27600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27600)', number=100, globals=globals()))
n = 27700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27700)', number=100, globals=globals()))
n = 27800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27800)', number=100, globals=globals()))
n = 27900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(27900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(27900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(27900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(27900)', number=100, globals=globals()))
n = 28000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28000)', number=100, globals=globals()))
n = 28100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28100)', number=100, globals=globals()))
n = 28200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28200)', number=100, globals=globals()))
n = 28300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28300)', number=100, globals=globals()))
n = 28400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28400)', number=100, globals=globals()))
n = 28500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28500)', number=100, globals=globals()))
n = 28600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28600)', number=100, globals=globals()))
n = 28700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28700)', number=100, globals=globals()))
n = 28800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28800)', number=100, globals=globals()))
n = 28900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(28900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(28900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(28900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(28900)', number=100, globals=globals()))
n = 29000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29000)', number=100, globals=globals()))
n = 29100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29100)', number=100, globals=globals()))
n = 29200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29200)', number=100, globals=globals()))
n = 29300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29300)', number=100, globals=globals()))
n = 29400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29400)', number=100, globals=globals()))
n = 29500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29500)', number=100, globals=globals()))
n = 29600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29600)', number=100, globals=globals()))
n = 29700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29700)', number=100, globals=globals()))
n = 29800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29800)', number=100, globals=globals()))
n = 29900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(29900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(29900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(29900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(29900)', number=100, globals=globals()))
n = 30000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30000)', number=100, globals=globals()))
n = 30100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30100)', number=100, globals=globals()))
n = 30200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30200)', number=100, globals=globals()))
n = 30300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30300)', number=100, globals=globals()))
n = 30400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30400)', number=100, globals=globals()))
n = 30500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30500)', number=100, globals=globals()))
n = 30600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30600)', number=100, globals=globals()))
n = 30700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30700)', number=100, globals=globals()))
n = 30800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30800)', number=100, globals=globals()))
n = 30900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(30900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(30900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(30900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(30900)', number=100, globals=globals()))
n = 31000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31000)', number=100, globals=globals()))
n = 31100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31100)', number=100, globals=globals()))
n = 31200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31200)', number=100, globals=globals()))
n = 31300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31300)', number=100, globals=globals()))
n = 31400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31400)', number=100, globals=globals()))
n = 31500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31500)', number=100, globals=globals()))
n = 31600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31600)', number=100, globals=globals()))
n = 31700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31700)', number=100, globals=globals()))
n = 31800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31800)', number=100, globals=globals()))
n = 31900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(31900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(31900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(31900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(31900)', number=100, globals=globals()))
n = 32000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32000)', number=100, globals=globals()))
n = 32100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32100)', number=100, globals=globals()))
n = 32200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32200)', number=100, globals=globals()))
n = 32300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32300)', number=100, globals=globals()))
n = 32400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32400)', number=100, globals=globals()))
n = 32500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32500)', number=100, globals=globals()))
n = 32600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32600)', number=100, globals=globals()))
n = 32700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32700)', number=100, globals=globals()))
n = 32800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32800)', number=100, globals=globals()))
n = 32900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(32900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(32900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(32900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(32900)', number=100, globals=globals()))
n = 33000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33000)', number=100, globals=globals()))
n = 33100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33100)', number=100, globals=globals()))
n = 33200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33200)', number=100, globals=globals()))
n = 33300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33300)', number=100, globals=globals()))
n = 33400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33400)', number=100, globals=globals()))
n = 33500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33500)', number=100, globals=globals()))
n = 33600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33600)', number=100, globals=globals()))
n = 33700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33700)', number=100, globals=globals()))
n = 33800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33800)', number=100, globals=globals()))
n = 33900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(33900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(33900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(33900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(33900)', number=100, globals=globals()))
n = 34000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34000)', number=100, globals=globals()))
n = 34100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34100)', number=100, globals=globals()))
n = 34200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34200)', number=100, globals=globals()))
n = 34300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34300)', number=100, globals=globals()))
n = 34400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34400)', number=100, globals=globals()))
n = 34500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34500)', number=100, globals=globals()))
n = 34600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34600)', number=100, globals=globals()))
n = 34700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34700)', number=100, globals=globals()))
n = 34800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34800)', number=100, globals=globals()))
n = 34900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(34900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(34900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(34900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(34900)', number=100, globals=globals()))
n = 35000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35000)', number=100, globals=globals()))
n = 35100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35100)', number=100, globals=globals()))
n = 35200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35200)', number=100, globals=globals()))
n = 35300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35300)', number=100, globals=globals()))
n = 35400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35400)', number=100, globals=globals()))
n = 35500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35500)', number=100, globals=globals()))
n = 35600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35600)', number=100, globals=globals()))
n = 35700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35700)', number=100, globals=globals()))
n = 35800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35800)', number=100, globals=globals()))
n = 35900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(35900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(35900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(35900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(35900)', number=100, globals=globals()))
n = 36000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36000)', number=100, globals=globals()))
n = 36100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36100)', number=100, globals=globals()))
n = 36200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36200)', number=100, globals=globals()))
n = 36300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36300)', number=100, globals=globals()))
n = 36400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36400)', number=100, globals=globals()))
n = 36500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36500)', number=100, globals=globals()))
n = 36600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36600)', number=100, globals=globals()))
n = 36700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36700)', number=100, globals=globals()))
n = 36800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36800)', number=100, globals=globals()))
n = 36900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(36900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(36900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(36900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(36900)', number=100, globals=globals()))
n = 37000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37000)', number=100, globals=globals()))
n = 37100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37100)', number=100, globals=globals()))
n = 37200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37200)', number=100, globals=globals()))
n = 37300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37300)', number=100, globals=globals()))
n = 37400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37400)', number=100, globals=globals()))
n = 37500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37500)', number=100, globals=globals()))
n = 37600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37600)', number=100, globals=globals()))
n = 37700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37700)', number=100, globals=globals()))
n = 37800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37800)', number=100, globals=globals()))
n = 37900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(37900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(37900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(37900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(37900)', number=100, globals=globals()))
n = 38000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38000)', number=100, globals=globals()))
n = 38100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38100)', number=100, globals=globals()))
n = 38200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38200)', number=100, globals=globals()))
n = 38300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38300)', number=100, globals=globals()))
n = 38400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38400)', number=100, globals=globals()))
n = 38500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38500)', number=100, globals=globals()))
n = 38600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38600)', number=100, globals=globals()))
n = 38700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38700)', number=100, globals=globals()))
n = 38800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38800)', number=100, globals=globals()))
n = 38900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(38900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(38900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(38900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(38900)', number=100, globals=globals()))
n = 39000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39000)', number=100, globals=globals()))
n = 39100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39100)', number=100, globals=globals()))
n = 39200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39200)', number=100, globals=globals()))
n = 39300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39300)', number=100, globals=globals()))
n = 39400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39400)', number=100, globals=globals()))
n = 39500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39500)', number=100, globals=globals()))
n = 39600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39600)', number=100, globals=globals()))
n = 39700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39700)', number=100, globals=globals()))
n = 39800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39800)', number=100, globals=globals()))
n = 39900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(39900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(39900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(39900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(39900)', number=100, globals=globals()))
n = 40000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40000)', number=100, globals=globals()))
n = 40100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40100)', number=100, globals=globals()))
n = 40200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40200)', number=100, globals=globals()))
n = 40300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40300)', number=100, globals=globals()))
n = 40400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40400)', number=100, globals=globals()))
n = 40500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40500)', number=100, globals=globals()))
n = 40600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40600)', number=100, globals=globals()))
n = 40700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40700)', number=100, globals=globals()))
n = 40800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40800)', number=100, globals=globals()))
n = 40900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(40900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(40900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(40900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(40900)', number=100, globals=globals()))
n = 41000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41000)', number=100, globals=globals()))
n = 41100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41100)', number=100, globals=globals()))
n = 41200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41200)', number=100, globals=globals()))
n = 41300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41300)', number=100, globals=globals()))
n = 41400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41400)', number=100, globals=globals()))
n = 41500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41500)', number=100, globals=globals()))
n = 41600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41600)', number=100, globals=globals()))
n = 41700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41700)', number=100, globals=globals()))
n = 41800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41800)', number=100, globals=globals()))
n = 41900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(41900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(41900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(41900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(41900)', number=100, globals=globals()))
n = 42000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42000)', number=100, globals=globals()))
n = 42100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42100)', number=100, globals=globals()))
n = 42200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42200)', number=100, globals=globals()))
n = 42300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42300)', number=100, globals=globals()))
n = 42400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42400)', number=100, globals=globals()))
n = 42500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42500)', number=100, globals=globals()))
n = 42600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42600)', number=100, globals=globals()))
n = 42700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42700)', number=100, globals=globals()))
n = 42800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42800)', number=100, globals=globals()))
n = 42900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(42900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(42900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(42900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(42900)', number=100, globals=globals()))
n = 43000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43000)', number=100, globals=globals()))
n = 43100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43100)', number=100, globals=globals()))
n = 43200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43200)', number=100, globals=globals()))
n = 43300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43300)', number=100, globals=globals()))
n = 43400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43400)', number=100, globals=globals()))
n = 43500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43500)', number=100, globals=globals()))
n = 43600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43600)', number=100, globals=globals()))
n = 43700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43700)', number=100, globals=globals()))
n = 43800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43800)', number=100, globals=globals()))
n = 43900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(43900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(43900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(43900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(43900)', number=100, globals=globals()))
n = 44000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44000)', number=100, globals=globals()))
n = 44100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44100)', number=100, globals=globals()))
n = 44200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44200)', number=100, globals=globals()))
n = 44300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44300)', number=100, globals=globals()))
n = 44400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44400)', number=100, globals=globals()))
n = 44500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44500)', number=100, globals=globals()))
n = 44600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44600)', number=100, globals=globals()))
n = 44700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44700)', number=100, globals=globals()))
n = 44800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44800)', number=100, globals=globals()))
n = 44900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(44900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(44900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(44900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(44900)', number=100, globals=globals()))
n = 45000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45000)', number=100, globals=globals()))
n = 45100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45100)', number=100, globals=globals()))
n = 45200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45200)', number=100, globals=globals()))
n = 45300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45300)', number=100, globals=globals()))
n = 45400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45400)', number=100, globals=globals()))
n = 45500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45500)', number=100, globals=globals()))
n = 45600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45600)', number=100, globals=globals()))
n = 45700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45700)', number=100, globals=globals()))
n = 45800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45800)', number=100, globals=globals()))
n = 45900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(45900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(45900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(45900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(45900)', number=100, globals=globals()))
n = 46000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46000)', number=100, globals=globals()))
n = 46100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46100)', number=100, globals=globals()))
n = 46200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46200)', number=100, globals=globals()))
n = 46300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46300)', number=100, globals=globals()))
n = 46400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46400)', number=100, globals=globals()))
n = 46500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46500)', number=100, globals=globals()))
n = 46600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46600)', number=100, globals=globals()))
n = 46700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46700)', number=100, globals=globals()))
n = 46800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46800)', number=100, globals=globals()))
n = 46900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(46900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(46900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(46900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(46900)', number=100, globals=globals()))
n = 47000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47000)', number=100, globals=globals()))
n = 47100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47100)', number=100, globals=globals()))
n = 47200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47200)', number=100, globals=globals()))
n = 47300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47300)', number=100, globals=globals()))
n = 47400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47400)', number=100, globals=globals()))
n = 47500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47500)', number=100, globals=globals()))
n = 47600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47600)', number=100, globals=globals()))
n = 47700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47700)', number=100, globals=globals()))
n = 47800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47800)', number=100, globals=globals()))
n = 47900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(47900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(47900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(47900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(47900)', number=100, globals=globals()))
n = 48000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48000)', number=100, globals=globals()))
n = 48100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48100)', number=100, globals=globals()))
n = 48200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48200)', number=100, globals=globals()))
n = 48300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48300)', number=100, globals=globals()))
n = 48400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48400)', number=100, globals=globals()))
n = 48500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48500)', number=100, globals=globals()))
n = 48600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48600)', number=100, globals=globals()))
n = 48700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48700)', number=100, globals=globals()))
n = 48800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48800)', number=100, globals=globals()))
n = 48900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(48900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(48900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(48900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(48900)', number=100, globals=globals()))
n = 49000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49000)', number=100, globals=globals()))
n = 49100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49100)', number=100, globals=globals()))
n = 49200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49200)', number=100, globals=globals()))
n = 49300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49300)', number=100, globals=globals()))
n = 49400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49400)', number=100, globals=globals()))
n = 49500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49500)', number=100, globals=globals()))
n = 49600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49600)', number=100, globals=globals()))
n = 49700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49700)', number=100, globals=globals()))
n = 49800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49800)', number=100, globals=globals()))
n = 49900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(49900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(49900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(49900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(49900)', number=100, globals=globals()))
n = 50000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50000)', number=100, globals=globals()))
n = 50100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50100)', number=100, globals=globals()))
n = 50200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50200)', number=100, globals=globals()))
n = 50300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50300)', number=100, globals=globals()))
n = 50400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50400)', number=100, globals=globals()))
n = 50500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50500)', number=100, globals=globals()))
n = 50600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50600)', number=100, globals=globals()))
n = 50700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50700)', number=100, globals=globals()))
n = 50800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50800)', number=100, globals=globals()))
n = 50900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(50900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(50900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(50900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(50900)', number=100, globals=globals()))
n = 51000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51000)', number=100, globals=globals()))
n = 51100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51100)', number=100, globals=globals()))
n = 51200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51200)', number=100, globals=globals()))
n = 51300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51300)', number=100, globals=globals()))
n = 51400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51400)', number=100, globals=globals()))
n = 51500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51500)', number=100, globals=globals()))
n = 51600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51600)', number=100, globals=globals()))
n = 51700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51700)', number=100, globals=globals()))
n = 51800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51800)', number=100, globals=globals()))
n = 51900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(51900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(51900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(51900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(51900)', number=100, globals=globals()))
n = 52000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52000)', number=100, globals=globals()))
n = 52100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52100)', number=100, globals=globals()))
n = 52200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52200)', number=100, globals=globals()))
n = 52300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52300)', number=100, globals=globals()))
n = 52400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52400)', number=100, globals=globals()))
n = 52500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52500)', number=100, globals=globals()))
n = 52600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52600)', number=100, globals=globals()))
n = 52700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52700)', number=100, globals=globals()))
n = 52800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52800)', number=100, globals=globals()))
n = 52900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(52900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(52900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(52900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(52900)', number=100, globals=globals()))
n = 53000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53000)', number=100, globals=globals()))
n = 53100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53100)', number=100, globals=globals()))
n = 53200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53200)', number=100, globals=globals()))
n = 53300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53300)', number=100, globals=globals()))
n = 53400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53400)', number=100, globals=globals()))
n = 53500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53500)', number=100, globals=globals()))
n = 53600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53600)', number=100, globals=globals()))
n = 53700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53700)', number=100, globals=globals()))
n = 53800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53800)', number=100, globals=globals()))
n = 53900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(53900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(53900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(53900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(53900)', number=100, globals=globals()))
n = 54000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54000)', number=100, globals=globals()))
n = 54100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54100)', number=100, globals=globals()))
n = 54200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54200)', number=100, globals=globals()))
n = 54300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54300)', number=100, globals=globals()))
n = 54400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54400)', number=100, globals=globals()))
n = 54500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54500)', number=100, globals=globals()))
n = 54600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54600)', number=100, globals=globals()))
n = 54700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54700)', number=100, globals=globals()))
n = 54800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54800)', number=100, globals=globals()))
n = 54900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(54900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(54900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(54900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(54900)', number=100, globals=globals()))
n = 55000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55000)', number=100, globals=globals()))
n = 55100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55100)', number=100, globals=globals()))
n = 55200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55200)', number=100, globals=globals()))
n = 55300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55300)', number=100, globals=globals()))
n = 55400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55400)', number=100, globals=globals()))
n = 55500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55500)', number=100, globals=globals()))
n = 55600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55600)', number=100, globals=globals()))
n = 55700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55700)', number=100, globals=globals()))
n = 55800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55800)', number=100, globals=globals()))
n = 55900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(55900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(55900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(55900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(55900)', number=100, globals=globals()))
n = 56000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56000)', number=100, globals=globals()))
n = 56100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56100)', number=100, globals=globals()))
n = 56200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56200)', number=100, globals=globals()))
n = 56300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56300)', number=100, globals=globals()))
n = 56400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56400)', number=100, globals=globals()))
n = 56500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56500)', number=100, globals=globals()))
n = 56600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56600)', number=100, globals=globals()))
n = 56700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56700)', number=100, globals=globals()))
n = 56800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56800)', number=100, globals=globals()))
n = 56900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(56900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(56900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(56900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(56900)', number=100, globals=globals()))
n = 57000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57000)', number=100, globals=globals()))
n = 57100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57100)', number=100, globals=globals()))
n = 57200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57200)', number=100, globals=globals()))
n = 57300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57300)', number=100, globals=globals()))
n = 57400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57400)', number=100, globals=globals()))
n = 57500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57500)', number=100, globals=globals()))
n = 57600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57600)', number=100, globals=globals()))
n = 57700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57700)', number=100, globals=globals()))
n = 57800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57800)', number=100, globals=globals()))
n = 57900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(57900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(57900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(57900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(57900)', number=100, globals=globals()))
n = 58000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58000)', number=100, globals=globals()))
n = 58100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58100)', number=100, globals=globals()))
n = 58200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58200)', number=100, globals=globals()))
n = 58300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58300)', number=100, globals=globals()))
n = 58400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58400)', number=100, globals=globals()))
n = 58500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58500)', number=100, globals=globals()))
n = 58600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58600)', number=100, globals=globals()))
n = 58700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58700)', number=100, globals=globals()))
n = 58800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58800)', number=100, globals=globals()))
n = 58900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(58900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(58900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(58900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(58900)', number=100, globals=globals()))
n = 59000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59000)', number=100, globals=globals()))
n = 59100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59100)', number=100, globals=globals()))
n = 59200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59200)', number=100, globals=globals()))
n = 59300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59300)', number=100, globals=globals()))
n = 59400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59400)', number=100, globals=globals()))
n = 59500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59500)', number=100, globals=globals()))
n = 59600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59600)', number=100, globals=globals()))
n = 59700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59700)', number=100, globals=globals()))
n = 59800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59800)', number=100, globals=globals()))
n = 59900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(59900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(59900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(59900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(59900)', number=100, globals=globals()))
n = 60000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60000)', number=100, globals=globals()))
n = 60100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60100)', number=100, globals=globals()))
n = 60200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60200)', number=100, globals=globals()))
n = 60300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60300)', number=100, globals=globals()))
n = 60400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60400)', number=100, globals=globals()))
n = 60500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60500)', number=100, globals=globals()))
n = 60600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60600)', number=100, globals=globals()))
n = 60700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60700)', number=100, globals=globals()))
n = 60800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60800)', number=100, globals=globals()))
n = 60900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(60900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(60900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(60900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(60900)', number=100, globals=globals()))
n = 61000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61000)', number=100, globals=globals()))
n = 61100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61100)', number=100, globals=globals()))
n = 61200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61200)', number=100, globals=globals()))
n = 61300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61300)', number=100, globals=globals()))
n = 61400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61400)', number=100, globals=globals()))
n = 61500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61500)', number=100, globals=globals()))
n = 61600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61600)', number=100, globals=globals()))
n = 61700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61700)', number=100, globals=globals()))
n = 61800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61800)', number=100, globals=globals()))
n = 61900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(61900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(61900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(61900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(61900)', number=100, globals=globals()))
n = 62000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62000)', number=100, globals=globals()))
n = 62100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62100)', number=100, globals=globals()))
n = 62200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62200)', number=100, globals=globals()))
n = 62300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62300)', number=100, globals=globals()))
n = 62400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62400)', number=100, globals=globals()))
n = 62500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62500)', number=100, globals=globals()))
n = 62600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62600)', number=100, globals=globals()))
n = 62700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62700)', number=100, globals=globals()))
n = 62800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62800)', number=100, globals=globals()))
n = 62900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(62900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(62900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(62900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(62900)', number=100, globals=globals()))
n = 63000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63000)', number=100, globals=globals()))
n = 63100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63100)', number=100, globals=globals()))
n = 63200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63200)', number=100, globals=globals()))
n = 63300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63300)', number=100, globals=globals()))
n = 63400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63400)', number=100, globals=globals()))
n = 63500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63500)', number=100, globals=globals()))
n = 63600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63600)', number=100, globals=globals()))
n = 63700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63700)', number=100, globals=globals()))
n = 63800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63800)', number=100, globals=globals()))
n = 63900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(63900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(63900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(63900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(63900)', number=100, globals=globals()))
n = 64000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64000)', number=100, globals=globals()))
n = 64100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64100)', number=100, globals=globals()))
n = 64200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64200)', number=100, globals=globals()))
n = 64300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64300)', number=100, globals=globals()))
n = 64400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64400)', number=100, globals=globals()))
n = 64500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64500)', number=100, globals=globals()))
n = 64600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64600)', number=100, globals=globals()))
n = 64700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64700)', number=100, globals=globals()))
n = 64800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64800)', number=100, globals=globals()))
n = 64900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(64900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(64900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(64900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(64900)', number=100, globals=globals()))
n = 65000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65000)', number=100, globals=globals()))
n = 65100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65100)', number=100, globals=globals()))
n = 65200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65200)', number=100, globals=globals()))
n = 65300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65300)', number=100, globals=globals()))
n = 65400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65400)', number=100, globals=globals()))
n = 65500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65500)', number=100, globals=globals()))
n = 65600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65600)', number=100, globals=globals()))
n = 65700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65700)', number=100, globals=globals()))
n = 65800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65800)', number=100, globals=globals()))
n = 65900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(65900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(65900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(65900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(65900)', number=100, globals=globals()))
n = 66000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66000)', number=100, globals=globals()))
n = 66100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66100)', number=100, globals=globals()))
n = 66200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66200)', number=100, globals=globals()))
n = 66300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66300)', number=100, globals=globals()))
n = 66400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66400)', number=100, globals=globals()))
n = 66500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66500)', number=100, globals=globals()))
n = 66600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66600)', number=100, globals=globals()))
n = 66700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66700)', number=100, globals=globals()))
n = 66800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66800)', number=100, globals=globals()))
n = 66900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(66900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(66900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(66900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(66900)', number=100, globals=globals()))
n = 67000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67000)', number=100, globals=globals()))
n = 67100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67100)', number=100, globals=globals()))
n = 67200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67200)', number=100, globals=globals()))
n = 67300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67300)', number=100, globals=globals()))
n = 67400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67400)', number=100, globals=globals()))
n = 67500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67500)', number=100, globals=globals()))
n = 67600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67600)', number=100, globals=globals()))
n = 67700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67700)', number=100, globals=globals()))
n = 67800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67800)', number=100, globals=globals()))
n = 67900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(67900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(67900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(67900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(67900)', number=100, globals=globals()))
n = 68000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68000)', number=100, globals=globals()))
n = 68100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68100)', number=100, globals=globals()))
n = 68200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68200)', number=100, globals=globals()))
n = 68300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68300)', number=100, globals=globals()))
n = 68400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68400)', number=100, globals=globals()))
n = 68500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68500)', number=100, globals=globals()))
n = 68600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68600)', number=100, globals=globals()))
n = 68700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68700)', number=100, globals=globals()))
n = 68800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68800)', number=100, globals=globals()))
n = 68900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(68900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(68900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(68900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(68900)', number=100, globals=globals()))
n = 69000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69000)', number=100, globals=globals()))
n = 69100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69100)', number=100, globals=globals()))
n = 69200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69200)', number=100, globals=globals()))
n = 69300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69300)', number=100, globals=globals()))
n = 69400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69400)', number=100, globals=globals()))
n = 69500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69500)', number=100, globals=globals()))
n = 69600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69600)', number=100, globals=globals()))
n = 69700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69700)', number=100, globals=globals()))
n = 69800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69800)', number=100, globals=globals()))
n = 69900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(69900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(69900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(69900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(69900)', number=100, globals=globals()))
n = 70000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70000)', number=100, globals=globals()))
n = 70100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70100)', number=100, globals=globals()))
n = 70200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70200)', number=100, globals=globals()))
n = 70300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70300)', number=100, globals=globals()))
n = 70400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70400)', number=100, globals=globals()))
n = 70500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70500)', number=100, globals=globals()))
n = 70600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70600)', number=100, globals=globals()))
n = 70700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70700)', number=100, globals=globals()))
n = 70800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70800)', number=100, globals=globals()))
n = 70900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(70900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(70900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(70900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(70900)', number=100, globals=globals()))
n = 71000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71000)', number=100, globals=globals()))
n = 71100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71100)', number=100, globals=globals()))
n = 71200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71200)', number=100, globals=globals()))
n = 71300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71300)', number=100, globals=globals()))
n = 71400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71400)', number=100, globals=globals()))
n = 71500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71500)', number=100, globals=globals()))
n = 71600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71600)', number=100, globals=globals()))
n = 71700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71700)', number=100, globals=globals()))
n = 71800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71800)', number=100, globals=globals()))
n = 71900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(71900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(71900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(71900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(71900)', number=100, globals=globals()))
n = 72000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72000)', number=100, globals=globals()))
n = 72100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72100)', number=100, globals=globals()))
n = 72200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72200)', number=100, globals=globals()))
n = 72300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72300)', number=100, globals=globals()))
n = 72400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72400)', number=100, globals=globals()))
n = 72500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72500)', number=100, globals=globals()))
n = 72600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72600)', number=100, globals=globals()))
n = 72700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72700)', number=100, globals=globals()))
n = 72800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72800)', number=100, globals=globals()))
n = 72900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(72900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(72900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(72900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(72900)', number=100, globals=globals()))
n = 73000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73000)', number=100, globals=globals()))
n = 73100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73100)', number=100, globals=globals()))
n = 73200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73200)', number=100, globals=globals()))
n = 73300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73300)', number=100, globals=globals()))
n = 73400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73400)', number=100, globals=globals()))
n = 73500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73500)', number=100, globals=globals()))
n = 73600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73600)', number=100, globals=globals()))
n = 73700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73700)', number=100, globals=globals()))
n = 73800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73800)', number=100, globals=globals()))
n = 73900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(73900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(73900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(73900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(73900)', number=100, globals=globals()))
n = 74000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74000)', number=100, globals=globals()))
n = 74100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74100)', number=100, globals=globals()))
n = 74200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74200)', number=100, globals=globals()))
n = 74300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74300)', number=100, globals=globals()))
n = 74400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74400)', number=100, globals=globals()))
n = 74500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74500)', number=100, globals=globals()))
n = 74600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74600)', number=100, globals=globals()))
n = 74700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74700)', number=100, globals=globals()))
n = 74800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74800)', number=100, globals=globals()))
n = 74900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(74900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(74900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(74900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(74900)', number=100, globals=globals()))
n = 75000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75000)', number=100, globals=globals()))
n = 75100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75100)', number=100, globals=globals()))
n = 75200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75200)', number=100, globals=globals()))
n = 75300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75300)', number=100, globals=globals()))
n = 75400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75400)', number=100, globals=globals()))
n = 75500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75500)', number=100, globals=globals()))
n = 75600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75600)', number=100, globals=globals()))
n = 75700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75700)', number=100, globals=globals()))
n = 75800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75800)', number=100, globals=globals()))
n = 75900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(75900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(75900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(75900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(75900)', number=100, globals=globals()))
n = 76000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76000)', number=100, globals=globals()))
n = 76100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76100)', number=100, globals=globals()))
n = 76200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76200)', number=100, globals=globals()))
n = 76300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76300)', number=100, globals=globals()))
n = 76400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76400)', number=100, globals=globals()))
n = 76500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76500)', number=100, globals=globals()))
n = 76600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76600)', number=100, globals=globals()))
n = 76700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76700)', number=100, globals=globals()))
n = 76800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76800)', number=100, globals=globals()))
n = 76900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(76900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(76900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(76900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(76900)', number=100, globals=globals()))
n = 77000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77000)', number=100, globals=globals()))
n = 77100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77100)', number=100, globals=globals()))
n = 77200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77200)', number=100, globals=globals()))
n = 77300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77300)', number=100, globals=globals()))
n = 77400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77400)', number=100, globals=globals()))
n = 77500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77500)', number=100, globals=globals()))
n = 77600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77600)', number=100, globals=globals()))
n = 77700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77700)', number=100, globals=globals()))
n = 77800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77800)', number=100, globals=globals()))
n = 77900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(77900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(77900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(77900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(77900)', number=100, globals=globals()))
n = 78000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78000)', number=100, globals=globals()))
n = 78100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78100)', number=100, globals=globals()))
n = 78200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78200)', number=100, globals=globals()))
n = 78300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78300)', number=100, globals=globals()))
n = 78400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78400)', number=100, globals=globals()))
n = 78500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78500)', number=100, globals=globals()))
n = 78600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78600)', number=100, globals=globals()))
n = 78700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78700)', number=100, globals=globals()))
n = 78800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78800)', number=100, globals=globals()))
n = 78900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(78900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(78900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(78900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(78900)', number=100, globals=globals()))
n = 79000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79000)', number=100, globals=globals()))
n = 79100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79100)', number=100, globals=globals()))
n = 79200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79200)', number=100, globals=globals()))
n = 79300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79300)', number=100, globals=globals()))
n = 79400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79400)', number=100, globals=globals()))
n = 79500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79500)', number=100, globals=globals()))
n = 79600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79600)', number=100, globals=globals()))
n = 79700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79700)', number=100, globals=globals()))
n = 79800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79800)', number=100, globals=globals()))
n = 79900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(79900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(79900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(79900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(79900)', number=100, globals=globals()))
n = 80000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80000)', number=100, globals=globals()))
n = 80100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80100)', number=100, globals=globals()))
n = 80200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80200)', number=100, globals=globals()))
n = 80300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80300)', number=100, globals=globals()))
n = 80400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80400)', number=100, globals=globals()))
n = 80500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80500)', number=100, globals=globals()))
n = 80600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80600)', number=100, globals=globals()))
n = 80700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80700)', number=100, globals=globals()))
n = 80800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80800)', number=100, globals=globals()))
n = 80900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(80900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(80900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(80900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(80900)', number=100, globals=globals()))
n = 81000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81000)', number=100, globals=globals()))
n = 81100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81100)', number=100, globals=globals()))
n = 81200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81200)', number=100, globals=globals()))
n = 81300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81300)', number=100, globals=globals()))
n = 81400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81400)', number=100, globals=globals()))
n = 81500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81500)', number=100, globals=globals()))
n = 81600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81600)', number=100, globals=globals()))
n = 81700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81700)', number=100, globals=globals()))
n = 81800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81800)', number=100, globals=globals()))
n = 81900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(81900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(81900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(81900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(81900)', number=100, globals=globals()))
n = 82000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82000)', number=100, globals=globals()))
n = 82100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82100)', number=100, globals=globals()))
n = 82200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82200)', number=100, globals=globals()))
n = 82300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82300)', number=100, globals=globals()))
n = 82400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82400)', number=100, globals=globals()))
n = 82500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82500)', number=100, globals=globals()))
n = 82600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82600)', number=100, globals=globals()))
n = 82700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82700)', number=100, globals=globals()))
n = 82800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82800)', number=100, globals=globals()))
n = 82900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(82900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(82900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(82900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(82900)', number=100, globals=globals()))
n = 83000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83000)', number=100, globals=globals()))
n = 83100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83100)', number=100, globals=globals()))
n = 83200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83200)', number=100, globals=globals()))
n = 83300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83300)', number=100, globals=globals()))
n = 83400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83400)', number=100, globals=globals()))
n = 83500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83500)', number=100, globals=globals()))
n = 83600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83600)', number=100, globals=globals()))
n = 83700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83700)', number=100, globals=globals()))
n = 83800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83800)', number=100, globals=globals()))
n = 83900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(83900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(83900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(83900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(83900)', number=100, globals=globals()))
n = 84000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84000)', number=100, globals=globals()))
n = 84100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84100)', number=100, globals=globals()))
n = 84200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84200)', number=100, globals=globals()))
n = 84300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84300)', number=100, globals=globals()))
n = 84400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84400)', number=100, globals=globals()))
n = 84500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84500)', number=100, globals=globals()))
n = 84600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84600)', number=100, globals=globals()))
n = 84700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84700)', number=100, globals=globals()))
n = 84800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84800)', number=100, globals=globals()))
n = 84900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(84900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(84900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(84900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(84900)', number=100, globals=globals()))
n = 85000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85000)', number=100, globals=globals()))
n = 85100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85100)', number=100, globals=globals()))
n = 85200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85200)', number=100, globals=globals()))
n = 85300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85300)', number=100, globals=globals()))
n = 85400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85400)', number=100, globals=globals()))
n = 85500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85500)', number=100, globals=globals()))
n = 85600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85600)', number=100, globals=globals()))
n = 85700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85700)', number=100, globals=globals()))
n = 85800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85800)', number=100, globals=globals()))
n = 85900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(85900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(85900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(85900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(85900)', number=100, globals=globals()))
n = 86000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86000)', number=100, globals=globals()))
n = 86100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86100)', number=100, globals=globals()))
n = 86200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86200)', number=100, globals=globals()))
n = 86300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86300)', number=100, globals=globals()))
n = 86400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86400)', number=100, globals=globals()))
n = 86500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86500)', number=100, globals=globals()))
n = 86600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86600)', number=100, globals=globals()))
n = 86700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86700)', number=100, globals=globals()))
n = 86800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86800)', number=100, globals=globals()))
n = 86900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(86900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(86900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(86900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(86900)', number=100, globals=globals()))
n = 87000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87000)', number=100, globals=globals()))
n = 87100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87100)', number=100, globals=globals()))
n = 87200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87200)', number=100, globals=globals()))
n = 87300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87300)', number=100, globals=globals()))
n = 87400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87400)', number=100, globals=globals()))
n = 87500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87500)', number=100, globals=globals()))
n = 87600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87600)', number=100, globals=globals()))
n = 87700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87700)', number=100, globals=globals()))
n = 87800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87800)', number=100, globals=globals()))
n = 87900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(87900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(87900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(87900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(87900)', number=100, globals=globals()))
n = 88000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88000)', number=100, globals=globals()))
n = 88100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88100)', number=100, globals=globals()))
n = 88200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88200)', number=100, globals=globals()))
n = 88300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88300)', number=100, globals=globals()))
n = 88400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88400)', number=100, globals=globals()))
n = 88500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88500)', number=100, globals=globals()))
n = 88600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88600)', number=100, globals=globals()))
n = 88700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88700)', number=100, globals=globals()))
n = 88800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88800)', number=100, globals=globals()))
n = 88900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(88900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(88900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(88900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(88900)', number=100, globals=globals()))
n = 89000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89000)', number=100, globals=globals()))
n = 89100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89100)', number=100, globals=globals()))
n = 89200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89200)', number=100, globals=globals()))
n = 89300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89300)', number=100, globals=globals()))
n = 89400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89400)', number=100, globals=globals()))
n = 89500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89500)', number=100, globals=globals()))
n = 89600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89600)', number=100, globals=globals()))
n = 89700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89700)', number=100, globals=globals()))
n = 89800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89800)', number=100, globals=globals()))
n = 89900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(89900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(89900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(89900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(89900)', number=100, globals=globals()))
n = 90000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90000)', number=100, globals=globals()))
n = 90100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90100)', number=100, globals=globals()))
n = 90200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90200)', number=100, globals=globals()))
n = 90300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90300)', number=100, globals=globals()))
n = 90400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90400)', number=100, globals=globals()))
n = 90500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90500)', number=100, globals=globals()))
n = 90600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90600)', number=100, globals=globals()))
n = 90700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90700)', number=100, globals=globals()))
n = 90800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90800)', number=100, globals=globals()))
n = 90900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(90900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(90900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(90900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(90900)', number=100, globals=globals()))
n = 91000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91000)', number=100, globals=globals()))
n = 91100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91100)', number=100, globals=globals()))
n = 91200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91200)', number=100, globals=globals()))
n = 91300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91300)', number=100, globals=globals()))
n = 91400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91400)', number=100, globals=globals()))
n = 91500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91500)', number=100, globals=globals()))
n = 91600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91600)', number=100, globals=globals()))
n = 91700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91700)', number=100, globals=globals()))
n = 91800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91800)', number=100, globals=globals()))
n = 91900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(91900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(91900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(91900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(91900)', number=100, globals=globals()))
n = 92000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92000)', number=100, globals=globals()))
n = 92100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92100)', number=100, globals=globals()))
n = 92200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92200)', number=100, globals=globals()))
n = 92300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92300)', number=100, globals=globals()))
n = 92400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92400)', number=100, globals=globals()))
n = 92500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92500)', number=100, globals=globals()))
n = 92600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92600)', number=100, globals=globals()))
n = 92700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92700)', number=100, globals=globals()))
n = 92800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92800)', number=100, globals=globals()))
n = 92900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(92900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(92900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(92900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(92900)', number=100, globals=globals()))
n = 93000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93000)', number=100, globals=globals()))
n = 93100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93100)', number=100, globals=globals()))
n = 93200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93200)', number=100, globals=globals()))
n = 93300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93300)', number=100, globals=globals()))
n = 93400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93400)', number=100, globals=globals()))
n = 93500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93500)', number=100, globals=globals()))
n = 93600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93600)', number=100, globals=globals()))
n = 93700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93700)', number=100, globals=globals()))
n = 93800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93800)', number=100, globals=globals()))
n = 93900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(93900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(93900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(93900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(93900)', number=100, globals=globals()))
n = 94000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94000)', number=100, globals=globals()))
n = 94100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94100)', number=100, globals=globals()))
n = 94200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94200)', number=100, globals=globals()))
n = 94300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94300)', number=100, globals=globals()))
n = 94400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94400)', number=100, globals=globals()))
n = 94500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94500)', number=100, globals=globals()))
n = 94600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94600)', number=100, globals=globals()))
n = 94700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94700)', number=100, globals=globals()))
n = 94800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94800)', number=100, globals=globals()))
n = 94900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(94900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(94900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(94900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(94900)', number=100, globals=globals()))
n = 95000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95000)', number=100, globals=globals()))
n = 95100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95100)', number=100, globals=globals()))
n = 95200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95200)', number=100, globals=globals()))
n = 95300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95300)', number=100, globals=globals()))
n = 95400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95400)', number=100, globals=globals()))
n = 95500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95500)', number=100, globals=globals()))
n = 95600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95600)', number=100, globals=globals()))
n = 95700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95700)', number=100, globals=globals()))
n = 95800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95800)', number=100, globals=globals()))
n = 95900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(95900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(95900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(95900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(95900)', number=100, globals=globals()))
n = 96000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96000)', number=100, globals=globals()))
n = 96100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96100)', number=100, globals=globals()))
n = 96200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96200)', number=100, globals=globals()))
n = 96300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96300)', number=100, globals=globals()))
n = 96400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96400)', number=100, globals=globals()))
n = 96500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96500)', number=100, globals=globals()))
n = 96600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96600)', number=100, globals=globals()))
n = 96700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96700)', number=100, globals=globals()))
n = 96800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96800)', number=100, globals=globals()))
n = 96900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(96900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(96900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(96900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(96900)', number=100, globals=globals()))
n = 97000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97000)', number=100, globals=globals()))
n = 97100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97100)', number=100, globals=globals()))
n = 97200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97200)', number=100, globals=globals()))
n = 97300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97300)', number=100, globals=globals()))
n = 97400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97400)', number=100, globals=globals()))
n = 97500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97500)', number=100, globals=globals()))
n = 97600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97600)', number=100, globals=globals()))
n = 97700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97700)', number=100, globals=globals()))
n = 97800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97800)', number=100, globals=globals()))
n = 97900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(97900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(97900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(97900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(97900)', number=100, globals=globals()))
n = 98000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98000)', number=100, globals=globals()))
n = 98100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98100)', number=100, globals=globals()))
n = 98200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98200)', number=100, globals=globals()))
n = 98300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98300)', number=100, globals=globals()))
n = 98400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98400)', number=100, globals=globals()))
n = 98500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98500)', number=100, globals=globals()))
n = 98600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98600)', number=100, globals=globals()))
n = 98700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98700)', number=100, globals=globals()))
n = 98800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98800)', number=100, globals=globals()))
n = 98900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(98900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(98900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(98900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(98900)', number=100, globals=globals()))
n = 99000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99000)', number=100, globals=globals()))
n = 99100
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99100)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99100)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99100)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99100)', number=100, globals=globals()))
n = 99200
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99200)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99200)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99200)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99200)', number=100, globals=globals()))
n = 99300
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99300)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99300)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99300)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99300)', number=100, globals=globals()))
n = 99400
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99400)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99400)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99400)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99400)', number=100, globals=globals()))
n = 99500
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99500)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99500)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99500)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99500)', number=100, globals=globals()))
n = 99600
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99600)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99600)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99600)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99600)', number=100, globals=globals()))
n = 99700
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99700)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99700)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99700)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99700)', number=100, globals=globals()))
n = 99800
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99800)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99800)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99800)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99800)', number=100, globals=globals()))
n = 99900
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(99900)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(99900)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(99900)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(99900)', number=100, globals=globals()))
n = 100000
print(f"{n = }")
print('old', timeit.timeit('my_old_min_max(100000)', number=100, globals=globals()))
print('new', timeit.timeit('my_new_min_max(100000)', number=100, globals=globals()))
print('prep_1', timeit.timeit('prep_1(100000)', number=100, globals=globals()))
print('prep_2', timeit.timeit('prep_2(100000)', number=100, globals=globals()))

"""
n = 100
old 0.00833600000000001
new 0.008474099999999984
prep_1 0.008194499999999993
prep_2 0.008423999999999987
n = 200
old 0.01648630000000001
new 0.01646529999999996
prep_1 0.01646840000000005
prep_2 0.01658930000000003
n = 300
old 0.02492150000000004
new 0.024955100000000008
prep_1 0.024875800000000003
prep_2 0.02500659999999999
n = 400
old 0.03383079999999994
new 0.033370299999999964
prep_1 0.03407309999999997
prep_2 0.03346640000000001
n = 500
old 0.042085700000000004
new 0.04285699999999992
prep_1 0.04365069999999993
prep_2 0.04316259999999994
n = 600
old 0.05114380000000007
new 0.05043159999999991
prep_1 0.051783399999999924
prep_2 0.051527700000000065
n = 700
old 0.05936890000000017
new 0.059256500000000045
prep_1 0.05884350000000005
prep_2 0.06006339999999999
n = 800
old 0.06779760000000001
new 0.06740260000000009
prep_1 0.06851039999999986
prep_2 0.06830139999999996
n = 900
old 0.07606429999999986
new 0.07678750000000001
prep_1 0.07749249999999996
prep_2 0.07783130000000016
n = 1000
old 0.08632079999999998
new 0.08598600000000012
prep_1 0.08505379999999985
prep_2 0.08595089999999983
n = 1100
old 0.09573790000000004
new 0.09693360000000029
prep_1 0.09496800000000016
prep_2 0.09398839999999975
n = 1200
old 0.10260709999999973
new 0.10432309999999978
prep_1 0.10318400000000016
prep_2 0.10295169999999976
n = 1300
old 0.11182519999999974
new 0.1129285999999996
prep_1 0.11091700000000015
prep_2 0.11241950000000012
n = 1400
old 0.12026450000000022
new 0.12497760000000024
prep_1 0.12211719999999993
prep_2 0.1258897000000001
n = 1500
old 0.13601410000000058
new 0.13349980000000006
prep_1 0.1298054999999998
prep_2 0.13032589999999988
n = 1600
old 0.1366960000000006
new 0.13787350000000043
prep_1 0.13791629999999966
prep_2 0.1373951
n = 1700
old 0.14657750000000025
new 0.1462829000000001
prep_1 0.14424720000000057
prep_2 0.14637490000000053
n = 1800
old 0.1556084000000002
new 0.1558332
prep_1 0.15468230000000016
prep_2 0.15444699999999933
n = 1900
old 0.16306379999999976
new 0.16231059999999964
prep_1 0.16228169999999942
prep_2 0.16402790000000067
n = 2000
old 0.17142619999999997
new 0.1726964999999998
prep_1 0.17101880000000058
prep_2 0.1771162000000004
n = 2100
old 0.18247310000000017
new 0.18340970000000034
prep_1 0.18045320000000054
prep_2 0.1818635999999998
n = 2200
old 0.18946940000000012
new 0.19130690000000072
prep_1 0.1895030000000002
prep_2 0.18973399999999963
n = 2300
old 0.19893180000000044
new 0.19761379999999917
prep_1 0.19734050000000103
prep_2 0.19883459999999964
n = 2400
old 0.20696960000000075
new 0.20811759999999957
prep_1 0.20787049999999851
prep_2 0.20630789999999877
n = 2500
old 0.21685150000000064
new 0.21481690000000064
prep_1 0.2148292000000005
prep_2 0.21451560000000036
n = 2600
old 0.22457750000000054
new 0.22558549999999933
prep_1 0.2229492000000004
prep_2 0.22399859999999983
n = 2700
old 0.23316270000000117
new 0.233155
prep_1 0.2337024999999997
prep_2 0.23233069999999856
n = 2800
old 0.24089350000000032
new 0.24093239999999838
prep_1 0.23984839999999963
prep_2 0.23982629999999894
n = 2900
old 0.24920950000000097
new 0.24943060000000017
prep_1 0.25095830000000063
prep_2 0.24974199999999946
n = 3000
old 0.25911669999999987
new 0.25919050000000077
prep_1 0.25701529999999906
prep_2 0.2572423999999991
n = 3100
old 0.26659289999999913
new 0.2668625999999996
prep_1 0.26873210000000114
prep_2 0.26820679999999797
n = 3200
old 0.2778740000000006
new 0.2757582999999997
prep_1 0.27462050000000104
prep_2 0.2732139000000018
n = 3300
old 0.28691109999999753
new 0.28322860000000105
prep_1 0.2825109999999995
prep_2 0.28167080000000055
n = 3400
old 0.2928986000000009
new 0.2923809000000013
prep_1 0.2899577999999998
prep_2 0.2920215000000006
n = 3500
old 0.3028103999999985
new 0.3013052000000016
prep_1 0.3009143000000023
prep_2 0.30039740000000137
n = 3600
old 0.3090857999999983
new 0.30871279999999857
prep_1 0.30837809999999877
prep_2 0.3097051999999998
n = 3700
old 0.32380850000000194
new 0.3196770000000022
prep_1 0.3188566999999978
prep_2 0.31890539999999845
n = 3800
old 0.3310719000000013
new 0.32529949999999985
prep_1 0.3271046999999996
prep_2 0.3298294999999989
n = 3900
old 0.3337555000000023
new 0.3337614000000002
prep_1 0.33553560000000004
prep_2 0.33392149999999887
n = 4000
old 0.3447944000000014
new 0.34491650000000007
prep_1 0.3451783000000006
prep_2 0.34429429999999783
n = 4100
old 0.3534150000000018
new 0.3525513999999994
prep_1 0.354114899999999
prep_2 0.3541043999999971
n = 4200
old 0.3615388000000017
new 0.3607624999999999
prep_1 0.3641982000000006
prep_2 0.3614286
n = 4300
old 0.38816440000000085
new 0.38880550000000014
prep_1 0.3730571999999981
prep_2 0.37506520000000165
n = 4400
old 0.38844569999999834
new 0.3851634999999973
prep_1 0.3854423000000011
prep_2 0.38323580000000135
n = 4500
old 0.3888183999999981
new 0.39079770000000025
prep_1 0.3863606000000033
prep_2 0.3887862999999996
n = 4600
old 0.39366270000000014
new 0.3983841999999953
prep_1 0.4051967999999988
prep_2 0.3994110000000006
n = 4700
old 0.40417419999999993
new 0.4090482999999949
prep_1 0.4192846999999986
prep_2 0.42452730000000116
n = 4800
old 0.4403396000000015
new 0.42110449999999844
prep_1 0.42126220000000103
prep_2 0.41820760000000234
n = 4900
old 0.4228410999999994
new 0.4253651000000005
prep_1 0.42195440000000417
prep_2 0.4229044000000002
n = 5000
old 0.4345908000000023
new 0.4313156000000049
prep_1 0.4325441000000012
prep_2 0.4286646000000047
n = 5100
old 0.44014549999999986
new 0.43890490000000426
prep_1 0.4382536999999971
prep_2 0.4386616000000032
n = 5200
old 0.44678589999999474
new 0.44662939999999907
prep_1 0.44651539999999557
prep_2 0.44864009999999865
n = 5300
old 0.45722510000000227
new 0.45664130000000114
prep_1 0.4528403999999995
prep_2 0.45393079999999486
n = 5400
old 0.4632207000000008
new 0.46237160000000443
prep_1 0.4749161000000015
prep_2 0.4786057000000028
n = 5500
old 0.476062799999994
new 0.47330649999999963
prep_1 0.47433800000000303
prep_2 0.4713548000000003
n = 5600
old 0.48385319999999865
new 0.4818168999999983
prep_1 0.4816716999999997
prep_2 0.48030390000000267
n = 5700
old 0.4934014999999974
new 0.4885729000000012
prep_1 0.49456100000000447
prep_2 0.48739559999999926
n = 5800
old 0.5110633999999976
new 0.5021027000000018
prep_1 0.5248715999999973
prep_2 0.5138102999999958
n = 5900
old 0.528872800000002
new 0.5227069000000029
prep_1 0.5178723000000005
prep_2 0.5090331999999975
n = 6000
old 0.5406718000000055
new 0.5331955999999991
prep_1 0.5333053999999962
prep_2 0.5267752999999971
n = 6100
old 0.5312708000000015
new 0.5270428999999979
prep_1 0.5798498999999993
prep_2 0.5419085000000052
n = 6200
old 0.5443831999999986
new 0.5463413000000088
prep_1 0.5502546999999964
prep_2 0.5472070999999943
n = 6300
old 0.5504849000000007
new 0.5577868000000024
prep_1 0.5507072999999991
prep_2 0.5599627999999939
n = 6400
old 0.5753857999999923
new 0.5564059999999955
prep_1 0.5573941999999903
prep_2 0.5803030999999947
n = 6500
old 0.5698938999999967
new 0.5633509000000032
prep_1 0.5843516999999991
prep_2 0.5644065999999981
n = 6600
old 0.5712067000000047
new 0.5707194999999956
prep_1 0.5599009999999964
prep_2 0.5575965999999966
n = 6700
old 0.563797699999995
new 0.562574799999993
prep_1 0.5853897000000075
prep_2 0.579287700000009
n = 6800
old 0.6169368999999989
new 0.6310657000000077
prep_1 0.5876568999999989
prep_2 0.5842435999999935
n = 6900
old 0.5845450999999997
new 0.5882708999999977
prep_1 0.5929423999999983
prep_2 0.5960577000000029
n = 7000
old 0.6032636999999994
new 0.5956694999999996
prep_1 0.594801700000005
prep_2 0.5935116999999934
n = 7100
old 0.5894942999999984
new 0.5913211000000018
prep_1 0.6036639999999949
prep_2 0.5901903999999973
n = 7200
old 0.5960520999999943
new 0.595547400000001
prep_1 0.5964316999999966
prep_2 0.5969447000000088
n = 7300
old 0.6080749999999995
new 0.6067212999999896
prep_1 0.6074567999999942
prep_2 0.6069666000000069
n = 7400
old 0.6146193999999952
new 0.6137847000000107
prep_1 0.6142941000000093
prep_2 0.6157757999999944
n = 7500
old 0.6234679000000085
new 0.6216665999999975
prep_1 0.621851300000003
prep_2 0.6220947999999993
n = 7600
old 0.6320375999999897
new 0.6294076000000075
prep_1 0.630069000000006
prep_2 0.6301564999999982
n = 7700
old 0.6406010000000038
new 0.6386964999999947
prep_1 0.6395051999999879
prep_2 0.6392633000000103
n = 7800
old 0.6467433000000113
new 0.6662582000000015
prep_1 0.6602352000000025
prep_2 0.6644590000000079
n = 7900
old 0.6731464000000074
new 0.6790916000000067
prep_1 0.658641099999997
prep_2 0.655256399999999
n = 8000
old 0.6696120999999948
new 0.6747673999999932
prep_1 0.6788396000000034
prep_2 0.6650332000000105
n = 8100
old 0.674816100000001
new 0.6873379999999969
prep_1 0.6734629999999981
prep_2 0.6712115999999924
n = 8200
old 0.680724699999999
new 0.6803574000000054
prep_1 0.6793423000000018
prep_2 0.6793164999999988
n = 8300
old 0.6895678000000061
new 0.6882001000000031
prep_1 0.6880012000000022
prep_2 0.6877692000000053
n = 8400
old 0.6976223000000061
new 0.696628000000004
prep_1 0.6955296999999945
prep_2 0.6977504999999979
n = 8500
old 0.7065796999999918
new 0.7038732000000039
prep_1 0.7067437999999981
prep_2 0.7062906999999967
n = 8600
old 0.7141660999999999
new 0.7126845000000088
prep_1 0.7121033999999895
prep_2 0.7127095999999966
n = 8700
old 0.7219987999999944
new 0.7226815000000215
prep_1 0.7206371000000047
prep_2 0.7200806999999827
n = 8800
old 0.7308371999999963
new 0.7296502000000089
prep_1 0.7294193999999834
prep_2 0.7287375999999881
n = 8900
old 0.7380046000000107
new 0.7371741999999983
prep_1 0.7465269000000205
prep_2 0.7827264000000014
n = 9000
old 0.7473877999999843
new 0.7457257000000084
prep_1 0.7465120999999897
prep_2 0.7447583999999949
n = 9100
old 0.759975699999984
new 0.7535249000000022
prep_1 0.756060500000018
prep_2 0.7547456000000068
n = 9200
old 0.7646497000000068
new 0.7622415999999816
prep_1 0.7667296999999849
prep_2 0.7618573000000026
n = 9300
old 0.7740442999999857
new 0.7722708000000011
prep_1 0.7711911999999757
prep_2 0.7682470999999964
n = 9400
old 0.7807300999999995
new 0.7791566999999873
prep_1 0.7793588000000113
prep_2 0.7824477000000059
n = 9500
old 0.7901967999999897
new 0.787349799999987
prep_1 0.7868442000000186
prep_2 0.787087299999996
n = 9600
old 0.7952149999999847
new 0.7975749999999948
prep_1 0.7955172000000061
prep_2 0.7946242000000154
n = 9700
old 0.8044539999999927
new 0.8026298999999995
prep_1 0.803922799999981
prep_2 0.8026361999999949
n = 9800
old 0.8134016000000202
new 0.8118628000000001
prep_1 0.8116208000000142
prep_2 0.8123065999999994
n = 9900
old 0.8228157000000067
new 0.8199177000000191
prep_1 0.8247894000000144
prep_2 0.8200628999999822
n = 10000
old 0.8310283999999797
new 0.8296230999999921
prep_1 0.8286024999999881
prep_2 0.8280424000000153
n = 10100
old 0.8381832000000031
new 0.8359915999999998
prep_1 0.8377509999999972
prep_2 0.8368874000000233
n = 10200
old 0.8448918999999933
new 0.8449311999999907
prep_1 0.8447377999999901
prep_2 0.8456175999999971
n = 10300
old 0.8536266999999782
new 0.8524376000000018
prep_1 0.8546987999999942
prep_2 0.8530341000000021
n = 10400
old 0.8635849000000064
new 0.8608059999999966
prep_1 0.8604085999999995
prep_2 0.861873299999985
n = 10500
old 0.8724129000000005
new 0.8706418000000156
prep_1 0.871049400000004
prep_2 0.868600200000003
n = 10600
old 0.8781448999999952
new 0.8771052999999824
prep_1 0.8773446999999805
prep_2 0.8788318000000004
n = 10700
old 0.8881772999999953
new 0.8865062000000137
prep_1 0.8881842999999776
prep_2 0.8867474000000186
n = 10800
old 0.8966815999999938
new 0.8958439000000169
prep_1 0.8932617999999763
prep_2 0.8957396999999787
n = 10900
old 0.9053041999999891
new 0.9036575000000084
prep_1 0.902039000000002
prep_2 0.9037289000000044
n = 11000
old 0.913045899999986
new 0.9089572999999973
prep_1 0.9107970999999964
prep_2 0.9120287000000076
n = 11100
old 0.920517000000018
new 0.9180350000000033
prep_1 0.9196634999999844
prep_2 0.9213604999999916
n = 11200
old 0.9295353999999918
new 0.9270845000000065
prep_1 0.9298675000000003
prep_2 0.9272302999999908
n = 11300
old 0.937382800000023
new 0.9384767999999895
prep_1 0.9363456000000099
prep_2 0.9367992999999899
n = 11400
old 0.9465797000000009
new 0.970218200000005
prep_1 0.9775661999999841
prep_2 1.023808900000006
n = 11500
old 0.9966615000000161
new 1.0812749999999767
prep_1 1.0925512000000026
prep_2 0.9763226000000031
n = 11600
old 0.9690267000000006
new 0.9649207999999874
prep_1 0.9695871999999781
prep_2 0.9680842999999868
n = 11700
old 0.976699300000007
new 0.9718683999999769
prep_1 0.9736733000000015
prep_2 0.9776971000000003
n = 11800
old 1.005321699999996
new 0.996417699999995
prep_1 0.9837971999999979
prep_2 0.9826617000000226
n = 11900
old 0.9931855000000098
new 0.9933117999999865
prep_1 0.9919510000000002
prep_2 0.990667000000002
n = 12000
old 1.0016240999999866
new 0.9986485999999957
prep_1 0.9989692999999988
prep_2 1.000883200000004
n = 12100
old 1.0117831999999964
new 1.008897300000001
prep_1 1.0105072000000064
prep_2 1.00956579999999
n = 12200
old 1.0181176999999764
new 1.0490556000000026
prep_1 1.0640405999999984
prep_2 1.055123000000009
n = 12300
old 1.023767399999997
new 1.076337599999988
prep_1 1.0690448000000288
prep_2 1.0513831000000096
n = 12400
old 1.0629134999999792
new 1.0465755000000172
prep_1 1.0599323999999797
prep_2 1.0530028000000016
n = 12500
old 1.0914968999999815
new 1.2071831999999745
prep_1 1.0700041000000056
prep_2 1.0601570000000038
n = 12600
old 1.0640529000000356
new 1.060068899999976
prep_1 1.0615645000000313
prep_2 1.054803599999957
n = 12700
old 1.0689552000000049
new 1.0611109999999826
prep_1 1.067887600000006
prep_2 1.0714183000000048
n = 12800
old 1.0881618999999887
new 1.0765664999999558
prep_1 1.075607600000012
prep_2 1.0782798000000184
n = 12900
old 1.0864766000000259
new 1.0787493999999924
prep_1 1.097974000000022
prep_2 1.0865229999999997
n = 13000
old 1.086876200000006
new 1.108722699999987
prep_1 1.098710799999992
prep_2 1.099998200000016
n = 13100
old 1.1000617999999918
new 1.1050425999999902
prep_1 1.0943139000000315
prep_2 1.0997674000000188
n = 13200
old 1.1164148999999952
new 1.10968749999995
prep_1 1.1080625999999825
prep_2 1.1222052999999619
n = 13300
old 1.128375300000016
new 1.1193269000000328
prep_1 1.1349346999999739
prep_2 1.1179258000000232
n = 13400
old 1.1291691000000128
new 1.1411522999999875
prep_1 1.1292406999999685
prep_2 1.136997699999995
n = 13500
old 1.1392132000000288
new 1.1326680999999894
prep_1 1.1385796999999798
prep_2 1.1362272000000075
n = 13600
old 1.1502385000000004
new 1.1556815999999799
prep_1 1.1372994999999833
prep_2 1.1464664000000084
n = 13700
old 1.1568379999999934
new 1.142834999999991
prep_1 1.147820500000023
prep_2 1.1485127000000261
n = 13800
old 1.1849771999999916
new 1.1780173999999874
prep_1 1.1649467999999956
prep_2 1.1999382999999852
n = 13900
old 1.1755029000000263
new 1.1707523000000037
prep_1 1.1747958999999923
prep_2 1.168045300000017
n = 14000
old 1.1815335000000005
new 1.1844902999999931
prep_1 1.1739928000000077
prep_2 1.1888314000000264
n = 14100
old 1.1904897999999662
new 1.1960917999999765
prep_1 1.1841579000000024
prep_2 1.1779073000000153
n = 14200
old 1.185294400000032
new 1.1829991999999834
prep_1 1.2011474999999905
prep_2 1.1980133000000137
n = 14300
old 1.2107138000000077
new 1.208959400000026
prep_1 1.1951685999999881
prep_2 1.1926499999999578
n = 14400
old 1.2021206999999663
new 1.211968899999988
prep_1 1.214849500000014
prep_2 1.2163127000000031
n = 14500
old 1.22914209999999
new 1.226233900000011
prep_1 1.2230405000000246
prep_2 1.2278751000000057
n = 14600
old 1.2429389999999785
new 1.2226893000000132
prep_1 1.228563300000019
prep_2 1.221841999999981
n = 14700
old 1.2402260999999726
new 1.2381838999999673
prep_1 1.2387666999999851
prep_2 1.24111309999995
n = 14800
old 1.2462392999999565
new 1.2406133999999724
prep_1 1.2381599000000278
prep_2 1.2428431999999816
n = 14900
old 1.266812200000004
new 1.2648460999999998
prep_1 1.2665617000000111
prep_2 1.2497994999999946
n = 15000
old 1.2688249999999925
new 1.2636475999999561
prep_1 1.2741048999999975
prep_2 1.2648156999999856
n = 15100
old 1.311408799999981
new 1.2796872000000121
prep_1 1.277670599999965
prep_2 1.269893799999977
n = 15200
old 1.283391800000004
new 1.274583000000007
prep_1 1.2787567000000308
prep_2 1.2740997999999877
n = 15300
old 1.2793475999999941
new 1.2804312000000095
prep_1 1.2786702999999875
prep_2 1.284682000000032
n = 15400
old 1.2867152000000033
new 1.2873685000000137
prep_1 1.2878047000000379
prep_2 1.2847340000000145
n = 15500
old 1.3019175000000018
new 1.361745400000018
prep_1 1.3277713999999605
prep_2 1.359431499999971
n = 15600
old 1.3637968999999543
new 1.3535870999999702
prep_1 1.324689899999953
prep_2 1.3139684999999872
n = 15700
old 1.330283100000031
new 1.3243018000000006
prep_1 1.315894300000025
prep_2 1.3180385000000001
n = 15800
old 1.3266206999999781
new 1.334873200000004
prep_1 1.394287399999996
prep_2 1.3339162999999985
n = 15900
old 1.3356311999999662
new 1.3402440999999499
prep_1 1.3418371000000207
prep_2 1.3519092000000228
n = 16000
old 1.3523106000000098
new 1.348407399999985
prep_1 1.3561823000000004
prep_2 1.3374827999999752
n = 16100
old 1.4397356000000059
new 1.3667314999999576
prep_1 1.3693937999999548
prep_2 1.3644564999999602
n = 16200
old 1.3868902999999477
new 1.3630468000000064
prep_1 1.3528855000000135
prep_2 1.3536732999999685
n = 16300
old 1.3754073999999719
new 1.3846022999999832
prep_1 1.3712365999999747
prep_2 1.3740439999999694
n = 16400
old 1.3806060000000002
new 1.3814863999999716
prep_1 1.3796065999999882
prep_2 1.3815386999999646
n = 16500
old 1.4348388999999884
new 1.43630619999999
prep_1 1.4204975000000104
prep_2 1.3829623999999967
n = 16600
old 1.399089100000026
new 1.3895951999999738
prep_1 1.4149649999999951
prep_2 1.3970828999999867
n = 16700
old 1.413640799999996
new 1.4045796999999993
prep_1 1.4030578999999648
prep_2 1.4149651999999833
n = 16800
old 1.4167974000000072
new 1.4170753999999874
prep_1 1.4180867000000035
prep_2 1.4229629999999815
n = 16900
old 1.4195934999999622
new 1.4206842000000393
prep_1 1.4193528999999785
prep_2 1.4203845999999771
n = 17000
old 1.4210231000000135
new 1.4156055000000265
prep_1 1.4272890000000302
prep_2 1.4345792999999958
n = 17100
old 1.4351644000000192
new 1.435406799999953
prep_1 1.4236053000000197
prep_2 1.4288273000000231
n = 17200
old 1.4336629999999673
new 1.436039199999982
prep_1 1.4342854999999872
prep_2 1.435735999999963
n = 17300
old 1.4463168999999994
new 1.4442529000000377
prep_1 1.4408960000000093
prep_2 1.4439694999999801
n = 17400
old 1.454364499999997
new 1.499472400000002
prep_1 1.522145999999907
prep_2 1.5021037000000206
n = 17500
old 1.4838098000000173
new 1.4626438000000235
prep_1 1.466835299999957
prep_2 1.4719778000001043
n = 17600
old 1.5092458000000306
new 1.4726260999999568
prep_1 1.4833671999999751
prep_2 1.4838451999999052
n = 17700
old 1.4936297000000422
new 1.4815648999999667
prep_1 1.5046874999999318
prep_2 1.4830453999999236
n = 17800
old 1.5355383999999503
new 1.503630199999975
prep_1 1.5040729000000965
prep_2 1.496698199999969
n = 17900
old 1.4993151999999554
new 1.5001357999999527
prep_1 1.5134352000000035
prep_2 1.507107700000006
n = 18000
old 1.5218880999999556
new 1.5319719999999961
prep_1 1.524091999999996
prep_2 1.5064028999998982
n = 18100
old 1.5295871000000716
new 1.5252656999999772
prep_1 1.5434440000000222
prep_2 1.5211553999999978
n = 18200
old 1.5398422999999184
new 1.5486568000000034
prep_1 1.5503228999999692
prep_2 1.5738382000000684
n = 18300
old 1.5321413000000348
new 1.5529619000000139
prep_1 1.552417900000023
prep_2 1.5473327999999356
n = 18400
old 1.556773700000008
new 1.5530621999999994
prep_1 1.548729099999946
prep_2 1.5554902000000084
n = 18500
old 1.559829200000081
new 1.5669984999999542
prep_1 1.5643974999999273
prep_2 1.5523098999999547
n = 18600
old 1.5754160000000184
new 1.568549399999938
prep_1 1.5717582999999422
prep_2 1.5713805999999977
n = 18700
old 1.5694551000000274
new 1.5645993999999064
prep_1 1.5636232000000518
prep_2 1.5746191000000636
n = 18800
old 1.5832398000000012
new 1.5826737999999523
prep_1 1.576932700000043
prep_2 1.5933954000000767
n = 18900
old 1.5905749999999443
new 1.5874516000000085
prep_1 1.604450799999995
prep_2 1.5976830000000746
n = 19000
old 1.6035199000000375
new 1.6076711000000614
prep_1 1.6074436000000105
prep_2 1.603915000000029
n = 19100
old 1.606110899999976
new 1.6195883999999978
prep_1 1.6122907999999825
prep_2 1.625506400000063
n = 19200
old 1.629477300000076
new 1.6160512000000153
prep_1 1.6195640000000822
prep_2 1.6245525000000498
n = 19300
old 1.6287167000000409
new 1.639985900000056
prep_1 1.6498679999999695
prep_2 1.6459253000000444
n = 19400
old 1.6523828000000549
new 1.642696199999932
prep_1 1.633757199999991
prep_2 1.641729699999928
n = 19500
old 1.6507264999999052
new 1.6565573000000313
prep_1 1.6468065999999908
prep_2 1.6333033000000796
n = 19600
old 1.677515699999958
new 1.6770305999999664
prep_1 1.6514518999999837
prep_2 1.651218399999948
n = 19700
old 1.6753544000000602
new 1.6664042999999538
prep_1 1.6547743999999511
prep_2 1.645984799999951
n = 19800
old 1.6528946999999334
new 1.6576396000000386
prep_1 1.6533214999999473
prep_2 1.6525441
n = 19900
old 1.6765671000000566
new 1.6898102000000108
prep_1 1.680487400000061
prep_2 1.6744277999999895
n = 20000
old 1.6908207999999831
new 1.687531100000001
prep_1 1.687382599999978
prep_2 1.6715249000000085
n = 20100
old 1.6802754000000277
new 1.6766470999999683
prep_1 1.6967810999999529
prep_2 1.702070899999967
n = 20200
old 1.7099084000000175
new 1.6999279000000342
prep_1 1.6880006000000094
prep_2 1.6847404000000097
n = 20300
old 1.6944288000000824
new 1.6972211999999445
prep_1 1.7175427999999329
prep_2 1.7036669999999958
n = 20400
old 1.735026199999993
new 1.7143456000000015
prep_1 1.702184000000102
prep_2 1.7083128000000443
n = 20500
old 1.7352609999999231
new 1.7429459999999608
prep_1 1.768814099999986
prep_2 1.7264056999999866
n = 20600
old 1.7372186999999712
new 1.7385750999999345
prep_1 1.741796000000022
prep_2 1.7382505999999012
n = 20700
old 1.776986099999931
new 1.7458569999998872
prep_1 1.7484523000000536
prep_2 1.7476132000000462
n = 20800
old 1.7628025999999863
new 1.7484759999999824
prep_1 1.741279400000053
prep_2 1.7436026999999967
n = 20900
old 1.7892486999999164
new 1.7904436000000032
prep_1 1.7797432000000981
prep_2 1.755794700000024
n = 21000
old 1.78623970000001
new 1.7873631999999589
prep_1 1.766774000000055
prep_2 1.7536872000000585
n = 21100
old 1.7609438999999156
new 1.7749347999999827
prep_1 1.7630275999999867
prep_2 1.7591026000000056
n = 21200
old 1.7717404999999644
new 1.78046489999997
prep_1 1.769941200000062
prep_2 1.769860499999936
n = 21300
old 1.7796323999999686
new 1.7787439999999606
prep_1 1.774727799999937
prep_2 1.7752360000000635
n = 21400
old 1.789984400000094
new 1.7874566000000414
prep_1 1.8665470999999343
prep_2 1.7842182000000548
n = 21500
old 1.7961754000000383
new 1.7958500999999387
prep_1 1.7976366000000326
prep_2 1.8036203999999998
n = 21600
old 1.8206238000000212
new 1.8284616999999344
prep_1 1.8151153000000022
prep_2 1.8336497000000236
n = 21700
old 1.8386404999999968
new 1.8156360000000404
prep_1 1.836514999999963
prep_2 1.86250670000004
n = 21800
old 1.8497035000000324
new 1.8501462000000402
prep_1 1.8867457000000059
prep_2 1.8549739999999701
n = 21900
old 1.8640424000000166
new 1.8510993999999528
prep_1 1.8684460000000627
prep_2 1.8472312999999758
n = 22000
old 1.8602732000000515
new 1.8661860000000843
prep_1 1.8556439999999839
prep_2 1.8379559999999628
n = 22100
old 1.8442426000000296
new 1.8467809999999645
prep_1 1.8783619000000726
prep_2 1.9520262999999431
n = 22200
old 1.9052220999999463
new 1.8796744999999646
prep_1 1.8947469999999385
prep_2 1.8783085999999685
n = 22300
old 1.881510599999956
new 1.8596631000000343
prep_1 1.8906013999999232
prep_2 1.9120399999999336
n = 22400
old 1.8842654000000039
new 1.8901639000000614
prep_1 1.8700962000000345
prep_2 1.8716796999999588
n = 22500
old 1.8936394999999493
new 1.8948198000000502
prep_1 1.898423899999898
prep_2 1.8877009999999927
n = 22600
old 1.9116559999999936
new 1.9051123000000416
prep_1 1.9012584999999262
prep_2 1.8932788999999275
n = 22700
old 1.900582600000007
new 1.896274700000049
prep_1 1.9080052000000478
prep_2 1.8948588999999174
n = 22800
old 1.905627500000037
new 1.9026073999999653
prep_1 1.9023985999999695
prep_2 1.9051470000000563
n = 22900
old 1.9144770999999992
new 1.9087528999999677
prep_1 1.916344200000026
prep_2 1.9108551000000489
n = 23000
old 1.9245777999999518
new 1.921716599999968
prep_1 1.918194299999982
prep_2 1.921021499999938
n = 23100
old 1.9271649000000934
new 1.9333660999999438
prep_1 1.9467056999999386
prep_2 1.925453599999969
n = 23200
old 1.969959900000049
new 1.968238700000029
prep_1 1.9772687999999334
prep_2 1.9799528999999438
n = 23300
old 1.974525799999924
new 1.9816629000000603
prep_1 1.9922024999999621
prep_2 1.9897585999999592
n = 23400
old 1.9932926999999836
new 2.0048245000000406
prep_1 2.0288918999999623
prep_2 1.983805699999948
n = 23500
old 1.997898599999985
new 1.9962653000000046
prep_1 2.005907200000024
prep_2 2.0321989999999914
n = 23600
old 2.0233325000000377
new 2.001716600000009
prep_1 2.041211800000042
prep_2 2.0085699999999633
n = 23700
old 2.0172968000000537
new 2.016480599999909
prep_1 1.9846062999999958
prep_2 1.9813791000000265
n = 23800
old 1.992346600000019
new 1.9891321000000062
prep_1 1.9851304000000027
prep_2 2.018622499999992
n = 23900
old 2.0286658999999645
new 2.0447710999999344
prep_1 2.024197000000072
prep_2 2.040433699999994
n = 24000
old 2.031833200000051
new 2.038208900000086
prep_1 2.0381913999999597
prep_2 2.0271141999999145
n = 24100
old 2.067776600000002
new 2.0490773999999874
prep_1 2.0347944000000098
prep_2 2.046764400000029
n = 24200
old 2.03891950000002
new 2.021942500000023
prep_1 2.078078499999947
prep_2 2.055416799999989
n = 24300
old 2.076647200000025
new 2.0554766999999856
prep_1 2.048505099999943
prep_2 2.0361840000000484
n = 24400
old 2.047523599999977
new 2.0409962999999607
prep_1 2.037316199999964
prep_2 2.061145799999963
n = 24500
old 2.076268599999935
new 2.0909348000000136
prep_1 2.076327900000024
prep_2 2.058679600000005
n = 24600
old 2.082613600000059
new 2.074958200000083
prep_1 2.100482300000067
prep_2 2.10280929999999
n = 24700
old 2.107692199999974
new 2.0734348000000864
prep_1 2.0992261999999755
prep_2 2.0964490000001206
n = 24800
old 2.180825700000014
new 2.1737430000000586
prep_1 2.1091863999999987
prep_2 2.1224448000000393
n = 24900
old 2.131918799999994
new 2.103519799999958
prep_1 2.1202709000001505
prep_2 2.132231099999899
n = 25000
old 2.145924599999944
new 2.115187999999989
prep_1 2.1280193000000054
prep_2 2.124608999999964
n = 25100
old 2.137935799999923
new 2.14419369999996
prep_1 2.1043710000001283
prep_2 2.101234599999998
n = 25200
old 2.123080100000152
new 2.1122444000000087
prep_1 2.1250416000000314
prep_2 2.1154712000000018
n = 25300
old 2.117332000000033
new 2.1121785999998792
prep_1 2.1116103999997904
prep_2 2.1146122000000105
n = 25400
old 2.125091599999905
new 2.166451099999904
prep_1 2.199028200000157
prep_2 2.13950090000003
n = 25500
old 2.1651367000001756
new 2.1442667999999685
prep_1 2.189966899999945
prep_2 2.169010000000071
n = 25600
old 2.247062000000142
new 2.2260246999999254
prep_1 2.1958457000000635
prep_2 2.1577323999999862
n = 25700
old 2.158739100000048
new 2.158542500000067
prep_1 2.1478389000001243
prep_2 2.1466886999999133
n = 25800
old 2.158097199999929
new 2.1551691999998184
prep_1 2.15567319999991
prep_2 2.154716299999791
n = 25900
old 2.167514100000062
new 2.164728700000069
prep_1 2.163467800000035
prep_2 2.16307740000002
n = 26000
old 2.177591300000131
new 2.1721394999999575
prep_1 2.1699275000000853
prep_2 2.163622200000191
n = 26100
old 2.174285700000155
new 2.179717900000014
prep_1 2.1683170999999675
prep_2 2.1793190000000777
n = 26200
old 2.181273800000099
new 2.1754237000000103
prep_1 2.1878251000000546
prep_2 2.2079584000000523
n = 26300
old 2.1882640000001174
new 2.1849443000000974
prep_1 2.1864806999999473
prep_2 2.21875799999998
n = 26400
old 2.2473267000000305
new 2.233147200000076
prep_1 2.2343565999999555
prep_2 2.238911899999948
n = 26500
old 2.243074100000058
new 2.2198421999999027
prep_1 2.2429133999999067
prep_2 2.2407034000000294
n = 26600
old 2.2581809999999223
new 2.2393701000000874
prep_1 2.2486003999999866
prep_2 2.236723299999994
n = 26700
old 2.2358950000000277
new 2.2610581000001275
prep_1 2.2737919000001057
prep_2 2.233104400000002
n = 26800
old 2.2400012000000515
new 2.2359864000000016
prep_1 2.29030130000001
prep_2 2.265912099999923
n = 26900
old 2.248907299999928
new 2.2475914999999986
prep_1 2.2471978000000945
prep_2 2.2500952000000325
n = 27000
old 2.257290600000033
new 2.2529431999998906
prep_1 2.2586787000000186
prep_2 2.2556993000000602
n = 27100
old 2.2745981000000484
new 2.260112700000036
prep_1 2.2626036999999997
prep_2 2.2854807999999593
n = 27200
old 2.273319399999991
new 2.2615633999998863
prep_1 2.2575031999999737
prep_2 2.2630142000000433
n = 27300
old 2.273166700000047
new 2.3249759000000267
prep_1 2.400685600000088
prep_2 2.338937900000019
n = 27400
old 2.380076800000097
new 2.506324100000029
prep_1 2.622278300000062
prep_2 2.4009066999999504
n = 27500
old 2.571504799999957
new 2.4122581999999966
prep_1 2.3691252000000986
prep_2 2.665835199999947
n = 27600
old 2.487897999999859
new 2.4692837000000054
prep_1 2.4667521000001216
prep_2 2.4076597000000675
n = 27700
old 2.3596388000000843
new 2.33220950000009
prep_1 2.3561976999999388
prep_2 2.386266199999909
n = 27800
old 2.4325589000000036
new 2.6669787999999244
prep_1 2.45904900000005
prep_2 3.0082856999999876
n = 27900
old 3.3335839999999735
new 2.5237414000000626
prep_1 2.464555100000098
prep_2 2.4926944999999705
n = 28000
old 2.5881879000000936
new 2.709115699999984
prep_1 2.4523885000000973
prep_2 2.4734326000000237
n = 28100
old 2.6695784999999432
new 2.5190845999998146
prep_1 2.49806650000005
prep_2 2.428987700000107
n = 28200
old 2.39641000000006
new 2.4474685000000136
prep_1 2.6211860999999317
prep_2 2.590578800000003
n = 28300
old 2.4808399999999438
new 2.492883200000051
prep_1 2.3711885999998685
prep_2 2.40129590000015
n = 28400
old 2.403387900000098
new 2.436743100000058
prep_1 2.4697453000001133
prep_2 2.4931627000000844
n = 28500
old 2.4375941999999213
new 2.4305409999999483
prep_1 2.4228901999999835
prep_2 2.3864059999998517
n = 28600
old 2.414976499999966
new 2.4461119999998573
prep_1 2.440865799999983
prep_2 2.428159399999913
n = 28700
old 2.449677900000097
new 2.4696166000001085
prep_1 2.4459739000001264
prep_2 2.4695495000000847
n = 28800
old 2.4709881000001133
new 2.472392599999921
prep_1 2.464926000000105
prep_2 2.4488483999998607
n = 28900
old 2.4485491999998885
new 2.447020099999918
prep_1 2.5048369999999522
prep_2 2.4981689999999617
n = 29000
old 2.494518800000151
new 2.4966546000000562
prep_1 2.4931587000000945
prep_2 2.4816012000001137
n = 29100
old 2.4887533999999505
new 2.535322800000131
prep_1 2.5089096999997764
prep_2 2.500817300000108
n = 29200
old 2.528370999999879
new 2.49964470000009
prep_1 2.5237593000001652
prep_2 2.517879200000152
n = 29300
old 2.5087508999999955
new 2.500828100000035
prep_1 2.5014243999999053
prep_2 2.5561124000000746
n = 29400
old 2.613489700000173
new 2.515308700000105
prep_1 2.499731600000132
prep_2 2.4956943999998202
n = 29500
old 2.47063049999997
new 2.4863136000001305
prep_1 2.466896899999938
prep_2 2.4847426999999698
n = 29600
old 2.5117917999998554
new 2.49861339999984
prep_1 2.5051696999998967
prep_2 2.5225580999999693
n = 29700
old 2.537359599999945
new 2.527559300000121
prep_1 2.498517200000151
prep_2 2.500131999999894
n = 29800
old 2.514700599999969
new 2.514752900000076
prep_1 2.5071140000000014
prep_2 2.5101042999999663
n = 29900
old 2.5204546999998456
new 2.5336499000000003
prep_1 2.5298043000000234
prep_2 2.5276295999999547
n = 30000
old 2.5422746000001553
new 2.494790299999977
prep_1 2.5250661999998556
prep_2 2.52195370000004
n = 30100
old 2.530635600000096
new 2.5530286999999134
prep_1 2.5622627000000193
prep_2 2.53765680000015
n = 30200
old 2.5563469999999597
new 2.6394880000000285
prep_1 2.5807698000000983
prep_2 2.584260800000038
n = 30300
old 2.6138080000000627
new 2.5705679000000146
prep_1 2.5744297999999617
prep_2 2.5655052999998134
n = 30400
old 2.569726800000126
new 2.562239399999953
prep_1 2.562610599999971
prep_2 2.5848797999999533
n = 30500
old 2.6039032999999563
new 2.5722279999999955
prep_1 2.6052930000000742
prep_2 2.6274682999999186
n = 30600
old 2.6435635000000275
new 2.5980418999999983
prep_1 2.6511058999999477
prep_2 2.638911300000018
n = 30700
old 2.6255043999999543
new 2.6179137999999966
prep_1 2.6311522000000878
prep_2 2.618291400000089
n = 30800
old 2.65596400000004
new 2.6152708000001894
prep_1 2.635691599999973
prep_2 2.6279325999998946
n = 30900
old 2.6470220999999583
new 2.6557212000000163
prep_1 2.6329785000000356
prep_2 2.6397746999998617
n = 31000
old 2.677748500000007
new 2.6674699000000146
prep_1 2.639992399999983
prep_2 2.714623500000016
n = 31100
old 2.6456150999999863
new 2.668149699999958
prep_1 2.653183300000137
prep_2 2.656643699999904
n = 31200
old 2.6599211000000196
new 2.6397183999999925
prep_1 2.658279300000004
prep_2 2.6369448000000375
n = 31300
old 2.638783000000103
new 2.6305393000000095
prep_1 2.6292429000000084
prep_2 2.621496200000138
n = 31400
old 2.673366499999929
new 2.6508292000000893
prep_1 2.659803199999942
prep_2 2.6429023999999117
n = 31500
old 2.661801799999921
new 2.638621899999862
prep_1 2.6682705999999143
prep_2 2.6536091000000397
n = 31600
old 2.6765135000000555
new 2.641962299999932
prep_1 2.6433777999998256
prep_2 2.722065799999882
n = 31700
old 2.7102451000000656
new 2.7697891999998774
prep_1 2.7226682000000437
prep_2 2.7575630000001183
n = 31800
old 2.7619986000001973
new 2.7814994999998817
prep_1 2.769108499999902
prep_2 2.7591968000001543
n = 31900
old 2.7145276000001104
new 2.673239100000046
prep_1 2.7431168000000525
prep_2 2.6674593999998706
n = 32000
old 2.679149300000063
new 2.6706676999999672
prep_1 2.6805391000000327
prep_2 2.711209700000154
n = 32100
old 2.698017099999788
new 2.719679199999973
prep_1 2.6993164000000434
prep_2 2.705330700000104
n = 32200
old 2.7762943999998697
new 2.720189899999923
prep_1 2.7766507999999703
prep_2 2.746433199999956
n = 32300
old 2.705633799999987
new 2.7096070999998574
prep_1 2.700862700000016
prep_2 2.709248699999989
n = 32400
old 2.712430399999903
new 2.7172840999999153
prep_1 2.7102274999999736
prep_2 2.7106466000000182
n = 32500
old 2.7113369999999577
new 2.7396909999999934
prep_1 2.722229299999981
prep_2 2.709885600000007
n = 32600
old 2.7173069000000396
new 2.7166062000001148
prep_1 2.7116819000000305
prep_2 2.725703199999998
n = 32700
old 2.727198000000044
new 2.7186901000000034
prep_1 2.722326899999871
prep_2 2.7245722000000114
n = 32800
old 2.7663082000001395
new 2.8054532999999537
prep_1 2.884956999999986
prep_2 2.874384799999916
n = 32900
old 2.856419599999981
new 2.8576523000001544
prep_1 2.8211155000001327
prep_2 2.8382885000000897
n = 33000
old 2.807280700000092
new 2.7611990000000333
prep_1 2.762015799999972
prep_2 2.7612839000000804
n = 33100
old 2.7724935000001096
new 2.7704400999998597
prep_1 2.7647256000000198
prep_2 2.7986783999999716
n = 33200
old 2.8374825999999302
new 2.8262988999999834
prep_1 2.8572391000000152
prep_2 2.8606419999998707
n = 33300
old 2.8247636000000966
new 2.860428200000115
prep_1 2.9288621999999123
prep_2 2.9856704000001173
n = 33400
old 2.96015280000006
new 2.8968093999999383
prep_1 2.9320890999999847
prep_2 2.8981284000001324
n = 33500
old 2.8631149999998797
new 2.905454899999995
prep_1 2.976410200000146
prep_2 2.8051026000000547
n = 33600
old 2.976287700000057
new 2.938139900000124
prep_1 2.8896879000001263
prep_2 2.8182213000000047
n = 33700
old 2.845362100000102
new 2.95424190000017
prep_1 2.8146299
prep_2 2.855904100000089
n = 33800
old 2.961022200000116
new 2.8397449999999935
prep_1 2.888280399999985
prep_2 2.876608000000033
n = 33900
old 2.89274730000011
new 2.897099600000047
prep_1 2.8540810000001784
prep_2 2.847704799999974
n = 34000
old 2.8449960000000374
new 2.857503100000031
prep_1 2.890421200000219
prep_2 2.859440100000029
n = 34100
old 2.896783599999935
new 2.9264290000000983
prep_1 2.896064900000056
prep_2 2.8686843999998928
n = 34200
old 2.8630542000000787
new 2.870471999999836
prep_1 2.8893465000001015
prep_2 2.8585218000000623
n = 34300
old 2.8814927000000807
new 2.8671355999999832
prep_1 2.8768830000001344
prep_2 2.9101958999999624
n = 34400
old 2.9327129999999215
new 2.9373264999999265
prep_1 2.9421961000000465
prep_2 2.9069180999999844
n = 34500
old 2.90328240000008
new 2.890505100000155
prep_1 2.900428599999941
prep_2 2.8919548999999733
n = 34600
old 2.894482200000084
new 2.900969099999884
prep_1 2.899855099999968
prep_2 2.8979345999998714
n = 34700
old 2.942524800000001
new 2.9312862000001587
prep_1 2.9307415000002948
prep_2 2.9289936999998645
n = 34800
old 2.926923800000168
new 2.9195557000002736
prep_1 2.947675700000218
prep_2 2.9446646000001238
n = 34900
old 2.9801948999997876
new 2.9340139000000818
prep_1 2.9191749999999956
prep_2 2.980832300000202
n = 35000
old 2.9798743999999715
new 2.955612100000053
prep_1 2.9410815999999613
prep_2 2.9367600000000493
n = 35100
old 2.97082730000011
new 3.0028283000001466
prep_1 2.965298300000086
prep_2 2.9941711000001305
n = 35200
old 2.977615700000115
new 2.985845700000027
prep_1 2.943073699999786
prep_2 2.9415220000000772
n = 35300
old 2.9712282999998934
new 2.9596615000000384
prep_1 2.950390900000002
prep_2 2.9510888999998315
n = 35400
old 3.008444800000234
new 2.982911499999773
prep_1 3.016770700000052
prep_2 2.999116000000413
n = 35500
old 2.9995207000001756
new 3.031997799999772
prep_1 2.9935639000000265
prep_2 2.9705354000002444
n = 35600
old 2.986172599999918
new 2.9779908000000432
prep_1 3.001639399999931
prep_2 3.024137399999745
n = 35700
old 3.0322229999997035
new 3.04074189999983
prep_1 3.01619380000011
prep_2 2.99455080000007
n = 35800
old 3.0070018999999775
new 2.999793299999965
prep_1 3.0228276999996524
prep_2 3.03601929999968
n = 35900
old 3.0824726999999257
new 3.0639892999997755
prep_1 3.028398399999787
prep_2 3.038295199999993
n = 36000
old 3.0347116000002643
new 3.039643200000228
prep_1 3.0468074000000342
prep_2 3.0091620000002877
n = 36100
old 3.022501000000375
new 3.0399320999999873
prep_1 3.062914599999658
prep_2 3.075724199999968
n = 36200
old 3.0740774999999303
new 3.0564226999999846
prep_1 3.0270619000002625
prep_2 3.023214100000132
n = 36300
old 3.0606699999998455
new 3.156147499999861
prep_1 3.0902046000001064
prep_2 3.0793531999997867
n = 36400
old 3.0884171999996397
new 3.0436423000001014
prep_1 3.0403559999999743
prep_2 3.047685800000181
n = 36500
old 3.052146200000152
new 3.048586200000045
prep_1 3.0536238999998204
prep_2 3.0627410000001873
n = 36600
old 3.063306499999726
new 3.0570161000000553
prep_1 3.05703050000011
prep_2 3.055630999999721
n = 36700
old 3.0539286000002903
new 3.069839299999785
prep_1 3.0973573999999644
prep_2 3.0897632999999587
n = 36800
old 3.118551000000025
new 3.1197981999998774
prep_1 3.1123523999999634
prep_2 3.1380983999997625
n = 36900
old 3.1353213000002143
new 3.128176600000188
prep_1 3.0930935000001227
prep_2 3.1291166999999405
n = 37000
old 3.1102826999999706
new 3.126132100000177
prep_1 3.1129880999997113
prep_2 3.0947136999998293
n = 37100
old 3.116425199999867
new 3.1134499999998297
prep_1 3.099380099999962
prep_2 3.1051720000000387
n = 37200
old 3.1158308999997644
new 3.1158941999997296
prep_1 3.1335014999999657
prep_2 3.1111737000001085
n = 37300
old 3.137963799999852
new 3.146304599999894
prep_1 3.1992973000001257
prep_2 3.1519109000000753
n = 37400
old 3.1405736000001525
new 3.1358948000001874
prep_1 3.21557810000013
prep_2 3.216696200000115
n = 37500
old 3.229408499999863
new 3.1837123000000247
prep_1 3.238774600000397
prep_2 3.162309499999992
n = 37600
old 3.148835599999984
new 3.2245044999999664
prep_1 3.256172300000344
prep_2 3.241855199999918
n = 37700
old 3.165539699999954
new 3.180030600000009
prep_1 3.1965202000001227
prep_2 3.2470299000001432
n = 37800
old 3.2308477999999923
new 3.276334699999552
prep_1 3.2160518000000593
prep_2 3.261435000000347
n = 37900
old 3.251614100000097
new 3.1679501000003256
prep_1 3.156627899999876
prep_2 3.2821321000001262
n = 38000
old 3.2358595000000605
new 3.2393512000003284
prep_1 3.2901004000000285
prep_2 3.2455722999998216
n = 38100
old 3.293830699999944
new 3.3543448000000353
prep_1 3.2098580999995647
prep_2 3.198953000000074
n = 38200
old 3.2152485999999953
new 3.218794500000058
prep_1 3.192250299999614
prep_2 3.1941037999999935
n = 38300
old 3.211263499999859
new 3.201866699999755
prep_1 3.1984362999996847
prep_2 3.2495223000000806
n = 38400
old 3.2868310999997448
new 3.218206399999872
prep_1 3.2380887999997867
prep_2 3.2417521000002125
n = 38500
old 3.263196500000049
new 3.26987280000003
prep_1 3.2467688000001544
prep_2 3.2422458999999435
n = 38600
old 3.2491989999998623
new 3.2502246999997624
prep_1 3.274756400000115
prep_2 3.2549321000001328
n = 38700
old 3.335860700000012
new 3.2782516000002033
prep_1 3.291517399999975
prep_2 3.2834585999999035
n = 38800
old 3.2923687000002246
new 3.282527900000332
prep_1 3.302213699999811
prep_2 3.2950401999996757
n = 38900
old 3.303505999999743
new 3.2768065999998726
prep_1 3.290765100000044
prep_2 3.2883403000000726
n = 39000
old 3.265968200000316
new 3.3366547000000537
prep_1 3.266076900000371
prep_2 3.3308883000004244
n = 39100
old 3.2768851999999242
new 3.2688020999999026
prep_1 3.283639899999798
prep_2 3.3257621999996445
n = 39200
old 3.330457099999876
new 3.353124100000059
prep_1 3.3482582000001457
prep_2 3.3500466000000415
n = 39300
old 3.353422099999989
new 3.3033958999999413
prep_1 3.3323036000001593
prep_2 3.3097743000002993
n = 39400
old 3.3223806000000877
new 3.2941570000002685
prep_1 3.2922743999997692
prep_2 3.2938193999998475
n = 39500
old 3.3016665999998622
new 3.2964272999997775
prep_1 3.301569599999766
prep_2 3.298734599999989
n = 39600
old 3.322924300000068
new 3.303307700000005
prep_1 3.3077886999999464
prep_2 3.3716262000002644
n = 39700
old 3.3844929000001684
new 3.3401349999999184
prep_1 3.4275306999998065
prep_2 3.452197800000249
n = 39800
old 3.364400299999943
new 3.308617400000003
prep_1 3.3503897999999026
prep_2 3.3713976999997612
n = 39900
old 3.464718300000186
new 3.47423149999986
prep_1 3.4768051999999443
prep_2 3.3447743000001537
n = 40000
old 3.4036872000001495
new 3.3567063000000417
prep_1 3.357755200000156
prep_2 3.3836105000000316
n = 40100
old 3.3892931000000317
new 3.436386500000026
prep_1 3.405046300000322
prep_2 3.381462300000294
n = 40200
old 3.421056099999987
new 3.45053420000022
prep_1 3.4161909000004016
prep_2 3.395328000000063
n = 40300
old 3.392261800000142
new 3.4455000000002656
prep_1 3.387864200000422
prep_2 3.410956199999873
n = 40400
old 3.4108923999997387
new 3.4560371000002306
prep_1 3.4417452999996385
prep_2 3.4685653000001366
n = 40500
old 3.509770000000117
new 3.4771576000002824
prep_1 3.6005165999999917
prep_2 3.454414700000143
n = 40600
old 3.472121299999799
new 3.4763278000000355
prep_1 3.4565637000000606
prep_2 3.4407320999998774
n = 40700
old 3.457284499999787
new 3.440113300000121
prep_1 3.4397406999996747
prep_2 3.423834600000191
n = 40800
old 3.438768799999707
new 3.4249187999998867
prep_1 3.4293791000000056
prep_2 3.422019999999975
n = 40900
old 3.441818499999954
new 3.5648207999997794
prep_1 3.430049699999927
prep_2 3.4596474999998463
n = 41000
old 3.48155560000032
new 3.469177899999977
prep_1 3.434329599999728
prep_2 3.5372247000000243
n = 41100
old 3.6531504000004134
new 3.666319299999941
prep_1 3.770754300000135
prep_2 3.621662699999888
n = 41200
old 3.6638937000002443
new 3.8342796000001726
prep_1 3.7067551000000094
prep_2 3.457674400000087
n = 41300
old 3.459360700000161
new 3.4548564000001534
prep_1 3.4498365999997986
prep_2 3.444444100000055
n = 41400
old 3.458911700000044
new 3.4545678999998017
prep_1 3.459547399999792
prep_2 3.453361700000187
n = 41500
old 3.460882400000173
new 3.4583560999999463
prep_1 3.4588825999999244
prep_2 3.460687599999801
n = 41600
old 3.480862100000195
new 3.4718729999999596
prep_1 3.466903899999579
prep_2 3.4699562999999216
n = 41700
old 3.4863781000003655
new 3.478706400000192
prep_1 3.4766626000000542
prep_2 3.478552900000068
n = 41800
old 3.489825899999687
new 3.5135368999999628
prep_1 3.526781000000028
prep_2 3.484699499999806
n = 41900
old 3.500627199999599
new 3.4894202999998924
prep_1 3.492935600000237
prep_2 3.4910288999999466
n = 42000
old 3.5056146000001718
new 3.5089011000000028
prep_1 3.5060284000001047
prep_2 3.5037105000001247
n = 42100
old 3.5087773999998717
new 3.512354000000414
prep_1 3.5098957000000155
prep_2 3.5080301999996664
n = 42200
old 3.5231251000000157
new 3.519881400000031
prep_1 3.5204999000002317
prep_2 3.515402499999709
n = 42300
old 3.5341561000000183
new 3.52438310000025
prep_1 3.5187997999996696
prep_2 3.522611300000335
n = 42400
old 3.5389148999997815
new 3.528870999999981
prep_1 3.5332486000002064
prep_2 3.533786500000133
n = 42500
old 3.551551400000335
new 3.540852100000393
prep_1 3.542489899999964
prep_2 3.5576555000002372
n = 42600
old 3.5615757000000485
new 3.552415199999814
prep_1 3.553688399999828
prep_2 3.5839128000002347
n = 42700
old 3.570898699999816
new 3.557926199999656
prep_1 3.5619689000000108
prep_2 3.5583842999999433
n = 42800
old 3.576564100000269
new 3.559451900000113
prep_1 3.5701748000001317
prep_2 3.566448599999603
n = 42900
old 3.578904799999691
new 3.577337499999885
prep_1 3.5691388999998708
prep_2 3.576556299999993
n = 43000
old 3.589876600000025
new 3.5923257999997986
prep_1 3.633528899999874
prep_2 3.5837437000000136
n = 43100
old 3.631059499999992
new 3.6692653999998583
prep_1 3.6044951999997465
prep_2 3.5907430000002023
n = 43200
old 3.6043119000000843
new 3.6014515000001666
prep_1 3.6091623999996045
prep_2 3.6033445000002757
n = 43300
old 3.618822700000237
new 3.6059227999999166
prep_1 3.6164435000000594
prep_2 3.6118186000003334
n = 43400
old 3.627418300000045
new 3.6174691999999595
prep_1 3.623845099999926
prep_2 3.6161418000001504
n = 43500
old 3.6474811000002774
new 3.6706623999998556
prep_1 3.674817300000086
prep_2 3.6293462000003274
n = 43600
old 3.644122200000311
new 3.6377895999999055
prep_1 3.637327599999935
prep_2 3.6383724000002076
n = 43700
old 3.6519235000000663
new 3.648235900000145
prep_1 3.6417003999999906
prep_2 3.646664200000032
n = 43800
old 3.657687299999907
new 3.649222099999861
prep_1 3.648373900000024
prep_2 3.659604400000262
n = 43900
old 3.6656066999998984
new 3.6837373000003026
prep_1 3.6598855000002004
prep_2 3.6629502999999204
n = 44000
old 3.675264100000277
new 3.6892989999996644
prep_1 3.670107800000096
prep_2 3.6688453000001573
n = 44100
old 3.6744855000001735
new 3.6719755999997687
prep_1 3.6769711999995707
prep_2 3.6749088000001393
n = 44200
old 3.6910477000001265
new 3.684996299999966
prep_1 3.6863257999998496
prep_2 3.6829529999999977
n = 44300
old 3.6972090999997818
new 3.712211000000025
prep_1 3.702846799999861
prep_2 3.6963227999999617
n = 44400
old 3.703441499999826
new 3.7034906999997474
prep_1 3.7055287000002863
prep_2 3.6929681000001437
n = 44500
old 3.722018200000093
new 3.707200699999703
prep_1 3.714232400000128
prep_2 3.7065929999998843
n = 44600
old 3.7147353000000294
new 3.7238814999996066
prep_1 3.7163470999998935
prep_2 3.7172833999998147
n = 44700
old 3.7381109999996625
new 3.7308906000002935
prep_1 3.7234937999996873
prep_2 3.7282836999997926
n = 44800
old 3.7408382000003257
new 3.7360250000001543
prep_1 3.7366139000000658
prep_2 3.7302379999996447
n = 44900
old 3.750580199999604
new 3.7430229999999938
prep_1 3.7423047000002043
prep_2 3.7476424000001316
n = 45000
old 3.761339599999701
new 3.751956000000064
prep_1 3.750850899999932
prep_2 3.811439099999916
n = 45100
old 3.8493306000000302
new 3.7686006999997517
prep_1 3.824231800000234
prep_2 3.829372599999715
n = 45200
old 3.7751932999999553
new 3.7696971999998823
prep_1 3.7697321999999076
prep_2 3.8016765000002124
n = 45300
old 3.790265999999974
new 3.781771800000115
prep_1 3.7796931000002587
prep_2 3.7784052000001793
n = 45400
old 3.804460100000142
new 3.8040829999999914
prep_1 3.788384800000131
prep_2 3.789514799999779
n = 45500
old 3.8195964999999887
new 3.84879170000022
prep_1 3.827027299999827
prep_2 3.833405099999709
n = 45600
old 3.8554572000002736
new 3.8588356999998723
prep_1 3.8431854000000385
prep_2 3.839907700000367
n = 45700
old 3.804745599999933
new 3.8022194000000127
prep_1 3.805180400000154
prep_2 3.8039237000002686
n = 45800
old 3.8203693999998904
new 3.8093386999998984
prep_1 3.808563099999901
prep_2 3.8157834000003277
n = 45900
old 3.8218196000002536
new 3.8239560999995774
prep_1 3.815875799999958
prep_2 3.8237011000001075
n = 46000
old 3.8355114999999387
new 3.8289042999999765
prep_1 3.832408100000066
prep_2 3.824377899999945
n = 46100
old 3.8434479999996256
new 3.844053299999814
prep_1 3.8351658999999927
prep_2 3.831474199999775
n = 46200
old 3.856434399999671
new 3.845554600000014
prep_1 3.940918600000259
prep_2 3.91134349999993
n = 46300
old 3.8967467000002216
new 3.8971396000001732
prep_1 3.920606599999701
prep_2 3.9000067000001764
n = 46400
old 3.930026199999702
new 3.8638636999999108
prep_1 3.869236000000001
prep_2 3.870097900000019
n = 46500
old 3.8805029000000104
new 3.9026535000002696
prep_1 3.8812738999999965
prep_2 3.875214600000163
n = 46600
old 3.8909152999999606
new 3.9605287999997927
prep_1 3.9094528000000537
prep_2 3.894551500000034
n = 46700
old 3.950259300000198
new 3.922623399999793
prep_1 3.8978675999996995
prep_2 3.891471200000069
n = 46800
old 3.9129541999996036
new 3.90457060000017
prep_1 3.898959300000115
prep_2 3.8970162999999047
n = 46900
old 3.915788000000248
new 3.907064099999843
prep_1 3.9117418000000725
prep_2 3.9085613000002013
n = 47000
old 3.9265909000000647
new 3.9636877999996614
prep_1 3.9269423999999162
prep_2 3.9235438999999133
n = 47100
old 3.941105900000366
new 3.9449547999997776
prep_1 3.932247400000051
prep_2 3.9300685000002886
n = 47200
old 3.9442130999996152
new 3.940890400000171
prep_1 3.938866500000131
prep_2 3.939650899999833
n = 47300
old 3.9519435000001977
new 3.947092200000043
prep_1 3.94780929999979
prep_2 3.9372536999999284
n = 47400
old 3.94843069999979
new 3.9485536000001957
prep_1 3.992814400000043
prep_2 4.019134099999974
n = 47500
old 4.024372899999889
new 3.974454600000172
prep_1 3.96380470000031
prep_2 3.960504000000128
n = 47600
old 3.974130200000218
new 3.9695444999997562
prep_1 3.975721799999974
prep_2 3.9739206999997805
n = 47700
old 3.9866526000000704
new 3.9807921999999962
prep_1 3.976093899999796
prep_2 3.97873780000009
n = 47800
old 3.988460600000053
new 4.008407499999976
prep_1 4.013372600000366
prep_2 3.9875043000001824
n = 47900
old 3.998525200000131
new 3.994170799999665
prep_1 4.000729200000023
prep_2 3.9826008
n = 48000
old 4.008132100000239
new 4.00399890000017
prep_1 3.9995061999998143
prep_2 4.002234200000203
n = 48100
old 4.01439180000034
new 4.007666999999856
prep_1 4.020307100000082
prep_2 4.0129361999997855
n = 48200
old 4.061439200000223
new 4.081556999999975
prep_1 4.105508699999973
prep_2 4.075353599999744
n = 48300
old 4.106932499999857
new 4.088259499999822
prep_1 4.028871600000002
prep_2 4.028499200000169
n = 48400
old 4.044762399999854
new 4.0353580000000875
prep_1 4.038836100000026
prep_2 4.036898299999848
n = 48500
old 4.056018900000254
new 4.039837799999987
prep_1 4.0434908000002
prep_2 4.076921100000163
n = 48600
old 4.103743599999689
new 4.102184699999725
prep_1 4.075547100000222
prep_2 4.049631899999895
n = 48700
old 4.0591302999996515
new 4.0568475999998554
prep_1 4.065390400000069
prep_2 4.050122599999668
n = 48800
old 4.072945999999774
new 4.073437999999896
prep_1 4.0679534000000785
prep_2 4.075085499999659
n = 48900
old 4.122740899999826
new 4.079902500000117
prep_1 4.110106200000246
prep_2 4.135309000000234
n = 49000
old 4.089632900000197
new 4.078917400000137
prep_1 4.091438300000391
prep_2 4.094314899999972
n = 49100
old 4.1041652999997495
new 4.094365200000084
prep_1 4.093383500000073
prep_2 4.097586700000193
n = 49200
old 4.1076412000002165
new 4.10175849999996
prep_1 4.096312699999544
prep_2 4.10537419999946
n = 49300
old 4.11721050000051
new 4.111491999999998
prep_1 4.110593299999891
prep_2 4.113217499999337
n = 49400
old 4.12446589999945
new 4.118856400000368
prep_1 4.12097679999988
prep_2 4.118701200000032
n = 49500
old 4.130419100000836
new 4.125436100000115
prep_1 4.124239499999931
prep_2 4.126467299999604
n = 49600
old 4.137037199999213
new 4.132023099999969
prep_1 4.125644300000204
prep_2 4.141400900000008
n = 49700
old 4.1490215000003445
new 4.14423110000007
prep_1 4.146238100000119
prep_2 4.1379243000001225
n = 49800
old 4.1552267000006395
new 4.1519311000001835
prep_1 4.148528599999736
prep_2 4.14856250000048
n = 49900
old 4.170159199999944
new 4.153985800000555
prep_1 4.1607225999996444
prep_2 4.171001000000615
n = 50000
old 4.160389599999689
new 4.165112399999998
prep_1 4.22923179999998
prep_2 4.1805051999999705
n = 50100
old 4.179917200000091
new 4.180218999999852
prep_1 4.17235890000029
prep_2 4.177676299999803
n = 50200
old 4.187604099999589
new 4.183610999999473
prep_1 4.183832699999584
prep_2 4.18739800000003
n = 50300
old 4.1962947000001805
new 4.199817300000177
prep_1 4.191804099999899
prep_2 4.192324199999348
n = 50400
old 4.281077100000402
new 4.24902099999963
prep_1 4.242564600000151
prep_2 4.22823470000003
n = 50500
old 4.257616100000632
new 4.238365399999566
prep_1 4.200928500000373
prep_2 4.2058852000000115
n = 50600
old 4.211377499999799
new 4.213779100000465
prep_1 4.209546699999919
prep_2 4.2090856999993775
n = 50700
old 4.286277100000007
new 4.220332099999723
prep_1 4.2297641999994084
prep_2 4.220163300000422
n = 50800
old 4.24704440000005
new 4.231373600000552
prep_1 4.226282900000115
prep_2 4.225549699999647
n = 50900
old 4.24283000000014
new 4.238237000000481
prep_1 4.230780599999889
prep_2 4.240090000000237
n = 51000
old 4.284141200000704
new 4.244366899999477
prep_1 4.255516700000044
prep_2 4.243046000000504
n = 51100
old 4.262821700000131
new 4.259757399999216
prep_1 4.266340099999979
prep_2 4.254567400000269
n = 51200
old 4.271422699999675
new 4.2623835000003965
prep_1 4.266386899999816
prep_2 4.262893600000098
n = 51300
old 4.277797400000054
new 4.265520900000411
prep_1 4.268536700000368
prep_2 4.270474100000683
n = 51400
old 4.287395000000288
new 4.2778959999996005
prep_1 4.281766400000379
prep_2 4.279046599999674
n = 51500
old 4.294959099999687
new 4.281518199999482
prep_1 4.28564009999991
prep_2 4.283223700000235
n = 51600
old 4.304682599999978
new 4.2889932999996745
prep_1 4.293863400000191
prep_2 4.302870399999847
n = 51700
old 4.313655900000413
new 4.306618100000378
prep_1 4.3045922000001156
prep_2 4.300521799999842
n = 51800
old 4.319335499999397
new 4.309542499999225
prep_1 4.314106800000445
prep_2 4.308531200000289
n = 51900
old 4.321067900000344
new 4.314923300000373
prep_1 4.329750600000807
prep_2 4.326352699999916
n = 52000
old 4.3370936999999685
new 4.330182499999864
prep_1 4.334874999999556
prep_2 4.331697699999495
n = 52100
old 4.346956699999282
new 4.335243100000298
prep_1 4.333555100000012
prep_2 4.3414070000008
n = 52200
old 4.352453999999852
new 4.350229800000307
prep_1 4.349759000000631
prep_2 4.351347699999678
n = 52300
old 4.375425599999289
new 4.3606588000002375
prep_1 4.355475499999557
prep_2 4.355561200000011
n = 52400
old 4.3720862000000125
new 4.36264409999967
prep_1 4.474359600000753
prep_2 4.365489300000263
n = 52500
old 4.421781200000623
new 4.370481299999483
prep_1 4.386245800000324
prep_2 4.372909499999878
n = 52600
old 4.389840899999399
new 4.382784100000208
prep_1 4.379829900000004
prep_2 4.384555900000123
n = 52700
old 4.409650700000384
new 4.393208600000435
prep_1 4.3879501000001255
prep_2 4.384711499999867
n = 52800
old 4.406870200000412
new 4.407194100000197
prep_1 4.4011978999997154
prep_2 4.390522200000305
n = 52900
old 4.409733999999844
new 4.408063900000343
prep_1 4.401941799999804
prep_2 4.413180399999874
n = 53000
old 4.416619200000241
new 4.413081799999418
prep_1 4.411035400000401
prep_2 4.413607299999967
n = 53100
old 4.426379400000769
new 4.415204199999607
prep_1 4.420828600000277
prep_2 4.481075499999861
n = 53200
old 4.4893622999998115
new 4.476749800000107
prep_1 4.440572200000133
prep_2 4.426292600000124
n = 53300
old 4.4390034999996715
new 4.438053599999876
prep_1 4.441609299999982
prep_2 4.440818000000036
n = 53400
old 4.4554277999995975
new 4.44460909999998
prep_1 4.448008300000765
prep_2 4.447124299999814
n = 53500
old 4.476744499999768
new 4.513959099999738
prep_1 4.457638799999586
prep_2 4.454481499999929
n = 53600
old 4.471838100000241
new 4.465553699999873
prep_1 4.467450699999972
prep_2 4.459618800000499
n = 53700
old 4.477823299999727
new 4.470407300000261
prep_1 4.4801557000000685
prep_2 4.477211100000204
n = 53800
old 4.490368899999339
new 4.488330199999837
prep_1 4.482195100000354
prep_2 4.487179300000207
n = 53900
old 4.502954200000204
new 4.491390400000455
prep_1 4.4982466999999815
prep_2 4.48967889999949
n = 54000
old 4.510365600000114
new 4.499960900000588
prep_1 4.500398600000153
prep_2 4.50067190000027
n = 54100
old 4.517831800000749
new 4.50997020000068
prep_1 4.54582019999998
prep_2 4.511035900000024
n = 54200
old 4.553489300000365
new 4.53877089999969
prep_1 4.520415099999809
prep_2 4.516204200000175
n = 54300
old 4.540623500000038
new 4.520175999999992
prep_1 4.528161000000182
prep_2 4.529015699999945
n = 54400
old 4.539024400000017
new 4.536756700000296
prep_1 4.532666099999915
prep_2 4.534992500000044
n = 54500
old 4.55828399999973
new 4.595044899999266
prep_1 4.5585011999992275
prep_2 4.543794500000331
n = 54600
old 4.557008900000255
new 4.543920600000092
prep_1 4.541217599999982
prep_2 4.555478899999798
n = 54700
old 4.555580000000191
new 4.550783599999704
prep_1 4.564663599999221
prep_2 4.550768099999914
n = 54800
old 4.575239299999339
new 4.563993900000241
prep_1 4.563862899999549
prep_2 4.571085100000346
n = 54900
old 4.581914700000198
new 4.57432770000014
prep_1 4.569483199999922
prep_2 4.572204000000056
n = 55000
old 4.594383999999991
new 4.579616899999564
prep_1 4.603581100000156
prep_2 4.581402000000708
n = 55100
old 4.603967500000181
new 4.596803600000385
prep_1 4.59036549999928
prep_2 4.585360400000354
n = 55200
old 4.605327600000237
new 4.59722789999978
prep_1 4.601026399999682
prep_2 4.59185079999952
n = 55300
old 4.609180800000104
new 4.612137199999779
prep_1 4.606091800000286
prep_2 4.610179300000709
n = 55400
old 4.62733389999994
new 4.617289400000118
prep_1 4.618543300000056
prep_2 4.611376800000471
n = 55500
old 4.705244599999787
new 4.688520199999402
prep_1 4.612167600000248
prep_2 4.627332200000637
n = 55600
old 4.641051600000537
new 4.632293499999832
prep_1 4.63089779999973
prep_2 4.6318216999998185
n = 55700
old 4.650343499999508
new 4.645674600000348
prep_1 4.639187100000527
prep_2 4.707036900000276
n = 55800
old 4.6566631000005145
new 4.652919600000132
prep_1 4.653868800000055
prep_2 4.649610099999336
n = 55900
old 4.664806200000385
new 4.648619900000085
prep_1 4.662151700000322
prep_2 4.660213499999372
n = 56000
old 4.671335899999576
new 4.672275900000386
prep_1 4.666057200000068
prep_2 4.657258899999761
n = 56100
old 4.686650199999349
new 4.699466600000051
prep_1 4.710036599999512
prep_2 4.771136999999726
n = 56200
old 4.744335000000319
new 4.736757900000157
prep_1 4.685182500000337
prep_2 4.681291800000508
n = 56300
old 4.698263600000246
new 4.689318700000513
prep_1 4.688439099999414
prep_2 4.694388099999742
n = 56400
old 4.727457199999662
new 4.698571900000388
prep_1 4.695845199999894
prep_2 4.719121399999494
n = 56500
old 4.723989199999778
new 4.710516699999971
prep_1 4.7054072000000815
prep_2 4.705873299999439
n = 56600
old 4.746839899999941
new 4.731377700000849
prep_1 4.738481200000024
prep_2 4.717835600000399
n = 56700
old 4.73797470000045
new 4.720703500000127
prep_1 4.718351900000016
prep_2 4.776868699999795
n = 56800
old 4.728426399999989
new 4.743724100000691
prep_1 4.738091400000485
prep_2 4.72628689999965
n = 56900
old 4.752711799999815
new 4.736835099999553
prep_1 4.743010099999992
prep_2 4.736231500000031
n = 57000
old 4.757594800000334
new 4.756276699999944
prep_1 4.753870499999721
prep_2 4.74375339999915
n = 57100
old 4.764468899999883
new 4.767311200000222
prep_1 4.762610799999493
prep_2 4.756650499999523
n = 57200
old 4.770884399999886
new 4.769067500000347
prep_1 4.767731500000082
prep_2 4.7688859999998385
n = 57300
old 4.779650799999217
new 4.773780699999406
prep_1 4.775467299999946
prep_2 4.818453500000032
n = 57400
old 4.796102500000416
new 4.785735399999794
prep_1 4.791904300000169
prep_2 4.788720399999875
n = 57500
old 4.799514199999976
new 4.793996800000059
prep_1 4.793164999999135
prep_2 4.788246699999945
n = 57600
old 4.807158300000083
new 4.803214699999444
prep_1 4.795640100000128
prep_2 4.804195000000618
n = 57700
old 4.814945999999509
new 4.876279999999497
prep_1 4.809956600000078
prep_2 4.8035140000001775
n = 57800
old 4.82560839999951
new 4.813364399999955
prep_1 4.811733399999866
prep_2 4.808764699999301
n = 57900
old 4.8253167999992
new 4.830519699999968
prep_1 4.8238883000003625
prep_2 4.8233517999997275
n = 58000
old 4.846169500000542
new 4.859843300000648
prep_1 4.835505099999864
prep_2 4.866176000000451
n = 58100
old 4.8500828999995065
new 4.8426370999995925
prep_1 4.845143699999426
prep_2 4.842327299999852
n = 58200
old 4.859361800000443
new 4.854639199999838
prep_1 4.8527813999999125
prep_2 4.853063400000792
n = 58300
old 4.867552099999557
new 4.895273199999792
prep_1 4.918117100000018
prep_2 4.920664000000215
n = 58400
old 4.934316400000171
new 4.863838399999622
prep_1 4.867182099999809
prep_2 4.86892110000008
n = 58500
old 4.872914200000196
new 4.874468999999408
prep_1 4.873130900000433
prep_2 4.875365099999726
n = 58600
old 4.888252400000056
new 4.8790594000001875
prep_1 4.885861499999919
prep_2 4.892357100000481
n = 58700
old 4.899748900000304
new 4.889081199999964
prep_1 4.885315499999706
prep_2 4.8922442000002775
n = 58800
old 4.915126799999598
new 4.906906500000332
prep_1 4.8962375999999495
prep_2 4.894546600000467
n = 58900
old 4.964192800000092
new 4.996358700000201
prep_1 4.963827300000048
prep_2 5.010679899999559
n = 59000
old 4.968647100000453
new 4.915162199999941
prep_1 4.92095209999934
prep_2 4.927289000000201
n = 59100
old 4.931729900000391
new 4.924332399999912
prep_1 4.91373990000011
prep_2 4.916263099999924
n = 59200
old 4.93537600000036
new 4.934656999999788
prep_1 4.964728200000536
prep_2 4.98821450000014
n = 59300
old 5.008218900000429
new 5.03296440000031
prep_1 4.93773069999952
prep_2 4.93999840000015
n = 59400
old 4.9587234000000535
new 4.952058199999556
prep_1 4.946050399999876
prep_2 4.955672800000684
n = 59500
old 4.964597900000626
new 4.962499799999932
prep_1 4.962046300000111
prep_2 4.998581599999852
n = 59600
old 4.984762500000215
new 4.968213599999217
prep_1 4.97211789999983
prep_2 4.958279199999197
n = 59700
old 4.982963899999959
new 4.9728948000001765
prep_1 4.9955198999996355
prep_2 4.979816600000049
n = 59800
old 4.990158700000393
new 4.984616900000219
prep_1 5.027721999999812
prep_2 4.97953890000008
n = 59900
old 4.99460900000031
new 4.996009000000413
prep_1 4.986054099999819
prep_2 4.9848920000004
n = 60000
old 5.011106599999948
new 5.018150900000364
prep_1 5.033659300000181
prep_2 5.003788099999838
n = 60100
old 5.015715200000159
new 5.007912999999462
prep_1 5.002407900000435
prep_2 5.004856800000198
n = 60200
old 5.024809699999423
new 5.021317900000213
prep_1 5.0190363000001526
prep_2 5.011572899999919
n = 60300
old 5.0428107000007
new 5.025518600000396
prep_1 5.030827599999611
prep_2 5.034219399999529
n = 60400
old 5.047436200000448
new 5.112034199999471
prep_1 5.038320499999827
prep_2 5.033514400000058
n = 60500
old 5.1689719000005425
new 5.058579599999575
prep_1 5.041780200000176
prep_2 5.123287899999923
n = 60600
old 5.048538299999564
new 5.04909730000054
prep_1 5.059693100000004
prep_2 5.055055400000128
n = 60700
old 5.056626500000675
new 5.061665400000493
prep_1 5.057985799999187
prep_2 5.055863099999442
n = 60800
old 5.075851400000829
new 5.065235500000199
prep_1 5.06227409999974
prep_2 5.070800700000291
n = 60900
old 5.078240599999845
new 5.07730520000041
prep_1 5.069482899999457
prep_2 5.0796143999996275
n = 61000
old 5.096999599999435
new 5.083775799999785
prep_1 5.094044600000416
prep_2 5.0802206999997
n = 61100
old 5.103194600000279
new 5.089780299999802
prep_1 5.0843064000000595
prep_2 5.093760200000361
n = 61200
old 5.124536699999226
new 5.101591200000257
prep_1 5.09804239999994
prep_2 5.106327899999997
n = 61300
old 5.113345099999606
new 5.123011499999848
prep_1 5.187754700000369
prep_2 5.18445789999987
n = 61400
old 5.149935000000369
new 5.122272300000077
prep_1 5.11157699999967
prep_2 5.114414800000304
n = 61500
old 5.134358299999803
new 5.124061800000163
prep_1 5.124611499999446
prep_2 5.126649400000133
n = 61600
old 5.1475971999998364
new 5.194066799999746
prep_1 5.1762392000000546
prep_2 5.132949399999234
n = 61700
old 5.15025759999935
new 5.140569199999845
prep_1 5.14262940000026
prep_2 5.141058000000157
n = 61800
old 5.151507700000366
new 5.150161699999444
prep_1 5.152111299999888
prep_2 5.177542299999914
n = 61900
old 5.167649999999412
new 5.160502899999301
prep_1 5.176832600000125
prep_2 5.1556745999996565
n = 62000
old 5.1813402000007045
new 5.168190200000026
prep_1 5.174144699999488
prep_2 5.162349900000663
n = 62100
old 5.179155200000423
new 5.166206900000361
prep_1 5.1854513999996925
prep_2 5.17694930000016
n = 62200
old 5.204703399999744
new 5.193753300000026
prep_1 5.187644299999192
prep_2 5.1802629000003435
n = 62300
old 5.199399600000106
new 5.189122699999643
prep_1 5.1885081000000355
prep_2 5.187426200000118
n = 62400
old 5.208415000000059
new 5.195730100000219
prep_1 5.2119887999997445
prep_2 5.200148200000513
n = 62500
old 5.229636299999584
new 5.213078699999642
prep_1 5.209947399999692
prep_2 5.205355799999779
n = 62600
old 5.220454000000245
new 5.2143175999999585
prep_1 5.222141600000214
prep_2 5.211284599999999
n = 62700
old 5.234936899999411
new 5.216369899999336
prep_1 5.221094300000004
prep_2 5.234282200000052
n = 62800
old 5.2371521999994
new 5.231492300000355
prep_1 5.237382499999512
prep_2 5.225447599999825
n = 62900
old 5.2552739000002475
new 5.238984499999788
prep_1 5.239907999999559
prep_2 5.238327700000809
n = 63000
old 5.258532799999557
new 5.251597999999831
prep_1 5.249012100000073
prep_2 5.251605299999937
n = 63100
old 5.2677549
new 5.257304900000236
prep_1 5.252847400000064
prep_2 5.261823699999695
n = 63200
old 5.2720800999995845
new 5.264943400000448
prep_1 5.273069299999406
prep_2 5.263119999999617
n = 63300
old 5.272921200000383
new 5.339531999999963
prep_1 5.30768050000006
prep_2 5.354325499999504
n = 63400
old 5.35361709999961
new 5.280894900000021
prep_1 5.286967600000025
prep_2 5.282645500000399
n = 63500
old 5.29406950000066
new 5.295624399999724
prep_1 5.295991999999387
prep_2 5.291401800000131
n = 63600
old 5.303060199999891
new 5.326378499999919
prep_1 5.309790900000735
prep_2 5.297634900000048
n = 63700
old 5.310998199999631
new 5.300985699999728
prep_1 5.313219000000572
prep_2 5.303675799999837
n = 63800
old 5.329418700000133
new 5.312147800000275
prep_1 5.317189399999734
prep_2 5.316376999999193
n = 63900
old 5.334767000000284
new 5.325498700000026
prep_1 5.318601699999817
prep_2 5.329844900000353
n = 64000
old 5.3392759999997
new 5.334750200000599
prep_1 5.3355622000008225
prep_2 5.327589200000148
n = 64100
old 5.351960099999815
new 5.339866100000108
prep_1 5.3425828999997975
prep_2 5.337331100000483
n = 64200
old 5.396655700000338
new 5.430376100000103
prep_1 5.373276600000281
prep_2 5.339637799999764
n = 64300
old 5.374699899999541
new 5.35327849999976
prep_1 5.357900599999994
prep_2 5.355337099999815
n = 64400
old 5.371671200000492
new 5.360916399999951
prep_1 5.362288100000114
prep_2 5.377511400000003
n = 64500
old 5.389230099999622
new 5.377316600000086
prep_1 5.371445099999619
prep_2 5.369021900000007
n = 64600
old 5.397726500000317
new 5.385245399999803
prep_1 5.381907400000273
prep_2 5.383195999999771
n = 64700
old 5.392466300000706
new 5.494517199999791
prep_1 5.418494200000168
prep_2 5.468851800000266
n = 64800
old 5.479816000000028
new 5.396681300000637
prep_1 5.40211200000067
prep_2 5.394628699999885
n = 64900
old 5.4198241999993115
new 5.410341099999641
prep_1 5.412732400000095
prep_2 5.4008592999998655
n = 65000
old 5.427163599999403
new 5.412648599999557
prep_1 5.413818699999865
prep_2 5.412387200000012
n = 65100
old 5.439597500000673
new 5.423611500000334
prep_1 5.432060900000579
prep_2 5.4183672999997725
n = 65200
old 5.443947300000218
new 5.422497499999736
prep_1 5.437279899999339
prep_2 5.424371200000678
n = 65300
old 5.4950450999995155
new 5.513267199999973
prep_1 5.445761599999969
prep_2 5.435559000000467
n = 65400
old 5.451741999999285
new 5.442943200000627
prep_1 5.452711300000374
prep_2 5.44456640000044
n = 65500
old 5.469343599999775
new 5.455010699999548
prep_1 5.4609905999996045
prep_2 5.458866300000409
n = 65600
old 5.558898499999486
new 5.547407199999725
prep_1 5.534761400000207
prep_2 5.520871900000202
n = 65700
old 5.486020900000767
new 5.466699599999629
prep_1 5.479168500000014
prep_2 5.475402000000031
n = 65800
old 5.5026175000002695
new 5.486837899999955
prep_1 5.518998999999894
prep_2 5.5695661999998265
n = 65900
old 5.578170199999477
new 5.527463600000374
prep_1 5.487783300000046
prep_2 5.493184300000394
n = 66000
old 5.5089622000004965
new 5.496668100000534
prep_1 5.508743999999751
prep_2 5.496547600000667
n = 66100
old 5.558089300000574
new 5.55496359999961
prep_1 5.578432999999677
prep_2 5.514025999999831
n = 66200
old 5.520998599999984
new 5.520257099999981
prep_1 5.522169300000314
prep_2 5.513841599999978
n = 66300
old 5.5346214999999575
new 5.526110000000699
prep_1 5.531406099999913
prep_2 5.5153598999995666
n = 66400
old 5.558856200000264
new 5.532183899999836
prep_1 5.527439399999821
prep_2 5.531241900000168
n = 66500
old 5.550606400000106
new 5.531234099999892
prep_1 5.543591900000138
prep_2 5.535788299999695
n = 66600
old 5.557075700000496
new 5.549927000000025
prep_1 5.55159409999942
prep_2 5.597852199999579
n = 66700
old 5.632880699999987
new 5.622155600000042
prep_1 5.576938700000028
prep_2 5.559988500000145
n = 66800
old 5.581950800000413
new 5.567192299999988
prep_1 5.565097600000627
prep_2 5.56890470000053
n = 66900
old 5.585941299999831
new 5.590380999999979
prep_1 5.589926900000137
prep_2 5.581820200000038
n = 67000
old 5.5896451999997225
new 5.581068000000414
prep_1 5.58670710000024
prep_2 5.584934599999542
n = 67100
old 5.602718399999503
new 5.586131199999727
prep_1 5.593976199999815
prep_2 5.587179900000592
n = 67200
old 5.611190200000237
new 5.5957042
prep_1 5.595488599999953
prep_2 5.603320000000167
n = 67300
old 5.615254400000595
new 5.6087055999996664
prep_1 5.607206599999699
prep_2 5.609302000000753
n = 67400
old 5.624070500000016
new 5.61504640000021
prep_1 5.694496400000389
prep_2 5.670777300000736
n = 67500
old 5.7140481999995245
new 5.674631799999588
prep_1 5.617295199999717
prep_2 5.631066300000384
n = 67600
old 5.626308300000346
new 5.630342099999325
prep_1 5.631615999999667
prep_2 5.634856600000603
n = 67700
old 5.654866399999264
new 5.644525599999724
prep_1 5.721566000000166
prep_2 5.7106910000002244
n = 67800
old 5.652834999999868
new 5.644094700000096
prep_1 5.645088999999643
prep_2 5.657332499999939
n = 67900
old 5.673107200000231
new 5.652536200000213
prep_1 5.661329800000203
prep_2 5.657346199999665
n = 68000
old 5.679666099999849
new 5.674221600000237
prep_1 5.669951900000342
prep_2 5.6680008000003
n = 68100
old 5.678291300000637
new 5.67326249999951
prep_1 5.682172099999661
prep_2 5.6735102999991796
n = 68200
old 5.695844500000021
new 5.682034100000237
prep_1 5.691764999999577
prep_2 5.68697819999943
n = 68300
old 5.699663999999757
new 5.690465599999698
prep_1 5.700458999999682
prep_2 5.692277899999681
n = 68400
old 5.712039000000004
new 5.69846409999991
prep_1 5.6986634000004415
prep_2 5.705597399999533
n = 68500
old 5.723445200000242
new 5.740982299999814
prep_1 5.799278299999969
prep_2 5.783194999999978
n = 68600
old 5.720766900000854
new 5.717712900000151
prep_1 5.722881300000154
prep_2 5.709827099999529
n = 68700
old 5.733363599999393
new 5.7286457999998674
prep_1 5.725824999999531
prep_2 5.776266299999406
n = 68800
old 5.747378900000513
new 5.742173900000125
prep_1 5.732749100000547
prep_2 5.733143100000234
n = 68900
old 5.755570900000748
new 5.754908500000056
prep_1 5.744607600000563
prep_2 5.744342599999982
n = 69000
old 5.756051600000319
new 5.759008399999402
prep_1 5.748580000000402
prep_2 5.752297199999703
n = 69100
old 5.7711443999996845
new 5.756276900000557
prep_1 5.778530900000078
prep_2 5.7587447999994765
n = 69200
old 5.776285899999493
new 5.772307600000204
prep_1 5.770558100000017
prep_2 5.766333099999429
n = 69300
old 5.784341699999459
new 5.779355399999986
prep_1 5.774884999999813
prep_2 5.780443499999819
n = 69400
old 5.797493599999143
new 5.78255259999969
prep_1 5.792225600000165
prep_2 5.788752899999963
n = 69500
old 5.797226799999407
new 5.794510300000184
prep_1 5.931164800000261
prep_2 5.827909999999974
n = 69600
old 5.848888299999999
new 5.805022999999892
prep_1 5.813236599999982
prep_2 5.82015919999958
n = 69700
old 5.820008400000006
new 5.805752500000381
prep_1 5.806455500000084
prep_2 5.8041597000001275
n = 69800
old 5.82118730000002
new 5.85258580000027
prep_1 5.902637199999845
prep_2 5.898849400000472
n = 69900
old 5.932702300000528
new 5.918783400000393
prep_1 5.833948200001032
prep_2 5.829243700000006
n = 70000
old 5.843397900000127
new 5.831469700000525
prep_1 5.9311744000006
prep_2 5.8597393999989436
n = 70100
old 5.858257299998513
new 5.842756900001405
prep_1 5.848695700000462
prep_2 5.837003900000127
n = 70200
old 5.8554769000002125
new 5.848441100000855
prep_1 5.84768620000068
prep_2 5.851295700000264
n = 70300
old 5.865623499999856
new 5.860585100001117
prep_1 5.86527550000028
prep_2 5.864665499999319
n = 70400
old 5.881228100000953
new 5.8695324000000255
prep_1 5.864064200000939
prep_2 5.874473700001545
n = 70500
old 5.88155899999947
new 5.863496899999518
prep_1 5.8752595000005385
prep_2 5.876827300000514
n = 70600
old 5.9134438000000955
new 5.898421199999575
prep_1 5.8851260999999795
prep_2 5.876186900000903
n = 70700
old 5.900150499999654
new 5.916160999999192
prep_1 5.89552089999961
prep_2 5.887385900001391
n = 70800
old 5.902862799999639
new 5.921857299999829
prep_1 5.904253099999551
prep_2 5.897734300000593
n = 70900
old 5.9169277000000875
new 5.9102867000001424
prep_1 5.909721699999864
prep_2 5.9103979999999865
n = 71000
old 5.94610239999929
new 5.921981900000901
prep_1 5.9134287999986554
prep_2 5.920808999999281
n = 71100
old 5.933392700000695
new 5.930214199999682
prep_1 5.921391899999435
prep_2 5.923476599999049
n = 71200
old 5.941850699999122
new 5.93099280000024
prep_1 5.933286499999667
prep_2 5.93700650000028
n = 71300
old 5.947150500000134
new 5.981202900000426
prep_1 5.963295200001085
prep_2 5.964968999998746
n = 71400
old 6.002655600001162
new 5.953606900000523
prep_1 5.957048199999917
prep_2 5.9419476999992185
n = 71500
old 5.965847499999654
new 5.963531500001409
prep_1 5.952694700001302
prep_2 5.963542800000141
n = 71600
old 6.014179499999955
new 6.079447599999185
prep_1 6.063272899998992
prep_2 6.021970300000248
n = 71700
old 6.006887800000186
new 5.974295199999688
prep_1 5.978054600000178
prep_2 5.969254399999045
n = 71800
old 5.994005200000174
new 5.98687499999869
prep_1 6.04710569999952
prep_2 6.045264700000189
n = 71900
old 6.06891369999903
new 6.004942199999277
prep_1 5.99079619999975
prep_2 5.997432800000752
n = 72000
old 6.009588500000973
new 6.008147700000336
prep_1 5.998559499999828
prep_2 5.997136399999363
n = 72100
old 6.031184700001177
new 6.039784799999325
prep_1 6.004927199999656
prep_2 6.009106500001508
n = 72200
old 6.023969500000021
new 6.028616600000532
prep_1 6.022333200000503
prep_2 6.011936400000195
n = 72300
old 6.038144699999975
new 6.018362699998761
prep_1 6.024831400000039
prep_2 6.025285100000474
n = 72400
old 6.051860699999452
new 6.029493899999579
prep_1 6.0280039999997825
prep_2 6.034576699999889
n = 72500
old 6.054066100001364
new 6.0562255999993795
prep_1 6.052716299998792
prep_2 6.081876199999897
n = 72600
old 6.053442100001121
new 6.055001800001264
prep_1 6.053540400000202
prep_2 6.047250300000087
n = 72700
old 6.073509600000762
new 6.048944699999993
prep_1 6.060393499999918
prep_2 6.058441799999855
n = 72800
old 6.075129700000616
new 6.065749000001233
prep_1 6.106260699998529
prep_2 6.129786299999978
n = 72900
old 6.079028599999219
new 6.0714753000011115
prep_1 6.081175200000871
prep_2 6.077406000000337
n = 73000
old 6.097034300000814
new 6.090926300001229
prep_1 6.0787944000003336
prep_2 6.084233200001108
n = 73100
old 6.151253399999405
new 6.16620359999979
prep_1 6.14941970000109
prep_2 6.176253200001156
n = 73200
old 6.138695199999347
new 6.113260200001605
prep_1 6.152074499999799
prep_2 6.109294300000329
n = 73300
old 6.125552999999854
new 6.109675499999867
prep_1 6.122974599998997
prep_2 6.13549680000142
n = 73400
old 6.146502400000827
new 6.113513899999816
prep_1 6.1116086000001815
prep_2 6.109778100000767
n = 73500
old 6.132037299999865
new 6.121805599999789
prep_1 6.1223922000008315
prep_2 6.124938999999358
n = 73600
old 6.195543499999985
new 6.1620010000006005
prep_1 6.131866900001114
prep_2 6.1320027999991
n = 73700
old 6.150894500000504
new 6.140739000000394
prep_1 6.140898199999356
prep_2 6.14352609999878
n = 73800
old 6.209010200000193
new 6.159262999999555
prep_1 6.145492699999522
prep_2 6.16215849999935
n = 73900
old 6.155934700000216
new 6.147577899999305
prep_1 6.1571607000005315
prep_2 6.149503900000127
n = 74000
old 6.1780987000001915
new 6.16805899999963
prep_1 6.160498999999618
prep_2 6.166135999999824
n = 74100
old 6.1882538000008935
new 6.167239500000505
prep_1 6.177239100001316
prep_2 6.168488500001331
n = 74200
old 6.19196440000087
new 6.18269490000057
prep_1 6.202923100001499
prep_2 6.196196199998667
n = 74300
old 6.195023599999331
new 6.196962899999562
prep_1 6.200333599999794
prep_2 6.1977992000011
n = 74400
old 6.202318300000115
new 6.204954300001191
prep_1 6.197943200000736
prep_2 6.195451700001286
n = 74500
old 6.229260199999771
new 6.211739200000011
prep_1 6.2056322999997064
prep_2 6.210678100000223
n = 74600
old 6.241151100000934
new 6.2255511000003025
prep_1 6.2120634999992035
prep_2 6.215133899999273
n = 74700
old 6.231801600000836
new 6.23491439999998
prep_1 6.223617499999818
prep_2 6.248649099999966
n = 74800
old 6.2381963999996515
new 6.233845400000064
prep_1 6.2286564000005455
prep_2 6.238407400000142
n = 74900
old 6.250429300000178
new 6.254301400000259
prep_1 6.237436400000661
prep_2 6.253791299999648
n = 75000
old 6.256019499998729
new 6.382135199999539
prep_1 6.3274587000014435
prep_2 6.361148600000888
n = 75100
old 6.261975999999777
new 6.2600179000000935
prep_1 6.261045200000808
prep_2 6.260515899999518
n = 75200
old 6.27550969999902
new 6.307239499999923
prep_1 6.263492800000677
prep_2 6.270233700000972
n = 75300
old 6.29557399999976
new 6.281275800000003
prep_1 6.2811093000000255
prep_2 6.253810500000327
n = 75400
old 6.290408099999695
new 6.283485300000393
prep_1 6.300138599999627
prep_2 6.273811700000806
n = 75500
old 6.295970000001034
new 6.2989689000005455
prep_1 6.333756699999867
prep_2 6.292557799999486
n = 75600
old 6.308682200000476
new 6.298364500000389
prep_1 6.305171399999381
prep_2 6.29808359999879
n = 75700
old 6.326973299999736
new 6.310236999999688
prep_1 6.346628399998735
prep_2 6.436998799999856
n = 75800
old 6.426283599999806
new 6.317658399999345
prep_1 6.317964800000482
prep_2 6.310521000001245
n = 75900
old 6.334625799998321
new 6.328757299999779
prep_1 6.3216061999992235
prep_2 6.323389600000155
n = 76000
old 6.460920900000929
new 6.340522799999235
prep_1 6.3374972000001435
prep_2 6.3291710000012245
n = 76100
old 6.343613200000618
new 6.342248799999652
prep_1 6.3433887000010145
prep_2 6.321773399999074
n = 76200
old 6.492808700000751
new 6.445109400001456
prep_1 6.366919500000222
prep_2 6.352739899999506
n = 76300
old 6.357981500001188
new 6.36497640000016
prep_1 6.358560399999988
prep_2 6.351516800001264
n = 76400
old 6.380415899999207
new 6.369571900000665
prep_1 6.3744028999990405
prep_2 6.358791200000269
n = 76500
old 6.390123899998798
new 6.377888699998948
prep_1 6.374077600001328
prep_2 6.366935000000012
n = 76600
old 6.399838500001351
new 6.38416640000105
prep_1 6.386549800001376
prep_2 6.379069999999047
n = 76700
old 6.405043500000829
new 6.392801199999667
prep_1 6.386487399999169
prep_2 6.384622600000512
n = 76800
old 6.411409000000276
new 6.3997992999993585
prep_1 6.397879299998749
prep_2 6.4022815999996965
n = 76900
old 6.420371899999736
new 6.4245207999993
prep_1 6.405955399999584
prep_2 6.411262400000851
n = 77000
old 6.420433299999786
new 6.417712500000562
prep_1 6.415584500000477
prep_2 6.417232400001012
n = 77100
old 6.450419700000566
new 6.426506800000425
prep_1 6.427138200000627
prep_2 6.480555399999503
n = 77200
old 6.508233799999289
new 6.519121299999824
prep_1 6.434502900001462
prep_2 6.425467799999751
n = 77300
old 6.448452200000247
new 6.449126100000285
prep_1 6.446030400000382
prep_2 6.500655899999401
n = 77400
old 6.468720200000462
new 6.564790500000527
prep_1 6.444726800000353
prep_2 6.453524300000936
n = 77500
old 6.477575299999444
new 6.460325299998658
prep_1 6.452655700000832
prep_2 6.453646500000104
n = 77600
old 6.479974099998799
new 6.4909511000005296
prep_1 6.456920500000706
prep_2 6.4672226999991835
n = 77700
old 6.47745439999926
new 6.473400500000935
prep_1 6.47415010000077
prep_2 6.472521399999096
n = 77800
old 6.493324000000939
new 6.481931299998905
prep_1 6.5032794999988255
prep_2 6.555405499999324
n = 77900
old 6.562252599998828
new 6.58557219999966
prep_1 6.495659700000033
prep_2 6.484530199999426
n = 78000
old 6.504401099999086
new 6.501380699999572
prep_1 6.493906800000332
prep_2 6.500098700000308
n = 78100
old 6.583542200000011
new 6.580025699999169
prep_1 6.5195361000005505
prep_2 6.504294699998354
n = 78200
old 6.52609560000019
new 6.515637399999832
prep_1 6.52074729999913
prep_2 6.511504899999636
n = 78300
old 6.552758499999982
new 6.6109878999996
prep_1 6.537260700000843
prep_2 6.519161700000041
n = 78400
old 6.542773999999554
new 6.527784699999756
prep_1 6.53725569999915
prep_2 6.53301570000076
n = 78500
old 6.5523988000004465
new 6.587815499999124
prep_1 6.558995099998356
prep_2 6.545527199999924
n = 78600
old 6.596094099999391
new 6.53829290000067
prep_1 6.547016200000144
prep_2 6.555295199999819
n = 78700
old 6.5675219999993715
new 6.551571100000729
prep_1 6.563733999999386
prep_2 6.555188199999975
n = 78800
old 6.5715130000007775
new 6.565594100000453
prep_1 6.57197509999969
prep_2 6.560384500000509
n = 78900
old 6.580395199998748
new 6.58169259999886
prep_1 6.576501999999891
prep_2 6.575028500001281
n = 79000
old 6.596659999999247
new 6.667187700000795
prep_1 6.593016300001182
prep_2 6.591152000000875
n = 79100
old 6.600782900000922
new 6.5893282999986695
prep_1 6.593518100000438
prep_2 6.581862400000318
n = 79200
old 6.607934400000886
new 6.605450999999448
prep_1 6.682200999999623
prep_2 6.71929739999905
n = 79300
old 6.694376399998873
new 6.664088699999411
prep_1 6.61481140000069
prep_2 6.612313199999335
n = 79400
old 6.6281646999996156
new 6.627888400000302
prep_1 6.624956099998599
prep_2 6.607810999999856
n = 79500
old 6.640148800001043
new 6.619223800000327
prep_1 6.625954799999818
prep_2 6.616716099999394
n = 79600
old 6.634935300000507
new 6.630334299999959
prep_1 6.718413399999918
prep_2 6.673590099999274
n = 79700
old 6.660392399999182
new 6.643551400000433
prep_1 6.648614900001121
prep_2 6.644448700000794
n = 79800
old 6.647539899999174
new 6.648792399999365
prep_1 6.653399499999068
prep_2 6.653111699999499
n = 79900
old 6.698739999999816
new 6.664472300000853
prep_1 6.6487922000014805
prep_2 6.672704099999464
n = 80000
old 6.675015799999528
new 6.661497600000075
prep_1 6.6681640000006155
prep_2 6.662735200001407
n = 80100
old 6.6910519000011845
new 6.704699199999595
prep_1 6.678606999999829
prep_2 6.690119100001539
n = 80200
old 6.692364700000326
new 6.6938122999999905
prep_1 6.6868184999984805
prep_2 6.703321200000573
n = 80300
old 6.709070000000793
new 6.697099700000763
prep_1 6.698781600000075
prep_2 6.697935199999847
n = 80400
old 6.698700900000404
new 6.6974465000002965
prep_1 6.6985476999998355
prep_2 6.699015599999257
n = 80500
old 6.714863100000002
new 6.708626000001459
prep_1 6.71697739999945
prep_2 6.712489599998662
n = 80600
old 6.7989077000002
new 6.757498699998905
prep_1 6.723982299999989
prep_2 6.718964600000618
n = 80700
old 6.751230300000316
new 6.72131040000022
prep_1 6.723942000000534
prep_2 6.808556999998473
n = 80800
old 6.741219099998489
new 6.745230200000151
prep_1 6.734682000000248
prep_2 6.728891500000827
n = 80900
old 6.746560800000225
new 6.734226399999898
prep_1 6.7506663000003755
prep_2 6.737358799999129
n = 81000
old 6.7620836999994935
new 6.771143899999515
prep_1 6.748686799999632
prep_2 6.758661700001539
n = 81100
old 6.771168100000068
new 6.760881199999858
prep_1 6.75517949999994
prep_2 6.761015599999155
n = 81200
old 6.7799434999997175
new 6.771200099999987
prep_1 6.7682566000003135
prep_2 6.779719399999522
n = 81300
old 6.78077999999914
new 6.782014399999753
prep_1 6.771291199998814
prep_2 6.766461299999719
n = 81400
old 6.801036300001215
new 6.78294840000126
prep_1 6.80651239999861
prep_2 6.837417700000515
n = 81500
old 6.89446240000143
new 6.874092699999892
prep_1 6.8246292999992875
prep_2 6.787693300000683
n = 81600
old 6.7998093999995035
new 6.801835199999914
prep_1 6.7974677000001975
prep_2 6.803104799999346
n = 81700
old 6.8832323000006
new 6.895702699999674
prep_1 6.8249775000003865
prep_2 6.805952399998205
n = 81800
old 6.818422299998929
new 6.8140954000009515
prep_1 6.818000399998709
prep_2 6.8752531000009185
n = 81900
old 6.8589239999982965
new 6.893113500000254
prep_1 6.864336299999195
prep_2 6.823334900000191
n = 82000
old 6.837951200001044
new 6.846128699999099
prep_1 6.826418000000558
prep_2 6.829973699999755
n = 82100
old 6.856547800000044
new 6.8648998999997275
prep_1 6.891115100001116
prep_2 6.906348900000012
n = 82200
old 6.921639899999718
new 6.86280540000007
prep_1 6.851332199999888
prep_2 6.857861700000285
n = 82300
old 6.853229799999099
new 6.853332500000761
prep_1 6.860916899999211
prep_2 6.8603626000003715
n = 82400
old 6.8807661999999254
new 6.861165899999833
prep_1 6.873928100001649
prep_2 6.8843959999994695
n = 82500
old 6.88918779999949
new 6.872630400001071
prep_1 6.870619799999986
prep_2 6.8752497999994375
n = 82600
old 6.899541599999793
new 6.877653699999428
prep_1 6.879297499999666
prep_2 6.881697800001348
n = 82700
old 6.905952099999922
new 6.882740500001091
prep_1 6.892791500000385
prep_2 6.90315819999887
n = 82800
old 6.929959199998848
new 6.90105179999955
prep_1 6.907825500000399
prep_2 6.898111800001061
n = 82900
old 6.91789880000033
new 6.915545399999246
prep_1 6.907940299999609
prep_2 6.95429939999849
n = 83000
old 6.9637302000010095
new 6.955642599999919
prep_1 6.929396800000177
prep_2 6.918444700000691
n = 83100
old 6.9376288000003115
new 6.923714600001404
prep_1 6.924983999999313
prep_2 6.917346099999122
n = 83200
old 6.942102999999406
new 6.932901300000594
prep_1 6.939852899999096
prep_2 6.923249399998895
n = 83300
old 6.942224800000986
new 6.946604700000535
prep_1 6.952560900001117
prep_2 6.933642999998483
n = 83400
old 6.955925899999784
new 6.951708499998858
prep_1 6.94446330000028
prep_2 6.948397100000875
n = 83500
old 6.968333999999231
new 6.963525400000435
prep_1 6.953828599998815
prep_2 6.964799600000333
n = 83600
old 6.979189600000609
new 6.977914899998723
prep_1 6.987341299998661
prep_2 6.95914890000131
n = 83700
old 6.969660299999305
new 6.976377999999386
prep_1 6.984743900000467
prep_2 6.983766600000308
n = 83800
old 6.991218600000138
new 6.979483200000686
prep_1 6.992399799999475
prep_2 6.98852640000041
n = 83900
old 7.000636400000076
new 6.995624000001044
prep_1 6.996424300001308
prep_2 6.986841800000548
n = 84000
old 7.005333600000085
new 6.998934700000973
prep_1 7.085902000000715
prep_2 7.004681700000219
n = 84100
old 7.02668310000081
new 7.0108249000004434
prep_1 7.010136699998839
prep_2 7.003225399999792
n = 84200
old 7.030968299999586
new 7.012756000000081
prep_1 7.009763399999429
prep_2 7.003756999998586
n = 84300
old 7.122124299999996
new 7.116262300000017
prep_1 7.126018599999952
prep_2 7.050135299999965
n = 84400
old 7.037538200000199
new 7.042950699998983
prep_1 7.032895900001677
prep_2 7.035871999998562
n = 84500
old 7.0445419999996375
new 7.061907100000099
prep_1 7.039008800000374
prep_2 7.045708800000284
n = 84600
old 7.063091099998928
new 7.046834700000545
prep_1 7.0897740999989765
prep_2 7.095504700000674
n = 84700
old 7.073157899998478
new 7.053185800001302
prep_1 7.0673986000001605
prep_2 7.055357699999149
n = 84800
old 7.068109100000584
new 7.170612100000653
prep_1 7.076927699999942
prep_2 7.069539199999781
n = 84900
old 7.085460300000705
new 7.079487500001051
prep_1 7.078212200000053
prep_2 7.068876899998941
n = 85000
old 7.099214600000778
new 7.101164300000164
prep_1 7.09680920000028
prep_2 7.075043799999548
n = 85100
old 7.104483099999925
new 7.130514299999049
prep_1 7.10593450000124
prep_2 7.124019599999883
n = 85200
old 7.121587099998578
new 7.102585099999487
prep_1 7.1060577999996895
prep_2 7.107636200000343
n = 85300
old 7.119942899998932
new 7.109416199999032
prep_1 7.110022599999866
prep_2 7.122357399999601
n = 85400
old 7.130226900000707
new 7.116656999998668
prep_1 7.116555300000982
prep_2 7.118652899998779
n = 85500
old 7.144026300000405
new 7.13057420000041
prep_1 7.127881399999751
prep_2 7.1224364999998215
n = 85600
old 7.1432034999997995
new 7.129750699999931
prep_1 7.1389603999996325
prep_2 7.1342748000006395
n = 85700
old 7.155313199999
new 7.147459700001491
prep_1 7.143876699999964
prep_2 7.223905499999091
n = 85800
old 7.295126400000299
new 7.227372399998785
prep_1 7.144533199998477
prep_2 7.152571700000408
n = 85900
old 7.162325299999793
new 7.161984500000472
prep_1 7.156681999998909
prep_2 7.159791199999745
n = 86000
old 7.186980799999219
new 7.162792200000695
prep_1 7.165153799998734
prep_2 7.15726739999991
n = 86100
old 7.18112629999996
new 7.187030899998717
prep_1 7.17137399999956
prep_2 7.267392799998561
n = 86200
old 7.2029247999998915
new 7.19369209999968
prep_1 7.1825926000001346
prep_2 7.187021100000493
n = 86300
old 7.197393500000544
new 7.199803999999858
prep_1 7.203060799998639
prep_2 7.195014300001276
n = 86400
old 7.209109999999782
new 7.204578900000342
prep_1 7.204636899999969
prep_2 7.21649350000007
n = 86500
old 7.224055900000167
new 7.206723400000556
prep_1 7.211569900000541
prep_2 7.210176100001263
n = 86600
old 7.2331128000005265
new 7.231549099999029
prep_1 7.208113999999114
prep_2 7.215782900000704
n = 86700
old 7.246492199999921
new 7.236634099999719
prep_1 7.233087199998408
prep_2 7.220678399999088
n = 86800
old 7.268496500000765
new 7.224263399999472
prep_1 7.232584299999871
prep_2 7.229136900001322
n = 86900
old 7.2530325000007
new 7.247989400000733
prep_1 7.251352899998892
prep_2 7.238625999998476
n = 87000
old 7.255545300000449
new 7.330293399998482
prep_1 7.361236699998699
prep_2 7.386590100000831
n = 87100
old 7.293673299998773
new 7.265483799999856
prep_1 7.264067600000999
prep_2 7.2616836999986845
n = 87200
old 7.325727100000222
new 7.27724279999893
prep_1 7.2741069000003336
prep_2 7.266344699999536
n = 87300
old 7.3002159999996366
new 7.265871299998253
prep_1 7.275960700000724
prep_2 7.276421500000652
n = 87400
old 7.298915400000624
new 7.280003300000317
prep_1 7.279842399999325
prep_2 7.289975600000616
n = 87500
old 7.306257300000652
new 7.298881500000789
prep_1 7.294158299999253
prep_2 7.292583500000546
n = 87600
old 7.322489400001359
new 7.342365200000131
prep_1 7.375901199999134
prep_2 7.390326400000049
n = 87700
old 7.4179205000000366
new 7.312798200000543
prep_1 7.314100999999937
prep_2 7.320165499999348
n = 87800
old 7.326890000000276
new 7.3123940999994375
prep_1 7.3224173999988125
prep_2 7.330671600000642
n = 87900
old 7.339322699999684
new 7.319627700000638
prep_1 7.327779400000509
prep_2 7.332373400000506
n = 88000
old 7.345788200000243
new 7.335507699999653
prep_1 7.428052799999932
prep_2 7.410570199999711
n = 88100
old 7.357117800000196
new 7.342833400000018
prep_1 7.36668820000159
prep_2 7.338050099999236
n = 88200
old 7.360939500000313
new 7.450989300001311
prep_1 7.371258099999977
prep_2 7.364554300000236
n = 88300
old 7.405012199998964
new 7.356135100000756
prep_1 7.365871699999843
prep_2 7.367162900000039
n = 88400
old 7.38328680000086
new 7.357941600001141
prep_1 7.3617178999993484
prep_2 7.379332300000897
n = 88500
old 7.378385100000742
new 7.388457900000503
prep_1 7.371290400000362
prep_2 7.3815059999997175
n = 88600
old 7.395690299999842
new 7.383233200000177
prep_1 7.380830399999468
prep_2 7.410697400000572
n = 88700
old 7.399197200000344
new 7.393203399999038
prep_1 7.397408400000131
prep_2 7.399390199998379
n = 88800
old 7.419927099999768
new 7.407562500000495
prep_1 7.399425700001302
prep_2 7.398787199999788
n = 88900
old 7.441276800000196
new 7.399628699999084
prep_1 7.411926599999788
prep_2 7.4144604000011896
n = 89000
old 7.427922199998648
new 7.426777399999992
prep_1 7.424963900000876
prep_2 7.53981770000064
n = 89100
old 7.5471464000002015
new 7.4935645000005024
prep_1 7.418733999998949
prep_2 7.43326850000085
n = 89200
old 7.453831700000592
new 7.489030699998693
prep_1 7.456177199999729
prep_2 7.548069899999973
n = 89300
old 7.454550700000254
new 7.450985899999068
prep_1 7.438057399998797
prep_2 7.439030800000182
n = 89400
old 7.450716699999248
new 7.454007899999851
prep_1 7.45513260000007
prep_2 7.453773700000966
n = 89500
old 7.484026599999197
new 7.461949200000163
prep_1 7.455404399999679
prep_2 7.461047900000267
n = 89600
old 7.49154819999967
new 7.476226800001314
prep_1 7.479104899999584
prep_2 7.4735285000006115
n = 89700
old 7.490685300001132
new 7.491719499999817
prep_1 7.466619900000296
prep_2 7.478410300000178
n = 89800
old 7.498411300000953
new 7.482004800000141
prep_1 7.488565300000118
prep_2 7.492774400001508
n = 89900
old 7.5050522000001365
new 7.485030100000586
prep_1 7.506228900001588
prep_2 7.484460199999376
n = 90000
old 7.506760399999621
new 7.5016104000005726
prep_1 7.510137399998712
prep_2 7.591038700000354
n = 90100
old 7.5214127999988705
new 7.5130117000007886
prep_1 7.528616700001294
prep_2 7.50401520000014
n = 90200
old 7.536241199999495
new 7.552140699999654
prep_1 7.564078999999765
prep_2 7.596764800000528
n = 90300
old 7.552308299998913
new 7.5298060000004625
prep_1 7.525773100000151
prep_2 7.523571899999297
n = 90400
old 7.533138200000394
new 7.553901300001598
prep_1 7.562125500000548
prep_2 7.657031699998697
n = 90500
old 7.6527987999998
new 7.5528648999988945
prep_1 7.542917599999782
prep_2 7.548372799999925
n = 90600
old 7.563940199999706
new 7.546967499998573
prep_1 7.560130800000479
prep_2 7.571149399998831
n = 90700
old 7.586150400000406
new 7.56367230000069
prep_1 7.563015900001119
prep_2 7.561273399998754
n = 90800
old 7.581701299999622
new 7.558972999999241
prep_1 7.579281600001195
prep_2 7.5752229999998235
n = 90900
old 7.582867200000692
new 7.574784599999475
prep_1 7.567927000000054
prep_2 7.582858699999633
n = 91000
old 7.59243620000052
new 7.593059299999368
prep_1 7.691481699999713
prep_2 7.700386100001197
n = 91100
old 7.702234000000317
new 7.600318400000106
prep_1 7.599886500000139
prep_2 7.593905599998834
n = 91200
old 7.624198299999989
new 7.653210399999807
prep_1 7.652191600000151
prep_2 7.620719100001224
n = 91300
old 7.647049799999877
new 7.61623740000141
prep_1 7.623386699999173
prep_2 7.618482399999266
n = 91400
old 7.6213994000008825
new 7.637402500000462
prep_1 7.619146800001545
prep_2 7.612351900001158
n = 91500
old 7.65341350000017
new 7.636859600001117
prep_1 7.6164066000001185
prep_2 7.622930100000303
n = 91600
old 7.648128400000132
new 7.64399880000019
prep_1 7.649782800001049
prep_2 7.660146300000633
n = 91700
old 7.681410899998809
new 7.6618614999988495
prep_1 7.671913299998778
prep_2 7.658098699999755
n = 91800
old 7.684838500001206
new 7.6784468999994715
prep_1 7.767407000001185
prep_2 7.716771700001118
n = 91900
old 7.681964400000652
new 7.6857390999994095
prep_1 7.678411400000186
prep_2 7.684427000000142
n = 92000
old 7.702964000000065
new 7.735825900001146
prep_1 7.737538999999742
prep_2 7.673104699999385
n = 92100
old 7.706759900000179
new 7.697189200000139
prep_1 7.702028000001519
prep_2 7.694966900000509
n = 92200
old 7.8458202999991045
new 7.733040499999333
prep_1 7.786911799999871
prep_2 7.733959600000162
n = 92300
old 7.737797399999181
new 7.708395199999359
prep_1 7.721155200000794
prep_2 7.705787799999598
n = 92400
old 7.735002200000963
new 7.80756669999937
prep_1 7.838640099998884
prep_2 7.746201199999632
n = 92500
old 7.736565700000938
new 7.7365294999999605
prep_1 7.729051899999831
prep_2 7.7266653000006045
n = 92600
old 7.746592299999975
new 7.838148099999671
prep_1 7.7578309000000445
prep_2 7.7373397999999725
n = 92700
old 7.758603799999037
new 7.756346100000883
prep_1 7.749974799999109
prep_2 7.740299400000367
n = 92800
old 7.773176599999715
new 7.757944599999973
prep_1 7.751782100000128
prep_2 7.756513000000268
n = 92900
old 7.764025000000402
new 7.75079900000128
prep_1 7.755085599999802
prep_2 7.762823399998524
n = 93000
old 7.789288699999815
new 7.770394600000145
prep_1 7.763021199998548
prep_2 7.787869800000408
n = 93100
old 7.78462490000129
new 7.776360899999418
prep_1 7.774301299999934
prep_2 7.810422000000472
n = 93200
old 7.804948900000454
new 7.8137125999983255
prep_1 7.778508499999589
prep_2 7.792814299999009
n = 93300
old 7.7970998999990115
new 7.78861119999965
prep_1 7.802399399999558
prep_2 7.797438499999771
n = 93400
old 7.8094130999998015
new 7.812114599999404
prep_1 7.811291300000448
prep_2 7.8024713000013435
n = 93500
old 7.814607199999955
new 7.8029243999990285
prep_1 7.807004000000234
prep_2 7.815293399999064
n = 93600
old 7.826659199999995
new 7.812350000000151
prep_1 7.816058899999916
prep_2 7.812099000000671
n = 93700
old 7.835195999999996
new 7.823943000001236
prep_1 7.836724599999798
prep_2 7.818090900000243
n = 93800
old 7.84944859999996
new 7.826473700000861
prep_1 7.84687490000033
prep_2 7.850628300000608
n = 93900
old 7.8805984999999055
new 7.843797100000302
prep_1 7.853768200000559
prep_2 7.847556700000496
n = 94000
old 7.869464000001244
new 7.855026600000201
prep_1 7.8627300999996805
prep_2 7.849202300001707
n = 94100
old 7.864638600000035
new 7.96890650000023
prep_1 7.868882800001302
prep_2 7.871605199999976
n = 94200
old 7.922758400000021
new 7.868443699999261
prep_1 7.873733599999468
prep_2 7.862675700000182
n = 94300
old 7.923248799999783
new 7.872240900000179
prep_1 7.871703200000411
prep_2 7.880110399999467
n = 94400
old 7.8991882000009355
new 7.8914784000007785
prep_1 7.886059299999033
prep_2 7.874042600000394
n = 94500
old 7.903156200000012
new 7.88806349999868
prep_1 7.8980037000001175
prep_2 7.910116499999276
n = 94600
old 7.908775799998693
new 7.908790499999668
prep_1 7.899297199999637
prep_2 7.913255999999819
n = 94700
old 7.922243900000467
new 7.978685799998857
prep_1 7.976504800000839
prep_2 7.915283099999215
n = 94800
old 7.925291100000322
new 7.91746620000049
prep_1 7.914549299999635
prep_2 7.917490800000451
n = 94900
old 7.935308100000839
new 7.925666499999352
prep_1 7.921445800000583
prep_2 7.918196599999646
n = 95000
old 7.956999599999108
new 8.018237799999042
prep_1 8.198777300000074
prep_2 8.090627400000812
n = 95100
old 8.02706709999984
new 8.0618527000006
prep_1 8.111604299998362
prep_2 8.09314380000069
n = 95200
old 8.120565699999133
new 7.98374479999984
prep_1 7.96005999999943
prep_2 7.9774927999987995
n = 95300
old 8.054278800000247
new 8.036184500000672
prep_1 8.047902199999953
prep_2 7.973747399999411
n = 95400
old 7.992452999998932
new 7.975840699999026
prep_1 7.994984900000418
prep_2 8.059231000001091
n = 95500
old 8.10195560000102
new 8.014345100000355
prep_1 7.9697581000000355
prep_2 7.980192899998656
n = 95600
old 8.000498699999298
new 7.983661399999619
prep_1 7.989026400000512
prep_2 7.9664505000000645
n = 95700
old 7.999006300000474
new 8.004792600000656
prep_1 8.012546300000395
prep_2 7.997806199999104
n = 95800
old 8.020115900000746
new 8.00730889999977
prep_1 8.018607400001201
prep_2 7.999766400000226
n = 95900
old 8.026724599998488
new 8.005989600000248
prep_1 8.009098500000619
prep_2 8.026488899999094
n = 96000
old 8.086952600000586
new 8.088666999999987
prep_1 8.113963399999193
prep_2 8.038500200000271
n = 96100
old 8.046948299999713
new 8.023652600000787
prep_1 8.040715600000112
prep_2 8.018490099999326
n = 96200
old 8.041297800000393
new 8.127955300000394
prep_1 8.083528000001024
prep_2 8.043680900000254
n = 96300
old 8.053315599998314
new 8.044540999999299
prep_1 8.05033469999944
prep_2 8.038061500001277
n = 96400
old 8.078089300001011
new 8.051094499998726
prep_1 8.06462830000055
prep_2 8.05005009999877
n = 96500
old 8.07641010000043
new 8.055165300000226
prep_1 8.05784339999991
prep_2 8.063508999999613
n = 96600
old 8.084444699999949
new 8.072690400000283
prep_1 8.062348099998417
prep_2 8.072804899999028
n = 96700
old 8.0943342999999
new 8.093980999999985
prep_1 8.063946500000384
prep_2 8.076851400001033
n = 96800
old 8.102785899998707
new 8.086845499999981
prep_1 8.093138800000816
prep_2 8.087334399999236
n = 96900
old 8.09493029999976
new 8.095182199998817
prep_1 8.131644700000834
prep_2 8.110498300000472
n = 97000
old 8.151613299998644
new 8.14241359999869
prep_1 8.102612700000464
prep_2 8.107805399999052
n = 97100
old 8.130912900000112
new 8.098823000000266
prep_1 8.162872299999435
prep_2 8.225268800000777
n = 97200
old 8.252420599999823
new 8.135174600000028
prep_1 8.116584899998998
prep_2 8.109075300000768
n = 97300
old 8.140867899999648
new 8.147379599999113
prep_1 8.140929799999867
prep_2 8.133234299999458
n = 97400
old 8.145393400000103
new 8.1346154999992
prep_1 8.139762899998459
prep_2 8.133562399998482
n = 97500
old 8.159555900001578
new 8.165598200001114
prep_1 8.145511400000032
prep_2 8.144940800000768
n = 97600
old 8.173337999998694
new 8.153313500000877
prep_1 8.159670299999561
prep_2 8.147357199999533
n = 97700
old 8.179364600000554
new 8.161895499999446
prep_1 8.165801299999657
prep_2 8.163252100001046
n = 97800
old 8.188745800000106
new 8.173495999999432
prep_1 8.221656600000642
prep_2 8.202927000000273
n = 97900
old 8.293204100000366
new 8.165590200000224
prep_1 8.183899999999994
prep_2 8.177474899999652
n = 98000
old 8.197403199999826
new 8.177584500001103
prep_1 8.19649279999976
prep_2 8.287981600000421
n = 98100
old 8.242400900000575
new 8.192036799999187
prep_1 8.196731500000169
prep_2 8.197261200000867
n = 98200
old 8.21951639999861
new 8.207163299999593
prep_1 8.229085299999497
prep_2 8.213999199999307
n = 98300
old 8.289887100001579
new 8.219094899999618
prep_1 8.221707099999549
prep_2 8.210606700000426
n = 98400
old 8.225112199999785
new 8.214580400001068
prep_1 8.262323099999776
prep_2 8.218575199998668
n = 98500
old 8.232690200000434
new 8.267878699998619
prep_1 8.225752399999692
prep_2 8.227826500000447
n = 98600
old 8.322275799999261
new 8.334083100000498
prep_1 8.284622599998329
prep_2 8.278356099999655
n = 98700
old 8.489276100001007
new 8.771685600000637
prep_1 8.725789599999189
prep_2 8.589558400000897
n = 98800
old 8.61587420000069
new 8.515852900000027
prep_1 9.0743317
prep_2 9.18929399999979
n = 98900
old 8.429377100001147
new 8.405137699999614
prep_1 8.29302639999878
prep_2 8.507393500000035
n = 99000
old 8.36048529999971
new 8.359809000001405
prep_1 8.375654899999063
prep_2 8.346552599999995
n = 99100
old 8.367828799997369
new 8.525667600002635
prep_1 8.292023300000437
prep_2 8.274673799998709
n = 99200
old 8.315898800003197
new 8.305209800000739
prep_1 8.413528900000529
prep_2 8.331258300000627
n = 99300
old 8.450595999998768
new 8.323065100001259
prep_1 8.304811100002553
prep_2 8.351648899999418
n = 99400
old 8.32902710000053
new 8.400305299997854
prep_1 8.411822399997618
prep_2 8.421715899999981
n = 99500
old 8.35531970000011
new 8.40390920000209
prep_1 8.324271299999964
prep_2 8.455298400000174
n = 99600
old 8.492840899998555
new 8.40850500000306
prep_1 8.400900399999955
prep_2 8.375514200000907
n = 99700
old 8.371322899998631
new 8.353551700001844
prep_1 8.352361300003395
prep_2 8.351437200002692
n = 99800
old 8.374340900001698
new 8.351018699999258
prep_1 8.34884189999866
prep_2 8.357482999999775
n = 99900
old 8.382111999999324
new 8.362180399999488
prep_1 8.37055859999964
prep_2 8.361943699997937
n = 100000
old 8.384042800000316
new 8.369189900000492
prep_1 8.374283500001184
prep_2 8.406800400000066
"""

cProfile.run('my_old_min_max(100_000)')

"""
502280 function calls in 0.218 seconds
Ordered by: standard name
ncalls tottime percall cumtime percall filename: lineno(function)
1       0.001   0.001   0.218   0.218 < string >: 1( < module >)
1       0.000   0.000   0.217   0.217 algs_4_t1.py: 53(my_old_min_max)
1       0.035   0.035   0.217   0.217 algs_4_t1.py: 57( < listcomp >)
100000  0.067   0.000   0.143   0.000 random.py: 200(randrange)
100000  0.039   0.000   0.182   0.000 random.py: 244(randint)
100000  0.054   0.000   0.076   0.000 random.py: 250(_randbelow_with_getrandbits)
1       0.000   0.000   0.218   0.218 {built - in method builtins.exec}
100000  0.009   0.000   0.009   0.000 {method 'bit_length' of 'int' objects}
1       0.000   0.000   0.000   0.000 {method 'disable' of '_lsprof.Profiler' objects}
102275  0.012   0.000   0.012   0.000 {method 'getrandbits' of '_random.Random' objects}
"""

cProfile.run('my_new_min_max(100_000)')

"""
502316 function calls in 0.206 seconds
Ordered by: standard name
ncalls  tottime percall cumtime percall filename: lineno(function)
1       0.001   0.001   0.206   0.206 < string >: 1( < module >)
1       0.000   0.000   0.204   0.204   algs_4_t1.py: 83(my_new_min_max)
1       0.032   0.032   0.204   0.204   algs_4_t1.py: 87( < listcomp >)
100000  0.067   0.000   0.135   0.000   random.py: 200(randrange)
100000  0.038   0.000   0.173   0.000   random.py: 244(randint)
100000  0.047   0.000   0.068   0.000   random.py: 250(_randbelow_with_getrandbits)
1       0.000   0.000   0.206   0.206   {built - in method builtins.exec}
100000  0.009   0.000   0.009   0.000   {method 'bit_length' of 'int' objects}
1       0.000   0.000   0.000   0.000   {method 'disable' of '_lsprof.Profiler' objects}
102311  0.011   0.000   0.011   0.000   {method 'getrandbits' of '_random.Random' objects}

"""

cProfile.run('prep_1(100_000)')

"""
502274 function calls in 0.207 seconds
Ordered by: standard name
ncalls  tottime percall cumtime percall filename: lineno(function)
1       0.001   0.001   0.207   0.207 < string >: 1( < module >)
1       0.000   0.000   0.205   0.205   algs_4_t1.py: 104(prep_1)
1       0.032   0.032   0.205   0.205   algs_4_t1.py: 108( < listcomp >)
100000  0.067   0.000   0.135   0.000   random.py: 200(randrange)
100000  0.038   0.000   0.173   0.000   random.py: 244(randint)
100000  0.048   0.000   0.068   0.000   random.py: 250(_randbelow_with_getrandbits)
1       0.000   0.000   0.207   0.207   {built - in method builtins.exec}
100000  0.009   0.000   0.009   0.000   {method 'bit_length' of 'int' objects}
1       0.000   0.000   0.000   0.000   {method 'disable' of '_lsprof.Profiler' objects}
102269  0.011   0.000   0.011   0.000   {method 'getrandbits' of '_random.Random'objects}
"""


cProfile.run('prep_2(100_000)')
"""
502322 function calls in 0.201 seconds 
Ordered by: standard name
ncalls  tottime    percall  cumtime percall filename: lineno(function)
1       0.001       0.001   0.201   0.201 < string >: 1( < module >)
1       0.000       0.000   0.200   0.200   algs_4_t1.py: 121(prep_2)
1       0.032       0.032   0.200   0.200   algs_4_t1.py: 125( < listcomp >)
100000  0.063       0.000   0.131   0.000   random.py: 200(randrange)
100000  0.038       0.000   0.168   0.000   random.py: 244(randint)
100000  0.047       0.000   0.068   0.000   random.py: 250(_randbelow_with_getrandbits)
1       0.000       0.000   0.201   0.201   {built - in method builtins.exec}
100000  0.009       0.000   0.009   0.000   {method 'bit_length' of 'int' objects}
1       0.000       0.000   0.000   0.000   {method 'disable' of '_lsprof.Profiler' objects}
102317  0.012       0.000   0.012   0.000   {method 'getrandbits' of '_random.Random' objects}
"""


"""
Выводы:
1.	Несмотря на визуальные различия в коде, значимых различий в эмпирической оценке кодов обнаружено не было.
Время выполнения каждого из 4 алгоритмов соответствует оценке - O(n) - линейное.
2.	При оценке алгоритмов методом cProfile.run блоков, усложняющих код каждого из алгоритмов обнаружено не было.
3.	Учитывая, что сложность кода №3 имеет оценку О(n), а оценка кода №4 оценку - О(3n)
и что фактическая оценка не показала значимых различий,
СЧИТАЮ ОБОСНОВАННЫМ ИГНОРИРОВАНИЕ КОЛИЧЕСТВА N ПРИ ЭМПИРИЧЕСКОМ ОЦЕНИВАНИИ АЛГОРИТМА. Т.е. O(n) примерно равно O(n*3).
Примерное равенство действует, вероятно, в разумных пределах.

Надеюсь, что я не ошибся в расчетах, но вполне допускаю.
Спасибо, что дочитали до конца.
P.s.
график расчетов приведен в файле https://drive.google.com/file/d/1bqIlfVmq3viOod1MMW-Ef7HYaA_7lYNx/view?usp=sharing
"""