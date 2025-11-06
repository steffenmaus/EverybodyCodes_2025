import math

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

ratio = 1

for i in range(len(lines) - 1):
    a = int(lines[i])
    b = int(lines[i + 1])
    ratio *= (a / b)

res = math.ceil(10000000000000 / ratio)
print(res)
