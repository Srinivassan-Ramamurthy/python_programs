def perfect():
    a=int(input('Enter a number '))
    b=a
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum+=i
    if(sum==b):
        print(sum,'is a perfect number')
    else:
        print(b,'Not a perfect number')
perfect()
