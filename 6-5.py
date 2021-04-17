# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''
    draw_msg = 'Запуск отрисовки'

    def draw(self):
        print(self.draw_msg)

class Pen(Stationery):
    def __init__(self):
        self.title = ' > рисуем ручкой'
    def draw(self):
        self.draw_msg += self.title
        print(self.draw_msg)

class Pencil(Stationery):
    def __init__(self):
        self.title = ' > рисуем карандашом'
    def draw(self):
        self.draw_msg += self.title
        print(self.draw_msg)

class Handle(Stationery):
    def __init__(self):
        self.title = ' > рисуем маркером'
    def draw(self):
        self.draw_msg += self.title
        print(self.draw_msg)

pen = Pen()
pencill = Pencil()
handle = Handle()

pen.draw()
pencill.draw()
handle.draw()
