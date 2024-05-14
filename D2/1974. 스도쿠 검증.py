T = int(input())

for test_case in range(1, T + 1):
    sudoku= []
    result= 1
    for _ in range(9):
        row= list(map(int, input().split()))
        sudoku.append(row)
        if len(set(row)) != 9: # 모든 행에서 겹치는 숫자가 있는지
            result= 0

    # 모든 열에서 겹치는 숫자가 있는지
    for i in range(9):
        rowCheck= set()
        for j in range(9):
            rowCheck.add(sudoku[j][i])
        if len(rowCheck) != 9:
            result= 0

    # 모든 3X3에서 겹치는 숫자가 있는지
    for i in range(0,9,3):
        sqCheck = set()
        for j in range(i,i+3):
            for k in range(i,i+3):
                sqCheck.add(sudoku[j][k])
        if len(sqCheck) != 9:
            result= 0


    print('#', end='')
    print(test_case, result)