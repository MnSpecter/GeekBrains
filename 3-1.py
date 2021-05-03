# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от
# 2 до 9. Примечание: 8 разных ответов.

nums = [i for i in range(2, 100)]
mult = [i for i in range(2, 10)]
res = [0 for i in range(2, 10)]

for i in nums:
    for j in mult:
        if i % j == 0:
            res[j-2] += 1

for i, num in enumerate(res):
    print(f'Кратно {i+2} - {num}')
