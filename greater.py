a=int(input('Enter an integer '))
b=int(input('Enter an integer '))
c=int(input('Enter an integer '))
if(a>b):
    if(a>c):
        print(a,' is greater')
    else:
        print(f'{c} is greater')
else:
    if(b>c):
        print(f'{b} is greater')
    else:
        print(f'{c} is greater')
        
