from itertools import count
from itertools import cycle

stop1 = 10
stop2 = 100

while True:
    try:
        first = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Принимаются только целые числа')
        continue

gen = []
for el in count(first):
    if el > first + stop1:
        break
    else:
        gen.append(el)

print(f'Генератор {stop1} целых чисел начиная с {first}:')
for el in gen:
    print(el)

i = 0
print(f'{stop2}-кратное повторение элементов из созданного ранее генератора целых чисел:')
for el in cycle(gen):
    if i > stop2:
        break
    else:
        print(el)
        i += 1
