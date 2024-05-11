T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[None] * N for _ in range(N)]

    x, y = 0, 0
    isDirs = [True, False, False, False]
    ceiling = [N - 1, N - 1, 0, 1]

    for i in range(1, (N*N)+1):
        arr[x][y] = i
        if isDirs[0]:  # 오른쪽 방향
            if y + 1 <= ceiling[0]:
                y += 1
            else: # 오른쪽 -> 아래 로 방향 전환
                isDirs[0], isDirs[1] = False, True
                x += 1
                ceiling[0] -= 1
                continue
        elif isDirs[1]:  # 아래 방향
            if x + 1 <= ceiling[1]:
                x += 1
            else: # 아래 -> 왼쪽 으로 방향 전환
                isDirs[1], isDirs[2] = False, True
                y -= 1
                ceiling[1] -= 1
                continue
        elif isDirs[2]:  # 왼쪽 방향
            if y - 1 >= ceiling[2]:
                y -= 1
            else: # 왼쪽 -> 위 로 방향 전환
                isDirs[2], isDirs[3] = False, True
                x -= 1
                ceiling[2] += 1
                continue
        elif isDirs[3]:  # 위 방향
            if x - 1 >= ceiling[3]:
                x -= 1
            else: # 위 -> 오른쪽 으로 방향 전환
                isDirs[3], isDirs[0] = False, True
                y += 1
                ceiling[3] += 1

    print('#', end='')
    print(test_case)
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()