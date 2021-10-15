a=int(input('enter range '))
b=[]
e=[]
d=[]
for i in range(a):
    c=int(input('enter value '))
    b.append(c)
for i in b:
    if(i%2==0):
        e.append(i)
    else:
        d.append(i)
print(b,e,d)
        
