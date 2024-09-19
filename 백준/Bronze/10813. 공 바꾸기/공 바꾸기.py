n, comm = map(int, input().split())

li = [i for i in range(1, n+1)]

for _ in range(comm):
    a,b = map(int, input().split())

    tmp = li[a-1]

    li[a-1] = li[b-1]

    li[b-1] = tmp

print(*li)