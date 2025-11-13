with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

input = [int(x) for x in lines[0].split(",")]

pairs = list(zip(input, input[1:]))

total = 0
for p in pairs:
    a, b = p
    if abs(a - b) == 16:
        total += 1
print(total)
