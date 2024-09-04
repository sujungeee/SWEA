TC= int(input())

# 인력 계산
def calculate(mid, idx1, idx2):
  # mid 왼쪽 force 계산
  forceLeft= 0
  for idx in range(0, idx1+1):
    forceLeft+= quantityInfo[idx]/(mid-xInfo[idx])**2

  # mid 오른쪽 force 계산
  forceRight= 0
  for idx in range(idx2, N):
    forceRight+= quantityInfo[idx]/(mid-xInfo[idx])**2

  if forceLeft < forceRight:
    return True
  return False

for test_case in range(1, TC+1):
  results= []

  # 1. 입력
  N= int(input())

  lists= list(map(int, input().split()))
  xInfo= lists[:N]
  quantityInfo= lists[N:]

  # 2. 이진 탐색 시작
  for i in range(1, N):
    idx1, idx2= i-1, i
    start, end= xInfo[idx1], xInfo[idx2] # 왼쪽 x 좌표, 오른쪽 x 좌표
    while end-start > (1/(10**12)):
      mid= (start+end)/2
      if calculate(mid, idx1, idx2) == True:
        end= mid
      else:
        start= mid
    results.append(mid)

  print(f"#{test_case}", end= " ")
  for result in results:
    print("{:.10f}".format(round(result, 10)), end= " ")
  print()