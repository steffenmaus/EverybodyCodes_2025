with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def calc_score(pa, pb, child):
    sim_a = 0
    for t in zip(child, pa):
        if t[0] == t[1]:
            sim_a += 1

    sim_b = 0
    for t in zip(child, pb):
        if t[0] == t[1]:
            sim_b += 1

    return sim_a * sim_b


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


codes = {}

for line in lines:
    id, rest = line.split(":")
    codes[int(id)] = rest

total = 0
for child_key in codes:
    res = search_for_parents(child_key)
    if res:
        pa_key, pb_key = res
        total += calc_score(codes[pa_key], codes[pb_key], codes[child_key])

print(total)
