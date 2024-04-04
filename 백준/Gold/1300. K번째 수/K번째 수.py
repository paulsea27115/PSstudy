n = int(input())
k = int(input())
# 원하는 수의 조건
# 2차원 베열의 작은 수의 갯수가 k - 1 이하 여야됨
# 2차원 베열의 큰 수의 갯수가 n * n - k 이하 여야됨

def small(x):
    x_s = 0
    for i in range(1, n+1):
        x_s += min(n, (x - 1) // i) # i 번째 행에서 x보다 작은 수의 갯수
    return x_s

def big(x):
    x_b = 0
    for i in range(1,n+1):
        x_b += n - min(n, x // i) # i 번째 행에서 x보다 큰수의 갯수
    return x_b

low = 1
high = min(n*n,int(1e9))
ans = -1
while low <= high:
    mid = (high + low) // 2
    if small(mid) > k-1: # mid 보다 작은 값이 많으면
        high = mid - 1
    elif big(mid) > n * n - k: # mid 보다 큰수가 많으면
        low = mid + 1
    else:
        # mid 보다 작은 수가 k-1개여야 하고 튼수가 n*n-k개 이하 이면 k번째 수 이다.
        ans = mid
        break

print(ans)