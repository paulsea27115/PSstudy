import sys
import math
n = int(sys.stdin.readline())
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    n=y-x
    sn=int(math.sqrt(n))
    c=n-sn**2
    print(2*sn+(-1 if c==0 else 0 if c<=sn else 1))
    