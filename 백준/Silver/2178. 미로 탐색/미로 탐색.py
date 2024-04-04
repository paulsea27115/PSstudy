import sys
from collections import deque, defaultdict


def bfs(graph, start, end):
    ans = []
    dq = deque([start])

    another = deque([])

    # print(dq)

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while dq:
        x, y = dq.popleft()

        if x == end[1] and y == end[0]:
            continue

        for dy, dx in direction:
            if dx + x >= end[1] or dx + x < 0 or dy + y >= end[0] or dy + y < 0:
                continue
            else:
                if graph[y + dy][x + dx] == 1:
                    graph[y + dy][x + dx] += graph[y][x]
                    dq.append((x + dx, y + dy))

    print(graph[end[0]-1][end[1]-1])
    
    return 0

h, w = map(int,sys.stdin.readline().split())

graph = [list(int(i) for i in input()) for _ in range(h)]

# print(graph)

bfs(graph, (0,0), (h, w))