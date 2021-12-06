b=int(input('enter range '))
a=[]
for i in range(b):
    a.append(input('enter input '))
temp=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a[-1])
print(a[1])
            
            
            
            
    
    
