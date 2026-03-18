l=[list(map(int,input().split())) for _ in range(2)]

print(1 if l[0][0] <= l[1][0] / l[1][1] else 0)