def invalid(func):
    def inner(a,b):
        if(b==0):
            return 'Invalid input'
        return(a/b)
    return inner
@invalid
def div(a,b):
    return(a/b)
print(div(4,2))
