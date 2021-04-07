def islatin(s):
    lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return lower.intersection(s.lower()) == set()

def int_func(word):
    return word[0].upper() + word[1:]

while True:
    inp = input('Введите слово или строку: ')
    notlatin = 0
    words = inp.split()
    print('Преобразованная строка: ', end=' ')
    for word in words:
        if islatin(word):
            print(int_func(word), end=' ')
        else:
            notlatin = 1
    print('\n')
    if notlatin == 1:
        print('Учитываются только слова, состоящие из латинских букв\n')