y=10
def outer():
    z=4'''enclosed''' 
    def inner():
        nonlocal z
        x=4
        z=z+1
        print('x:',x)
        print('inside y:',y)
        print('inside z',z)
    inner()
outer()
        
