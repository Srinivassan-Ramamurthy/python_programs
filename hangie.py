hangman=['      _______','     |/      |','     |      (_)','     |      \|/','     |       |','     |      / \\','     |','    _|___']
a='aeroplane'
c=[]
for i in a:
    c.append('_ ')
print(*c)
n=len(a)
def inp():
    user=input("enter the word")
    for i in range(len(a)):
        if(a[i] == user):
            c[i] = user
            print(*c)
for i in range(8):
    inp()
    
                
            

