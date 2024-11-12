# 4012: [모의 SW 역량테스트] 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
from itertools import combinations

def cal_combs(cursin1, cursin2):
    global answer
    sum1, sum2= 0, 0
    for cursin in combinations(cursin1, 2):
        sum1+= maps[cursin[0]-1][cursin[1]-1] + maps[cursin[1]-1][cursin[0]-1]
    for cursin in combinations(cursin2, 2):
        sum2+= maps[cursin[0]-1][cursin[1]-1] + maps[cursin[1]-1][cursin[0]-1]
    answer= min(answer, abs(sum1-sum2))
    return

TC= int(input())
for test_case in range(1, TC+1):
    answer= float('inf')
    N= int(input())
    maps= [list(map(int, input().split())) for _ in range(N)]

    combs= list(combinations(range(1, N+1), N//2))
    total_ingredient= set(range(1, N+1))

    for i in range(len(combs)//2):
        cursin1= list(combs[i])
        cursin2= list(total_ingredient - set(cursin1))
        cal_combs(cursin1, cursin2)
    print(f'#{test_case} {answer}')