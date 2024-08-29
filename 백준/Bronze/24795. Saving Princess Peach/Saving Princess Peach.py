n, y = map(int, input().split())

li = []

for _ in range(y):
    li.append(int(input()))

li = set(li)

for i in range(n):
    if i not in li:
        print(i)

print(f"Mario got {len(li)} of the dangerous obstacles.")