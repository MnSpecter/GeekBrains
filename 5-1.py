file = open('task1file.txt', 'w')
while True:
    string = input('Введите строку для записи в файл. Для завершения введите пустую строку: ')
    if(string == ''):
        break
    file.writelines(f'{string}\n')
file.close()