i=input
S,T=i(),i()
r,l="",len(T)
for c in S:
    r+=c
    if r[-l:]==T:r=r[:-l]
print(r)