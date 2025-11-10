import re

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def calc_score(encoded):
    spine = []
    for n in encoded:
        for i in range(len(spine)):
            l, s, r = spine[i]
            if l is None and n < s:
                spine[i] = (n, s, r)
                break
            elif r is None and n > s:
                spine[i] = (l, s, n)
                break
        else:
            spine.append((None, n, None))

    score = int("".join([str(n[1]) for n in spine]))

    levels = []
    for s in spine:
        current = "".join([str(x) for x in s if x is not None])
        levels.append(int(current))
    return score, levels


results = []
for l in intlines:
    score, levels = calc_score(l[1:])
    results.append((score, levels, l[0]))

results = sorted(results, reverse=True)

res = 0
for i in range(len(results)):
    res += (i + 1) * results[i][2]
print(res)
