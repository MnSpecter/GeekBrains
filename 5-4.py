dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Zero': 'Ноль'
}

def corr(line):
    for eng, rus in dict.items():
        line = line.replace(eng, rus)
    return line

with open("task4file.txt", "r") as content:
    new_content = ''
    for line in content:
        new_content = new_content + corr(line) + '\n'

with open("task4file-new.txt", "w") as file:
    file.write(new_content)
