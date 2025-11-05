with open('input3.txt') as file:
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


def validate(p):
    a, b = (0, 0)
    for _ in range(100):
        a, b = mult((a, b), (a, b))
        a, b = div((a, b), (100000, 100000))
        a, b = add((a, b), p)
        if not a in range(-1000000, 1000000 + 1) or b not in range(-1000000, 1000000 + 1):
            return False
    return True


A = [int(x) for x in lines[0][3:-1].split(",")]

total = 0
for x in range(A[0], A[0] + 1001):
    for y in range(A[1], A[1] + 1001):
        if validate((x, y)):
            total += validate((x, y))

print(total)
