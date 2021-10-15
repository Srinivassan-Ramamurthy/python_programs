a=input('Enter a string ')
b=input()
x=a.split()
for i in x:
    if(i.startswith(b)):
        print(i)
