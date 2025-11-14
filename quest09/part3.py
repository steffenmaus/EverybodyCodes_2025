from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def check_parents(pa, pb, child):
    for i in range(len(child)):
        if child[i] != pa[i] and child[i] != pb[i]:
            return False
    return True


def search_for_parents(child_id):
    for pa_id in codes:
        for pb_id in codes:
            if pb_id > pa_id and child_id != pa_id and child_id != pb_id:
                if check_parents(codes[pa_id], codes[pb_id], codes[child_id]):
                    return [pa_id, pb_id]
    return []


def get_all(current, completed):
    completed.add(current)
    for c in connects[current]:
        if c not in completed:
            get_all(c, completed)


codes = {}
connects = defaultdict(list)


for line in lines:
    id, rest = line.split(":")
    codes[int(id)] = rest

for child_key in codes:
    res = search_for_parents(child_key)
    for p in res:
        connects[child_key].append(p)
        connects[p].append(child_key)

max_size = 0
result = 0
done = set()
for k in codes:
    if k not in done:
        family = set()
        get_all(k, family)
        if len(family) > max_size:
            max_size = len(family)
            result = sum(family)
        done |= family

print(result)
