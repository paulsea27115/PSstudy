days, stress = map(int, input().split())

li = list(map(int, input().split()))

s = []
s.append(li[0] if li[0] >= 0 else 0)

for i in range(1,len(li)):
    s.append(s[i-1] + li[i] if s[i-1] + li[i] >= 0 else 0)

res = 0

for x in s:
    if x >= stress:
        res += 1

print(res)