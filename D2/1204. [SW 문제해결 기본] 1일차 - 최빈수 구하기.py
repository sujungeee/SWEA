from collections import Counter

T = int(input())

for _ in range(1, T + 1):
    N= int(input())
    score= list(map(int, input().split()))

    counter= Counter(score)
    print('#', end='')
    print(N, counter.most_common()[0][0])
