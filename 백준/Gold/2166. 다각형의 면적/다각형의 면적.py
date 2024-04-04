n = int(input())
li = []
for _ in range(0,n):
    li.append(list(map(int, input().split())))

li.append(li[0])

res,res1,res2 = 0,0,0
i = 0
j = 1
while i != len(li)-1:
    res1 += li[i][0]*li[i+1][1]
    res2 += li[j][0]*li[j-1][1]
    i+=1
    j+=1
res = res1 - res2
res = -res if res < 0 else res
res = res / 2

print(round(res,1))