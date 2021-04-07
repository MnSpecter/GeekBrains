def my_func(a,b):
    first = a**b
    i=b
    second = a
    for i in range(b, 1):
        second = second/a
        i += 1
    print('a в степени b через a**b = :', first)
    print ('a в степени b через for = :', second)

while True:
    while 'a' and 'b' not in locals():
        try:
            a = float(input('Введите положительное число a: '))
            b = int(input('Введите отрицательное число b: '))
        except ValueError:
            print('Вводить только числа! Давай заново... ')

    if (a > 0 and b < 0):
        my_func(a,b)
        exit()
    else:
        print('a должно быть положительным, b - отрицательным!')
        del(a)
        del(b)
        continue


