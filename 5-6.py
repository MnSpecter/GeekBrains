import io

def course(line):
    split = line.split(':')
    return split[0]

def count(line):
    num_list = []

    num = ''
    for char in line:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))

    sum = 0
    for d in num_list:
        sum = sum + d
    return sum

with io.open("task6file.txt", encoding='utf-8') as content:
    dict = {}
    for line in content:
        dist = course(line)
        hours = count(line)
        dict.update({dist: hours})

print(dict)
