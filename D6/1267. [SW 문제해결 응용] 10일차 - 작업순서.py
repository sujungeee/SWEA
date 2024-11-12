# 1267: [S/W 문제해결 응용] 10일차 - 작업순서
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN&categoryId=AV18TrIqIwUCFAZN&categoryType=CODE&problemTitle=%EC%9E%91%EC%97%85%EC%88%9C%EC%84%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
from collections import defaultdict
from collections import deque

for test_case in range(1, 11, 1):
    answers= []

    V, E= map(int, input().split())
    infos= list(map(int, input().split()))
    degrees= [0] * (V+1)

    graphs= defaultdict(list)
    for i in range(0, 2*E, 2):
        start, end= infos[i], infos[i+1]
        graphs[start].append(end)
        degrees[end]+= 1

    que= deque([])
    for i in range(1, V+1, 1):
        if degrees[i] == 0:
            que.append(i)
            answers.append(i)

    while que:
        node= que.popleft()

        for neighbor_node in graphs[node]:
            degrees[neighbor_node]-= 1
            if degrees[neighbor_node] == 0:
                answers.append(neighbor_node)
                que.append(neighbor_node)

    print(f'#{test_case}', end= ' ')
    for answer in answers:
        print(answer, end= ' ')
    print()