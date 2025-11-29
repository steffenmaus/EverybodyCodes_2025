with open('input2.txt') as file:
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

def steps(start, target):
    out = {}
    border = set()
    border.add(start)
    completed = set()
    steps = 1
    while border:
        next_border = set()
        completed.update(border)
        for p in border:
            out[p] = steps
            for n in get_all_nei(p):
                if n == target:
                    return steps
                if n in trampolines and n not in completed:
                    next_border.add(n)
        border = next_border
        steps +=1
    return out

X = len(lines[0])
Y = len(lines)

trampolines = set()
start = None
end = None
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "T":
                trampolines.add(p)
            case "S":
                start = p
            case "E":
                end = p

print(steps(start,end))