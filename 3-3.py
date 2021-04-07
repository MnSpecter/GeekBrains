def my_func(a,b,c):
    ls = sorted([a,b,c], reverse=True)
    return sum(ls[:2])

while 'a' and 'b' and 'c' not in locals():
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
    except ValueError:
        print('Вводить только числа! Давай заново... ')

print('Сумма 2-х наибольших значений:', my_func(a,b,c))