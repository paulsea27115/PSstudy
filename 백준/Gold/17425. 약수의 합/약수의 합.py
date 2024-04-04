import sys
prime = [0 for _ in range(0,1000001)]
for i in range(1,len(prime)):
    for j in range(i, len(prime), i): # 자신이 약수로 들어 있는 수의 갯수를 카운트
        prime[j] += i
for i in range(2,len(prime)): # 누적합
    prime[i] += prime[i-1]

T = int(input())
i = 0
while i < T:
    n = int(sys.stdin.readline())
    print(prime[n])
    i += 1