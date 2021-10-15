a=input('enter a paragraph').split(' ')
b=input('find-')
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b):
            print(a[i])
