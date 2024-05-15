# 프림 알고리즘 이용
import heapq

T = int(input())

for test_case in range(1, T + 1):
    N= int(input()) # 섬의 개수
    islandX= list(map(int, input().split())) # x 좌표 모음
    islandY= list(map(int, input().split())) # y 좌표 모음
    E= float(input())

    islands= []
    for i in range(N):
        for j in range(i, N):
            if i!=j:
                dWeight= (islandX[i]-islandX[j])**2 + (islandY[i]-islandY[j])**2
                islands.append((i, j, dWeight))

    # 0. settings
    hq = []
    heapq.heapify(hq)
    visited = set()
    weightSum= 0

    # 1. 0번 섬 선택
    cnt=1
    startNode= 0
    visited.add(startNode)

    # 2. 0번 섬과 연결된 섬의 가중치와 섬 번호를 heapq에 삽입
    for island in islands:
        if island[0] == startNode:
            heapq.heappush(hq, [island[2], island[1]])
        elif island[1] == startNode:
            heapq.heappush(hq, [island[2], island[0]])

    # 3. 가중치가 가장 작은 노드를 꺼내 방문되지 않았다면 -> 방문 처리를 하고
    #   꺼낸 노드와 연결된 노드들을 heapq에 삽입
    while cnt!=N:
        weight, node= heapq.heappop(hq)

        if node not in visited:
            visited.add(node)
            cnt+=1
            weightSum+= weight

            for island in islands:
                if island[0] == node:
                    heapq.heappush(hq, [island[2], island[1]])
                elif island[1] == node:
                    heapq.heappush(hq, [island[2], island[0]])

    price = int(round(E * weightSum))
    print('#', end='')
    print(test_case, price)