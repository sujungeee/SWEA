for test_case in range(1, 11):
    N= int(input())
    box= []
    for _ in range(8):
        box.append([ch for ch in input()])
    cnt= 0
    for i in range(8):
        for j in range(9-N): # 시작점
            rowCheck= [0]
            columnCheck= [0]
            for k in range(j, j+N): # 시작점 ~ 시작점+N 까지
                rowCheck.append(box[i][k])
                columnCheck.append(box[k][i])

            rowSymmetric, columnSymmetric = True, True
            for idx in range(1, int(N/2)+2):
                if rowCheck[idx] != rowCheck[-idx]:
                    rowSymmetric= False
                if columnCheck[idx] != columnCheck[-idx]:
                    columnSymmetric= False

            if rowSymmetric:
                cnt+=1
            if columnSymmetric:
                cnt+=1

    print('#', end= '')
    print(test_case, cnt)