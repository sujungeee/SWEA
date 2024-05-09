for test_case in range(1, 11):
    total= 0
    N= int(input())
    buildings= list(map(int, input().split()))

    for idx in range(2, N-2):
        cur= buildings[idx] # 현재 위치의 층수
        maxNum= max(buildings[idx-2],buildings[idx-1],buildings[idx+1],buildings[idx+2])
        if cur-maxNum>0:
            total= total + (cur - maxNum)

    print('#', end='')
    print(test_case, total)