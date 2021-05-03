# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
array = [randint(1, 10) for _ in range(100)]
numbers = set(array)
max = 1
for i in numbers:
    count = 0
    for j in array:
        if i == j:
            count +=1
    if count > max:
        max = count
        number = i

print('Исходный массив')
print(array)

if max > 1:
    print(f'Самая частая цифра в массиве - {number}. Количество повторений: {max}')
else:
    print('Все числа в массиве уникальны')