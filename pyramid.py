for i in range(5):
    for j in range (8):
        if((i+j==5)or((i==3)and(j%2==0))or(j-i==5)or((i==2)and(j%2!=0))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
