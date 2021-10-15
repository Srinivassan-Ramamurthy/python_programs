a=[]
result=[]
x=int(input('enter range '))
for i in range(x):
    a.append([])
    for j in range(x):
        a[i].append(int(input('enter values')))
for i in range(x):
    result.append([])
    for j in range(x):
        result[i].append(a[j][i])
for i in result:
    print(*i,end=' ')
    print()

    
        
        
