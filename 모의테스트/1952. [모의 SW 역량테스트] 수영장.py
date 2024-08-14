# 백트래킹으로 풀기
T = int(input())
for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    months = list(map(int, input().split()))
    min_cost = prices[3]


    def dfs(idx, cost):
        global min_cost
        if idx >= 12:
            min_cost = min(min_cost, cost)
            return
        # 1일
        dfs(idx + 1, cost + prices[0] * months[idx])

        # 1달
        dfs(idx + 1, cost + prices[1])

        # 3달
        dfs(idx + 3, cost + prices[2])

    dfs(0, 0)
    print(f"#{test_case} {min_cost}")