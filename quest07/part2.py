from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

names = lines[0].split(",")
follower = defaultdict(list)

for rule in lines[2:]:
    l, r = rule.split(" > ")
    follower[l] = r.split(',')


def validate(word):
    if len(word) == 1:
        return True
    if word[1] in follower[word[0]]:
        return validate(word[1:])
    else:
        return False


total = 0
for pos, name in enumerate(names, 1):
    if validate(name):
        total += pos

print(total)
