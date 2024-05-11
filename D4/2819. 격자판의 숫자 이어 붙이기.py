T = int(input())

for test_case in range(1, T + 1):
    result= set()
    arr= []
    for _ in range(4):
        arr.append(list(input().split()))

    dirs= [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북
    def bt(cnt, num, x, y):
        if cnt == 7:
            result.add(num)
            return

        for dir in dirs:
            newx, newy= x+dir[0], y+dir[1]
            if 0<= newx <4 and 0<= newy <4:
                num+= arr[newx][newy]
                bt(cnt+1, num, newx, newy)
                num= num[:-1]

    for i in range(4):
        for j in range(4):
            bt(0, '', i, j)

    print('#', end='')
    print(test_case, len(result))