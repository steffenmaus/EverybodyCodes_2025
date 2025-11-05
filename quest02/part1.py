with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def add(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 + x2, y1 + y2)


def mult(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)


def div(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (int(x1 / x2), int(y1 / y2))  # x1//x2 will NOT work for negative numbers...


A = [int(x) for x in lines[0][3:-1].split(",")]
R = (0, 0)

for _ in range(3):
    R = mult(R, R)
    R = div(R, (10, 10))
    R = add(R, A)

out = str(list(R)).replace(" ", "")
print(out)
