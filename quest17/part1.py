with open('input1.txt') as file:
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

R = 10
Xv, Yv = vulcano

total = 0
for _ in range(10):
    for Xc, Yc in maze:
        if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R:
            total += maze[(Xc, Yc)]

print(total)
