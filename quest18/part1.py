import re

groups = [group.split("\n") for group in open("input1.txt").read().split("\n\n")]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def f(id):
    thickness, branches = nodes[id]
    if id in leafs:
        return 1
    out = 0
    for cid, thick in branches:
        out += thick * f(cid)
    if out < thickness:
        out = 0
    return out


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

print(f(root))