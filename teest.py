a=[16,17,18,21,24,36]
b=[f'{x} Eligible to vote' if x>=18 else f'{x} not eligible' for x in a]
print(a)
print(b)