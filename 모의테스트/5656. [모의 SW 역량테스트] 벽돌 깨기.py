# 5656: [모의 SW 역량테스트] 벽돌 깨기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE&problemTitle=%EB%B2%BD%EB%8F%8C+%EA%B9%A8%EA%B8%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import copy
from collections import deque
# 1. 부실 수 있는 벽돌의 y 번째 인덱스 리스트를 찾는 함수
def find_idxs(copy_maps, col):
    global H
    for row in range(H):
        if copy_maps[row][col]!= 0:
            return row
    return -1

# 2. 벽돌을 부시는 함수
def cal_range(copy_maps, row, col):
    global que
    range_num = copy_maps[row][col]
    for d in range(-range_num + 1, range_num, 1):
        if d != 0:
            if 0 <= row + d < H:
                if copy_maps[row + d][col] != 0:
                    que.append([row + d, col])
            if 0 <= col + d < W:
                if copy_maps[row][col + d] != 0:
                    que.append([row, col + d])

def breaking_bricks(copy_maps, start_row, start_col):
    global que
    que= deque([])
    cal_range(copy_maps, start_row, start_col)
    results= copy.deepcopy(copy_maps)
    results[start_row][start_col]= 0

    while que:
        x, y= que.popleft()
        cal_range(results, x, y)
        results[x][y]= 0

    return results

# 3. 벽돌이 떨어지는 함수
def drop_bricks(copy_maps):
    global W, H
    for col in range(W):
        move_bricks = deque([])
        for row in range(H):
            if copy_maps[row][col] != 0:
                move_bricks.append(copy_maps[row][col])
            copy_maps[row][col]= 0

        max_row= H - 1
        while len(move_bricks) > 0:
            brick= move_bricks.pop()
            copy_maps[max_row][col]= brick
            max_row-= 1

    return copy_maps

# 4. 남은 벽돌 개수를 세는 함수
def count_bricks(copy_maps):
    global W, H
    cnt= 0
    for i in range(H):
        for j in range(W):
            if copy_maps[i][j] != 0:
                cnt+= 1
    return cnt

# 5. 벽돌 깨트리는 게임
def dfs(cnt, copy_maps):
    global N, W, H, answer, que
    if count_bricks(copy_maps) == 0:
        answer= 0
        return

    if cnt == N:
        answer= min(answer, count_bricks(copy_maps))
        return

    for col in range(W):
        row= find_idxs(copy_maps, col)
        if row != -1:
            dfs(cnt+1, drop_bricks(breaking_bricks(copy_maps, row, col)))
    return

TC= int(input())
for test_case in range(1, TC+1):
    answer= float('inf') # 남아있는 최소한의 벽돌 개수
    N, W, H= map(int, input().split())
    maps= [list(map(int, input().split())) for _ in range(H)]
    que = deque([])

    dfs(0, maps)
    print(f'#{test_case} {answer}')