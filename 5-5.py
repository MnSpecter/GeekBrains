def check(line):
    new = line.split()
    for value in new:
        try:
            int(value)
        except ValueError:
            print('Неверный формат ввода')
            exit()

def calculate(line):
    new = line.split()
    sum = 0
    for value in new:
            sum = sum + int(value)
    return sum

line = input('Введите набор чисел, разделенных пробелами: ')
check(line)

with open("task5file.txt", "w") as file:
    file.write(line)

with open("task5file.txt", "r") as content:
    print('Сумма веденных чисел:', calculate(line))
