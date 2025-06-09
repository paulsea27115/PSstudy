import sys

def input():
    return sys.stdin.readline().strip()

l, p = map(int, input().split())
t = l * p

li = list(map(int, input().split()))

ans = ""

for i in range(5):
    ans += str(li[i] - t) + " "

ans.strip()

print(ans)