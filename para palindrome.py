'''a=input('enter paragraph').strip(',')
b=a.split(' ')
count=0
for i in b:
    c=i[::-1]
    if(len(c)>1 and c==i):
        count+=1
print(count)'''
a=input('enter paragraph ').strip(',')
b=a.split(' ')
count=0
for i in b:
    if(len(i)>1 and i==i[::-1]):
        count+=1
print(count)
