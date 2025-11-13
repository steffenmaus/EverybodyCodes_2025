with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

input = [int(x) for x in lines[0].split(",")]

pairs = list(zip(input, input[1:]))
pairs = [tuple(sorted(p)) for p in pairs]

total = 0
for p in pairs:
    a, b = p
    for p2 in pairs:
        c, d = p2
        if p != p2:
            if a < c < b < d:
                total += 1
print(total)
