# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.

n = int(input('Введите число элементов ряда 1, -0.5, 0.25, -0.125: '))
sum = 0
elem = 1
for i in range(n):
    sum += elem
    elem = elem * -1 / 2

print(f'сумма {n} элементов ряда равна: {sum}')
