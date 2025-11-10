import math

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

ratio = int(lines[0]) / int(lines[-1])

res = math.ceil(10000000000000 / ratio)
print(res)
