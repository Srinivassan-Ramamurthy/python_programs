a=[]
b=[]

temp=0
result=[]
n=int(input('number of matrix '))
m=int(input('Range of matrix '))
for i in range(1,n+1):
    print(f'enter matrix{i} ')
    if(i==1):
        temp=a
    else:
        temp=b
    for i in range(m):
        temp.append([])
        for j in range(m):
            temp[i].append(int(input('enter value ')))
'''for i in range(m):
    result.append([])
    for j in range(m):
        res[i][j]=0
        for k in range(m):
            res[i][j]+=a[i][k]*b[k][j]
            result[i].append(res[j][i])
for i in result:
        print(*i)'''
for i in a:
    print(*i)
for i in b:
    print(*i)

    
    
    
