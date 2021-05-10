# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque, defaultdict

class HexNum():
    def __init__(self, num):
        self.num = num.upper()
        signs = '0123456789ABCDEF'
        table = defaultdict(int)
        count = 0
        for key in signs:
            table[key] += count
            count += 1
        self.table = table

    def __add__(self, other):
        spam = self.get_hash() + other.get_hash()
        return self.get_hex(spam)

    def __mul__(self, other):
        spam = self.get_hash() * other.get_hash()
        return self.get_hex(spam)

    def get_hash(self):
        num = deque(self.num)
        num.reverse()
        spam = 0
        for i in range(len(num)):
            spam += self.table[num[i]] * 16 ** i
        return spam

    def get_hex(self, hash):
        num = deque()
        while hash > 0:
            d = hash % 16
            for i in self.table:
                if self.table[i] == d:
                    num.append(i)
            hash //= 16
        num.reverse()
        return list(num)

num1 = HexNum(input('Введите число 1 в шестнадцатиричном формате: '))
num2 = HexNum(input('Введите число 2 в шестнадцатиричном формате: '))

print('Сумма чисел: ', num1 + num2)
print('Произведение чисел: ', num1 * num2)
