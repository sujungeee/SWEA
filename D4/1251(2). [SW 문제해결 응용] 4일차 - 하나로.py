# 크루스칼 알고리즘 이용
from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    N= int(input()) # 섬의 개수
    islandX= list(map(int, input().split())) # x 좌표 모음
    islandY= list(map(int, input().split())) # y 좌표 모음
    E= float(input())

    # 0. settings
    weightSum = 0 # 가중치 합
    cnt= 0 # 간선 개수
    CPR= [i for i in range(N)] # 사이클 확인하기 위한 부모-자식 관계 배열

    # 1. 각 섬에서 섬까지의 노드 번호와 가중치^2 를 저장
    islands= []
    for i in range(N):
        for j in range(i, N):
            if i!=j:
                dWeight= (islandX[i]-islandX[j])**2 + (islandY[i]-islandY[j])**2
                islands.append((i, j, dWeight))

    # 2. 가중치^2이 작은 순서부터 오름차순으로 저장
    islands.sort(key= lambda x: x[2])
    islands= deque(islands)

    # 3. 가중치가 작은 순서부터 하나씩 꺼내어 간선의 수를 1씩 늘려감
    # (단, 사이클이 형성되지 않아야 1씩 늘릴 수 있음)
    while cnt != N-1:
        start, end, weight= islands.popleft()
        # 3-1 사이클 확인
        # start, end 와의 루트 노드 구하기
        while CPR[start]!= start:
            start= CPR[start]
        while CPR[end]!= end:
            end= CPR[end]

        # 3-2 사이클 형성하지 않으면 간선의 개수(cnt)를 1씩 늘리기
        if start!=end:
            cnt+=1
            CPR[start]= end
            weightSum+= weight

    price= int(round(E*weightSum))
    print('#', end='')
    print(test_case, price)