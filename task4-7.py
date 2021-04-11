def fact(n):
    f = 1
    for num in range(1, n+1):
        f *= num
        yield f

while True:
    try:
        n = int(input('Введите целое число n: '))
        break
    except ValueError:
        print('Принимаются только целые числа')
        continue

i = 0
for el in fact(n):
    i += 1
    print(f'!{i} = {el}')
