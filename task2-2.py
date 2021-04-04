total = int(input('Требуемое количество элементов в списке (минимум 1): '))
if total < 1:
    total = 1

my_list = []

num = 0
while num < total:
    num += 1
    my_list.append(input(f'Введите элемент {num}: '))

i = 0
for element in my_list:
    if i%2 != 0:
        reverse = my_list.pop(i)
        my_list.insert((i-1), reverse)
    i += 1

print(my_list)