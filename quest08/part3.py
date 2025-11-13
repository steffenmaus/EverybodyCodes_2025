with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

input = [int(x) for x in lines[0].split(",")]

pairs = list(zip(input, input[1:]))  # using a set instead lead to ~30 minutes of bug search...
pairs = [tuple(sorted(p)) for p in pairs]

SIZE = 256
opt = 0
for a in range(1, SIZE + 1):
    for b in range(a + 1, SIZE + 1):
        p = a, b
        candidate = 0
        for p2 in pairs:
            c, d = p2
            if (a < c < b < d) or (c < a < d < b) or (p == p2):
                candidate += 1
        opt = max(opt, candidate)
print(opt)
