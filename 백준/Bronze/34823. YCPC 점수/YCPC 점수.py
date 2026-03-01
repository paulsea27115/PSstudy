li=list(map(int,input().split()))
s=(1,2,1)
print(min(map((lambda x:li[x]//s[x]), range(0,3))))