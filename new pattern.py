x=int(input('enter value '))
for i in range(x):
    for j in range(x):
        if((i+j==4) or (i+j==5) or(i+j==6)or(i+j==7)or(i+j==8)):
            print((i+j)-(x-2) ,end=' ')
        else:
            print('*',end=' ')
    print()
    
