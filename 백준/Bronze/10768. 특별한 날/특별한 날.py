a = int(input())
b = int(input())

n = 2
m = 18

if a == n and b == m:
    print("Special")
elif a > n or a == 2 and b > m:
    print("After")
elif a < n or a == 2 and b < m:
    print("Before")