with open('input3.txt') as file:
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


def f(barrels, start):
    open = {start}
    completed = set()
    while open:
        current = open.pop()
        completed.add(current)
        for n in get_all_nei(current):
            if n in barrels and n not in completed and barrels[n] <= barrels[current]:
                open.add(n)
    return completed


destroyed = set()
for _ in range(3):
    seen = set()
    best_set = set()
    for p in barrels:
        if p not in seen:
            res = f(barrels, p)
            if len(res) > len(best_set):
                best_set = res
            seen |= res

    destroyed |= best_set
    for p in best_set:
        barrels.pop(p)

print(len(destroyed))
