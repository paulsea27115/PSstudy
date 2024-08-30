n, k, b = map(int,input().split())

li = list(map(int, input().split()))

i = b % n

res = 0

while k != 0:
    if i > n:
        i = 1

    res += li[i-1]

    i += 1
    k -= 1

print(res)