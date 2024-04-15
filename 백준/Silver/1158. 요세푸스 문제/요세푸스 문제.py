def sol():
    i, idx = -1, 0
    if k == 1:
        print("<" + ", ".join(map(str, numbers)) + ">")
        return 0
    while len(put_num) < n:
        if i >= len(numbers):
            i = 0
            continue
        idx += 1
        i += 1
        if idx == k:
            if i > len(numbers) - 1:
                i = 0
            put_num.append(numbers[i])
            del numbers[i]
            idx = 1
    print("<" + ", ".join(map(str, put_num)) + ">")
n, k = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
put_num = []
sol()