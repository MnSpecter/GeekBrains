def my_func(a,b):
    try:
        calc = a / b
    except ArithmeticError:
        calc = 'На 0 делить нельзя'
    return calc

while 'a' and 'b' not in locals():
    try:
        a = int(input('Введите числитель a: '))
        b = int(input('Введите знаменатель b: '))
    except ValueError:
        print('Вводить только числа! Давай заново... ')

print(my_func(a,b))
