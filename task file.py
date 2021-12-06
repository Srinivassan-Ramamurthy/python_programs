f=open('task.txt','r+')
b=input('enter username ').strip()
c=input('enter password ').strip()
for i in f:
    if(i.split()[0] == b and i.split()[1] == c):
        print("already have an account")
        break
else:
    f.write("\n")
    f.write(b)
    f.write(" ")
    f.write(c)
        
f.close()
