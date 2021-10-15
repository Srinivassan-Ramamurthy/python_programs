'''a=int(input('Enter a number '))
b=str(a)
rev=0
for i in range(len(b)):
    rev=(rev*10)+(a%10)
    a=a//10
print(rev)'''
a=int(input('Enter a number '))
rev=0
while(a>0):
    rev=(rev*10)+(a%10)
    a=a//10
print(rev)
