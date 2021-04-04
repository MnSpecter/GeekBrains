my_list = [7, 5, 3, 3, 2]
ranking = int(input('Введите значение рейтинга: '))
if ranking > max(my_list):
    my_list.insert(0, ranking)
elif ranking < min(my_list):
    my_list.append(ranking)
else:
    my_list = list(reversed(my_list))
    if my_list.count(ranking) > 0:
        my_list.insert(my_list.index(ranking), ranking)
    else:
        for i, value in enumerate(my_list):
            if value > ranking:
                my_list.insert(i, ranking)
                break
    my_list = list(reversed(my_list))
print(my_list)
