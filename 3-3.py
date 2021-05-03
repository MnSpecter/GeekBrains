# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

# Определение минимальных и максимальных значений списка и их индексов без использования стандартных методов списка
def get_max(array):
    max = 0
    max_i = 0
    for i, num in enumerate(array):
        if num > max:
            max = num
            max_i = i
    return(max_i, max)
def get_min(array):
    min_i = -1
    for i, num in enumerate(array):
        if (min_i == -1):
            min_i = i
            min = num
        if num < min:
            min = num
            min_i = i
    return(min_i, min)

array = [randint(1, 1000) for _ in range(10)]
print('Исходный массив')
print(array)

max = get_max(array)
min = get_min(array)

array[min[0]], array[max[0]] = array[max[0]], array[min[0]]

print('Новый массив')
print(array)
