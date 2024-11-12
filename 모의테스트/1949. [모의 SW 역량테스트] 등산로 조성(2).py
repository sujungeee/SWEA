# 1949: [모의 SW 역량테스트] 등산로 조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
"""
    1. 한 가장 높은 봉우리에 적용
        1-1. 한 봉우리에서 사방탐색을 하여 기존 좌표보다 새 좌표가 낮으면 다음 가능한 좌표 재귀로 호출
        1-2. 한 봉우리에서 사방탐색을 하여 기존 좌표보다 새 좌표가 같거나 높으면 한 번 깎기
"""
dirs= [[0, 1], [0, -1], [1, 0], [-1, 0]]

def backtracking(is_carve, x, y, length, maps, visited):
    global N, K, max_length
    max_length= max(max_length, length)

    for dir in dirs:
        newx, newy= x + dir[0], y + dir[1]
        if 0 > newx or newx >= N or 0 > newy or newy >= N or visited[newx][newy]: continue
        new_value= maps[newx][newy]
        if maps[x][y] > new_value:
            visited[newx][newy]= True
            backtracking(is_carve, newx, newy, length+1, maps, visited)
            visited[newx][newy]= False
        else:
            if not is_carve:
                for carve_num in range(1, K+1):
                    if maps[newx][newy] - carve_num >= 0 and maps[newx][newy] - carve_num < maps[x][y]:
                        visited[newx][newy]= True
                        maps[newx][newy]-= carve_num
                        backtracking(True, newx, newy, length+1, maps, visited)
                        visited[newx][newy]= False
                        maps[newx][newy]+= carve_num

    return

TC= int(input())
for test_case in range(1, TC+1):
    max_length= 0
    highest_lands= [] # 가장 높은 봉우리를 가진 부지의 좌표
    highest_depth= 0 # 가장 높은 봉우리

    N, K= map(int, input().split())
    maps= []
    for i in range(N):
        tmps= list(map(int, input().split()))
        for j in range(N):
            if highest_depth < tmps[j]:
                highest_depth= tmps[j]
                highest_lands= [[i, j]]
            elif highest_depth == tmps[j]:
                highest_lands.append([i, j])
        maps.append(tmps)

    for highest_land in highest_lands:
        visited = [[False] * N for _ in range(N)]
        visited[highest_land[0]][highest_land[1]]= True
        backtracking(False, highest_land[0], highest_land[1], 1, maps, visited)

    print(f'#{test_case} {max_length}')