a={'a':'hello','b':'1','c':'jayalatha','d':[1,2]}
d=sorted(list(a.values()),key=len)
e={}
for i in d:
    for j in a:
        if(i==a[j]):
            e.update({j:a[j]})
print(e)
            
