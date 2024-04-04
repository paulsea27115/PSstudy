import sys
from collections import deque
def sol():
    w, h = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    queue = deque([])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                queue.append([i,j])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            if dx[i] + x < 0 or dx[i] + x >= w or dy[i] + y < 0 or dy[i] + y >= h:
                continue
            else:
                if graph[dy[i] + y][dx[i] + x] == 0:
                    graph[dy[i] + y][dx[i] + x] = graph[y][x] + 1
                    queue.append([dy[i] + y, dx[i] + x])
    res = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                print(-1)
                return 0
        res = max(res, max(graph[i]))
    print(res-1)
sol()