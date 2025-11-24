with open('input2.txt') as file:
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


columns = [int(n) for n in lines[0].split(",")]

length = len(columns)

spell = []
for i in range(1, length + 1):
    res = check(spell + [i], columns)
    if res[0]:
        spell.append(i)
    if res[1] == length:
        break

import math

print(math.prod(spell))
