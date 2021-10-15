n=int(input('enter value '))
a=[]
for i in range(n):
    b=input('enter command ').casefold().split(' ')
    if(b[0]=='insert'):
        a.insert(int(b[1]),int(b[2]))
    elif(b[0]=='append'):
        a.append(int(b[1]))
    elif(b[0]=='remove'):
        a.remove(int(b[1]))
    elif(b[0]=='pop'):
        if(len(a)!=0):
            a.pop()
    elif(b[0]=='sort'):
        a.sort()
    elif(b[0]=='reverse'):
        a.reverse()
    elif(b[0]=='print'):
        print(a)
        
    
        
    
