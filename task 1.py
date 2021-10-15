bill=0
a=input('Enter pizza size ')
if(a=='small'):
    bill+=20
elif(a=='medium'):
    bill+=30
else:
    bill+=50
b=input('Do you want pepper and onion? ')
if(b=='yes'and a=='small'):
    bill+=10
elif(b=='yes'and a=='medium'):
    bill+=20
elif(b=='yes'and a=='large'):
    bill+=30
c=input('Do you want extra Cheese? ')
if(c=='yes'):
    bill+=10
    print('bill=',bill)
else:
    print('bill=',bill)





        
        
    
    
    
    
