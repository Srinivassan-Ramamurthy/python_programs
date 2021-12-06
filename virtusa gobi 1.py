input1=[2,3]
input2='PN'
input3=2
total=0
for i in range(input3):
    if(input2[i]=='P'):
        total+=input1[i]
    if(input2[i]=='N'):
        total-=input1[i]
print(abs(total*100))

