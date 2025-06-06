import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(y: int,x: int) -> int:
    li2 = [[0 for _ in range(m)] for _ in range(n)]
    dq = deque([(y,x)])
    res = 0
    li2[y][x] = 1

    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            if 0 <= y+d[i][0] < n and 0 <= x+d[i][1] < m and li[y+d[i][0]][x+d[i][1]] == "L" and li2[y+d[i][0]][x+d[i][1]] == 0:

                li2[y+d[i][0]][x+d[i][1]] = li2[y][x] + 1

                dq.append((y+d[i][0], x+d[i][1]))

    for i in range(len(li2)):
        res = max(res, *li2[i])

    return res - 1

n, m = map(int, input().split())

li = [list("".join(input())) for _ in range(n)]

res = 0

for i in range(n):
    for ii in range(m):
        if li[i][ii] == "L":
            res = max(res, bfs(i,ii))

print(res)