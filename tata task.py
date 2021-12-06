a=[3,2,11,7,6,5,6,1]
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[j]<a[i]):
            b.append(a[j])
            break
    else:

print(b)
    
            
            
    
