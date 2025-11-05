from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

crates = [int(x) for x in lines[0].split(",")]

count = defaultdict(int)
for c in crates:
    count[c] += 1

print(max(count.values()))
