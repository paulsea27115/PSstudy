from collections import deque

res = []
graph = []
h, w = 0, 0

def bfs(dq):

    check = []

    count = 0

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while dq:
        y, x = dq.popleft()
        graph[y][x] = 0

        if x not in check:
            check.append(x)

        for dy, dx in direction:
            
            y_near, x_near = dy + y, dx + x
            
            if y_near < 0 or y_near >= h or x_near < 0 or x_near >= w:
                continue
            else:
                if graph[y_near][x_near]:
                    graph[y_near][x_near] = 0
                    dq.append((y_near, x_near))
                    
        count += 1

    for x in check:
        res[x] += count

    return 0


def solution(land):
    global res, graph, h, w

    graph = land

    h, w = len(graph), len(graph[0])

    res = [0 for _ in range(w)]

    for i in range(h):
        for j in range(w):
            if graph[i][j]:bfs(deque([(i,j)]))

    return max(res)
