with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

names = lines[0].split(",")
instructions = lines[2].split(",")
N = len(names)

pointer = 0
for instr in instructions:
    offset = int(instr[1:])
    if instr.startswith("R"):
        pointer += offset
    else:
        pointer -= offset

pointer%=N

print(names[pointer])
