f=open('task.txt','r+')
a=f.readlines()
b=input('enter username ').strip()
c=input('enter password ').strip()
d=b+' '+c+'\n'
if d in a:
    print('ok')
else:
    f.write(b+' '+c+'\n')
    print('written')
f.close()
