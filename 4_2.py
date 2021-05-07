# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо
# исключить/заменить функции print() и input() в анализируемом коде. С ними вы будете замерять время вывода данных в
# терминал и время, потраченное пользователем, на ввод данных, а не быстродействие самого алгоритма.

# Номер простого числа по порядку:
n = 100

# На основе решета Эратосфена
def sieve(n):
    if n <= 3:
        array = [i for i in range(10)]
    else:
        array = [i for i in range(n**2)]

    array[1] = 0

    for i in range(2, len(array)):
        if array[i] != 0:
            j = i * 2

            while j < len(array):
                array[j] = 0
                j += i

    result = [i for i in array if i != 0]

    return result[n-1]

# Без решета Эратосфена
def prime(n):
    array = []
    i = 1
    count = 0
    while True:
        i += 1
        ignore = ''
        for j in range(2, i):
            if i % j == 0:
                ignore = 1
                break
        if(ignore != 1):
            array.append(i)
            count += 1
        if count == n:
            break
    return array[-1]

print(f'\nПростое число № {n}:\n')
a = sieve(n)
print('Решето:', a)
# cProfile:
# n = 100: 24305 function calls in 0.006 seconds
# n = 1000: 2853713 function calls in 0.742 seconds
# n = 10000: 315037286 function calls in 85.316 seconds

b = prime(n)
print('Не решето:', b)

# cProfile:
# n = 100: 104 function calls in 0.001 seconds
# n = 1000: 1004 function calls in 0.126 seconds
# n = 10000: 10004 function calls in 17.371 seconds

print('\n', '-' * 80, '\n')
import cProfile
cProfile.run('sieve(n)')
cProfile.run('prime(n)')
