import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n, turn = map(int, input().split())

li = [i for i in range(1,n+1)]

for _ in range(turn):
    a,b = map(int, input().split())

    dq = deque()

    num = b - a

    for i in range(a-1, b):
        dq.append(li[i])

    for i in range(len(dq)):
        li[a-1+i] = dq[len(dq) - i - 1]

print(*li)