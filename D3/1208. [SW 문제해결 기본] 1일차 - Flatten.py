for test_case in range(1, 11):
    dump= int(input())
    boxList= list(map(int, input().split()))

    # dump가 0이 될때까지 최고 높이는 -1 최저 높이는 +1
    # 최고 높이 - 최저 높이가 1 이하이면 break
    while dump > 0:
        maxValue, maxIdx= max((value, idx) for idx, value in enumerate(boxList))
        minValue, minIdx= min((value, idx) for idx, value in enumerate(boxList))

        if maxValue - minValue <= 1:
            break
        else:
            dump -= 1
            boxList[maxIdx] -= 1
            boxList[minIdx] += 1

    diff= max(boxList) - min(boxList)
    print('#', end='')
    print(test_case, diff)