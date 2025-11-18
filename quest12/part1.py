with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


X = len(lines[0])
Y = len(lines)

barrels = {}
for y in range(0, Y):
    for x in range(0, X):
        barrels[(x, y)] = int(lines[y][x])

open = {(0, 0)}
completed = set()
while open:
    current = open.pop()
    completed.add(current)
    for n in get_all_nei(current):
        if n in barrels and n not in completed and barrels[n] <= barrels[current]:
            open.add(n)

print(len(completed))
