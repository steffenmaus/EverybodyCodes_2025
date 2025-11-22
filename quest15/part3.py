with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def next_point(x, y, d):
    if d == 0:
        t = [h for h in horizontals if h < y]
        if t:
            return x, max(t), d
    elif d == 1:
        t = [v for v in verticals if v > x]
        if t:
            return min(t), y, d
    elif d == 2:
        t = [h for h in horizontals if h > y]
        if t:
            return x, min(t), d
    elif d == 3:
        t = [v for v in verticals if v < x]
        if t:
            return max(t), y, d
    return None


def wall_in_front(x, y, d):
    for w in walls:
        p1, p2 = w
        x1, y1 = p1
        x2, y2 = p2
        if d == 0:
            if y1 == y2 and y1 == y - 1:
                if x1 <= x <= x2 or x2 <= x <= x1:
                    return True
        elif d == 2:
            if y1 == y2 and y1 == y + 1:
                if x1 <= x <= x2 or x2 <= x <= x1:
                    return True
        elif d == 1:
            if x1 == x2 and x1 == x + 1:
                if y1 <= y <= y2 or y2 <= y <= y1:
                    return True
        elif d == 3:
            if x1 == x2 and x1 == x - 1:
                if y1 <= y <= y2 or y2 <= y <= y1:
                    return True
    return False


input = lines[0].split(",")

walls = set()
dir = 0
dir_deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 0 == north, clockwise
x = 0
y = 0
verticals = set()
horizontals = set()
for instr in input:
    if instr[0] == "L":
        dir -= 1
    else:
        dir += 1
    dir %= 4
    steps = int(instr[1:])
    if dir % 2 == 0:
        verticals.add(x - 1)
        verticals.add(x + 1)
    else:
        horizontals.add(y - 1)
        horizontals.add(y + 1)
    dx, dy = dir_deltas[dir]
    nx = x + steps * dx
    ny = y + steps * dy
    walls.add(((x, y), (nx, ny)))
    x = nx
    y = ny

# :( forgot to add those, took 90m to find the bug...:
verticals.add(x - 1)
verticals.add(x + 1)
horizontals.add(y - 1)
horizontals.add(y + 1)

start = (0, 0)
end = (x, y)

open = set()
x, y = start
open.add((x, y, 0))
open.add((x, y, 1))
open.add((x, y, 2))
open.add((x, y, 3))

in_steps = {}
for x, y, d in open:
    in_steps[(x, y)] = 0

SEEN = set()
while open:
    SEEN |= open
    next_open = set()
    for x, y, d in open:
        if abs(x - end[0]) == 1 and abs(y - end[1]) == 1:
            print(in_steps[(x, y)] + 2)
            exit()
        for dd in (-1, 0, 1):
            nd = (d + dd) % 4
            if not wall_in_front(x, y, nd):
                n = next_point(x, y, nd)
                if n is not None:
                    nx, ny, nd = n
                    steps = abs(nx - x) + abs(ny - y)
                    if (nx, ny) in in_steps:
                        in_steps[(nx, ny)] = min(in_steps[(nx, ny)], in_steps[(x, y)] + steps)
                    else:
                        in_steps[(nx, ny)] = in_steps[(x, y)] + steps
                    if n not in SEEN:
                        next_open.add(n)
    open = next_open
