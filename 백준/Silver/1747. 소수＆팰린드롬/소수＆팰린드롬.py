prime = [True] * 1003002
prime[1] = False
for i in range(2, len(prime)):
    if prime[i] == True:
        for j in range(i + i, len(prime), i):
            prime[j] = False
n = int(input())
while True:
    if prime[n] and str(n)[::] == str(n)[::-1]:
        print(n)
        break
    n += 1
