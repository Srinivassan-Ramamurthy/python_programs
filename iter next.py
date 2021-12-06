a='sri'
b=iter(a)
while ('true'):
    try:
        print(next(b))
    except StopIteration:
        print('error')
        break

