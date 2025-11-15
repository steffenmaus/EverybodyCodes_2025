with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_dragon(p):
    x, y = p
    r = [(x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1),
         (x - 1, y + 2)]
    return [p for p in r if p[0] in range(X) and p[1] in range(Y)]


X = len(lines[0])
Y = len(lines)

dragon = None
sheeps = set()
safe = set()

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
                dragon = p

cache = {}


def f(sheeps, dragon, sheep_turn):
    key = (tuple(sorted(tuple(sheeps))), dragon, sheep_turn)
    if key in cache:
        return cache[key]
    if not sheeps:
        cache[key] = 1
        return 1
    out = 0
    sheep_moved = False
    escape_possible = False
    if sheep_turn:
        for s in sheeps:
            if s[1] == Y - 1:
                escape_possible = True
            s2 = (s[0], s[1] + 1)
            if s2[1] < Y and (s2 != dragon or s2 in safe):
                sheep_moved = True
                new_sheeps = sheeps.copy()
                new_sheeps.remove(s)
                new_sheeps.add(s2)
                out += f(new_sheeps, dragon, False)
    if not sheep_moved:
        if escape_possible:
            return 0
        for d2 in get_all_nei_dragon(dragon):
            new_sheeps = set()
            for s in sheeps:
                if s != d2 or s in safe:
                    new_sheeps.add(s)
            out += f(new_sheeps, d2, True)
    cache[key] = out
    return out


print(f(sheeps, dragon, True))
