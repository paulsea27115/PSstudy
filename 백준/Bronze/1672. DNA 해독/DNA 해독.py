a = int(input())
s = list(input())

dna = [
    ["A","C","A","G"],
    ["C","G","T","A"],
    ["A","T","C","G"],
    ["G","A","G","T"]
]

while len(s) > 1:
    use1 = s.pop()
    use2 = s.pop()
    
    a = 0
    b = 0
    
    if use1 == "A":
        a = 0
    elif use1 == "G":
        a = 1  
    elif use1 == "C":
        a = 2
    elif use1 == "T":
        a = 3
    
    if use2 == "A":
        b = 0
    elif use2 == "G":
        b = 1  
    elif use2 == "C":
        b = 2
    elif use2 == "T":
        b = 3
    
    use1 = dna[a][b]
    
    s.append(use1)

print(s[0])
    
