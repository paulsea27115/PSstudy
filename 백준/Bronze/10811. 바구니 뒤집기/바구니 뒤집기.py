import sys

def input():
    return sys.stdin.readline().rstrip()


n, turn = map(int, input().split())

li = [i for i in range(1,n+1)]

for _ in range(turn):
    a,b = map(int, input().split())

    test = []

    for i in range(a-1, b):
        test.append(li[i])

    for i in range(len(test)):
        li[i + a - 1] = test[len(test) - i - 1]


print(*li)