a={'a':'hello','b':'1','c':'jayalatha','d':[1,2]}
d={}
val=list(a.values())
val.sort(key=len)
print(val)
for i in val:
    for j in a:
        if(i==a[j]):
            d.update({j:a[j]})
print(d)
            


            
            
    
    
