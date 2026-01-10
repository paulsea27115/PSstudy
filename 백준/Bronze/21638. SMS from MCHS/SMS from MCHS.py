def sol():
    s = ""
    
    if t2 < 0 and w2 >= 10:
        s = "A storm warning for tomorrow! Be careful and stay home if possible!"
    elif t1 > t2:
        s = "MCHS warns! Low temperature is expected tomorrow."
    elif w1 < w2:
        s = "MCHS warns! Strong wind is expected tomorrow."
    else:
        s = "No message"
    return s

t1, w1 = map(int,input().split())
t2, w2 = map(int,input().split())

print(sol())