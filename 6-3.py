class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

director = Position('John', 'Smith', 'Director', 1000000, 2500000)
slave = Position('Иван', 'Иванов', 'Manager', 20000, 1000)

print(director.get_full_name() + ' имеет общий доход: ' + str(director.get_total_income()) + ' руб')
print(slave.get_full_name() + ' имеет общий доход: ' + str(slave.get_total_income()) + ' руб')
