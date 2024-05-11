for _ in range(1, 11):
    N= int(input())
    can_value= []
    arr= []

    for _ in range(100): # 입력, 행의 합
        row= list(map(int, input().split()))
        arr.append(row)
        can_value.append(sum(row))

    for i in range(100): # 열의 합
        column= 0
        for j in range(100):
            column+= arr[j][i]
        can_value.append(column)

    diag1= 0 # 왼쪽 위 -> 오른쪽 아래
    diag2= 0 # 오른쪽 위 -> 왼쪽 아래
    for i in range(100): # 대각선의 합
        diag1+= arr[i][i]
        diag2+= arr[i][100-i-1]
    can_value.append(diag1)
    can_value.append(diag2)

    print('#', end='')
    print(N, max(can_value))