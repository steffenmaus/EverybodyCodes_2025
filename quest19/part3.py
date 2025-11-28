import re
from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def calc_steps(p):
    x, y = p
    return ((x - y) // 2) + y


def range_trim(r1, r2):
    l1, u1 = r1
    l2, u2 = r2

    lower = max(l1, l2)
    upper = min(u1, u2)
    if lower <= upper:
        return lower, upper
    else:
        return None


X = intlines[-1][0] + 1
Y = max([l[1] + l[2] for l in intlines]) + 1

walls = set()
gaps_at = defaultdict(list)

for line in intlines:
    walls.add(line[0])

for line in intlines:
    ahead, above, large = line
    gaps_at[ahead].append((above, above + large - 1))

next_wall = {0: min(walls)}
for w in walls:
    candidates = [w2 for w2 in walls if w2 > w]
    if candidates:
        next_wall[w] = min(candidates)

reachable = set()
x = 0
open = {(0, 0, 0)}  # x, lower_bound, upper_bound
while open:
    current = open.pop()
    reachable.add(current)
    x1, l1, u1 = current
    if x1 in next_wall:
        x2 = next_wall[x1]
        dx = x2 - x1
        l2 = max(l1 - dx, 0)
        u2 = min(u1 + dx, X - 1)
        for gap in gaps_at[x2]:
            trimmed = range_trim((l2, u2), gap)
            if trimmed:
                open.add((x2, trimmed[0], trimmed[1]))
                # merging of overlapping ranges not required

best_exit = min([p for p in reachable if p[0] == X - 1])
x, l, u = best_exit
if x % 2 != l % 2:  # lowest point might not be reachable
    l += 1
    assert l <= u  # gap might be too small

print(calc_steps((x, l)))
