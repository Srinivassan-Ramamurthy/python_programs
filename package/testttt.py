def pattern():
    a=input('enter 5 letter word ')
    for i in range(len(a)):
        for j in range(len(a)):
            if(j==i):
                print(a[i],end='')
            elif(j+i==4):
                print(a[-1-i],end='')
            else:
                print(' ',end='')
        print()
pattern()
