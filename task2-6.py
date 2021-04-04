total_goods = int(input('Введите общее количество товаров: '))
total_atributes = int(input('Введите количество атрибутов для каждого из товаров: '))
i = 1
goods = []
atributes = []

while i <= total_atributes:
    atributes.append(input(f'Укажите наименование атрибута {i}: '))
    i += 1

i = 1
while i <= total_goods:
    info = []
    for atribute in atributes:
        info.append(input(f'Заполнител поле "{atribute}" для товара {i}: '))
    good_dict = dict(zip(atributes, info))
    good = (i, good_dict)
    goods.append(good)
    i += 1

statistics = []
for atribute in atributes:
    stats = []
    for element in goods:
        info = element[1]
        stats.append(info[atribute])
    stats_dict = {atribute: stats}
    statistics.append(stats_dict)

print(statistics)



