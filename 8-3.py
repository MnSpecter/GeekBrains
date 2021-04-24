class OwnError():
    def __init__(self, txt):
        print(txt)

data = []

while True:
    inp_data = input('введите число или слово "stop" для завершения: ')
    if inp_data == 'stop':
        break
    else:
        try:
            inp_data = int(inp_data)
            data.append(inp_data)
        except ValueError:
            OwnError("вводите только числа!")

if data:
    print('\nВы ввели:')
    for i in data:
        print(f'{i} ')
