def sol(area, base):
    s = "The height of the triangle is "
    ans = f"{round(area * 2 / base,2):.2f}"
    last = " units"
    
    
    
    return s + ans + last

n = int(input())

res = []

for _ in range(n):
    a, b = map(float,input().split())

    res.append(sol(a, b))

print("\n".join(res))