import json
import io

with io.open("task7file.txt", "r", encoding='utf-8') as content:
    medium = 0
    i = 0
    firms = {}
    for line in content:
        info = line.split()
        profit = int(info[2]) - int(info[3])
        if(profit) > 0:
            i += 1
            medium += profit
        firms.update({info[0]: profit})
    medium = medium / i

    end = [firms, {"average_profit": medium}]

    with open("task7file.json", "w") as file:
        json.dump(end, file)
