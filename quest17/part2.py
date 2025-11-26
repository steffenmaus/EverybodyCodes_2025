with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

X = len(lines[0])
Y = len(lines)

vulcano = None

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        if c == "@":
            vulcano = p
        else:
            maze[p] = int(c)

Xv, Yv = vulcano

steps = [0]
for R in range(X // 2):
    total = 0
    for Xc, Yc in maze:
        if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R:
            total += maze[(Xc, Yc)]
    total -= sum(steps)
    steps.append(total)

ma = max(steps)
idx = steps.index(ma) - 1
print(ma * idx)
