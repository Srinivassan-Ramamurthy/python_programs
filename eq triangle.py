for i in range(5):
    for j in range (5):
        if((j==0)or((4>i>0)and(j==1))or(i==2 and j==2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
