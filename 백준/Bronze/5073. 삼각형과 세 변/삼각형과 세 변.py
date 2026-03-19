while True:
    li = list(map(int,input().split()))
    c = tuple(set(li))
    
    if sum(li) == 0:
        break
    
    if sum(li) - max(li) <= max(li):
        print("Invalid")
    elif len(c) == 1:
        print("Equilateral")
    elif len(c) == 2:
        print("Isosceles")
    else:
        print("Scalene")