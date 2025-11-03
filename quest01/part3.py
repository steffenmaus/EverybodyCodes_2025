with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

names = lines[0].split(",")
instructions = lines[2].split(",")
N = len(names)

for instr in instructions:
    offset = int(instr[1:])
    first = names[0]
    second = 0
    if instr.startswith("R"):
        names[0], names[offset % N] = names[offset % N], names[0]
    else:
        names[0], names[(N - offset) % N] = names[(N - offset) % N], names[0]

print(names[0])
