# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint
array = [randint(-10, 10) for _ in range(100)]

print('Исходный массив')
print(array)
target = 0
index = -1

for i, num in enumerate(array):
    if num < 0 and index == -1:
        target = num
        index = i
    elif target < num < 0 and index != -1:
        target = num
        index = i

if target == 0:
    print('В массиве нет отрицательных значений')
else:
    print(f'Максимальное отрицательное число {target} является {index} элементом массива')