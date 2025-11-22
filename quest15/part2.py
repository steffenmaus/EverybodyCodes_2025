with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

input = lines[0].split(",")


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def f(start, end):
    open = set()
    open.add(start)
    completed = set()
    steps = 0
    while open:
        steps += 1
        next_open = set()
        completed |= open
        for p in open:
            for n in get_all_nei(p):
                if n == end:
                    return steps
                elif n not in completed and n not in wall:
                    next_open.add(n)
        open = next_open
    return None


wall = set()
dir = 0
dir_deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 0 == north, clockwise
x = 0
y = 0
for instr in input:
    if instr[0] == "L":
        dir -= 1
    else:
        dir += 1
    dir %= 4
    steps = int(instr[1:])
    for _ in range(steps):
        dx, dy = dir_deltas[dir]
        x += dx
        y += dy
        wall.add((x, y))

start = (0, 0)
end = (x, y)
wall.remove(end)

print(f(start, end))
