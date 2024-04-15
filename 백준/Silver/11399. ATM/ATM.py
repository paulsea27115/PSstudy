n=int(input())
l=sorted(list(map(int,input().split())))
a=[l[0]]
for i in range(1,n):a.append(a[i-1] + l[i])
print(sum(a))