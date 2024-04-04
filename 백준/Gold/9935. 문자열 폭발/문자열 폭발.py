import sys
n = sys.stdin.readline().rstrip()
use = sys.stdin.readline().rstrip()

len_use = len(use)
stack = []

for i in range(len(n)):
    stack.append(n[i])
    if "".join(stack[-len_use:]) == use:
        for _ in range(len_use):stack.pop()

print("".join(stack) if stack else "FRULA")