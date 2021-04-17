class Car:
    speed = 0
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed_message = ' едет со скоростью '
        self.car_message = self.color + (' полицейская' if self.is_police == True else '') + ' машина ' + self.name

    def go(self, speed):
        self.speed = speed
        return self.car_message + ' поехала со скоростью ' + str(self.speed) + 'км/ч'

    def stop(self):
        self.speed = 0
        return self.car_message + ' остановилась'

    def turn(self, direction):
        self.direction = direction
        return self.car_message + ' повернула ' + self.direction

    def show_speed(self):
        self.speed_message += str(self.speed) + 'км/ч.'
        return self.car_message + self.speed_message

class TownCar(Car):
    def show_speed(self):
        self.speed_message = self.car_message + self.speed_message + str(self.speed) + 'км/ч.'
        if self.speed > 60:
            self.speed_message += ' !! превышен скоростной лимит !!'
        return self.speed_message

class WorkCar(Car):
    def show_speed(self):
        self.speed_message = self.car_message + self.speed_message + str(self.speed) + 'км/ч.'
        if self.speed > 40:
            self.speed_message += ' !! превышен скоростной лимит !!'
        return self.speed_message

class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police = True

mazda = TownCar('Mazda', 'серебристая')
bmw = TownCar('BMW', 'черная')
lamborgini = SportCar('Lamborgini', 'белая')
police = PoliceCar('Ford', 'бело-синяя')
kamaz = WorkCar('Камаз', 'оранжевый')

print(mazda.go(90))
print(police.turn('влево'))
print(mazda.show_speed())
print(mazda.stop())
print(lamborgini.go(200))
print(lamborgini.show_speed())
print(lamborgini.turn('вправо'))
