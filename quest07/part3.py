from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

prefixes = lines[0].split(",")
follower = defaultdict(list)
solutions = set()

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


def create(current):
    if len(current) > 11:
        return
    if len(current) >= 7:
        solutions.add(current)
    for c in follower[current[-1]]:
        create(current + c)


for pre in prefixes:
    if validate(pre):
        create(pre)

print(len(solutions))
