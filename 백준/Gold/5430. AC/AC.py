import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ans = ''
    flag = False
    controller = sys.stdin.readline()

    num_c = int(sys.stdin.readline())

    li = sys.stdin.readline()[1:-2].split(',')

    if '' in li:
        li.remove('')

    for x in controller:
        if x == 'R':
            flag = not flag
        elif x == 'D':
            try:
                if flag:
                    del li[len(li)-1]
                else:
                    del li[0]
            except:
                print("error")
                break;
    else:
        if flag:
            li.reverse()
        print("[" + ",".join(li) + "]")
        continue

