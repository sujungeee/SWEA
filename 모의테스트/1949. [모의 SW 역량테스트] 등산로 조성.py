T= int(input())
 
for test_case in range(1, T+1):
  dirs= [[0, 1], [0, -1], [1, 0], [-1, 0]]
  results= []
   
  # 입력
  N, K= map(int, input().split())
  maps= []
  for _ in range(N):
    maps.append(list(map(int, input().split())))
 
  # dfs()
  def dfs(x, y, visited, prev, cnt):
    global maps
    results.append(cnt)
     
    for dir in dirs:
      newx= x + dir[0]
      newy= y + dir[1]
       
      if 0<=newx<N and 0<=newy<N and visited[newx][newy] == False and prev > maps[newx][newy]:
        visited[newx][newy]= True
        dfs(newx, newy, visited, maps[newx][newy], cnt+1)
        visited[newx][newy]= False
    return
   
  # enter()
  def enter(x, y, value):
    global maps
     
    for k in range(K+1):
      for i in range(N):
        for j in range(N):
          if i==x and j==y:
            continue
          maps[i][j]-=k
          visited= [[False for _ in range(N)] for _ in range(N)]
          visited[x][y]= True
          dfs(x, y, visited, value, 1)
          maps[i][j]+=k
    return
     
  # 최댓값인 경우 탐색 대상
  max_value = max(max(row) for row in maps)
  for i in range(N):
    for j in range(N):
      if maps[i][j] == max_value:
        enter(i, j, maps[i][j])
   
  print(f"#{test_case} {max(results)}")