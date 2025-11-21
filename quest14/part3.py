with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    return r


X = len(lines[0])
Y = len(lines)

target = set()
non_target = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x + 13, y + 13)
        c = lines[y][x]
        match c:
            case "#":
                target.add(p)
            case ".":
                non_target.add(p)

active = set()
total = 0

X = 34
Y = 34
ALL = set()
for x in range(X):
    for y in range(Y):
        ALL.add((x, y))

mem = {}
total_at = {}
i = 0
while i < 1000000000:
    next = set()
    for a in active:
        if len([x for x in get_all_nei(a) if x in active]) % 2 == 1:
            next.add(a)
    for p in ALL - active:
        if len([n for n in get_all_nei(p) if n in active]) % 2 == 0:
            next.add(p)
    active = next

    if all([p in active for p in target]):
        if all([p not in active for p in non_target]):
            total += len(active)
            key = frozenset(active)
            if key in mem:
                stepsize = i - mem[key]
                total_diff = total - total_at[key]
                steps = (1000000000 - i) // stepsize
                total += total_diff * steps
                i += stepsize * steps
            else:
                mem[key] = i
                total_at[key] = total
    i += 1

print(total)
