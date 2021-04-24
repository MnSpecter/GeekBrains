import random

class Store():
    ticket = 0
    def __init__(self):
        self._store = {}
        self._dict = {}

    def entry(self, eqp):
        self.ticket += 1
        category = eqp.group_name()
        self._store.setdefault(self.ticket, eqp)
        eqp.change_ticket(self.ticket)
        self._dict.setdefault(category, []).append(1)

    def delivery(self, eqp):
        category = eqp.group_name()
        if self._store[eqp.get_ticket()]:
            self._store.pop(eqp.get_ticket())
            self._dict[category].pop()
            eqp.change_ticket(0)

    def count(self):
        data = ''
        for category, eq in self._dict.items():
            data += f'\n{category} - {len(eq)} шт.'
        return data

    def count_dif(self, no_eq):
        data = ''
        if no_eq[0] > 0 or no_eq[1] > 0 or no_eq[2] > 0:
            data += 'Для отгрузки со склада не хватило: '
            if no_eq[0] > 0:
                data += f'\n{no_eq[0]} принтеров'
            if no_eq[1] > 0:
                data += f'\n{no_eq[1]} сканеров'
            if no_eq[2] > 0:
                data += f'\n{no_eq[2]} ксероксов'
            return data
        return False

class Eqp():
    def __init__(self, brand, model, year, price, mass):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mass = mass
        self.group = self.__class__.__name__
        self.ticket = 0
    def group_name(self):
        return f'{self.group}'
    def get_ticket(self):
        return self.ticket
    def change_ticket(self, ticket):
        self.ticket = ticket

class Printer(Eqp):
    speed = 0

class Scaner(Eqp):
    type = 0

class Xerox(Eqp):
    height = 0


store = Store()

while 'n_p' and 'n_s' and 'n_x' not in locals():
    try:
        n_p = int(input(f'Сколько принтеров HP LaserJet100 хотите купить на склад?: '))
        n_s = int(input(f'Сколько сканеров Epson Model123 хотите купить на склад?: '))
        n_x = int(input(f'Сколько ксероксов Xerox WorkCentre хотите купить на склад?: '))
        break
    except ValueError:
        print('Неверный формат ввода данных')


printers = [Printer('HP', 'LaserJet100', 2021, 300, 4.3) for i in range(n_p)]
scaners = [Scaner('Epson', 'Model123', 2020, 180, 2.3) for i in range(n_s)]
xeroxes = [Xerox('Xerox', 'WorkCentre', 2021, 4000, 16.7) for i in range(n_x)]

for printer in printers:
    printer.speed = random.randint(1, 10)
    store.entry(printer)
for scaner in scaners:
    store.entry(scaner)
    scaner.type = random.randint(1, 2)
for xerox in xeroxes:
    store.entry(xerox)
    xerox.height = random.randint(40, 250)

print('\nТеперь на вашем складе имеется следующая оргтехника:', store.count())

while True:
    errors = []
    out = input('\nУкажите через пробел сколько принтеров, сканеров и ксероксов соответственно вы хотите отгрузить: ')
    try:
        out = [int(i) for i in out.split(' ')]
    except:
        errors.append('Ошибка!')
    if len(out) == 3 and not errors:
        break
    else:
        print('вводите данные правильно!')

no_eq = [0,0,0]
for i in range(out[0]):
    try:
        store.delivery(printers.pop())
    except IndexError:
        no_eq[0] += 1
for i in range(out[1]):
    try:
        store.delivery(scaners.pop())
    except IndexError:
        no_eq[1] += 1
for i in range(out[2]):
    try:
        store.delivery(xeroxes.pop())
    except IndexError:
        no_eq[2] += 1

if store.count_dif(no_eq):
    errors.append(store.count_dif(no_eq))

print('\nТеперь на вашем складе имеется следующая оргтехника:', store.count())
if errors:
    print(f'Внимание!' + '\n'.join(errors))
