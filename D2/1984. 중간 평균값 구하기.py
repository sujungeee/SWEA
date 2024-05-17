T= int(input())

for test_case in range(1, T+1):
    numList= list(map(int, input().split()))

    minNum= min(numList)
    maxNum= max(numList)

    numList.remove(minNum)
    numList.remove(maxNum)

    result= int(round(sum(numList)/8.0))

    print('#', end='')
    print(test_case, result)