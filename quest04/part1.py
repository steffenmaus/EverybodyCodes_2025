with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

ratio = 1

for i in range(len(lines) - 1):
    a = int(lines[i])
    b = int(lines[i + 1])
    ratio *= (a / b)

res = int(ratio * 2025)
print(res)
