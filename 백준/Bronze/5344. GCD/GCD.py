def euclidean(a, b):
    mod_res = a % b
    if mod_res == 0:
        return b 
    return euclidean(b, mod_res)

n = int(input())

for _ in range(n):
    li = list(map(int,input().split()))
    
    a = 0
    b = 0
    
    if li[0] >= li[1]:
        a = li[0]
        b = li[1]
    else:
        a = li[1]
        b = li[0]
        
    res = euclidean(a,b)
    
    print(res)