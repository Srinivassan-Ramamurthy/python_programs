a=int(input('Enter a number '))
c=str(a)
b=a
sum=0
while(a>0):
    sum+=(a%10)**len(c)
    a=a//10
if(sum==b):
    print(sum,'is an armstrong number')
else:
    print(b,'Not an AMstrong Number number')
    
    
    
