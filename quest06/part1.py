with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

input = lines[0]

total = 0
for i in range(len(input)):
    if input[i] == "A":
        total += input[i:].count("a")

print(total)
