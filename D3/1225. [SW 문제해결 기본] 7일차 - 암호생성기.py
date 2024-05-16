from collections import deque

for _ in range(10):
    N= int(input())
    pwArray= deque(list(map(int, input().split())))

    while 0 not in pwArray:
        for i in range(1, 6): # 한 사이클
            startNum= pwArray.popleft()
            endNum= startNum-i
            pwArray.append(endNum)
            if pwArray[-1]<=0:
                pwArray[-1]= 0
                break

    print('#', end='')
    print(N, end= ' ')
    for pw in pwArray:
        if pw == 0:
            print(pw)
        else:
            print(pw, end=' ')