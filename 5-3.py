def middle(staff):
    sallary = 0
    i=0
    for guy in staff:
        sallary += guy[1]
        i += 1
    return sallary / i

def find (staff, salary):
    str = ''
    for guy in staff:
        if guy[1] < salary:
            str = str + '[' + guy[0] + '] '
    if(str) == '':
        str = 'отсутствуют'
    return str

with open("task3file.txt", "w") as file:
    while True:
        string = input(
            'Введите информацию по сотрудникам в формате: ФАМИЛИЯ ОКЛАД. Для завершения введите пустую строку: ')
        if (string == ''):
            break
        file.writelines(f'{string}\n')

with open("task3file.txt", "r") as content:
    staff = []
    for line in content:
        line_split = line.split()
        try:
            line_split[1] = int(line_split[1])
        except ValueError:
            print('Некорректный формат ввода оклада для сотрудника,', line_split[0])
            exit()
        staff.append(line_split)

print('Сотрудники с окладом менее 20 000 руб:', find(staff, 20000))
print('Средний оклад всех сотрудников =', middle(staff))
