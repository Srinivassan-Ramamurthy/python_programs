a=input('To find treasure which way do you want to go left or right?')
if(a=='right'):
    b=input('Do you want to wait or swim?')
    if(b=='swim'):
        c=input('What colour treasure do you want?')
        if(c=='yellow'):
            print('You win')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')
    
