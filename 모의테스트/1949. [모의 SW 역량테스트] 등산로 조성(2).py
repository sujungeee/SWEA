# 1949: [모의 SW 역량테스트] 등산로 조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
dirs= [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque
import sys
input= sys.stdin.readline

def bfs():

    return

def backtracking(is_carve, carve_x, carve_y, x, y):
    global K

    return

TC= int(input())
for test_case in range(1, TC+1):
    answer= 0
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
        backtracking(False, 0, 0, highest_land[0], highest_land[1])

    print(f'#{test_case} {answer}')