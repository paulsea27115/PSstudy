li = []

for i in range(0,5):
    s = input()
    
    try:    
        if s.index("FBI") < 99999:
            li.append(str(i+1))
    except:
        pass

print("HE GOT AWAY!" if not li else " ".join(li))