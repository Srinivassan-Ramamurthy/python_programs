a=input('Enter input').strip()
count=1
b=[]
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count+=1
        b.append(count)
    else:
        count=1
        b.append(count)
print(max(b))
        
        
