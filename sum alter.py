a=int(input('Enter an integer '))
sum=0
for i in range(1,a+1):
    sum+=i
    if(i!=a):
        print(i,end='+')
    else:
        print(a,'=',sum)
        
