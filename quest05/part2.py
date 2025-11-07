import re

with open('input2.txt') as file:
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
    return score

scores = set()
results = []
for l in intlines:
    scores.add(calc_score(l[1:]))

print(max(scores) - min(scores))
