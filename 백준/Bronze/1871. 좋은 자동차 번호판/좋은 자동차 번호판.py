def sol(s, n):
    ans = ""
    
    n = int(n)
    
    min_n = ord("A")
    
    num = 0

    for i in range(len(s),):
        num += (ord(s[i]) - min_n ) * (26 ** (2-i))
    
    if abs(num-n) <= 100:
        ans = "nice"
    else:
        ans = "not nice"
    
    return ans

for _ in range(int(input())):
    a, b = map(str,input().split("-"))
    print(sol(a, b))