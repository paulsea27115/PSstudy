def sol():
    a = max(li)
    b = min(li)
    
    res = a - b
    
    return res

n = int(input())
li = list(map(int,input().split()))


print(sol())