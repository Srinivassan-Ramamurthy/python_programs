a=input('enter string ')
b=input('enter letter ').strip()
count=0
for i in range(len(a)):
    if(a[i]==b):
        count+=1
print(count)
        
