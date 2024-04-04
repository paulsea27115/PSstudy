li = list(tuple(map(int,input().split())) for _ in range(3))
# (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1)
res = ((li[1][0] - li[0][0]) * (li[2][1] - li[0][1])) - ((li[2][0] - li[0][0]) * (li[1][1] - li[0][1]))

if res > 0:
    print(1)
elif res == 0:
    print(0)
elif res < 0:
    print(-1)