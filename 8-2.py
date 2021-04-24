er = {
    'ValueError': 'вводить можно только числа\n',
    'ZeroDivisionError': 'нельзя делить на ноль\n'
}

class Errors():
    def __init__(self, errors):
        print(errors)

errors = ''
a = input('Введите числитель: ')
b = input('Введите знаменатель: ')
try:
    b = int(b)
except ValueError:
    errors += er['ValueError']
try:
    a = int(a)
except ValueError:
    errors += er['ValueError']
    if b == 0:
        errors += er['ZeroDivisionError']

if not errors:
    try:
        c = a/b
    except ZeroDivisionError:
        errors += er['ZeroDivisionError']

if not errors:
    print(f'{a}/{b} = {c}')
else:
   Errors(errors)
