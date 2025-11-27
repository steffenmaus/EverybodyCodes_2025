import re

groups = [group.split("\n") for group in open("input2.txt").read().split("\n\n")]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def f(id, code):
    thickness, branches = nodes[id]
    if not branches:
        return code[id - 1] == "1"
    out = 0
    for cid, thick in branches:
        out += thick * f(cid, code)
    if out < thickness:
        out = 0
    return out


tests = groups[-1][1:]
groups = groups[:-1]

non_roots = set()
nodes = {}
leafs = set()

for g in groups:
    id, thickness = all_ints_in_string(g[0])
    branches = []
    for branch in g[1:]:
        if "free branch" in branch:
            leafs.add(id)
        else:
            target, th = all_ints_in_string(branch)
            non_roots.add(target)
            branches.append((target, th))
    nodes[id] = (thickness, branches)

root = (nodes.keys() ^ non_roots).pop()

total = 0
for run in range(len(tests)):
    total += f(root, tests[run].split())

print(total)
