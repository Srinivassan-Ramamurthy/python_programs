a=input('Enter input ').strip()
vowel=0
consonant=0
digit=0
special=0
for i in range(len(a)):
    if(a[i])in 'aeiouAEIOU':
        vowel+=1
    elif(a[i])in '~!@#$%^&*()':
        special+=1
    elif(a[i].isnumeric()):
        digit+=1
    elif(a[i])not in 'aeiouAEIOU' and a[i]!=' ':
        consonant+=1
print(f'vowel={vowel},consonant={consonant},digit={digit},special={special}')
