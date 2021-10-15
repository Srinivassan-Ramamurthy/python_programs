a=int(input('Enter range '))
for i in range(a+1):
    for j in range(2,a//2+1):
        if(i%j!=0):
            print(i,end=' ')
            break
        else:
            break
