import sys

def input():
    return sys.stdin.readline().rstrip()

AL = ["A", "B", "C", "D", "E", "F", "G", "H"]
NUM = ["1", "2", "3", "4", "5", "6", "7", "8"]

# li = [list(0 for _ in range(0, 8)) for _ in range(0, 8)]

# (영어, 숫자)
dt = {
    "R":(0,1),
    "L":(0,-1),
    "B":(-1,0),
    "T":(1,0),
    "RT":(1,1),
    "LT":(1,-1),
    "RB":(-1,1),
    "LB":(-1,-1),
}

# y = num | x = al

king = [0, 0]
stone = [0, 0]

# 0 = 빈칸 1 = 킹 2 = 돌 

def setKing(pos_a, pos_n):
    king[0] = NUM.index(pos_n)
    king[1] = AL.index(pos_a)
    return 0

def setStone(pos_a, pos_n):
    stone[0] = NUM.index(pos_n)
    stone[1] = AL.index(pos_a)

    return 0

def check_stone(pos_a, pos_n):
    check_1 = pos_a == stone[0]
    check_2 = pos_n == stone[1]

    return check_1 and check_2

def move(move_str):
    move = [dt[move_str][0], dt[move_str][1]]
    # print(king, move)
    king_m = [king[0] + move[0], king[1] + move[1]]

    if(king_m[0] > 7 or king_m[0] < 0 or king_m[1] > 7 or king_m[1] < 0):
        return 0
    elif(check_stone(king_m[0], king_m[1])):
        stone_m = [stone[0] + move[0], stone[1] + move[1]]
        
        if(stone_m[0] > 7 or stone_m[0] < 0 or stone_m[1] > 7 or stone_m[1] < 0):
            return 0

        stone[0] = stone_m[0]
        stone[1] = stone_m[1]
        # print("확인")

    king[0] = king_m[0]
    king[1] = king_m[1]

    # print("통과")

    return 0

def print_ans():
    print(AL[king[1]]+ NUM[king[0]])
    print(AL[stone[1]]+ NUM[stone[0]])
    return 0

k, s, c = map(str,input().split())

setKing(k[0], k[1])
setStone(s[0], s[1])

for i in range(int(c)):
    use = input()

    move(use)

print_ans()
