with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

ratio = int(lines[0]) / int(lines[-1])

res = int(ratio * 2025)
print(res)
