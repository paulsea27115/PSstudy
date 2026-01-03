import sys
def input():
    return sys.stdin.readline().strip()
n=int(input())
for i in range(n):
    d = {}
    l = []
    for x in list(map(str, input().split(","))):
        a, b = x.split(":")
        d[a] = int(b)
    for x in list(map(str, input().split("|"))):
        a = list(map(lambda y: d[y], x.split("&")))
        l.append(max(a))
    print(min(l))