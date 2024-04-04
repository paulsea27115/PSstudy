import sys
from collections import deque
import copy

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_dq(graph):
    dq = deque()
    for i in range(area[0]):
        for j in range(area[1]):
            if graph[i][j] != 0:
                dq.append((i, j))
    return dq

def check_ice(graph,dq): # 빙산의 갯수
    check_graph = copy.deepcopy(graph)

    # print(check_graph)

    check_dq = deque([dq[0]])
    # print(check_dq)

    dq_len = len(dq)

    check_len = 0

    while check_dq:
        y,x = check_dq.popleft()

        check_graph[y][x] = 0

        check_len += 1

        for dx,dy in direction:
            near_y, near_x = y + dy, x + dx
            if near_y < 0 or near_y >= area[0] or near_x >= area[1] or near_x < 0:
                continue
            else:
                if check_graph[near_y][near_x] != 0:
                    check_dq.append((near_y, near_x))
                    check_graph[near_y][near_x] = 0
        # print(check_graph)
    # print(check_len, dq_len)

    if check_len != dq_len:
        return 1
    return 0
def remove_ice(graph, dq): # 빙산 녹이기

    remove_ice = copy.deepcopy(graph)

    while dq:
        y,x = dq.popleft()

        count = 0

        for dy, dx in direction:
            near_y, near_x = y + dy, x + dx
            if near_y < 0 or near_y >= area[0] or near_x >= area[1] or near_x < 0:
                continue
            else:
                if graph[near_y][near_x] == 0:
                    count += 1

        remove_ice[y][x] -= count

        if remove_ice[y][x] < 0:
            remove_ice[y][x] = 0
    return remove_ice

def sol(graph):

    check_day = 1

    target_graph = graph

    while True:

        dq = get_dq(target_graph)

        if not len(dq):
            break

        target_graph = remove_ice(target_graph, dq)

        dq = get_dq(target_graph)

        if not len(dq):
            break

        if check_ice(target_graph, dq) == 1:
            return check_day

        # print(*target_graph, check_day)

        check_day += 1

    return 0


y, x = map(int, sys.stdin.readline().split())

area = (y,x)

li = [list(map(int,sys.stdin.readline().split())) for _ in range(area[0])]

# print(li)

print(sol(li))