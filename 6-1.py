import time

class TrafficLight:
    __color = 'red'

    __true_colors = {'red': 'yellow', 'yellow': 'green', 'green': 'red'}

    def check(self, colors):
        if self.__true_colors[colors[-2]] != colors[-1]:
            print('Светофор сломался и отключен')
            exit()

    def running(self):
        colors = []
        while True:
            print(self.__color)
            if len(colors) > 1:
                self.check(colors)
            elif len(colors) >= 3:
                colors.clear()

            if(self.__color == 'red'):
                time.sleep(7)
                self.__color = 'yellow'
                colors.append(self.__color)
                continue
            elif(self.__color == 'yellow'):
                time.sleep(2)
                self.__color = 'green'
                colors.append(self.__color)
                continue
            elif (self.__color == 'green'):
                time.sleep(5)
                self.__color = 'red'
                colors.append(self.__color)
                continue

light = TrafficLight()
light.running()
