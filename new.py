dict={}
a=[[1,['ocean','pondy','2']],[2,['xxx','yyy','zzz']]]
for i in a:
        dict.update({i[0]:i[1]})
print(dict)
b=int(input('enter value '))
x=dict.get(b)
y=['name','place','age']
for i in range(len(y)):
    print(y[i],':',x[i])
    

