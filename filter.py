l=[1,2,3,4,5]
def even(n):
    return n%2==0
l=list(filter(even,l))
print(l)
