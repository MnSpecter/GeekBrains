def in_range(a, rng):
    if a in range(rng):
        return True
    else:
        return False

class Data():
    def __init__(self, date):
        self.date = date

    @staticmethod
    def validate(num):
        val = (31, 12, 2021)
        errors = []
        for i, a in enumerate(num):
            if not in_range(a, val[i]):
                errors.append(f'{i+1}-ое число в дате должно быть в пределах 1-{val[i]}')
        if not errors:
            return 'Дата введена корректно'
        else:
            return '\n'.join(errors)

    @classmethod
    def change(cls, date):
        errors = 'Данные введены не кооректно'
        try:
            num = [int(f) for f in date.split('-')]
            if(len(num) == 3):
                return Data.validate(num)
        except ValueError:
            ...
        return errors

date = input('Введите дату в формате чч-мм-ггг: ')
a = Data(date)

print(f'Вы ввели: {a.date}')
print(a.change(a.date))
