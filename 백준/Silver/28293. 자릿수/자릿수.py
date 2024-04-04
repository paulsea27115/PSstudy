import math
import sys

M, p = map(int, sys.stdin.readline().split())

print(math.floor(p * math.log10(M))+1)