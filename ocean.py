a=input('enter a value')
print(chr(ord(a[0])-32),end='')
for i in range(1,len(a)):
    print(a[i],end='')
