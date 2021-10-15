count=0
bucket=input('enter letters ').split(',')
no_of_words=int(input('enter no of words '))
words=[]
for i in range(no_of_words):
    c=input('enter word')
    words.append(c)
for k in bucket:
    for j in words:
        for l in range(len(j)):
            print(l)
            '''if(j[l]==k):
                bucket.remove(k)
                count+=1
            print(f'count{count}')
            print(f'len{len(j)}')
            if(count==len(j)):
                print('YES')
                break
            else:
                print('NO')
                break'''
