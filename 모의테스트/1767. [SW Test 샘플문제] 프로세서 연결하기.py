# 1767: [SW Test 샘플문제] 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
dirs= [[0, 1], [0, -1], [1, 0], [-1, 0]] # 직선 방향

# 코어에서부터 특정 방향에 다른 코어가 없는지 확인하는 함수, 다른 코어가 없으면 전선을 채워야 할 정보를 return함
def is_connect(dir, core):
    global N, maps
    x, y= core[0], core[1]
    new_apply= []
    while 0<=x<N and 0<=y<N:
        x, y = x + dir[0], y + dir[1]
        if x < 0 or y < 0 or x >= N or y >= N:
            break
        new_apply.append([x, y])
        if maps[x][y] == 1:
            return False
    return new_apply

# 연결할 때 소모되는 전선 개수를 구하는 함수
def connect(results):
    global maps
    for result in results:
        maps[result[0]][result[1]]^= 1

# 코어가 가장 자리에 있는지 확인하는 함수
def is_edge(core):
    global N
    return core[0] == 0 or core[0] == N-1 or core[1] == 0 or core[1] == N-1

def backtracking(idx, core_cnt, wire_cnt):
    global max_core, min_wire, total_core_cnt

    if max_core < core_cnt:
        max_core= core_cnt
        min_wire= wire_cnt
    elif max_core == core_cnt:
        if min_wire > wire_cnt:
            min_wire= wire_cnt

    if idx == total_core_cnt:
        return

    if is_edge(cores[idx]):
        backtracking(idx + 1, core_cnt + 1, wire_cnt)
    else:
        for dir in dirs:
            results= is_connect(dir, cores[idx])
            if results:
                connect(results)
                backtracking(idx + 1, core_cnt + 1, wire_cnt + len(results))
                connect(results)

        backtracking(idx + 1, core_cnt, wire_cnt)

TC= int(input())
for test_case in range(1, TC+1):
    max_core, min_wire= 0, float('inf')
    N= int(input())
    cores= []
    total_core_cnt= 0
    maps= []
    for idx1 in range(N):
        tmps= list(map(int, input().split()))
        for idx2, tmp in enumerate(tmps):
            if tmp == 1:
                cores.append([idx1, idx2])
                total_core_cnt+= 1
        maps.append(tmps)

    backtracking(0, 0, 0)
    print(f'#{test_case} {min_wire}')