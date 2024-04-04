import sys
def xor(s, f):
    def xor_up(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0

    result = xor_up(f) ^ xor_up(s - 1)
    return result

T = int(sys.stdin.readline())

for _ in range(T):
    S, F = map(int, sys.stdin.readline().split())

    result = xor(S, F)
    print(result)