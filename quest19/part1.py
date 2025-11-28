import re

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def get_all_nei(p):
    x, y = p
    r = [(x + 1, y + 1), (x + 1, y - 1)]
    r = [p for p in r if 0 <= p[0] < X and 0 <= p[1] < Y]
    r = [p for p in r if p not in walls]
    return r


def calc_steps(p):
    x, y = p
    return ((x - y) // 2) + y


X = intlines[-1][0] + 1
Y = max([l[1] + l[2] for l in intlines]) + 1

walls = set()

for line in intlines:
    ahead, above, large = line
    for y in range(Y):
        if not above <= y < above + large:
            walls.add((ahead, y))

reachable = set()
open = {(0, 0)}
while open:
    current = open.pop()
    reachable.add(current)
    for nei in get_all_nei(current):
        open.add(nei)

exits = [p for p in reachable if p[0] == X - 1]
print(calc_steps(min(exits)))
