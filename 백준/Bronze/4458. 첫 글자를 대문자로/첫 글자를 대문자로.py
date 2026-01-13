n = int(input())

for _ in range(n):
    s = input()
    
    a = s[0]
    
    if ord("a") <= ord(a) and ord(a) <= ord("z"):
        a = chr(ord(a) - 32)
        s = a + s[1:]
    
    print(s)