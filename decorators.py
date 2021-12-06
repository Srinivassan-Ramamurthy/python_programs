def split(func):
    def inner():
        str1=func()
        return str1.split()
    return inner
def strupr(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
@strupr
@split
def printstr():
    return 'Good evening'
print(printstr())

