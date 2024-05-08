# import sys
# import itertools
#
# cnt, b= map(int, sys.stdin.readline().split())
#
# num = [int(n) for n in str(b)]
# dNum = sorted(num, reverse=True)
# print(cnt)
# print(b)
# print(num)
# print(dNum)
#
# hDuplicate= (False if len(set(num))==len(num) else True)
# print(hDuplicate)
# comb=[i for i in range(len(num))]
# def swap(num, idx1, idx2):
#     num[idx1], num[idx2] = num[idx2], num[idx1]
#     return num
#
# combinations= list(itertools.combinations(comb,2))
# for combination in combinations:
#     print('combination: ', combination)
#     print(swap(num, combination[0], combination[1]))
#
# arr1= [5, 4, 3, 3, 2, 1]
# finNum= int(''.join(map(str, arr1)))
# print(finNum)

result= [4, 9]
result[-1], result[-2] = result[-2], result[-1]
print(result)