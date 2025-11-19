with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

clock = [1]

right = True
pos = 0
for l in lines:
    n = int(l)
    if right:
        clock.append(n)
    else:
        clock = [n] + clock
        pos += 1
    right = not right

pos += 2025
pos %= len(clock)
print(clock[pos])
