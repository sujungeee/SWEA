T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    days= int(input())
    daysList= list(map(int, input().split()))
    n= days-1 # daysList의 끝 인덱스
    score=0 # 점수

    while n > 0:
        standValue= daysList[n] # 기준 값
        cnt= 0 # 기준 값(standValue)보다 작은 개수
        i=n-1 # 기준 값의 왼쪽부터 비교
        while standValue >= daysList[i]:
            cnt+=1
            score -= daysList[i]
            i-=1
            if i == -1:
                break
        score= score+ (cnt*standValue)
        n= n-cnt-1

    print('#', end='')
    print(test_case, score)
    # ///////////////////////////////////////////////////////////////////////////////////
