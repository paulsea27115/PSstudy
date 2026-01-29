n = input()
use = input()

len_use = len(use)
stack = []

for i in range(len(n)):
    stack.append(n[i])
    if "".join(stack[-len_use:]) == use:
        for _ in range(len_use):
            stack.pop()

print("".join(stack))