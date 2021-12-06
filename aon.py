instr='LRLL1'
count=0
for i in range(len(instr)):
    if(instr[i]=='L'):
        count= count-1
    elif(instr[i]=='R'):
        count= count+1
    else:
        num=int(instr[i])
        if(instr[num]=='L'):
            count= count-1
        else:
            count= count+1
print(count)
            
    
    
