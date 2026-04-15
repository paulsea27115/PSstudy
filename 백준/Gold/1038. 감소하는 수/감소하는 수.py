import sys
from itertools import combinations

def input():
    return sys.stdin.readline().strip()

use_nums = [9,8,7,6,5,4,3,2,1,0]

li = []

for i in range(10,-1,-1):
    comb = list(combinations(use_nums, i))

    for x in comb:
        x = list(map(str, x))
        x = "".join(x)

        li.append(x)

n = int(input())

if n >= 1023:
    print(-1)
else:
    print(li[1022-n])