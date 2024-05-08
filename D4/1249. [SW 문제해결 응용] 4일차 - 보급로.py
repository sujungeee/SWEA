from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    nn= int(input())
    path= [[] for _ in range(nn)]
    costPath= [[float('inf')]*nn for _ in range(nn)]
    costPath[0][0] = 0

    direction= [[0,-1], [0,1], [-1,0], [1,0]]

    for i in range(nn):
        info= input()
        path[i]= [int(ch) for ch in info]

    queue= deque()
    queue.append([0,0,0])

    while queue:
        x, y, cost= queue.popleft()
        for dir in direction:
            newx, newy= x+dir[0], y+dir[1]

            if 0<= newx<nn and 0<=newy<nn:
                newCost = cost + path[newx][newy]
                if costPath[newx][newy] > newCost:
                    costPath[newx][newy]= newCost
                    queue.append([newx, newy, newCost])

    print('#', end='')
    print(test_case, costPath[-1][-1])
    # ///////////////////////////////////////////////////////////////////////////////////
