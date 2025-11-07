import re

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def calc_score(encoded):
    spine = []
    spine.append((None, encoded[0], None))
    for n in encoded[1:]:
        done = False
        for i in range(len(spine)):
            if not done:
                l, s, r = spine[i]
                if l is None and n < s:
                    spine[i] = (n, s, r)
                    done = True
                elif r is None and n > s:
                    spine[i] = (l, s, n)
                    done = True
        if not done:
            spine.append((None, n, None))

    score = int("".join([str(n[1]) for n in spine]))

    levels = []
    for s in spine:
        cur = ""
        l, n, r = s
        if l is not None:
            cur += str(l)
        cur += str(n)
        if r is not None:
            cur += str(r)
        levels.append(int(cur))
    return score, levels


results = []
for l in intlines:
    score, levels = calc_score(l[1:])
    results.append((score, levels, l[0]))

results = sorted(results, key=lambda x: (x[0], x[1], x[2]), reverse=True)

res = 0
for i in range(len(results)):
    res += (i + 1) * results[i][2]
print(res)
