a=[]
b=int(input('enter no of digits '))
for k in range(b):
      c=int(input('enter values '))
      a.append(c)
temp=0
for i in range(len(a)-1):
    for j in range (i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            print(a)
        
