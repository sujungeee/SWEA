N= int(input())
for num in range(1, N+1):
    s= ''
    cnt= 0
    for ch in str(num):
        if ch == '3' or ch == '6' or ch =='9':
            cnt+=1
        else:
            s+=ch

    if cnt!=0: # 숫자에 3또는 6또는 9가 포함되면
        sp=['-'*cnt]
        print(s.join(sp), end='')
    else:
        print(s, end='')

    print(end= ' ')