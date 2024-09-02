TC = int(input())
info = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9}

for test_case in range(1, TC + 1):
    result = 0
    N, M = map(int, input().split())
    bit_chunks = []  # 총 56개 7개씩 들어갈 배열
    passwords = []
    bitStr = ''
    score = 0

    # 1. 입력값들로부터 56 size의 가로 길이 추출하기
    for _ in range(N):
        str = input()
        strList = list(str.rstrip())
        if '1' in strList:
            revList = list(reversed(strList))
            endIdx = len(str) - 1 - revList.index('1')
            startIdx = endIdx + 1 - 56
            bitStr = str[startIdx:endIdx + 1]

    # 2. 가로 길이를 7개 단위로 자르기
    bit_chunks = [bitStr[i:i + 7] for i in range(0, len(bitStr), 7)]

    # 3. 7개 비트들을 0~9까지의 숫자로 변환
    for bits in bit_chunks:
        passwords.append(info[bits])

    # 4. 검증
    for idx, pw in enumerate(passwords):
        if idx % 2 == 0:
            score = score + (3 * pw)
        else:
            score += pw

    result = sum(passwords) if score % 10 == 0 else 0
    print(f"#{test_case} {result}")