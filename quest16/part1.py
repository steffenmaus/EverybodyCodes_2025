with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

total = 0
for n in lines[0].split(","):
    total += 90 // int(n)

print(total)
