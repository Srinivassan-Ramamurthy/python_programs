def number_reverse():
    rev=0
    while(a>0):
        rev=(rev*10)+(a%10)
        a=a//10
    return rev
a=int(input('Enter a number '))
number_reverse()
