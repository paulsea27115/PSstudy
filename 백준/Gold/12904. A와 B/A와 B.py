def sol(n, m):
    while len(n) != len(m):
        if m[len(m)-1] == "B":
            del m[len(m)-1]
            m = m[::-1]
        else:
            del m[len(m)-1]
    print(1 if m == n else 0)


n = list(input())
m = list(input())

sol(n, m)