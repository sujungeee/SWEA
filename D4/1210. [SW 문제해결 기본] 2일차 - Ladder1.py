# 10개에 대한 테케를 각각 출력

# 위에서부터 찾는게 아니라 2(목적지)부터 거슬러 올라가서 x 좌표를 찾기

for _ in range(1, 11):
    N= int(input())
    firstLadder= list(map(int, input().split()))
    n= len(firstLadder)

    ladderList= [ [0]*3 for _ in range(n)]
    ladderList[0][1:2]= firstLadder
    for i in range(1, n):
        ladderList[i][1:2]= list(map(int, input().split()))

    destIdx= ladderList[-1].index(2)
    x, y= n-1, destIdx # start

    direction= [True, True] # 좌, 우
    while x>0:
        # 올라갈 수 있는 방향 찾기 (1st. 좌(y-1) or 우(y+1), 2nd. 위(x-1))
        if ladderList[x][y-1] == 1 and direction[0] == True: # 좌
            y= y-1
            direction[1]= False
            continue
        elif ladderList[x][y+1] == 1 and direction[1] == True: # 우
            y= y+1
            direction[0]= False
            continue
        else: # 위
            x= x-1
            direction[0], direction[1]= True, True

    print('#', end='')
    print(N, y-1)