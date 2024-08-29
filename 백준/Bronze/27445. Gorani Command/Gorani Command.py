def check_zero():
    for i in range(n-1):
        if 0 == li[i]:
            print(i+1, 1)
            return True


    if 0 in li[n-1]:
        for i in range(len(li[n-1])):
            if li[n-1][i] == 0:
                print(n, i + 1)
                return True
    return False

def sol():
    if check_zero():
        return

    ans = [0,0]

    hori = li[0:n-1]

    ans[0] = hori.index(min(hori))
    ans[1] = li[n-1].index(min(li[n-1]))

    print(ans[0] + 1, ans[1] + 1)


n, m = map(int,input().split())

li = []

for _ in range(n):
    li.append(list(map(int,input().split())))

sol()