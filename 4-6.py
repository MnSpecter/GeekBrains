# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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
        if(min_i == -1):
            min_i = i
            min = num
        if num < min:
            min = num
            min_i = i
    return(min_i, min)

array = [randint(1, 100) for _ in range(10)]
print('Исходный массив')
print(array)

min = get_min(array)
max = get_max(array)

if(min[0] < max[0]):
    new_array = array[(min[0]+1):max[0]]
else:
    new_array = array[(max[0]+1):min[0]]

sum = 0
for num in new_array:
    sum += num
print(f'Сумма эдементов массива, находящихся между минимальным {min[1]} и максимальным {max[1]}: {sum}')
