a=input().strip(' ')
lower=0
upper=0
b=''.join(a.split())
print(b)
for i in b:
    if(i.isupper()):
        upper+=1
    else:
        lower+=1
print(lower,upper)

