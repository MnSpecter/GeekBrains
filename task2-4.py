line = input('Введите строку: ')
words = line.split(' ')
row = 0
for word in words:
    row +=1
    if len(word) > 10:
        word = word[0:10]
    print(f'{row} => {word}')