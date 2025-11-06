with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

ratio = 1

for i in range(len(lines) - 1):
    a = int(lines[i].split("|")[-1])
    b = int(lines[i + 1].split("|")[0])
    ratio *= (a / b)

res = int(ratio * 100)
print(res)
