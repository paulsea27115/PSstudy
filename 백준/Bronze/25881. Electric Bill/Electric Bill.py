a, b = map(int,input().split())

for _ in range(int(input())):
    n = int(input())
    ans = 0
    
    if n <= 1000:
        ans = n * a
    else:
        ans = 1000 * a
        
        ans += (n - 1000) * b
    
    print(n, ans)