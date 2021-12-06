class A:
    def __init__(self):
        print('a is class')
class B(A):
   def __init__(self):
        super().__init__()
        print('b is class')
obj=B()

        
