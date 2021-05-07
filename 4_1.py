# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Замер скорости трех разных вариантов кода

import timeit
from random import randint

SIZE = 100000
array = [randint(1, SIZE**2) for _ in range(SIZE)]

#Вариант 1
start_time = timeit.default_timer()
def get_max(array):
    mmax = 0
    mmax_i = 0
    for i, num in enumerate(array):
        if num > mmax:
            mmax = num
            mmax_i = i
    return(mmax_i, mmax)
def get_min(array):
    mmin_i = -1
    for i, num in enumerate(array):
        if (mmin_i == -1):
            mmin_i = i
            mmin = num
        if num < mmin:
            mmin = num
            mmin_i = i
    return(mmin_i, mmin)

mmax = get_max(array)
mmin = get_min(array)

array[mmin[0]], array[mmax[0]] = array[mmax[0]], array[mmin[0]]

time1 = timeit.default_timer() - start_time

#Вариант 2
start_time = timeit.default_timer()
mmin = 0
mmax = 0
for i in range(SIZE):
    if array[i] < array[mmin]:
        mmin = i
    elif array[i] > array[mmax]:
        mmax = i
array[mmin], array[mmax] = array[mmax], array[mmin]

time2 = timeit.default_timer() - start_time

# #Вариант 3
start_time = timeit.default_timer()
min_num = min(array)
max_num = max(array)
mmin = array.index(min_num)
mmax = array.index(max_num)
array[mmin], array[mmax] = array[mmax], array[mmin]

time3 = timeit.default_timer() - start_time

time = [time1, time2, time3]

# Требований по минимальному кол-ву прогонов для замера времени в задании не установлено, поэтому принято судьбоносное
# решение прогонять все варианты по 1 разу с выводом результатов замера непосредственно в программе:
print('Время выполнения')
for i, t in enumerate(time):
    print(f'Вариант {i+1} - {t}')
    add = 'нет'
    if t == min(time):
        fast = str(i+1)
        if(i != 0):
            add = str(round(time[0]/time[i], 1)) + ' раз'
    if t == max(time):
        slow = str(i+1)
        if(i != 0):
            add2 = str(round(time[i]/time[0], 1)) + ' раз'
print(f'Самый оптимальный код - это вариант {fast}. Ускорение относительно изначального варианта при 1 попытке: {add}')
print(f'Самый тормозной код - это вариант {slow}. Замедление относительно изначального варианта при 1 попытке: {add2}')
