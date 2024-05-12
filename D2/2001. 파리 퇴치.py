T = int(input())

for test_case in range(1, T + 1):
    N, M= map(int, input().split())

    result=[]
    arr= []*N
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N-M+1):
        for j in range(N-M+1): # start 부터
            sum= 0
            for x in range(M): # M*M 동안
                for y in range(M):
                    sum+= arr[i+x][j+y]
            result.append(sum)

    print('#', end='')
    print(test_case, max(result))