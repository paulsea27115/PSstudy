N,M = map(int,input().split())
li = list(map(int,input().split()))

left = 0
right = int(1e9)

while left <= right:
    mid = (right+left)//2
    em = [li[i] for i in range(N)]
    count = 0
    for i in range(N-1):
        if em[i] + mid < em[i+1]:
            count += em[i+1] - (em[i] + mid)
            em[i+1] = em[i] + mid

    for i in range(N-1, 0, -1):
        if em[i] + mid < em[i - 1]:
            count += em[i - 1] - (em[i] + mid)
            em[i - 1] = em[i] + mid
    if count <= M:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

for i in range(N-1): # 이 부분을 이해를 못하여 잘 못 풀음
    if li[i] + ans < li[i+1]:
        li[i+1] = li[i] + ans # e.x)어짜피 li[i]가 li[i+1]와 mid 만큼 차이가 있으니까 

for i in range(N-1, 0, -1):
    if li[i] + ans < li[i-1]:
        li[i-1] = li[i] + ans # 여기도 마찬가지

print(*li)