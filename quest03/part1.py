with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

crates = [int(x) for x in lines[0].split(",")]

print(sum(set(crates)))
