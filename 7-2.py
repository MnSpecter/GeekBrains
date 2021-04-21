from abc import ABC, abstractmethod

class Dress:
    @abstractmethod
    def count_out(self):
        pass
    @property
    def get_name(self):
        return self.name

class Coat(Dress):
    name = 'пальто'
    def __init__(self, v):
        self.v = v
    def count_out(self):
        return self.v / 6.5 + 0.5

class Costume(Dress):
    name = 'костюм'
    def __init__(self, h):
        self.h = h
    def count_out(self):
        return 2 * self.h + 0.3

coat_size = int(input('Введите размер пальто: '))
costume_size = int(input('Введите размер костюма: '))

coat1 = Coat(coat_size)
costume1 = Costume(costume_size)

print(f'Общий расход ткани на {coat1.get_name} и {costume1.get_name} = {coat1.count_out()} + \
{costume1.count_out()} = ', coat1.count_out() + costume1.count_out())
