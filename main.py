import random

nums= [random.randint(1,50) for _ in range(10)]

with open('numbers.txt', 'a') as file:
    for i in nums:
        file.write(f'{str(i)}\n')

with open('numbers.txt', 'r') as file:
    lines=file.readlines()
    print(lines)