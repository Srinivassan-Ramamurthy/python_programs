def gr():
    a=int(input('Enter an integer '))
    b=int(input('Enter an integer '))
    c=int(input('Enter an integer '))
    if(a>b):
        if(a>c):
            return(a,' is greater')
        else:
            return(f'{c} is greater')
    else:
        if(b>c):
            return(f'{b} is greater')
        else:
            return(f'{c} is greater')
print(gr())
        
