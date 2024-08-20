import sys
import math
from queue import PriorityQueue

V, E = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline())

node = [[] for _ in range(V + 1)]
value = [math.inf for _ in range(V+1)]

value[K] = 0

pq = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    node[u].append([v, w])

pq.put((0,K))

while not pq.empty():
    x, u = pq.get()

    for i in range(len(node[u])):
        v = node[u][i][0]
        w = node[u][i][1]

        if x + w < value[v]:
            value[v] = x + w
            pq.put((x + w, v))

for i in range(1,V+1):
    if value[i] == math.inf:
        print("INF")
    else:
        print(value[i])