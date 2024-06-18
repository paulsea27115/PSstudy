print("Gnomes:")

n = int(input())

for _ in range(n):
    li = list(map(int, input().split()))
    
    first = li[0] - li[1]
    
    second = 0
    
    last = li[2] - li[1]
    
    if first <= second <= last:
        print("Ordered")
    elif last <= second <= first:
        print("Ordered")
    else:
        print("Unordered")
