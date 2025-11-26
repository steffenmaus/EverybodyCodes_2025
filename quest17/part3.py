import heapq

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


def dijkstra_with_path(start, burned, max_dist):
    out = {start: 0}
    out_paths = {start: [start]}
    Q = []
    for nei in get_all_nei(start):
        if nei not in burned:
            heapq.heappush(Q, (maze[nei], nei, start))
    while Q:
        dist, current, prev = heapq.heappop(Q)
        if dist > max_dist:
            break
        if current not in out:
            out[current] = dist
            path = out_paths[prev].copy()
            path.append(current)
            out_paths[current] = path
            for nei in get_all_nei(current):
                if nei not in burned:
                    heapq.heappush(Q, (maze[nei] + dist, nei, current))
    return out, out_paths


def dijkstra(start, burned, max_dist):
    out = {start: 0}
    Q = []
    for nei in get_all_nei(start):
        if nei not in burned:
            heapq.heappush(Q, (maze[nei], nei, start))
    while Q:
        dist, current, prev = heapq.heappop(Q)
        if dist > max_dist:
            break
        if current not in out:
            out[current] = dist
            for nei in get_all_nei(current):
                if nei not in burned:
                    heapq.heappush(Q, (maze[nei] + dist, nei, current))
    return out


X = len(lines[0])
Y = len(lines)

vulcano = None
start = None

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        if c in ["@", "S"]:
            maze[p] = 0
            if c == "@":
                vulcano = p
            if c == "S":
                start = p
        else:
            maze[p] = int(c)

Xv, Yv = vulcano

burned_after = {}
for R in range(X // 2):
    current = set()
    for Xc, Yc in maze:
        if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R:
            current.add((Xc, Yc))
    if R - 1 in burned_after:
        current |= burned_after[R - 1]
    burned_after[R] = current

left_cut = set([p for p in maze if p[0] < Xv and p[1] == Yv])
right_cut = set([p for p in maze if p[0] > Xv and p[1] == Yv])
lower_cut = set([p for p in maze if p[0] == Xv and p[1] > Yv])

t = 29
solution = None
while not solution:
    current_R = t // 30
    burned = burned_after[current_R]
    distances_from_start, paths_from_start = dijkstra_with_path(start, burned, t)

    lower_candidates = lower_cut & distances_from_start.keys()
    if not lower_candidates:
        t += 30
        continue

    min_loop_length = min([distances_from_start[p] for p in lower_candidates]) * 2
    if min_loop_length > t:
        while min_loop_length > t:
            t += 30
        continue

    solutions = set()
    for l in lower_candidates:
        path_to_lower = paths_from_start[l]
        dist_to_lower = distances_from_start[l]
        third_point_candidates = distances_from_start.keys()
        if set(path_to_lower) & left_cut:
            third_point_candidates &= right_cut
        else:
            third_point_candidates &= left_cut

        distances_from_lower = dijkstra(l, burned, t - dist_to_lower)

        for tp in third_point_candidates & distances_from_lower.keys():
            total_distance = dist_to_lower + distances_from_lower[tp] + (distances_from_start[tp] - maze[tp])
            if total_distance <= t:
                solutions.add(total_distance)

    if solutions:
        solution = current_R * min(solutions)
        break
    t += 30

print(solution)
