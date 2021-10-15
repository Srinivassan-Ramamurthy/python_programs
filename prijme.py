a=int(input('Enter a number '))
x=0
for i in range (2,(a//2)+1):
    if(a%i==0):
        x=1
if(x!=0):
    print('not a prime')
else:
    print('prime')
    
