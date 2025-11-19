with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


class Node:
    def __init__(self, a, b, reverse):
        self.a = a
        self.b = b
        self.reverse = reverse
        self.next = None
        self.prev = None


root = Node(1, 1, False)
most_right = root
most_left = root

right = True
for l in lines:
    a, b = l.split("-")
    a = int(a)
    b = int(b)
    if right:
        inter = Node(a, b, False)
        inter.prev = most_right
        most_right.next = inter
        most_right = inter
    else:
        inter = Node(a, b, True)
        inter.next = most_left
        most_left.prev = inter
        most_left = inter
    right = not right

most_right.next = most_left
most_left.prev = most_right

turns = 202520252025
current = root
while current.b - current.a + 1 < turns:
    turns -= current.b - current.a + 1
    current = current.next

detail = list(range(current.a, current.b + 1))
if current.reverse:
    detail = detail[::-1]

print(detail[turns])
