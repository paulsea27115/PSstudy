a, b = map(str, input().split())
m = list(a.split('.'))
use = len(m[1]) * int(b)
a = int(a.replace('.', ''))
res = str(a ** int(b))
if m[0] != '0':
    res=res[:-use]+"."+res[-use:]
else:
    em="0."
    for _ in range(0, use-len(res)):em+='0'
    res=em+res
print(res)