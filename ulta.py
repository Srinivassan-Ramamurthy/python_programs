a=input('Enter input ')
for i in range(0,len(a),2):
    if(a[i].isnumeric()):
        print(a[(i+1)]*(int(a[i])),end='')
    else:
        print(a[i]*(int(a[i+1])),end='')
        
        
        
