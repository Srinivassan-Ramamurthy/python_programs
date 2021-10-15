a=['H','F','B','A','C','L','K','G','V','C','B','I','U', 'K', 'F']
b=int(input('enter no of words'))
c=[]
new=[]
count=0
for i in range(b):
    d=input()
    c.append(d)
for j in c:
    for k in range(len(j)):
        if j[k] in a:
            a.remove(j[k])
            count+=1
    new.append(count)
    count=0
    if(len(j))in new:
        print('yes')
    else:
        print('no')

