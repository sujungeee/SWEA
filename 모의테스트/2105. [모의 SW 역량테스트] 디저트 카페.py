# 2105: [모의 SW 역량테스트] 디저트 카페
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
dirs= [[1, 1], [1, -1], [-1, -1], [-1, 1]] # 대각선 dirs

# 1. 만들어진 사각형이 투어를 돌 수 있는지 확인하는 함수
def is_tour(squares):
    return len(squares) == len(set(squares))

def make_square(x, y):
    global answer, N
    # x, y 로부터 사각형 만들기
    max_width= N - 1 - y
    max_height= y

    for width in range(1, max_width+1):
        for height in range(1, max_height+1):
            square = []
            if (0 <= x + width + height < N and
                    0 <= y - height < N and
                    0 <= y + width < N):

                # 사각형 채우기
                newx, newy= x, y
                for idx, dir in enumerate(dirs):
                    steps= width if idx % 2 == 0 else height
                    for _ in range(steps):
                        newx += dir[0]
                        newy += dir[1]
                        if not (0 <= newx < N and 0 <= newy < N):
                            break
                        square.append(maps[newx][newy])
                    else:
                        continue
                    break

                if is_tour(square):
                    answer= max(answer, len(square))

    return

TC= int(input())
for test_case in range(1, TC+1):
    answer= -1
    N= int(input())
    maps= []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    for i in range(N-2):
        for j in range(1, N-1):
            make_square(i, j)

    print(f'#{test_case} {answer}')