hangman=['      _______','     |/      |','     |      (_)','     |      \|/','     |       |','     |      / \\','     |','    _|___']
a='aeroplane'
c=[]
for i in range(len(a)):
    c.append(' ') 
print(len(a)*'_')
for i in range(8):
    b=input('enter letter ').strip()
    if(a[i]==b):
        c[i].append(b)
        print(*c)
        print('_'*8)
    else:
        print(hangman[i])
    if(i==7):
        print(a)
        print(len(a)*'_')


