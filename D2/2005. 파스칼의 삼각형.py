T= int(input())

for test_case in range(1, T+1):
    N= int(input())
    arr= [[0] for _ in range(N)]

    arr[0].append(1)
    arr[0].append(0)

    for i in range(1, N):
        for j in range(1, i+2):
            arr[i].append(arr[i-1][j-1] + arr[i-1][j])
        arr[i].append(0)

    print('#', end='')
    print(test_case)
    for i in range(N):
        for j in range(1, len(arr[i])-1):
            print(arr[i][j], end= ' ')
        print()