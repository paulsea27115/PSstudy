from collections import deque
import sys
import copy

sys.setrecursionlimit(10 ** 5)

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def color(n, graph, start, check):
    dq = deque([start])

    if start[0] >= n:
        return graph

    while dq:
        y, x = dq.popleft()

        for dy, dx in direction:
            if dy + y < 0 or dx + x < 0 or dy + y >= n or dx + x >= n:
                continue
            else:
                if graph[dy + y][dx + x] == check:
                    dq.appendleft((dy + y, dx + x))
                    graph[dy + y][dx + x] = "G"

    return color(n, graph, (start[0], start[1] + 1) if start[1] + 1 < n else (start[0] + 1, 0), check)


def bfs(n, graph, start, check, res):
    dq = deque([start])

    check_res = True

    if start[0] >= n:
        return graph, res

    while dq:
        y, x = dq.popleft()

        if graph[y][x] == check:
            graph[y][x] = "X"
            if check_res:
                res += 1
                check_res = False

            for dy, dx in direction:
                if dy + y < 0 or dx + x < 0 or dy + y >= n or dx + x >= n:
                    continue
                else:
                    if graph[dy+y][dx+x] == check:
                        if check_res:
                            res += 1
                            check_res = False
                        dq.appendleft((dy+y, dx+x))

    return bfs(n, graph, (start[0], start[1] + 1) if start[1] + 1 < n else (start[0] + 1, 0), check, res)


n = int(sys.stdin.readline())

li1 = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
li2 = copy.deepcopy(li1)

res1 = 0
for word in "RGB":
    li1, res1 = bfs(n, li1, (0, 0), word, res1)

li2 = color(n, li2, (0, 0), "R")

res2 = 0
for word in "GB":
    li2, res2 = bfs(n, li2, (0, 0), word, res2)

print(res1, res2)