with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y, z = p
    z2 = (z + 1) % 3
    out = []
    out.append((x, y, z2))  # this jump is also allowed
    out.append((x - 1, y, z2))
    out.append((x + 1, y, z2))
    if x % 2 == y % 2:
        out.append((x, y - 1, z2))
    else:
        out.append((x, y + 1, z2))
    return out


def steps(start, targets):
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
                if n in targets:
                    return steps
                if n in trampolines and n not in completed:
                    next_border.add(n)
        border = next_border
        steps += 1
    return out


# not proud of it, but it works...
def create_rotated_lines(lines_to_rotate):
    new_lines = []
    for offset in range(Y):
        templine = ""
        for _ in range(offset):
            templine += "."
        next_top = True
        y = Y - 1 - offset
        x = X // 2 + offset
        while y >= 0:
            templine += lines_to_rotate[y][x]
            if next_top:
                y -= 1
            else:
                x -= 1
            next_top = not next_top
        for _ in range(offset):
            templine += "."
        new_lines.append(templine)
    return new_lines


X = len(lines[0])
Y = len(lines)

trampolines = set()
starts = []
ends = []

lines2 = create_rotated_lines(lines)
lines3 = create_rotated_lines(lines2)

for y in range(0, Y):
    for x in range(0, X):
        for i, li in enumerate([lines, lines2, lines3]):
            p = (x, y, i)
            c = li[y][x]
            match c:
                case "T":
                    trampolines.add(p)
                case "S":
                    starts.append(p)
                case "E":
                    ends.append(p)

res = steps(starts[0], ends)
print(res)
