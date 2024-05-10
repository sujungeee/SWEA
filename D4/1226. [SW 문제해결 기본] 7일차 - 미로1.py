from collections import deque

for _ in range(1, 11):
    N= int(input())
    goal= 0

    maze= []
    for i in range(16):
        maze.append([int(i) for i in input()])

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우

    visited= [[False]*16 for _ in range(16)] # visited
    visited[1][1]= True

    que= deque()
    que.append([1,1,visited]) # start

    while que:
        x, y, visited= que.popleft()
        if maze[x][y] == 3:
            goal= 1
            break

        for d in direction:
            newx, newy= x+d[0], y+d[1]

            if 0<=newx<16 and 0<=newy<16 and maze[newx][newy]!=1:
                if not visited[newx][newy]:
                    visited[newx][newy]= True
                    que.append([newx, newy, visited])

    print('#', end='')
    print(N, goal)