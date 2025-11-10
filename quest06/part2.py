with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

input = lines[0]

total = 0
for i in range(len(input)):
    c = input[i]
    if c.isupper():
        total += input[i:].count(c.lower())

print(total)
