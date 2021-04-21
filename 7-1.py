import random

def print_matrix(name, matrix):
    data = ''
    for a in matrix:
        line = ''
        for b in a:
            b = str(b)
            if len(b) > 1:
              line += f' {b} '
            else:
              line += f' {b}  '
        data += f'| {line}|\n'
    return name + ':\n' + data

class Matrix:
    def __init__(self, name, m, n):
        self.name = name
        self.m = m
        self.n = n
        self.matrix = [[random.randrange(0, 10) for y in range(self.m)] for x in range(self.n)]

    def __str__(self):
        return print_matrix(self.name, self.matrix)

    def __add__(self, other):
        new_matrix = [[self.matrix[x][y] + other.matrix[x][y] for y in range(self.m)] for x in range(self.n)]
        return print_matrix('', new_matrix)

m = int(input('Введите ширину матриц: '))
n = int(input('Введите высоту матриц: '))

first = Matrix('Матрица 1', m, n)
second = Matrix('Матрица 2', m, n)

print(first)
print(second)

print(f'{first.name} + {second.name} = ', first+second)
