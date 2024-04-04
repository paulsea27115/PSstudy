import sys

n = int(sys.stdin.readline())

li = []

for _ in range(0,n):
    li.append(int(sys.stdin.readline()))

li.sort()

ans = []

for i in range(1,len(li)-1):
    selected1 = [li[i-1], li[i], li[-1]]
    selected2 = [li[0], li[i], li[i+1]]
    ans.append(abs(sum(selected1) - (selected1[1]*3)))
    ans.append(abs(sum(selected2) - (selected2[1]*3)))


print(max(ans))