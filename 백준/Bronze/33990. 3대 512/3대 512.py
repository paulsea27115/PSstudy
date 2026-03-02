li = [sum(map(int, input().split())) for _ in range(int(input()))]

print(list(map(lambda x: x if x >= 512 else -1, sorted(li, key=lambda x: x if x >= 512 else 999)))[0])