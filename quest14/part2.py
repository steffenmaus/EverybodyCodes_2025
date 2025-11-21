with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    return r


X = len(lines[0])
Y = len(lines)

active = set()
ALL = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        ALL.add(p)
        if lines[y][x] == "#":
            active.add(p)

total = 0
for _ in range(2025):
    next = set()
    for a in active:
        if len([x for x in get_all_nei(a) if x in active]) % 2 == 1:
            next.add(a)
    for p in ALL - active:
        if len([n for n in get_all_nei(p) if n in active]) % 2 == 0:
            next.add(p)
    active = next
    total += len(active)

print(total)
