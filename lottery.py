import random

BALLS = [i for i in range(1, 51, 1)]

result = random.sample(BALLS, 10)
result.sort()

print(f'Wining numbers are {result}')
