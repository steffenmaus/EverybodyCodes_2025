with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    out = []
    out.append((x - 1, y))
    out.append((x + 1, y))
    if x % 2 == y % 2:
        out.append((x, y - 1))
    else:
        out.append((x, y + 1))
    return out


X = len(lines[0])
Y = len(lines)

trampolines = set()
for y in range(0, Y):
    for x in range(0, X):
        if lines[y][x] == "T":
            trampolines.add((x, y))

pairs = set()

for t in trampolines:
    for n in get_all_nei(t):
        if n in trampolines and n > t:
            pairs.add((t, n))

print(len(pairs))
