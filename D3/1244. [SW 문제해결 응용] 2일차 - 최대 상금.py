# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# import sys
# sys.stdin = open("1244-input.txt", "r")
# sys.setrecursionlimit(10**6)

# import itertools
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    b, cnt= map(int, input().split()) # 교환할 값, 교환 횟수

    num = [int(n) for n in str(b)] # 교환할 값의 배열
    dNum= sorted(num, reverse=True) # 내림차순 배열
    finArr= [] # 교환이 완료된 조합
    hDuplicate= (True if len(set(num))!=len(num) else False) # 중복이 있으면 True, 없으면 False
    comb= [i for i in range(len(num))] # num 조합 경우의 수 [0, 1, 2, 3, 4, 5]

    def swap(num, idx1, idx2):
        num[idx1], num[idx2] = num[idx2], num[idx1]
        return num

    def dfs(cnt, num, dNum, n, result, hDuplicate): # result: swap 결과
        if n == cnt: # cnt 번의 교환을 마침
            finArr.append(int(''.join(map(str, result))))
            return

        if result == dNum: # 교환 결과가 내림차순일 경우 --> 아예 return
            finArr.clear()
            if (cnt-n)%2==1 and hDuplicate==False:
                result[-1], result[-2] = result[-2], result[-1]
            finArr.append(int(''.join(map(str, result))))
            return True

        combinations=[]
        for i in range(len(comb)):
            for j in range(i + 1, len(comb)):
                combinations.append((comb[i], comb[j]))

        for combination in combinations:
            if dfs(cnt, num, dNum, n+1, swap(result.copy(), combination[0], combination[1]), hDuplicate):
                return True

    dfs(cnt, num, dNum,0, num, hDuplicate)

    print('#', end='')
    print(test_case, max(finArr))
    # ///////////////////////////////////////////////////////////////////////////////////
