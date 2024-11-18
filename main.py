import random

nums= [random.randint(1,50) for _ in range(10)]
names = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
    "Grace", "Hank", "Ivy", "Jack", "Karen", "Leo",
    "Mona", "Nathan", "Olivia", "Paul", "Quincy", "Rachel",
    "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander",
    "Yara", "Zack"]

with open('numbers.txt', 'a') as file:
    for i in nums:
        file.write(f'{str(i)}\n')
    for _ in range(10):
        file.write(f'{random.choice(names)}\n')


with open('numbers.txt', 'r') as file:
    lines=file.readlines()
    print(lines)