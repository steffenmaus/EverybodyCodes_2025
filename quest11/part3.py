with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

birds = [int(x) for x in lines]
# birds already strictly ordered, only second phase required
# this results in a constant drain across all columns (until saturation)

avg = sum(birds) / len(birds) # target value for each column
deltas = [abs(avg - x) for x in birds] # I/O required per column
total = sum(deltas) // 2 # input of one column == output of neighbor column

print(total)
