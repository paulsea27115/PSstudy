import sys

from collections import deque


def bfs(graph, v):
    global visited
    if v not in graph.keys():
        # print(v, end="")
        return 0

    d = deque([v])
    visited.append(v)

    while d:
        n = d.popleft()
        # print(n, end=" ")

        for i in graph[n]:
            if i not in visited:
                d.append(i)
                visited.append(i)

    return 0
# sys.setrecursionlimit(10000)
#
#
# def dfs(graph, v, visited):  # 재귀 ,스택
#     global list_
#
#     if v not in graph.keys():
#         list_ = visited
#         return 0
#     visited.append(v)
#     # list_.append(v)
#
#     for i in graph[v]:
#         if i not in visited:
#             dfs(graph, i, visited)
#
#     return 0


visited = []

cnt = 0

dic = dict()

p_c, l_c = map(int, sys.stdin.readline().split())

# start_num = 1

for _ in range(l_c):
    n, m = map(int, sys.stdin.readline().split())
    if n not in dic.keys():
        dic[n] = []

    if m not in dic.keys():
        dic[m] = []

    dic[n].append(m)
    dic[m].append(n)

for x in dic.keys():
    dic[x].sort()

for i in range(1, p_c + 1):
    if i not in visited:
        # print(visited, i)
        bfs(dic, i)
        cnt += 1

print(cnt)
