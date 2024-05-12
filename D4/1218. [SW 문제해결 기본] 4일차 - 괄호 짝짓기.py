for test_case in range(1, 11):
    n= int(input())

    inStr= input()
    isCheck=[ch for ch in inStr]

    bracket= {'(': ')', '<': '>', '[':']', '{':'}'}

    stack= []
    for i in range(n):
        if isCheck[i] in bracket:
            stack.append(isCheck[i])
        else: # 닫힌 괄호
            if len(stack)>0 and bracket[stack[-1]] == isCheck[i]:
                stack.pop()
            else:
                stack.append(1)
                break

    if len(stack)==0:
        result= 1
    else:
        result= 0

    print('#', end='')
    print(test_case, result)