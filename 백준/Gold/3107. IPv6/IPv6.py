em = []

def sol1(sum):
    n = list(filter(None,map(str, sum.split(":"))))
    for item in n:
        item = "0" * (4 - len(item)) + item;
        em.append(item)
    for i in range(0,7):
        em[i]+=":"
        print(em[i],end='')
    print(em[7], end='')

def sol2():
    cnt=0
    for i in sum.split("::"):
        n = list(map(str,i.split(':')))
        for i in n:
            if i=='':
                continue
            cnt+=1
    for i in range(len(sum)):
        if sum[i]==":" and sum[i+1] == ":":
            num = sum[:i]+":0000"*(8-cnt)+":"+sum[i+2:]
            break;
    sol1(num)

sum = input()
sol2() if sum.__contains__("::") else sol1(sum)