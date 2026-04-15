import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    
    res = 0
    
    num = y - x
    
    sqrt_natural = math.floor(math.sqrt(num))
    
    natural = sqrt_natural ** 2
    
    check = num - natural 
    
    # print("----", num, sqrt_natural, check, natural)
    
    if check == 0:
        res = 2 * sqrt_natural - 1
    elif check <= sqrt_natural:
        res = 2 * sqrt_natural
    else:
        res = 2 * sqrt_natural + 1
    
    print(res)
    