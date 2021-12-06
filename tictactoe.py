print('Enter the places according to the below description')
print('\n','0','1','2','\n','3','4','5','\n','6','7','8')
print('player1 is O')
print('player2 is X')
global a
count=0
list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
inputs=[0,1,2,3,4,5,6,7,8]
n=8
err=[]
def condi():
    global count
    if list[0]==list[4]==list[8]=='X' or list[2]==list[4]==list[6]=='X' or list[0]==list[1]==list[2]=='X' or list[3]==list[4]==list[5]=='X' or list[6]==list[7]==list[8]=='X' or list[0]==list[3]==list[6]=='X' or list[1]==list[4]==list[7]=='X' or list[2]==list[5]==list[8]=='X':
        print("Player2 is winner!!")
        count += 1
        print('\n',list[0], list[1], list[2],'\n',list[3], list[4], list[5],'\n',list[6], list[7], list[8])
    elif list[0]==list[4]==list[8]=='O' or list[2]==list[4]==list[6]=='O' or list[0]==list[1]==list[2]=='O' or list[3]==list[4]==list[5]=='O' or list[6]==list[7]==list[8]=='O' or list[0]==list[3]==list[6]=='O' or list[1]==list[4]==list[7]=='O' or list[2]==list[5]==list[8]=='O':
        print("Player1 is winner!!")
        count += 1
        print('\n',list[0], list[1], list[2],'\n',list[3], list[4], list[5],'\n',list[6], list[7], list[8])
    else:
        print('\n',list[0], list[1], list[2],'\n',list[3], list[4], list[5],'\n',list[6], list[7], list[8])
def player_input(n):
    global a
    a=int(input('Enter Place '))
    if((a in err)or(a not in inputs)):
        print('invalid')
        player_input(n)
    else:
        for i in range(len(list)):
            if((n%2)==0):
                list[a]='O'
            else:
                list[a]='X'
    err.append(a)
    condi()
    n=n-1
    if(n>=0):   
        player_input(n)

player_input(n)
            

