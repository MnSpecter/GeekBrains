class Cell:
    def __init__(self, name, cells):
        self.name = name
        self.cells = int(cells)
    def __add__(self, other):
        return self.cells + other.cells
    def __sub__(self, other):
        s = self.cells - other.cells
        if s > 0:
            return self.cells - other.cells
        else:
            return f'разность меньше или равна нулю'
    def __mul__(self, other):
        return self.cells * other.cells
    def __truediv__(self, other):
        return int(round(self.cells / other.cells, 0))
    def make_order(self, row):
        data = ''
        i = 0
        for cell in range(self.cells):
            i += 1
            data += '*'
            if i == row:
                data += '\n'
                i = 0
        return data

cells = [Cell(f'Клетка {i}', input(f'Введите количество клеток для объекта Клетка {i}: ')) for i in range(1, 4)]
order = int(input('введите количество ячеек в строке: '))

for cell in cells:
    print(f'{cell.name}:')
    print(cell.make_order(order))

print(f'{cells[0].name} + {cells[1].name} = ', cells[0] + cells[1])
print(f'{cells[1].name} - {cells[2].name} = ', cells[1] - cells[2])
print(f'{cells[2].name} * {cells[0].name} = ', cells[2] * cells[0])
print(f'{cells[2].name} / {cells[1].name} = ', cells[2] / cells[1])
