a, b = map(int,input().split())

li = []

for i in range(1, a + 1):
    if a % i == 0:
        li.append(i)

if len(li) < b:
    print(0)
else:
    print(li[b-1])