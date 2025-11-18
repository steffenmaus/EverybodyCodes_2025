with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

birds = [int(x) for x in lines]

rounds = 0
move = True
while move and rounds < 10:
    move = False
    for i in range(len(birds) - 1):
        a = birds[i]
        b = birds[i + 1]
        if a > b:
            move = True
            birds[i] -= 1
            birds[i + 1] += 1
    if move:
        rounds += 1

move = True
while move and rounds < 10:
    move = False
    for i in range(len(birds) - 1):
        a = birds[i]
        b = birds[i + 1]
        if a < b:
            move = True
            birds[i] += 1
            birds[i + 1] -= 1

    if move:
        rounds += 1

total = 0
for i, n in enumerate(birds, 1):
    total += i * n
print(total)
