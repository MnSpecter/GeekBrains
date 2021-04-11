from sys import argv

try:
    script_name, out, rate, prize = argv
except ValueError:
    print('Через командную строку нужно передать 3 параметра')
    exit()

out = int(out)
rate = int(rate)
prize = int(prize)

print(f'Выработка * Ставка + Премия =: {out} * {rate} + {prize} = {out*rate+prize}')
