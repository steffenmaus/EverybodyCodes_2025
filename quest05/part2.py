import re

with open('input2.txt') as file:
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
    return score

scores = set()
for l in intlines:
    scores.add(calc_score(l[1:]))

print(max(scores) - min(scores))
