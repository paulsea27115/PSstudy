li = [int(input()) for _ in range(6)]

n1 = sum(li[:4]) - min(li[:4])

n2 = sum(li[4:]) - min(li[4:])

print(n1 + n2)