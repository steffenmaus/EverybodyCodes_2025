with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1),
         (x - 1, y + 2)]
    return [p for p in r if p[0] in range(X) and p[1] in range(Y)]


X = len(lines[0])
Y = len(lines)

sheeps = set()
safe = set()
dragons = set()

for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "S":
                sheeps.add(p)
            case "#":
                safe.add(p)
            case "D":
                dragons.add(p)

init_sheep_count = len(sheeps)

for _ in range(20):
    next_dragons = set()
    for d in dragons:
        for n in get_all_nei(d):
            next_dragons.add(n)
    dragons = next_dragons

    exposed = sheeps - safe
    eatable = exposed & dragons
    sheeps -= eatable

    new_sheeps = set()
    for s in sheeps:
        x, y = s
        new_sheeps.add((x, y + 1))
    sheeps = new_sheeps

    exposed = sheeps - safe
    eatable = exposed & dragons
    sheeps -= eatable

print(init_sheep_count - len(sheeps))
