def check():
    check = 60
    
    same = 0;
    
    i = 1;
    
    if sum(li) != 180:
        print("Error")
    elif li[i-1] == check and li[i] == check and li[i+1] == check:
        print("Equilateral")
    else:
        if li[i-1] == li[i]:
            same += 1
        if li[i] == li[i+1]:
            same += 1
        if li[i-1] == li[i+1]:
            same += 1
        
        if same >= 1:
            print("Isosceles")
        else:
            print("Scalene")
            

li = [int(input()) for _ in range(3)]

check()