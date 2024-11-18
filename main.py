import random

names = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
    "Grace", "Hank", "Ivy", "Jack", "Karen", "Leo",
    "Mona", "Nathan", "Olivia", "Paul", "Quincy", "Rachel",
    "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander",
    "Yara", "Zack"]

with open('numbers.txt', 'a') as file:
    for _ in range(10):
        file.write(f'{random.choice(names)}\n')

