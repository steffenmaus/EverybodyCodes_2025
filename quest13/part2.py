with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

clock = [1]

right = True
pos = 0
for l in lines:
    a, b = l.split("-")
    a = int(a)
    b = int(b)
    inter = list(range(a, b + 1))
    if right:
        clock = clock + inter
    else:
        inter = inter[::-1]
        clock = inter + clock
        pos += len(inter)
    right = not right

pos += 20252025
pos %= len(clock)
print(clock[pos])
