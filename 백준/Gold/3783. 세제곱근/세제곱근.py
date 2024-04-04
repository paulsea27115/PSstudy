from decimal import *

getcontext().prec = 800

t = int(input())

for i in range(t):
    n = Decimal(input())
    r = str(round(n ** (Decimal("1") / Decimal("3")), 500))
    print(r[0:r.find('.') + 11])