a=input('INPUT ')
b={}
c=[]
for i in range(len(a)):
    x=0
    for j in a:
        if(a[i]==j):
            x+=1
    b.update({a[i]:x})

y=b.items()
for k in y:
    c.append(k[1])
c.sort()
print(c)
for k in y:
    if(c[-1]==k[1]):
        print(k[0])
