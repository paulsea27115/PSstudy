
def check():
    s = ""
    if a > b:
        s = "Subway"
    elif a < b:
        s = "Bus"
    else:
        s = "Anything"
    
    return s

n, a, b = map(int,input().split())

print(check())