# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = input('Введите число: ')
char = len(num)
reverse = list()
while char > 0:
    char -= 1
    reverse.append(num[char])
print(''.join(reverse))