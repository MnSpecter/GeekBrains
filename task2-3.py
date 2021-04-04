print('Решение через list:')
seasons = ['нулевого месяца не существует']
i = 0
while i < 12:
    i += 1
    if i >= 3 and i < 6:
        seasons.append('весна')
    elif i >= 6 and i < 9:
        seasons.append('лето')
    elif i >= 9 and i < 12:
        seasons.append('осень')
    else:
        seasons.append('зима')

month = int(input('Введите номер месяца: '))
if month > 0 and month <= 12:
    print(f'Выбранный месяц соответствует сезону: {seasons[month]}')
else:
    print('Указан некорректный номер месяца')
    exit()

print('Решение через dict:')
seasons_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

print(f'Согласно справочнику выбранный месяц соответствует сезону: {seasons_dict[month]}')