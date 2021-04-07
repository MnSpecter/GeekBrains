def my_func(**kwargs):
    print('Инфа о пользователе: ', end=' ')
    for param, word in kwargs.items():
        print(param,': ', word,',', sep='', end=' ')

params = {'имя' : '', 'фамилия' : '', 'год рождения' : '', 'город проживания' : '', 'email' : '', 'телефон' : ''}

for a in params.keys():
    params[a] = input(f'Введите значение параметра {a}: ')

my_func(**params)
