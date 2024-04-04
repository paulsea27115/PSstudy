import sys

sys.setrecursionlimit(10 ** 5)

def josephus(n):
    if n == 1:
        return 0
    if k > n:
        return (josephus(n - 1) + k) % n    
    res = josephus(n - n // k) - n % k
    return res + (n if res < 0 else res // (k - 1))

def sol():
    return (n if k == 1 else josephus(n) + 1)
    
n, k = map(int, input().split())

print(sol())