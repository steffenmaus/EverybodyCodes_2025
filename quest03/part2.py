with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

crates = [int(x) for x in lines[0].split(",")]

best = sorted(list(set(crates)))[:20]

print(sum(best))
