T = int(input())

bitInfo= {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
          '0110001': 5 , '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for test_case in range(1, T + 1):
    N, M= map(int, input().split())

    arr= []
    for i in range(N):
        row= input()
        if '1' in row: # 암호 코드 구하기
            endIdx= M- row[::-1].index('1')
            password=row[endIdx-56:endIdx]

    decimalInfo= []
    # 10진수 암호 코드
    for i in range(0, 56, 7):
        bitKey= password[i:i+7]
        decimalInfo.append(bitInfo[bitKey])

    # 검증
    codeSum= 0
    for i in range(8):
        if i%2 == 1: # 짝수(인덱스는 0부터 시작)
            codeSum+= decimalInfo[i]
        else:
            codeSum+= decimalInfo[i]*3

    if codeSum%10 == 0:
        result= sum(decimalInfo)
    else:
        result= 0

    print('#', end='')
    print(test_case, result)