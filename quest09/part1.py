with open('input1.txt') as file:
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


codes = []

for line in lines:
    codes.append(line.split(":")[1])

print(calc_score(*codes))
