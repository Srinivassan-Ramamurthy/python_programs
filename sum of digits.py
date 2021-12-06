a=[3,2,11,7,6,5,6,1]
b=[]
for x in a:
    for y in a[1:]:
        if(y<x):
            b.append(y)
print(*b)
