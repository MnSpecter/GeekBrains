# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, deque

Factory = namedtuple('Factory', 'name, profit')
f = deque()

num = int(input('Введите количество компаний: '))

for n in range(num):
    f.append(Factory(input('Введите название компании: '), int(input('Введите прибыль компании за 4 квартала: '))))

sum = 0
for i in f:
    sum += i.profit

medium = sum/len(f)

print('Средняя прибыль за год для всех предприятий: ', round(medium, 1))
print('Прибыль выше среднего у компаний: ')
for i in f:
    if i.profit > medium:
        print(i.name)
