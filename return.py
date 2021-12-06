def outer():
    x=3
    def inner():
        y=3
        res=x+y
        return res
    return inner
a= outer()
print(a())
print(a.__name__)
