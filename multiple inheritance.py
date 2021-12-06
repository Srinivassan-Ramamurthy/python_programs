class A:
    def sum1(self):
        print(5+8)
class B(A):
    def sub2(self):
        print(5-9)
class C(B):
    def mul(self):
        print(6*7)
cl=C()
cl.sum1()

