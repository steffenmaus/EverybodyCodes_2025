with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

input = lines[0] * 1000

total = 0
for i in range(len(input)):
    c = input[i]
    if c.islower():
        nearby = input[max(0, i - 1000): i + 1001]
        total += nearby.count(c.upper())

print(total)
