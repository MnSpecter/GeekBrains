class Cmp():
    def __init__(self, real, img):
        try:
            self.real = float(real)
            self.img = float(img)
        except ValueError:
            print('Неверный формат ввода данных. Вводите только числа!')
            exit()

    def get_string(self, part1, part2):
        if part2 < 0:
            operator = ''
        else:
            operator = '+'
        return f'{part1}{operator}{part2}j'

    def __add__(self, other):
        part1 = self.real + other.real
        part2 = self.img + other.img
        return self.get_string(part1, part2)

    def __mul__(self, other):
        part1 = self.real * other.real - self.img * other.img
        part2 = (self.real * other.img) + (other.real * self.img)
        return self.get_string(part1, part2)

a1 = input('Введите действительную часть первого числа: ')
b1 = input('Введите мнимую часть первого числа: ')
a2 = input('Введите действительную часть второго числа: ')
b2 = input('Введите мнимую часть второго числа: ')

a = Cmp(a1, b1)
b = Cmp(a2, b2)

print(f'сумма комплексных чисел  = {a+b}')
print(f'произведение комплексных чисел  = {a*b}')
