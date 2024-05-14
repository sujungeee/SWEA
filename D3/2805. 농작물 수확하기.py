T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    sqaure = [] * N
    for _ in range(N):
        values = input()
        sqaure.append([int(value) for value in values])

    sqaureSum = 0
    center = (N - 1) // 2

    for i in range(N):
        if i <= center:
            start = center - i
            end = center + i
        else:
            start = center - (N- 1 - i)
            end = center + (N- 1- i)

        for j in range(start, end+1, 1):
            sqaureSum += sqaure[i][j]

    print('#', end='')
    print(test_case, sqaureSum)