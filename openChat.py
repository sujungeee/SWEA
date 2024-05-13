N= 10
k= 24

mStr= ['A']*(N-2)
mStr.append('B')
mStr.append('B')

sortedStr= ''
end= N-2

for _ in range(k-1):
    if mStr[end] == mStr[end+1]:
        end-= 1
        mStr[end]='B'
        for i in range(end+1,N-1):
            mStr[i]= 'A'
        mStr[N-1]= 'B'
        s= 1
    else:
        if s != N-end:
            mStr[-s], mStr[-s-1]= mStr[-s-1], mStr[-s]
        s+=1

print(mStr)

