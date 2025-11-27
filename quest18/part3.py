import re

groups = [group.split("\n") for group in open("input3.txt").read().split("\n\n")]


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


# no general solution and not even working on sample... :/
def opt_search(id):
    thickness, branches = nodes[id]
    out = 0
    for cid, thick in branches:
        if cid in leafs:
            if thick > 0:
                out += thick
        else:
            out += thick * opt_search(cid)
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

perfect_solution = opt_search(root)

total = 0
for run in range(len(tests)):
    temp = f(root, tests[run].split())
    if temp != 0:
        total += perfect_solution - temp

print(total)
