from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def command(dq, comm):
    # print(comm)

    try:
        if comm[0] == "NUM":
            dq.append(int(comm[1]))
        elif comm[0] == "POP":
            dq.pop()
        elif comm[0] == "INV":
            n = dq.pop()
            dq.append(-n)
        elif comm[0] == "DUP":
            n = dq.pop()
            dq.append(n)
            dq.append(n)
        elif comm[0] == "SWP":
            n1 = dq.pop()
            n2 = dq.pop()
            dq.append(n1)
            dq.append(n2)
        elif comm[0] == "ADD":
            n1 = dq.pop()
            n2 = dq.pop()
            dq.append(n1 + n2)
        elif comm[0] == "SUB":
            n1 = dq.pop()
            n2 = dq.pop()
            dq.append(n2 - n1)
        elif comm[0] == "MUL":
            n1 = dq.pop()
            n2 = dq.pop()
            dq.append(n1 * n2)
        elif comm[0] == "DIV":
            n1 = dq.pop()
            n2 = dq.pop()

            if n1 < 0 and n2 < 0:
                n = -n2 // -n1
            elif n1 < 0:
                n = -1 * (n2 // -n1)
            elif n2 < 0:
                n = -1 * (-n2 // n1)
            else:
                n = n2 // n1

            dq.append(n)
        elif comm[0] == "MOD":
            n1 = dq.pop()
            n2 = dq.pop()

            if n2 > 0:
                n = abs(n2) % abs(n1)
            elif n2 < 0:
                n = abs(n2) % abs(n1)
                n *= -1
            else:
                n = n2 % n1

            dq.append(n)
    except ZeroDivisionError:
        return True
    except IndexError:
        return True


check = False

while True:
    comm = []

    i = 0
    while True:
        comm.append(input().split(" "))
        if comm[i][0] == "QUIT":
            check = True
            break
        elif comm[i][0] == "END":
            break

        i += 1

    if check:
        break

    N = int(input())

    for _ in range(N):
        dq = deque()
        dq.append(int(input()))

        for x in comm:
            if command(dq, x):
                print("ERROR")
                break
        else:
            if len(dq) != 1:
                print("ERROR")
            else:
                n = dq.pop()

                if abs(n) > 1000000000:
                    print("ERROR")
                else:
                    print(n)

    print()
