def words(line):
    words = line.split()
    return len(words)

file = open('task2file.txt', 'r')

count = []
i=0

for line in file:
    count.append(words(line))
    i += 1

file.close()

print(f'Общее количество строк в файле', file.name, ':', i)
print('Количество слов (включая отдельные числа и символы) в каждой строке:')
for key, element in enumerate(count):
    print('Строка', key+1, '-', element)