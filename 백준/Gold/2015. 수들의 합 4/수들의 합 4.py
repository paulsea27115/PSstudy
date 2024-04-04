import sys

def no(em):
    res = [0 for _ in range(N)]
    res[0] = em[0]
    for i in range(1, len(em)):
        res[i] = em[i] + res[i - 1]
    # print(res)
    return res


def sol(li_func, test):
    use = no(li_func)

    cnt = {}
    ans = 0
    for i in range(N):
        check = use[i] - test
        if check in cnt:
            ans += cnt[check]
        if check == 0:
            ans += 1
        if use[i] not in cnt:
            cnt[use[i]] = 0
        cnt[use[i]] += 1
        # print(check, cnt)
    print(ans)

N, K = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

sol(li, K)
