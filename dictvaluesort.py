a={'a':'hello','b':'1','c':'jayalatha','d':[1,2]}
b={}
d={}
for i in a:
        b.update({i:len(a[i])})
c=list(b.values())
print(c)
c.sort()
print(c)
for i in c:
    for j in a:
        if(i==len(a[j])):
            d.update({j:a[j]})
print(d)