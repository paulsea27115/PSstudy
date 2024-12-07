import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def recognize():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if li[z][y][x] == 1:
                    dq.append((z, y, x))

def sol():
    res = 0
    for z in li:
        for y in z:
            for x in y:
                if x == 0:
                    return -1
                res = max(res, x)
    return res - 1

direction = [(0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0,-1), (-1, 0, 0), (1, 0, 0)]

M, N, H = map(int, input().split())

li = []

dq = deque([])

for i in range(H):
    li.append([list(map(int, input().split())) for j in range(N)])

recognize()

while dq:
    z, y, x = dq.popleft()

    # print(z,y,x)

    for dz, dy, dx in direction:
        if z + dz < 0 or z + dz >= H or y + dy < 0 or y + dy >= N or x + dx < 0 or x + dx >= M:
            continue
        else:
            if li[z + dz][y + dy][x + dx] == 0:
                li[z + dz][y + dy][x + dx] = li[z][y][x] + 1
                dq.append((z + dz, y + dy, x + dx))
        # print(dz, dy, dx)

print(sol())