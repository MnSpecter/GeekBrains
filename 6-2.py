class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self, height):
        return self._length * self._width * 0.025 * height

length = int(input('Введите длину дороги в м: '))
width = int(input('Введите ширину дороги в м: '))

height = int(input('Введите толщину полотна в см: '))

new_road = Road(length, width)

print('Масса асфальта по странной формуле из ДЗ: ' + str(int(new_road.count(height))) + ' т')
