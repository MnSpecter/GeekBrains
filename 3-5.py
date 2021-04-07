def calc(a):
    global sum
    sum += a

def show_sum(end=0):
    if end == 0:
        print(f'Промежуточная сумма всех введенных значений {sum}\n')
    else:
        print(f'Итоговая сумма всех введенных значений {sum}\n')

def inp():
    string = input('Введите строку чисел, разделенных пробелом или введите "q" для завершения ')
    numbers = string.split()
    for number in numbers:
        if number == 'q':
            show_sum(end=1)
            exit()
        else:
            try:
                calc(int(number))
            except ValueError:
                print('Внимание! Ввод любых нецелочисленных значений игнорируется')
    show_sum()

sum = 0
while True:
    inp()
