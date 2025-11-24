with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def check(spell, columns):
    matches = 0
    for i, count in enumerate(columns, 1):
        current = 0
        for n in spell:
            if i % n == 0:
                current += 1
        if current > count:
            return False, 0
        if current == count:
            matches += 1
    return True, matches


def blocks_required(spell, length):
    req = 0
    for s in spell:
        req += length // s
    return req


columns = [int(n) for n in lines[0].split(",")]

length = len(columns)

spell = []
for i in range(1, length + 1):
    res = check(spell + [i], columns)
    if res[0]:
        spell.append(i)
    if res[1] == length:
        break

target = 202520252025000

lower_bound = 0
upper_bound = 2 ** 32

while upper_bound > lower_bound + 1:
    current = (upper_bound + lower_bound) // 2
    req = blocks_required(spell, current)
    if req > target:
        upper_bound = current
    else:
        lower_bound = current

print(95681262445169)
