def backtracking(visited, cnt, info, distance):
    global result
    if distance >= result:
        return

    if cnt == N:  # 모든 고객을 다 방문하면 마지막 방문 고객 ~ 집까지의 거리를 합산하고 result 갱신
        result = min(result, distance + abs(house[0] - info[0]) + abs(house[1] - info[1]))
        return

    for idx, values in enumerate(customers):
        if visited[idx] == False:
            visited[idx] = True
            backtracking(visited, cnt + 1, values, distance + (abs(info[0] - values[0]) + abs(info[1] - values[1])))
            visited[idx] = False


TC = int(input())

for test_case in range(1, TC + 1):
    result = float('inf')

    N = int(input())
    infos = list(map(int, input().split()))

    # 회사, 고객들, 집
    company = infos[:2]
    customers = []
    for i in range(4, len(infos), 2):
        customers.append([infos[i], infos[i + 1]])
    house = infos[2:4]

    backtracking([False for _ in range(N)], 0, company, 0)

    print(f"#{test_case} {result}")